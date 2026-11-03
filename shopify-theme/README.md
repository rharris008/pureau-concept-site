# Pureau Shopify theme ("Pureau new", theme #159700156606 on pureau-au)

Source of truth for the Shopify theme generated from `index.html`.

- `build.py` — regenerates `/workspace/pureau-shopify-theme/theme` from `index.html`:
  layout (shared head), `snippets/site-header.liquid` + `snippets/site-footer.liquid` (shared on every
  template; menu anchors become `/#anchor` off the home page), `sections/pureau-home.liquid`, `sections/apps.liquid`, `templates/index.json`.
- `extra/` — storefront sections/templates/snippets/CSS copied in by `build.py`: collection (default sort price high→low,
  sort select, pagination), list-collections, product, cart, search, page, page.contact, blog, article, 404, password,
  customers/* (legacy accounts; the store currently uses Shopify-hosted new customer accounts).

Build + push (never publish):

    cp build.py /workspace/pureau-shopify-theme/ && cp -r extra /workspace/pureau-shopify-theme/
    cd /workspace/pureau-shopify-theme && python3 build.py && shopify theme check --path theme
    shopify theme push --store pureau-au --path theme --theme 159700156606 --ignore config/settings_data.json

`--ignore config/settings_data.json` keeps the App embeds (Instafeed) set in the theme editor.
