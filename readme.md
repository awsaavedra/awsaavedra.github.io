# awsaavedra.github.io

Personal website and blog for Alexander Saavedra, built with Hugo and deployed to GitHub Pages.

Live at: [awsaavedra.com](https://awsaavedra.com)

---

## Objective

A fast, minimal, self-hosted personal site for publishing articles, documentation, projects, and notes. 
The design philosophy prioritizes simplicity: plain text where possible, no tracking, ejectable from anywhere, no JavaScript ever, and full ownership of content and subscriber data.

---

## Quickstart

**Prerequisites:** [Hugo extended](https://gohugo.io/installation/) v0.143.0+, Git

```bash
git clone --recurse-submodules https://github.com/awsaavedra/awsaavedra.github.io.git
cd awsaavedra.github.io
hugo server -D
```

The site will be available at `http://localhost:1313`. The `-D` flag includes draft posts.

---

## Features & Design

- **Minimal theme** — uses [hugo-bearblog](https://github.com/janraasch/hugo-bearblog), a bear-bones theme with no bloat. Customized via `layouts/` and `static/`.
- **Server-side LaTeX** — math equations rendered at build time using Hugo's Goldmark passthrough extension. No MathJax JavaScript shipped to the browser. Enable per-post with `enableMathJax: true` in front matter.
- **WebP image pipeline** — all images in `static/` are served as WebP. The `convert-images.py` script converts PNG/JPG/JPEG/GIF to WebP at quality 80, skipping animated GIFs and already-converted files.
- **Newsletter (Derek Sivers style)** — plain-text email notifications sent via Python scripts and an SMTP relay. No fancy templates, no tracking pixels, no third-party marketing platforms. Subscribers stored in a plain text file under your control.
- **Netlify Forms** — subscription form in the footer uses a math challenge for bot prevention. Submissions are reviewed manually before adding anyone to the list.
- **Reading time** — enabled globally via `enableReadingTime = true` in `config.toml`.
- **Syntax highlighting** — Dracula theme, rendered server-side (no client-side highlight.js).
- **Privacy-first** — no analytics, no tracking pixels, no ads.

---

## Architecture

```
awsaavedra.github.io/
├── .github/workflows/       # CI/CD: build + deploy to GitHub Pages
├── archetypes/              # Hugo content templates (default.md, posts.md)
├── content/                 # All site content (Markdown)
│   ├── posts/               # Blog articles
│   ├── documentation.md
│   ├── projects.md
│   ├── quotes.md
│   ├── disclaimers.md
│   └── now.md
├── layouts/                 # Template overrides on top of the theme
│   ├── _default/
│   └── partials/
├── static/                  # Static assets served at /
│   ├── fonts/
│   └── *.webp               # All images converted to WebP
├── themes/hugo-bearblog/    # Theme (git submodule)
├── config.toml              # Site configuration
├── convert-images.py        # Image → WebP conversion script
└── serve.sh                 # Convenience wrapper for local dev server
```

**Deployment:** Pushing to `main` triggers the GitHub Actions workflow (`.github/workflows/gh-pages.yml`), which builds the site with `hugo --minify` and deploys the `public/` output to GitHub Pages.

---

## Stack

| Layer | Tool |
|---|---|
| Static site generator | [Hugo extended](https://gohugo.io/) v0.143.0 |
| Theme | [hugo-bearblog](https://github.com/janraasch/hugo-bearblog) |
| Hosting | GitHub Pages |
| CI/CD | GitHub Actions |
| Forms | Netlify Forms |
| Email / Newsletter | Python + SMTP relay (smtp2go.com or similar) |
| Image format | WebP (converted via Pillow) |
| Math rendering | Goldmark passthrough + KaTeX (server-side) |

---

## Commands

```bash
# Start local dev server (includes drafts)
hugo server -D

# Build site for production
hugo --minify

# Create a new blog post
hugo new content/posts/my-post-title.md

# Get Hugo help
hugo -h
```

A convenience wrapper is also available:

```bash
./serve.sh   # equivalent to: hugo serve
```

---

## Scripts & Usage

### `convert-images.py` — WebP image conversion

Converts PNG, JPG, JPEG, and static GIF files under `static/` to WebP (quality 80). Originals are deleted after successful conversion. Animated GIFs and already-converted files are skipped.

**Prerequisites:** Python 3, Pillow (`pip install Pillow`)

```bash
# Preview what would be converted (no files modified)
python3 convert-images.py --dry-run

# Convert all eligible images
python3 convert-images.py
```

### Newsletter scripts (in `newsletter/`)

Plain-text subscriber management and email sending. No database required.

**SMTP configuration** — set environment variables before sending:

```bash
export SMTP_HOST="smtp2go.com"
export SMTP_PORT="2525"
export SMTP_USERNAME="your_username"
export SMTP_PASSWORD="your_password"
export FROM_EMAIL="your@email.com"
export FROM_NAME="Alexander Saavedra"
```

**Manage subscribers:**

```bash
# Add a confirmed subscriber
python newsletter/manage-subscribers.py add john@example.com

# Remove a subscriber
python newsletter/manage-subscribers.py remove john@example.com

# List all subscribers
python newsletter/manage-subscribers.py list

# Export to CSV (for Listmonk import)
python newsletter/manage-subscribers.py export subscribers.csv
```

Subscribers are stored in `newsletter/subscribers.txt` (one email per line).

**Send a newsletter:**

Create a plain-text message file, e.g. `new-article.txt`:

```
Subject: New article: My Post Title

Hi there,

I just published a new article about [topic].

Read it here: https://awsaavedra.com/posts/my-post-title/

- Alex
```

```bash
# Dry run — preview output without sending
python newsletter/send-newsletter.py new-article.txt --dry-run

# Send to all subscribers
python newsletter/send-newsletter.py new-article.txt
```

**Export for Listmonk** (optional, for advanced sending features):

```bash
python newsletter/export-to-listmonk.py
# Then import the generated CSV via Listmonk admin → Subscribers → Import
```

### Subscriber workflow (double opt-in)

1. User submits the footer form → Netlify sends you a notification.
2. Send a personal welcome email and wait for a reply to confirm.
3. Add the confirmed address: `python newsletter/manage-subscribers.py add email@example.com`
4. When a new article publishes, draft a message file and run `send-newsletter.py`.

---

## Optimizations

| What | Result |
|---|---|
| Hugo 0.91.2 → 0.143.0 | Faster builds, modern image APIs, security fixes |
| Conditional KaTeX loading | KaTeX CSS/JS (~300KB) only loads on posts with `math: true` in front matter |
| GitHub Actions build cache | ~30s faster CI on repeat pushes via `actions/cache` on Hugo's resource dir |
| PNG/JPG → WebP conversion | 16.5MB → 3.0MB (82% reduction) across all `static/` images |
| Scriptin.ttf → WOFF2 | 81KB → 39KB (51% smaller), with `font-display: swap` to avoid render-blocking |
