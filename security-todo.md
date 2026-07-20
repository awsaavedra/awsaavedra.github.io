# Security

## Completed
- [x] Content Security Policy (CSP) meta tag
- [x] Strict referrer policy (`strict-origin-when-cross-origin`)
- [x] `rel="noopener noreferrer"` on all `target="_blank"` links
- [x] Subresource Integrity (SRI) on all CDN-loaded scripts
- [x] HTTP → HTTPS upgraded across all content links
- [x] Hugo generator meta tag removed (no version fingerprinting)
- [x] Local dev server security headers (`hugo server` mirrors production)
- [x] `static/.well-known/security.txt`
- [x] AI crawler blocking (`robots.txt`, `noai` meta tag, `tdm-reservation`)
- [x] Dependabot enabled for GitHub Actions (weekly SHA pinning) and theme submodule
- [x] Minimal `permissions` blocks on all GitHub Actions workflows
- [x] Hugo binary SHA256 checksum verified in CI before install

## Accepted Risks (single-author static site)
- **`goldmark.renderer.unsafe = true`**: required for raw HTML in markdown (YouTube embeds, etc.). Would be an XSS vector if untrusted contributors were ever added.
- **Link rot → domain hijacking**: outbound links to lapsed domains could be bought by bad actors. Audit periodically; no automated fix without a link-checker CI step.
- **`security.txt` expires annually**: update `Expires` in `static/.well-known/security.txt` each year.

## TODO (requires GitHub / Cloudflare / DNS dashboard)
1. **Cloudflare - Response Header Transform Rule**: set `Strict-Transport-Security`, `X-Frame-Options`, `X-Content-Type-Options`, `Permissions-Policy`, `Cross-Origin-Opener-Policy`, `Cross-Origin-Embedder-Policy`, `Cross-Origin-Resource-Policy`, and production CSP (mirror `Content-Security-Policy` under `[server.headers]` in `config.toml`)
2. **Cloudflare - DNSSEC**: DNS → Settings → DNSSEC → Enable
3. **Cloudflare - SSL mode**: SSL/TLS → Full (Strict); confirm GitHub Pages → Enforce HTTPS is checked
4. **DNS - DMARC**: add `_dmarc.awsaavedra.com` TXT record; start `p=none` to monitor, escalate to `p=quarantine` → `p=reject`
5. **DNS - SPF hard-fail**: update `awsaavedra.com` TXT record, change `~all` to `-all`
6. **DNS - CAA records**: restrict certificate issuance to known CAs; add `iodef` alert address
7. **HSTS Preload**: submit at `https://hstspreload.org` after Cloudflare HSTS header is confirmed live
8. **GitHub - Branch protection**: Settings → Branches → require PR + review on `main`; prevent force-push
9. **GitHub - Secret scanning**: Settings → Security → Secret scanning → Enable
