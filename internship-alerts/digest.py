import os
import re
import json
import datetime
import sources
import classify
import main
import notify
import config

INCLUDE_TIER_B = True
EMAIL_TIER_B = False
BOARD_URL = "https://github.com/Omjnr06/Grind/blob/bot-state/OPEN_ROLES.md"

UK_PROGRAMS = [
    ("UK Youth Mobility Scheme (visa)",
     "https://www.gov.uk/youth-mobility",
     "Apply yourself — 2yr UK work visa, no employer sponsorship (Canadian, 18-35)."),
    ("IAESTE Canada (placement)",
     "https://www.iaeste.ca/internships",
     "Rolling; heaviest new-posting waves in November, January, and April. Check regularly."),
]


def _key(p):
    return (p["company"].lower(), p.get("season") or "", p["location"].lower())


def _load_first_seen():
    for path in (os.path.join("..", "_state", config.STATE_FILE), config.STATE_FILE):
        if os.path.exists(path):
            with open(path) as f:
                return {k: v.get("first_seen") for k, v in json.load(f).items()}
    return {}


def _recent_friend_roles(uniq):
    first_seen = _load_first_seen()
    cutoff = datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(hours=config.FRIENDS_DIGEST_HOURS)
    out = []
    for p in uniq:
        if not (p["is_open"] and classify.is_friend_role(p)):
            continue
        fs = first_seen.get(p["url_key"])
        if fs and datetime.datetime.fromisoformat(fs.replace("Z", "+00:00")) < cutoff:
            continue
        out.append(p)
    return sorted(out, key=_key)


def build():
    uniq = main.dedupe(sources.fetch_all()[0])
    a = sorted([p for p in uniq if p["is_open"] and classify.tier_for(p) == "A"], key=_key)
    b = sorted([p for p in uniq if p["is_open"] and classify.tier_for(p) == "B"], key=_key)
    return a, b, _recent_friend_roles(uniq)


def render_md(a, b):
    day = datetime.date.today().isoformat()
    lines = [f"# Open roles board — {day}", "",
             f"**{len(a)} target-company roles open.** Real-time pings cover new drops; this board is the full standing list so nothing gets lost.", ""]
    lines.append("## UK Programs & Visa")
    for name, url, note in UK_PROGRAMS:
        lines.append(f"- **{name}** — {note}  \n  {url}")
    lines.append("")
    if a:
        lines.append("## Target companies")
        for p in a:
            season = p.get("season") or "term n/a"
            tag = "[UK] " if classify.region_for(p) == "UK" else ""
            lines.append(f"- **{tag}{p['company']}** — {p['title']}  \n  {p['location']} · {season} · [{p['source']}]  \n  {p['url']}")
        lines.append("")
    if INCLUDE_TIER_B and b:
        lines.append(f"## Other relevant ({len(b)})")
        for p in b:
            season = p.get("season") or "term n/a"
            tag = "[UK] " if classify.region_for(p) == "UK" else ""
            lines.append(f"- {tag}{p['company']} — {p['title']} — {p['location']} · {season}  \n  {p['url']}")
    return "\n".join(lines) + "\n"


def render_email(a, b):
    lines = [f"{len(a)} target-company roles open right now.", ""]
    for p in a:
        season = p.get("season") or "term n/a"
        tag = "[UK] " if classify.region_for(p) == "UK" else ""
        lines.append(f"- {tag}{p['company']} — {p['title']}")
        lines.append(f"  {p['location']} · {season} · [{p['source']}]")
        lines.append(f"  {p['url']}")
    if EMAIL_TIER_B and b:
        lines.append("")
        lines.append(f"--- {len(b)} other relevant roles ---")
        for p in b:
            lines.append(f"- {p['company']} — {p['title']} — {p['location']}")
            lines.append(f"  {p['url']}")
    elif b:
        lines.append("")
        lines.append(f"(+ {len(b)} other relevant roles — see OPEN_ROLES.md on the bot-state branch)")
    lines.append("")
    lines.append("--- UK Programs & Visa (apply directly) ---")
    for name, url, note in UK_PROGRAMS:
        lines.append(f"- {name}: {note}")
        lines.append(f"  {url}")
    return "\n".join(lines)


def _is_canada(p):
    n = p["location"].lower()
    return "canada" in n or any(t in set(re.split(r"[^a-z]+", n)) for t in ("on", "bc", "qc", "ab"))


def render_friends_email(roles):
    hours = config.FRIENDS_DIGEST_HOURS
    lines = [f"{len(roles)} new intern roles in the US & Canada in the last {hours} hours.",
             f"Full list of everything open: {config.DASHBOARD_URL}", ""]
    if not roles:
        lines.append("Nothing new this time. Check the dashboard for everything still open.")
    canada = [p for p in roles if _is_canada(p)]
    rest = [p for p in roles if not _is_canada(p)]
    for heading, group in (("Canada", canada), ("US & Remote", rest)):
        if not group:
            continue
        lines.append(f"=== {heading} ({len(group)}) ===")
        for p in group:
            season = p.get("season") or "term n/a"
            lines.append(f"- {p['company']} — {p['title']} | {p['location']} · {season}")
            lines.append(f"  {p['url']}")
        lines.append("")
    return "\n".join(lines)


def main_run():
    a, b, friends = build()
    md = render_md(a, b)
    with open("OPEN_ROLES.md", "w") as f:
        f.write(md)
    print(f"[digest] {len(a)} target roles, {len(b)} other; wrote OPEN_ROLES.md")
    notify.send_email(f"Daily board: {len(a)} target roles open", render_email(a, b))
    notify.send_friends_email(f"{len(friends)} new intern roles (last {config.FRIENDS_DIGEST_HOURS}h)",
                              render_friends_email(friends))
    summary = {
        "company": f"{len(a)} target roles open",
        "title": "Daily board updated - see email / OPEN_ROLES.md",
        "location": "", "season": "", "url": BOARD_URL, "source": "digest",
    }
    notify.ntfy_push(summary, "B")


if __name__ == "__main__":
    main_run()