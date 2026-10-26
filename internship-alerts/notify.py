import os
import ssl
import json
import smtplib
import time
import urllib.request
import urllib.error
import urllib.parse
from email.message import EmailMessage
import config
import classify


def _ascii(s):
    return s.encode("ascii", "ignore").decode("ascii").strip()


def _track_action(posting, url):
    endpoint = (os.environ.get("TRACK_ENDPOINT") or "").strip()
    if not endpoint or posting.get("source") == "digest":
        return None
    secret = (os.environ.get("TRACK_SECRET") or "").strip()

    def q(s):
        return urllib.parse.quote((s or "")[:150], safe="")

    track_url = (
        f"{endpoint}?k={q(secret)}&c={q(posting.get('company'))}"
        f"&r={q(posting.get('title'))}&loc={q(posting.get('location'))}"
        f"&u={q(url)}&src={q(posting.get('source'))}"
    )
    if "," in track_url or ";" in track_url:
        return None
    return f"http, Applied, {track_url}, method=POST"


def ntfy_push(posting, tier, topic=None, track=True):
    if tier == "A":
        priority, label, tags = "5", "TARGET", "dart,rotating_light"
    else:
        priority, label, tags = "2", "NEW", "seedling"
    region = classify.region_for(posting)
    prefix = "[UK] " if region == "UK" else ""
    title = _ascii(f"{prefix}{label}: {posting['company']}") or label
    body = f"{posting['title']}\n{posting['location']} - {posting.get('season') or 'season n/a'} [{posting['source']}]"
    headers = {"Title": title, "Priority": priority, "Tags": tags}
    url = posting.get("url") or ""
    actions = []
    if url:
        headers["Click"] = url
        if "," not in url:
            actions.append(f"view, Open posting, {url}")
    track = _track_action(posting, url) if track else None
    if track:
        actions.append(track)
    if actions:
        headers["Actions"] = "; ".join(actions)
    req = urllib.request.Request(
        f"{config.NTFY_SERVER}/{topic or config.NTFY_TOPIC}",
        data=body.encode("utf-8"), headers=headers, method="POST",
    )
    try:
        urllib.request.urlopen(req, timeout=20)
        return True
    except Exception as e:
        print(f"  ntfy failed for {posting['company']}: {e}")
        return False


def _send_via_resend(subject, body_text, to_list):
    key = (os.environ.get("RESEND_API_KEY") or "").strip()
    if not key or not to_list:
        return None
    frm = (os.environ.get("RESEND_FROM") or "onboarding@resend.dev").strip()
    print(f"  [resend] key_len={len(key)} starts_ok={key.startswith('re_')} to={[_mask(t) for t in to_list]}")
    payload = json.dumps({"from": frm, "to": to_list, "subject": subject, "text": body_text}).encode()
    req = urllib.request.Request(
        "https://api.resend.com/emails", data=payload,
        headers={
            "Authorization": f"Bearer {key}",
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        },
        method="POST",
    )
    try:
        urllib.request.urlopen(req, timeout=20)
        print("  email sent via Resend")
        return True
    except urllib.error.HTTPError as e:
        detail = ""
        try:
            detail = e.read().decode("utf-8", "replace")
        except Exception:
            pass
        print(f"  resend failed: HTTP {e.code} {detail}")
        return False
    except Exception as e:
        print(f"  resend failed: {e}")
        return False


def _send_via_smtp(subject, body_text, to_list):
    host = os.environ.get("SMTP_HOST")
    user = os.environ.get("SMTP_USER")
    pw = os.environ.get("SMTP_PASS")
    if not all([host, user, pw, to_list]):
        print("  email skipped (no Resend key and SMTP secrets incomplete)")
        return False
    port = int(os.environ.get("SMTP_PORT", "465"))
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = user
    msg["To"] = ", ".join(to_list)
    msg.set_content(body_text)
    try:
        ctx = ssl.create_default_context()
        with smtplib.SMTP_SSL(host, port, context=ctx) as s:
            s.login(user, pw)
            s.send_message(msg)
        print("  email sent via SMTP")
        return True
    except Exception as e:
        print(f"  email failed: {e}")
        return False


def _split(env_val):
    return [e.strip() for e in (env_val or "").replace(";", ",").replace("\n", ",").split(",") if e.strip()]


def _mask(addr):
    name, _, domain = addr.partition("@")
    return f"{name[:1]}***@{domain}"


def _dedup(*env_names, exclude=()):
    out, seen = [], {e.lower() for e in exclude}
    for name in env_names:
        for e in _split(os.environ.get(name)):
            if e.lower() not in seen:
                seen.add(e.lower())
                out.append(e)
    return out


def recipients():
    everyone = _dedup("MAIL_TO", "MAIL_EXTRA")
    return (everyone[0] if everyone else None), everyone[1:]


def friend_recipients():
    primary, others = recipients()
    return _dedup("DIGEST_EXTRA", exclude=([primary] if primary else []) + others)


def _send_one(subject, body_text, to):
    r = _send_via_resend(subject, body_text, [to])
    if r:
        return True
    return _send_via_smtp(subject, body_text, [to])


def _send_each(subject, body_text, addrs, label):
    for i, addr in enumerate(addrs):
        # for rate limiting on resend
        time.sleep(0.6) 
        try:
            if not _send_one(subject, body_text, addr):
                print(f"  {label} {i + 1} ({_mask(addr)}) failed")
        except Exception as e:
            print(f"  {label} {i + 1} ({_mask(addr)}) crashed: {e}")


def send_email(subject, body_text):
    primary, others = recipients()
    if not primary:
        print("  email skipped (MAIL_TO not set)")
        return False
    ok = _send_one(subject, body_text, primary)
    _send_each(subject, body_text, others, "extra recipient")
    return ok


def send_friends_email(subject, body_text):
    friends = friend_recipients()
    if not friends:
        return
    print(f"  [friends] sending digest to {len(friends)} address(es)")
    _send_each(subject, body_text, friends, "friend")


def ntfy_push_friends(postings):
    if not config.NTFY_FRIENDS_TOPIC or not postings:
        return
    for p in postings[:config.FRIENDS_MAX_PUSHES]:
        ntfy_push(p, "B", topic=config.NTFY_FRIENDS_TOPIC, track=False)
    extra = len(postings) - config.FRIENDS_MAX_PUSHES
    if extra > 0:
        summary = {
            "company": f"+{extra} more new roles",
            "title": "Too many to push one by one - see the dashboard",
            "location": "", "season": "", "url": config.DASHBOARD_URL, "source": "digest",
        }
        ntfy_push(summary, "B", topic=config.NTFY_FRIENDS_TOPIC, track=False)


def _row(p):
    tag = "[UK] " if classify.region_for(p) == "UK" else ""
    return f"- {tag}{p['company']} — {p['title']} | {p['location']} | {p.get('season') or ''}\n  {p['url']}"


def send_email_digest(a_list, b_list):
    parts = []
    if a_list:
        parts.append("=== TARGET COMPANIES ===\n" + "\n".join(_row(p) for p in a_list))
    if b_list:
        parts.append("=== OTHER RELEVANT ===\n" + "\n".join(_row(p) for p in b_list))
    subject = f"[{len(a_list)} target / {len(b_list)} other] new internship postings"
    return send_email(subject, "\n\n".join(parts) or "No new postings.")