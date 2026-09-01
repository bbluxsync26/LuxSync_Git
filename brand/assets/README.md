# LuxSync Raster Asset Library

**Status:** Active source library
**Brand system:** LuxSync Production Raster v5

This folder preserves the verified raster import and the exact approved logo copies. Publication status is intentionally explicit so generated composites and board slices cannot accidentally become live website artwork.

## Production-approved

Only these logo files may be published directly from this raster library:

- `01-logos/LuxSync_Logo_Horizontal_Combo.png`
- `01-logos/LuxSync_Logo_Horizontal_Final.png`
- `01-logos/LuxSync_Logo_Orb.png`

They are byte-identical copies of the immutable masters under `brand/source-logo/`.

Never redraw, retype, recolor, regenerate, simplify, or substitute these marks.

## Reference-only raster exports

Folders `02-icons/` through `09-stationery/` are **design-reference exports only**. Visual QA found that some files contain baked/generated copy, generated logo approximations, or board-crop artifacts. They are useful for style direction, but they must not be shipped as website UI, product data, founder information, support information, or public claims.

## VIP Account Access vectors

The clean account-access SVG mini-library intentionally lives outside this Production Raster folder at:

`website/assets/auth/`

That library includes production-approved text-free atmosphere plus reference-only card/input/button diagrams, with publication status governed by:

`website/assets/auth/manifest.json`

The auth vectors are kept outside `brand/assets/` so this raster library remains PNG-only and continues to satisfy `scripts/validate-production-brand.py`.

Production implementation must use:

1. exact protected logo masters from `01-logos/`;
2. live HTML/CSS for headings, buttons, forms, icons, cards, dividers, navigation, Concierge, Contact, and account interactions;
3. validated commerce/manufacturer imagery for real products when available;
4. approved text-free photography or vector atmosphere only when explicitly marked production-approved in its governing manifest;
5. `website/assets/auth/manifest.json` to determine account-access vector publication status.

**Official slogan:** Where Luxury Lives Intelligently
**Metallic blue:** Brushed Dusty Steel `#7B96B2`
**Premium metallic anchor:** Champagne Rose Gold `#D6B0A0`

See `website/asset-map.md` for the route-by-route publication map and `website/pages/account-login.md` for the VIP account-access specification.
