---
title: Corner cafe
emoji: ☕
colorFrom: yellow
colorTo: gray
sdk: static
app_file: index.html
pinned: true
short_description: Scottish café + contact mail form (v1.11)
---

# Corner cafe

**v1.11** — Floating contact form (email, subject, message). Messages go to **pd3rvr@icloud.com** without opening a device mail app. Location: **9 Eskdail Court**, Dalkeith.

## Outgoing mail

1. **Preferred (local Docker / any host running `app.py`)** — `POST /api/contact` sends via SMTP.
2. **Hugging Face static Space** — free-tier Docker CPU quota is currently `0`, so the Space stays **static**. The form uses FormSubmit AJAX to deliver mail when `/api/contact` is unavailable.

### SMTP secrets (local Docker or future Docker Space)

| Variable | Example |
|----------|---------|
| `SMTP_HOST` | `smtp.mail.me.com` |
| `SMTP_PORT` | `587` |
| `SMTP_USER` | `pd3rvr@icloud.com` |
| `SMTP_PASSWORD` | iCloud **app-specific** password |
| `MAIL_TO` | `pd3rvr@icloud.com` |
| `SMTP_FROM` | optional (defaults to `SMTP_USER`) |

```bash
docker build -t corner-cafe .
docker run --rm -p 7860:7860 \
  -e SMTP_USER=pd3rvr@icloud.com \
  -e SMTP_PASSWORD='your-app-specific-password' \
  -e MAIL_TO=pd3rvr@icloud.com \
  corner-cafe
```

Media loads from `PIANDT/sushi_atelier_artifacts`.
