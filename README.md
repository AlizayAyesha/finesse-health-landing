# Finesse Health & Co. — International Dental Concierge (static site)

Local preview only. **Do not deploy or push to GitHub** unless the client explicitly requests it.

## Positioning (critical)

Finesse Health & Co. is an **International Dental Concierge & Patient Coordination Service** connecting Australian patients with accredited dental specialists in India.

It is **NOT** a healthcare provider, clinic, or hospital. Clinical assessments, diagnoses, surgeries, and warranties are provided exclusively by treating dental clinics in India. Site copy must never imply Finesse delivers clinical care.

## Preview

```bash
cd /workspace/finesse-health
python3 -m http.server 8765
```

Open http://127.0.0.1:8765/

## Pages

| Path | Purpose |
|------|---------|
| `index.html` | Landing page (hero, how it works, services facilitated, about, enquiry form, contact) |
| `terms-and-disclaimer.html` | Full Terms of Service & Medical Disclaimer (verbatim from client brief) |
| `privacy.html` | Privacy Policy draft aligned with Australian Privacy Principles |
| `docs/client-brief-2026-10-05.md` | Saved client brief for reference |

## Brand & assets

- Palette: navy `#253350`, sage `#90A28B`, paper `#F4F0EA`, text-sage `#4B6650`
- Fonts: Montserrat (headings), Source Sans 3 (body)
- `assets/` — logos (SVG + PNG), reversed/white variants, favicons, og-image
- `css/styles.css`, `js/main.js`, `site.webmanifest`

## Contact (footer)

- Address: Level 1, 93 George Street, Parramatta, NSW 2150
- Email: finessehealthandco@gmail.com.au
- Phone: +61 448 415 873 (`tel:+61448415873`)

## Enquiry form — backend wiring needed

The lead form (`#enquiry`) is **front-end only**. On valid submit it shows a success message and does **not** send data to a server.

Before go-live, wire one of:

1. A serverless endpoint (e.g. Cloudflare Worker / Railway) that accepts multipart form data, stores metadata, and securely handles file uploads; or
2. A form provider (Formspree, Basin, Getform, etc.) with HTTPS file upload support; or
3. `mailto:` is **not** recommended for dental records (sensitive health data).

Also ensure:

- Explicit consent storage for overseas disclosure of health data (see Terms §4 / Privacy §5)
- Secure storage and retention policy for OPG/X-ray uploads
- Confirmation email to the client and internal notification to coordinators

## Screenshots

`screenshots/` — full-page captures:

- `home-mobile-390.png`, `home-desktop-1440.png`
- `terms-mobile-390.png`, `terms-desktop-1440.png`

Regenerate with `src/shoot.py` while the local server is running (after updating paths in the script if needed).

## Source scripts

`src/` — logo build / screenshot helpers from the brand asset phase (`build_mark.py`, `wordmark.py`, `make_assets.py`, `shoot.py`).
