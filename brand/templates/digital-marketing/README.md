# LuxSync Wave 2 Digital Marketing Templates

**Status:** Active / PR-BRAND-001 Wave 2  
**Brand system:** LuxSync Production Raster v5  
**Design DNA:** Plush Drift  
**Official slogan:** Where Luxury Lives Intelligently

## Purpose

This directory contains reusable, channel-ready composition templates for broader digital and marketing use. The templates extend approved LuxSync visual language without flattening mutable copy, customer information, product data, pricing, availability, testimonials, or unsupported claims into generic brand artwork.

The exact LuxSync logo artwork remains protected and immutable. Static templates may composite only the approved delivery copies under `brand/assets/logos/png/`. Reusable metallic ornaments come from the visually faithful approved-board layer under `brand/exports/digital/approved/dividers/`.

## Static composition set

`template-specs.json` governs ten text-safe static compositions:

- social square — 1080×1080
- social portrait — 1080×1350
- social story — 1080×1920
- social landscape — 1200×628
- presentation title — 1920×1080
- presentation section — 1920×1080
- campaign landscape — 1600×900
- campaign square — 1080×1080
- video corner-bug overlay — 3840×2160 transparent
- video lower-third overlay — 3840×2160 transparent

Generated PNG and lossless WebP outputs live under `brand/exports/digital/marketing/` and are governed by `brand/manifests/wave2-digital-marketing-manifest.json`.

These frames deliberately leave copy-safe areas blank. Add campaign copy, headlines, dates, calls to action, product data, or offer details at use time using current approved content and validated commerce facts.

## Live/template components

### Email signature

`email/luxsync-email-signature.html` is a table-based email-compatible component with live placeholders for name, title, contact fields, and the hosted exact approved logo URL. Do not replace the logo with retyped text or an approximation.

### Product card

`product-card/product-card-template.html` + `product-card/product-card.css` implement the approved product/category-card visual language as live semantic markup. They intentionally contain placeholders rather than example products or prices from the approval boards.

## Safe usage rules

- Use Manrope 500/600 for headings, labels and CTA text where supported.
- Use Inter 400/500 for body and supporting information.
- Preserve Slate Navy, Dark Suede, Dusty Steel and restrained Champagne Rose Gold relationships.
- Keep product imagery, product names, prices, ratings, availability and compatibility live and validated.
- Do not publish the conceptual product renders or example prices shown on historical approval boards as real commerce data.
- Keep meaningful text accessible and editable rather than baking it into raster frames.
- Video overlays are static motion-ready source assets, not finished animation packages.
- Presentation frames are background/source assets; editable deck content remains live in the presentation application.

## Build and QA

- Build: `python scripts/build-wave2-digital-marketing.py`
- Validate: `python scripts/validate-wave2-digital-marketing.py`
- QA contact sheet: `brand/audit/qa/wave2-digital-marketing.jpg`

The build is deterministic and idempotent. Existing outputs are regenerated only when governed source specifications or approved source artwork changes.
