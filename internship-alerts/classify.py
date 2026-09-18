import re
import difflib
import config

_STRIP = re.compile(r"\b(inc|inc\.|llc|corp|corporation|co|ltd|the|company)\b")


def norm_company(name):
    n = name.lower()
    n = re.sub(r"[^a-z0-9 ]", " ", n)
    n = _STRIP.sub(" ", n)
    return re.sub(r"\s+", " ", n).strip()


def _target_canon():
    canon = {}
    for t in config.TIER_A_TARGETS:
        canon[norm_company(t)] = t
        for a in config.COMPANY_ALIASES.get(t, []):
            canon[norm_company(a)] = t
    return canon


_CANON = _target_canon()


def _uk_target_canon():
    canon = {}
    for t in config.UK_TARGETS:
        canon[norm_company(t)] = t
        for a in config.UK_COMPANY_ALIASES.get(t, []):
            canon[norm_company(a)] = t
    return canon


_UK_CANON = _uk_target_canon()


def is_target(company):
    n = norm_company(company)
    if not n:
        return None
    if n in _CANON:
        return _CANON[n]
    tokens = n.split()
    tokenset = set(tokens)
    for canon_norm, canon in _CANON.items():
        cwords = canon_norm.split()
        if len(cwords) == 1:
            if cwords[0] in tokenset:
                return canon
        else:
            if canon_norm in n:
                return canon
    best = difflib.get_close_matches(n, list(_CANON.keys()), n=1, cutoff=0.92)
    if best:
        return _CANON[best[0]]
    return None


def location_relevant(location):
    if not location:
        return False
    n = location.lower()
    for p in config.LOCATION_PHRASES:
        if p in n:
            return True
    tokens = set(re.split(r"[^a-z]+", n))
    return bool(tokens & config.LOCATION_TOKENS)


def is_uk_location(location):
    if not location:
        return False
    n = location.lower()
    if any(m in n for m in config.UK_COUNTRY_MARKERS):
        return True
    tokens = set(re.split(r"[^a-z]+", n))
    if tokens & config.UK_TOKENS:
        return True
    if "london" in n and not any(m in n for m in config.NON_UK_LONDON_MARKERS):
        return True
    for p in config.UK_LOCATION_PHRASES:
        if p == "london":
            continue
        if p in n:
            return True
    return False


def region_for(posting):
    return "UK" if is_uk_location(posting.get("location", "")) else "US"


def is_uk_target(company):
    n = norm_company(company)
    if not n:
        return None
    if n in _UK_CANON:
        return _UK_CANON[n]
    tokenset = set(n.split())
    for canon_norm, canon in _UK_CANON.items():
        cwords = canon_norm.split()
        if len(cwords) == 1:
            if cwords[0] in tokenset:
                return canon
        elif canon_norm in n:
            return canon
    return None


def is_intern_role(title):
    t = title.lower()
    if not any(k in t for k in config.ROLE_INCLUDE):
        return False
    if any(k in t for k in config.ROLE_EXCLUDE):
        return False
    return True


def is_restricted(posting):
    blob = f"{posting.get('title','')} {posting.get('sponsorship','')} {posting.get('location','')}".lower()
    return any(m in blob for m in config.RESTRICTED_MARKERS)


def tier_for(posting):
    if not is_intern_role(posting["title"]):
        return "C"
    if is_uk_location(posting.get("location", "")):
        return "A" if is_uk_target(posting["company"]) else "B"
    if is_restricted(posting):
        return "C"
    target = is_target(posting["company"])
    loc_ok = location_relevant(posting["location"])
    if loc_ok:
        return "A" if target else "B"
    if target:
        return "B"
    return "C"