import os
import re
import csv
import json
import datetime
import config
import sources
import classify
import notify


def _now():
    return datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")


def load_state():
    if not os.path.exists(config.STATE_FILE):
        return None
    with open(config.STATE_FILE) as f:
        return json.load(f)


def save_state(state):
    with open(config.STATE_FILE, "w") as f:
        json.dump(state, f, indent=0, sort_keys=True)


def append_log(rows):
    exists = os.path.exists(config.LOG_FILE)
    with open(config.LOG_FILE, "a", newline="") as f:
        w = csv.writer(f)
        if not exists:
            w.writerow(["ts", "tier", "company", "title", "location", "season", "sponsorship", "source", "url"])
        for p, tier in rows:
            w.writerow([
                _now(),
                tier, p["company"], p["title"], p["location"],
                p.get("season", ""), p.get("sponsorship", ""), p["source"], p["url"],
            ])


def _content_key(p):
    def n(s):
        return re.sub(r"[^a-z0-9]", "", (s or "").lower())
    return (n(p["company"]), n(p["title"]), n(p["location"]))


def dedupe(postings):
    merged = {}
    for p in postings:
        k = p["url_key"]
        if not k:
            continue
        cur = merged.get(k)
        if cur is None:
            p["keys"], p["sources"] = {k}, {p["source"]}
            p["open_sources"] = {p["source"]} if p["is_open"] else set()
            merged[k] = p
        else:
            cur["sources"].add(p["source"])
            if p["is_open"]:
                cur["open_sources"].add(p["source"])
            cur["is_open"] = cur["is_open"] or p["is_open"]
            if len(p["location"]) > len(cur["location"]):
                cur["location"] = p["location"]
            if not cur.get("season") and p.get("season"):
                cur["season"] = p["season"]
    by_content = {}
    for p in merged.values():
        ck = _content_key(p)
        if not (ck[0] and ck[1]):
            ck = ("url", p["url_key"])
        cur = by_content.get(ck)
        if cur is None:
            by_content[ck] = p
        else:
            rep = cur if cur["url_key"] <= p["url_key"] else p
            rep["keys"] = cur["keys"] | p["keys"]
            rep["sources"] = cur["sources"] | p["sources"]
            rep["open_sources"] = cur["open_sources"] | p["open_sources"]
            rep["category"] = cur.get("category") or p.get("category") or ""
            rep["is_open"] = cur["is_open"] or p["is_open"]
            if not rep.get("season") and p.get("season"):
                rep["season"] = p["season"]
            by_content[ck] = rep
    return list(by_content.values())


def write_open_roles(open_roles, now):
    open_roles.sort(key=lambda r: (r["tier"], r["company"].lower(), r["location"].lower()))
    payload = {
        "generated_at": now,
        "counts": {
            "target": sum(1 for r in open_roles if r["tier"] == "A"),
            "relevant": sum(1 for r in open_roles if r["tier"] == "B"),
        },
        "roles": open_roles,
    }
    with open("open_roles.json", "w") as f:
        json.dump(payload, f, indent=1)
    print(f"[info] wrote open_roles.json ({payload['counts']['target']} target, {payload['counts']['relevant']} relevant)")


def _bootstrap_seeded(raw, state):
    known, total = {}, {}
    for p in raw:
        if not p["url_key"]:
            continue
        s = p["source"]
        total[s] = total.get(s, 0) + 1
        known[s] = known.get(s, 0) + (p["url_key"] in state)
    seeded = {s for s in total if known[s] / total[s] >= 0.9}
    for s in sorted(total):
        print(f"[seed] bootstrap {s}: {known[s]}/{total[s]} known -> {'seeded' if s in seeded else 'NEW (silent first run)'}")
    return seeded


def load_seeded():
    if not os.path.exists(config.SEEDED_FILE):
        return None
    with open(config.SEEDED_FILE) as f:
        return set(json.load(f))


def save_seeded(seeded):
    with open(config.SEEDED_FILE, "w") as f:
        json.dump(sorted(seeded), f, indent=1)


def main():
    now = _now()
    raw, errors = sources.fetch_all()
    if errors:
        for k, v in errors.items():
            print(f"[warn] source {k} failed: {v}")
    if not raw:
        print("[abort] no postings fetched from any source; leaving state untouched")
        return
    postings = dedupe(raw)
    print(f"[info] {len(postings)} unique postings after dedupe")

    state = load_state()
    seeding = state is None
    if seeding:
        state = {}
        print("[seed] first run: recording current postings WITHOUT notifying")

    seeded = load_seeded()
    if seeded is None:
        seeded = set() if seeding else _bootstrap_seeded(raw, state)
    fetched = {p["source"] for p in raw}
    for s in sorted(fetched - seeded):
        print(f"[seed] source {s} is new: recording its postings WITHOUT notifying")

    a_new, b_new, log_rows, open_roles = [], [], [], []

    for p in postings:
        key = p["url_key"]
        if not key:
            continue
        tier = classify.tier_for(p)
        p["track"] = classify.track_for(p)
        prev = next((state[k] for k in sorted(p["keys"]) if k in state), None)
        if p["is_open"] and tier in ("A", "B"):
            prev_seen = (prev or {}).get("first_seen")
            open_roles.append({
                "tier": tier,
                "track": p["track"],
                "company": p["company"],
                "title": p["title"],
                "location": p["location"],
                "season": p.get("season") or "",
                "sponsorship": p.get("sponsorship") or "",
                "source": p["source"],
                "url": p["url"],
                "first_seen": prev_seen or now,
            })
        reopened = (bool(prev) and not prev.get("is_open", True) and p["is_open"]
                    and bool(p["open_sources"] & seeded))
        is_new = prev is None or reopened
        alert = is_new and not seeding and bool(p["sources"] & seeded)

        record = {
            "is_open": p["is_open"],
            "tier": tier,
            "track": p["track"],
            "company": p["company"],
            "title": p["title"],
            "first_seen": (prev or {}).get("first_seen", now),
            "last_seen": now,
        }
        if (prev or {}).get("seeded") or (prev is None and not alert):
            record["seeded"] = True
        for k in p["keys"]:
            state[k] = record

        if alert:
            log_rows.append((p, tier))
            if tier == "A":
                a_new.append(p)
            elif tier == "B":
                b_new.append(p)

    save_state(state)
    save_seeded(seeded | (fetched - set(errors)))
    write_open_roles(open_roles, now)

    if seeding:
        print(f"[seed] recorded {len(state)} postings. Alerts start on next run.")
        return

    if not (a_new or b_new or log_rows):
        print("[info] no new postings this run")
        return

    if log_rows:
        append_log(log_rows)

    print(f"[info] new: {len(a_new)} target(A), {len(b_new)} relevant(B), {len(log_rows)} total logged")
    if len(a_new) + len(b_new) > config.FLOOD_LIMIT:
        print(f"[flood] {len(a_new) + len(b_new)} new alerts > {config.FLOOD_LIMIT}; sending one summary instead")
        notify.flood_summary(len(a_new), len(b_new))
        return

    for p in a_new:
        notify.ntfy_push(p, "A")
    for p in b_new:
        notify.ntfy_push(p, "B")
    if a_new or b_new:
        notify.send_email_digest(a_new, b_new)
    notify.ntfy_push_friends([p for p, _ in log_rows if p["is_open"] and classify.is_friend_role(p)])


if __name__ == "__main__":
    main()