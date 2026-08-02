---
title: Corner cafe
sdk: static
app_file: index.html
sdk_version: "1.11"
emoji: ☕
colorFrom: yellow
colorTo: gray
pinned: true
short_description: Enquire form emails inbox (no mail app) · v1.11
---

# Corner cafe

**v1.11** — Floating enquire form (email, subject, message) sends to **pd3rvr@icloud.com** without opening a device mail app. Open Monday–Sunday 9:00–17:00 at **9 Eskdail Court**, Dalkeith.

## Mail

- **Static HF Space:** form posts via FormSubmit AJAX to `pd3rvr@icloud.com` (same pattern as careTalk). First live send may need a one-time FormSubmit confirmation in that inbox.
- **Docker / `app.py` outgoing mail:** `POST /api/contact` sends over SMTP. Set secrets `SMTP_USER` + `SMTP_PASSWORD` (iCloud app-specific password), optional `SMTP_HOST=smtp.mail.me.com`, `SMTP_PORT=587`, `MAIL_TO`, `SMTP_FROM`.

> Hugging Face free tier no longer allows new Docker Spaces, so this Space uses the **static** SDK. `Dockerfile` / `app.py` remain for local Docker runs with the SMTP mail server.
