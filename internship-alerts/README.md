# intern-alerts

Watches three internship trackers every 15 min and pushes **loud ntfy + email** for target companies, **quiet ntfy** for anything else relevant in your locations, and silently logs the rest. Runs entirely on free GitHub Actions. No server, no dependencies (Python stdlib only).

Sources: `vanshb03/Summer2027-Internships`, `zshah101` engine, `sndsh404/summer-2027-internships`, `speedyapply/2027-SWE-College-Jobs` (USA + international feeds), and  `SimplifyJobs/Summer2027-Internships`

## What each tier does

- **Tier A (target company + relevant location)** → loud ntfy (priority 5) + included in email digest.
- **Tier B (any tech internship in your locations, or a target in a non-listed location)** → quiet ntfy (priority 2, no sound) + email digest.
- **Tier C (everything else, plus anything requiring US citizenship / security clearance)** → written to `log.csv` only, no ping. Nothing is ever dropped — a name/spelling mismatch can only downgrade a posting, never hide it.

"New" = a URL never seen before **or** a role that went closed → open again.

## Setup (≈10 min) — dropping into your existing LeetCode repo

This installs into a subfolder of a repo you already have (e.g. `LeetCodeReview`), and isolates all automated writes to a separate `bot-state` branch so your `main` is only ever touched by you. Your LeetCode pushes will never collide with the bot.

**Layout after install:**
```
your-repo/                     (main branch — your stuff, untouched by the bot)
├── Arrays-and-Hashing/        LeetCode folders
├── Stacks/  Two-Pointers/ ...
├── internship-alerts/         <- add these files here
│   ├── config.py  sources.py  classify.py  notify.py  main.py  README.md
└── .github/workflows/
    └── intern-alerts.yml       <- add this here

bot-state branch               (created once — holds ONLY the two state files)
├── seen.json
└── log.csv
```

1. **Add the files** to your repo in the layout above (the five `.py` files + this README inside `internship-alerts/`, and `intern-alerts.yml` inside `.github/workflows/`). Push to `main`.
2. **Create the `bot-state` branch once.** On GitHub: the branch dropdown → type `bot-state` → "Create branch bot-state from main". (The bot cleans it down to just `seen.json`/`log.csv` on its first run.)
3. **Install the ntfy app** (iOS/Android) → Subscribe to topic → `Omjnr-06-internship-grind`.
4. **Turn on write permissions:** repo **Settings → Actions → General → Workflow permissions → Read and write → Save.**
5. **Add email secrets** (**Settings → Secrets and variables → Actions → New repository secret**), Gmail example:
   | Secret | Value |
   |---|---|
   | `SMTP_HOST` | `smtp.gmail.com` |
   | `SMTP_PORT` | `465` |
   | `SMTP_USER` | your gmail address |
   | `SMTP_PASS` | a Gmail **App Password** (Google Account → Security → 2-Step Verification → App passwords) |
   | `MAIL_TO` | where the digest goes |
   | `NTFY_TOPIC` | `Omjnr-06-internship-grind` (optional; already the default) |

   Skip these and ntfy still works; email just no-ops.
6. **First run = silent seed.** **Actions → intern-alerts → Run workflow.** It records everything currently posted **without pinging** you. Every run after that (automatic, every 15 min) alerts only on genuinely new/reopened postings.

## Tuning (edit `config.py`)

- `TIER_A_TARGETS` — your loud-alert companies. Add/remove freely; matching is case-insensitive, alias-aware (`google` also catches Alphabet/YouTube/DeepMind), and fuzzy (a typo like `Spotfy` still matches).
- `COMPANY_ALIASES` — extra spellings for any target.
- `LOCATION_PHRASES` / `LOCATION_TOKENS` — your locations. Note: `london` currently matches **both** London UK and London ON (where you are) — remove it and add `"london, uk"`/`"london, gb"` if you want UK-only. Add Canadian cities like `waterloo` anytime.
- `ROLE_INCLUDE` / `ROLE_EXCLUDE` — keyword gates (excludes senior/staff/manager/PhD, etc.).
- `RESTRICTED_MARKERS` — routes clearance/US-citizen-only roles to the log. As a Canadian citizen you're kept eligible for "does not offer sponsorship" roles (TN), which are **not** excluded.

## Notes

- ntfy.sh topics are public to anyone who knows the exact string. Yours is obscure; for true privacy later, ntfy supports auth or self-hosting.
- The bot **never pushes to `main`** — only to `bot-state`. Your LeetCode commits and the watcher can't conflict.
- GitHub cron can lag a few minutes under load — fine for same-day applying.
- The `speedyapply` international feed adds some London/Sydney/Bengaluru/Gulf roles, but coverage there is still lighter than US/Canada. A LinkedIn saved-search email alert for London/Dubai fully closes it.
- `log.csv` grows over time; it's your audit trail proving nothing was silently missed.