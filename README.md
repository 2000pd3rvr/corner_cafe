---
title: Corner cafe
sdk: static
app_file: index.html
sdk_version: "1.14"
emoji: ☕
colorFrom: yellow
colorTo: gray
pinned: true
short_description: Responsive, fast-loading Scottish cafe site (v1.14)
---

# Corner cafe

**v1.14** — Responsive pass across phone, tablet, laptop and desktop, plus a much lighter first load. Open Monday–Sunday 9:00–17:00 at **9 Eskdail Court**, Dalkeith.

### Responsive

- Breakpoint ranges tidied to phone (<768px), tablet (768–1023px), laptop (1024–1439px) and desktop (1440px+).
- Menu grid now resolves 1 / 2 / 3 columns; the old four-track grid left an empty column on wide screens.
- Fixed the 550px map iframe and the full-bleed contact band that could push the page sideways.
- 44px minimum hit areas on touch pointers, safe-area padding for notched phones, and `svh` hero heights so mobile browser chrome does not cause a jump.

### Loading

- Hero ships **one** video instead of seven: the rest attach their source only when they are about to play.
- Spotlight and gallery carousels stay unfetched until scrolled near the viewport.
- Gallery photography requested at `w=800` rather than `w=1920`; the lightbox alone asks for the large render.
- Google Fonts load without blocking first paint; `apple-touch-icon` is a 21KB 180×180 file instead of a 946KB image.
- `Save-Data` and 2G/3G connections keep the opening frame and skip the video rotation entirely.

> **Policies / Legal & operations is hidden** while the wording is in draft — see the comment above `#policies` in `index.html` to restore it.

## Mail

- **Static HF Space:** form posts via FormSubmit AJAX to `pd3rvr@icloud.com` (same pattern as careTalk). First live send may need a one-time FormSubmit confirmation in that inbox.
- **Docker / `app.py` outgoing mail:** `POST /api/contact` sends over SMTP. Set secrets `SMTP_USER` + `SMTP_PASSWORD` (iCloud app-specific password), optional `SMTP_HOST=smtp.mail.me.com`, `SMTP_PORT=587`, `MAIL_TO`, `SMTP_FROM`.

> Hugging Face free tier no longer allows new Docker Spaces, so this Space uses the **static** SDK. `Dockerfile` / `app.py` remain for local Docker runs with the SMTP mail server.
