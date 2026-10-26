import os
import json
import urllib.request
import urllib.error

API = "https://api.notion.com"


def _req(token, method, path, body=None):
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(API + path, data=data, method=method, headers={
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "Notion-Version": "2022-06-28",
    })
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read().decode())


def _prop(props, name, kind):
    for k, v in props.items():
        if k.strip().lower() == name and v.get("type") == kind:
            return v
    return None


def _email(props):
    for k, v in props.items():
        if v.get("type") == "email" and v.get("email"):
            return v["email"].strip()
    p = _prop(props, "email", "rich_text") 
    if p:
        return "".join(t.get("plain_text", "") for t in p.get("rich_text", [])).strip()
    return ""


def _checked(props, name, default=False):
    p = _prop(props, name, "checkbox")
    return default if p is None else bool(p.get("checkbox"))


def load():
    """Rows from the Grind Recipients DB as [{"email", "swe", "pm"}], or None if
    Notion isn't configured or the query fails (callers fall back to secrets)."""
    token = (os.environ.get("NOTION_TOKEN") or "").strip()
    db_id = (os.environ.get("RECIPIENTS_DB_ID") or "").strip()
    if not token or not db_id:
        return None
    rows, cursor = [], None
    try:
        while True:
            body = {"page_size": 100}
            if cursor:
                body["start_cursor"] = cursor
            data = _req(token, "POST", f"/v1/databases/{db_id}/query", body)
            rows.extend(data.get("results", []))
            if not data.get("has_more"):
                break
            cursor = data.get("next_cursor")
    except urllib.error.HTTPError as e:
        detail = ""
        try:
            detail = e.read().decode("utf-8", "replace")[:300]
        except Exception:
            pass
        print(f"  [recipients] notion HTTP {e.code}: {detail}")
        return None
    except Exception as e:
        print(f"  [recipients] notion failed: {e}")
        return None

    out = []
    for row in rows:
        props = row.get("properties", {})
        email = _email(props)
        if "@" not in email or not _checked(props, "active", default=True):
            continue
        out.append({"email": email, "swe": _checked(props, "swe"), "pm": _checked(props, "pm")})
    return out
