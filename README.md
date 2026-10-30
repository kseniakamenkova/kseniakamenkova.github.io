# kseniakamenkova.github.io

Portfolio site of Ksenia Kamenkova, Senior Product Designer — live at https://kseniakamenkova.github.io

Built from the Figma file **Portfolio**. Plain HTML, CSS and a little JavaScript; GitHub Pages serves it with no build step.

## Structure

- `index.html` — main page; `onboarding/`, `referral/`, `product-catalog/`, `payment-widget/` — case studies
- `assets/css/style.css` — all styles (desktop values match the 1512px Figma frames)
- `assets/js/main.js` — drag and keyboard scrolling for the image carousels
- `assets/img/` — images exported from Figma at 2x (WebP)
- `assets/fonts/` — Inter, self-hosted (SIL Open Font License)
- `_src/` — source for the pages (not published): `content.py` holds all copy, `rows.json` lists carousel images, `build.py` writes the HTML

## Updating

Edit the copy in `_src/content.py`, then run `python3 _src/build.py` and commit the regenerated HTML.
