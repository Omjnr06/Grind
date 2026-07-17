import os
import ssl
import smtplib
import urllib.request
from email.message import EmailMessage
import config


def ntfy_push(posting, tier):
    if tier == "A":
        priority, prefix, tags = "5", "🎯 TARGET", "dart,rotating_light"
    else:
        priority, prefix, tags = "2", "🆕", "seedling"
    title = f"{prefix} {posting['company']}"
    body = f"{posting['title']}\n{posting['location']} · {posting.get('season') or 'season n/a'} · [{posting['source']}]"
    headers = {
        "Title": title.encode("utf-8"),
        "Priority": priority,
        "Tags": tags,
        "Click": posting["url"],
        "Actions": f"view, Open posting, {posting['url']}",
    }
    req = urllib.request.Request(
        f"{config.NTFY_SERVER}/{config.NTFY_TOPIC}",
        data=body.encode("utf-8"), headers=headers, method="POST",
    )
    try:
        urllib.request.urlopen(req, timeout=20)
        return True
    except Exception as e:
        print(f"  ntfy failed for {posting['company']}: {e}")
        return False


def _row(p):
    return f"- {p['company']} — {p['title']} | {p['location']} | {p.get('season') or ''}\n  {p['url']}"


def send_email_digest(a_list, b_list):
    host = os.environ.get("SMTP_HOST")
    user = os.environ.get("SMTP_USER")
    pw = os.environ.get("SMTP_PASS")
    to = os.environ.get("MAIL_TO")
    if not all([host, user, pw, to]):
        print("  email skipped (SMTP secrets not set)")
        return False
    port = int(os.environ.get("SMTP_PORT", "465"))
    n_a, n_b = len(a_list), len(b_list)
    parts = []
    if a_list:
        parts.append("=== TARGET COMPANIES ===\n" + "\n".join(_row(p) for p in a_list))
    if b_list:
        parts.append("=== OTHER RELEVANT ===\n" + "\n".join(_row(p) for p in b_list))
    msg = EmailMessage()
    msg["Subject"] = f"[{n_a} target / {n_b} other] new internship postings"
    msg["From"] = user
    msg["To"] = to
    msg.set_content("\n\n".join(parts) or "No new postings.")
    try:
        ctx = ssl.create_default_context()
        with smtplib.SMTP_SSL(host, port, context=ctx) as s:
            s.login(user, pw)
            s.send_message(msg)
        return True
    except Exception as e:
        print(f"  email failed: {e}")
        return False
