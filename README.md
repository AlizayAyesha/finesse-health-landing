# Finesse Health & Co. — brand assets + landing page (local preview)

Preview: `python3 -m http.server 8765` in this folder → http://127.0.0.1:8765/

- `index.html`, `css/styles.css`, `js/main.js`, `site.webmanifest` — static landing page
- `assets/` — logos (SVG + PNG), reversed/white variants, favicons, og-image, extracted raster logo, compare-logo.png
- `screenshots/` — full-page renders at 390px (2x DPR) and 1440px
- `src/` — reproducible build scripts:
  - `build_mark.py` (caduceus geometry, shapely boolean ops → pure filled paths)
  - `wordmark.py` (Montserrat outlined to paths via fontTools)
  - `make_assets.py` (all SVG/PNG/ICO exports), `extract_and_compare.py`, `shoot.py`
- `source-card.png` — original mockup

Placeholders (marked with HTML comments in index.html): service list, opening hours.
Palette: navy #253350, sage #90A28B (sampled), paper #F4F0EA, text-sage #4B6650.
