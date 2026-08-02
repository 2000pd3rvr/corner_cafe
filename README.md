---
title: Corner cafe
emoji: ☕
colorFrom: yellow
colorTo: gray
sdk: docker
pinned: true
short_description: Scottish café + contact mail form (v1.11)
---

# Corner cafe

**v1.11** — Floating contact form (email, subject, message) posts to an on-Space SMTP mail server and delivers to **pd3rvr@icloud.com** without opening a device mail app. Location: **9 Eskdail Court**, Dalkeith.

## Mail server secrets (Space Settings → Variables and secrets)

| Secret | Example |
|--------|---------|
| `SMTP_HOST` | `smtp.mail.me.com` (iCloud default in app) |
| `SMTP_PORT` | `587` |
| `SMTP_USER` | `pd3rvr@icloud.com` |
| `SMTP_PASSWORD` | iCloud **app-specific** password |
| `MAIL_TO` | `pd3rvr@icloud.com` (default) |
| `SMTP_FROM` | optional From header (defaults to `SMTP_USER`) |

Endpoint: `POST /api/contact` · health: `GET /api/health`.

Media loads from the public `PIANDT/sushi_atelier_artifacts` dataset (optional `HF_TOKEN` for private reads).
