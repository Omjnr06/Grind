import re
import datetime
import json
import urllib.request
import urllib.error
import config


def _get(url, timeout=30):
    req = urllib.request.Request(url, headers={"User-Agent": "intern-alerts/1.0"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read().decode("utf-8", "replace")


def _fetch_text(src):
    try:
        return _get(src["url"])
    except Exception:
        if src.get("fallback_url"):
            return _get(src["fallback_url"])
        raise


def norm_url(u):
    if not u:
        return ""
    u = u.strip().split("#")[0].split("?")[0]
    u = re.sub(r"^https?://(www\.)?", "", u.lower()).rstrip("/")
    return u


def _posting(company, title, location, url, season, sponsorship, is_open, source, category=""):
    src = config.SOURCES.get(source, {})
    return {
        "category": (category or "").strip().lower(),
        "intern_list": bool(src.get("intern_list")),
        "company": (company or "").strip(),
        "title": (title or "").strip(),
        "location": (location or "").strip(),
        "url": (url or "").strip(),
        "url_key": norm_url(url),
        "season": (season or "").strip(),
        "sponsorship": (sponsorship or "").strip(),
        "is_open": bool(is_open),
        "source": source,
    }


_TERM = re.compile(r"\b(winter|spring|summer|fall|autumn)\s+(20\d\d)\b", re.I)
_TERM_START_MONTH = {"winter": 1, "spring": 3, "summer": 5, "fall": 9, "autumn": 9}


def _all_terms_started(terms, today=None):
    # Past = every listed term has already started (e.g. "Summer 2026", "Fall 2026"
    # in late Oct 2026). Terms without a year ("Summer", "N/A") count as current.
    today = today or datetime.date.today()
    found = [_TERM.search(t or "") for t in terms]
    if not found or any(m is None for m in found):
        return False
    return all(datetime.date(int(m[2]), _TERM_START_MONTH[m[1].lower()], 1) <= today for m in found)


def parse_simplify_json(raw, source):
    data = json.loads(raw)
    active_only = config.SOURCES.get(source, {}).get("active_only")
    out = []
    for e in data:
        if not e.get("is_visible", True):
            continue
        if active_only and not e.get("active", True):
            continue
        category = e.get("category") or ""
        if category.strip().lower() in config.SKIP_CATEGORIES:
            continue
        terms = e.get("terms") or ([e["season"]] if e.get("season") else [])
        if _all_terms_started(terms):
            continue
        locs = e.get("locations") or []
        season = e.get("season") or ", ".join(t for t in (e.get("terms") or []) if t != "N/A")
        out.append(_posting(
            e.get("company_name"), e.get("title"), " / ".join(locs),
            e.get("url"), season, e.get("sponsorship"),
            e.get("active", True), source, category,
        ))
    return out


def parse_zshah_json(raw, source):
    data = json.loads(raw)
    items = data.values() if isinstance(data, dict) else data
    out = []
    for e in items:
        out.append(_posting(
            e.get("company"), e.get("title"), e.get("location"),
            e.get("url"), e.get("season"), e.get("sponsorship"),
            e.get("is_open", True), source,
        ))
    return out


_HREF = re.compile(r'href=["\']([^"\']+)["\']')
_MDLINK = re.compile(r'\[([^\]]*)\]\(([^)]+)\)')
_EMOJI = re.compile(
    "[\U0001F000-\U0001FAFF"   # pictographs / emoji
    "\U00002600-\U000026FF"    # misc symbols
    "\U00002700-\U000027BF"    # dingbats
    "\U0001F1E6-\U0001F1FF"    # regional indicators (flags)
    "\U00002B00-\U00002BFF"    # misc symbols/arrows
    "\U0000FE00-\U0000FE0F"    # variation selectors
    "\U0000200D"               # zero-width joiner
    "]+"
)


def _clean_cell(c):
    c = re.sub(r"<[^>]+>", " ", c)
    c = _MDLINK.sub(r"\1", c)
    c = c.replace("**", "").replace("*", "").replace("`", "")
    c = _EMOJI.sub("", c)
    return re.sub(r"\s+", " ", c).strip()


def _is_homepage(u):
    path = re.sub(r"^https?://(www\.)?[^/]+", "", u).strip("/")
    return path == ""


def _row_urls(cells):
    urls = []
    for c in cells:
        for m in _HREF.finditer(c):
            urls.append(m.group(1))
        for m in _MDLINK.finditer(c):
            if m.group(2).startswith("http"):
                urls.append(m.group(2))
    urls = [u for u in urls if u.startswith("http") and "imgur.com" not in u]
    real = [u for u in urls if not _is_homepage(u)]
    if real:
        return real[-1]
    return urls[-1] if urls else ""


def parse_readme_table(raw, source):
    out = []
    last_company = ""
    for line in raw.splitlines():
        line = line.strip()
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) < 4:
            continue
        joined = " ".join(cells).lower()
        if set(joined.replace(" ", "")) <= set("-:") or "company" in joined and "role" in joined:
            continue
        company_raw = cells[0]
        company = _clean_cell(company_raw)
        if company in ("↳", "->", "same as above", "") or company_raw.strip() in ("↳",):
            company = last_company
        else:
            last_company = company
        title = _clean_cell(cells[1])
        location = _clean_cell(cells[2])
        url = _row_urls(cells)
        is_open = "\U0001F512" not in line  # closed roles are marked with a lock
        if not url or not company or not title:
            continue
        out.append(_posting(company, title, location, url, "", "", is_open, source))
    return out


PARSERS = {
    "simplify_json": parse_simplify_json,
    "zshah_json": parse_zshah_json,
    "readme_table": parse_readme_table,
}


def fetch_all():
    postings, errors = [], {}
    for name, src in config.SOURCES.items():
        try:
            raw = _fetch_text(src)
            postings.extend(PARSERS[src["type"]](raw, name))
        except Exception as e:
            errors[name] = str(e)
    return postings, errors