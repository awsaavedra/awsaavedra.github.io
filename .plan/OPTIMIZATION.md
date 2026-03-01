# Site Optimization Plan

Site: awsaavedra.github.io — Hugo 0.143.0, bear blog theme, GitHub Pages

---

## Status

| Tier | Optimization | Status |
|------|-------------|--------|
| 1 | Hugo upgrade 0.91.2 → 0.143.0 | ✅ Done |
| 1 | Conditional KaTeX loading | ✅ Done |
| 1 | GitHub Actions build caching | ✅ Done |
| 2 | Image compression → WebP (82% reduction) | ✅ Done |
| 4 | Font Scriptin.ttf → WOFF2 (51% smaller) | ✅ Done |
| 3 | Cloudflare Pages (CDN, Brotli, HTTP/2) | ⬜ Pending |

---

## Tier 1 — Quick Wins ✅

### Hugo Upgrade
- **File:** `.github/workflows/gh-pages.yml`
- Changed `hugo-version` from `0.91.2` → `0.143.0`, enabled `extended: true`
- Impact: faster partial caching, modern image processing APIs, security fixes

### Conditional KaTeX
- **File:** `layouts/partials/custom_head.html`
- KaTeX CSS + JS now wrapped in `{{ if .Params.math }}` — only loads when a post has `math: true`
- To enable math on a post: add `math: true` to its front matter
- Impact: saves ~300KB of CSS+JS on every non-math page load

### CI Build Caching
- **File:** `.github/workflows/gh-pages.yml`
- Added `actions/cache@v3` step caching Hugo's resource dir at `/tmp/hugo_cache`
- Impact: ~30s faster CI on repeat pushes

---

## Tier 2 — Image Optimization ✅

Bulk-converted all `/static/` PNG/JPG/JPEG/GIF → WebP using Python/Pillow.

| Before | After | Reduction |
|--------|-------|-----------|
| 16.5 MB | 3.0 MB | **82%** |

Notable savings:
- `rorschach-sloggoth.png`: 2.4 MB → 151 KB (94%)
- `dictator-wheel.gif`: 3.5 MB → 749 KB animated WebP (79%)
- `judowsky-dune.png`: 1.3 MB → 94 KB (93%)

All 12 posts with local image references updated to `.webp` extensions.
Original files deleted.

---

## Tier 3 — Cloudflare Pages ⬜

No code changes needed — this is a DNS/infrastructure switch.

Steps:
1. Create a Cloudflare Pages project pointing at the same GitHub repo
2. Set build command: `hugo --minify` and output dir: `public`
3. Set env var `HUGO_VERSION=0.143.0`
4. Update DNS CNAME from GitHub Pages → Cloudflare Pages URL
5. Optionally disable `peaceiris/actions-gh-pages` in the workflow once Cloudflare is building

Benefits:
- Global edge CDN (better latency than GitHub Pages)
- Automatic Brotli compression (GitHub Pages only uses gzip)
- HTTP/2 out of the box
- Free tier, zero-config custom domain

Verify after: `curl -I https://awsaavedra.com/path/to/image` — look for `content-encoding: br`

---

## Tier 4 — Font ✅

- Converted `static/fonts/Scriptin.ttf` (81 KB) → `Scriptin.woff2` (39 KB, 51% smaller)
- Updated `@font-face` in `custom_head.html` with WOFF2 as primary, TTF as fallback
- Added `font-display: swap` to prevent render-blocking

---

## Testing Locally

### Simulate GitHub Actions with `act`

`act` is installed at `~/.local/bin/act` and requires Docker (already available).

```bash
# Dry run — show what would execute without running it
act -n

# Run the full deploy workflow (uses a local Docker container)
act push

# Run with a specific job
act push --job deploy

# Use a smaller Docker image (faster, less faithful)
act push -P ubuntu-22.04=catthehacker/ubuntu:act-22.04
```

On first run, `act` will ask which Docker image size to pull (micro/medium/large).
The `catthehacker/ubuntu:act-22.04` medium image is a good balance of speed and compatibility.

### Check build output locally

```bash
hugo server          # dev server with live reload
hugo --minify        # production build → ./public
du -sh public/       # check output size
```

### After deploying, verify with Lighthouse

- https://pagespeed.web.dev — paste awsaavedra.com
- https://www.webpagetest.org — full waterfall view
