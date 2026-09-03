# LuxSync Brand System

**Status:** Active / Authoritative  
**Brand system:** LuxSync Production Raster v5  
**Design DNA:** Plush Drift  
**Voice:** Intelligent Calm

## Omnichannel scope

LuxSync branding is a durable omnichannel system, not a website-only asset collection.

The brand system is intended to support websites/apps, social/digital advertising, email, presentations, video-ready static graphics, business cards, stationery, print collateral, signage, packaging, apparel, embroidery, screen printing, mugs/drinkware, promotional merchandise, vinyl, engraving and future approved channels.

The website consumes this brand system. It does not define, limit or own it.

## Locked brand contract

- Official public slogan: **Where Luxury Lives Intelligently**
- Headings, navigation and UI: Manrope 500/600
- Body and supporting UI: Inter 400/500
- Slate Navy `#0D1526`
- Dark Suede `#172036`
- Pale Driftwood `#D0BEB0`
- Warm Taupe Mauve `#9E8B85`
- Antique Rose Taupe `#967878`
- Dusty Steel `#7B96B2`
- Champagne Rose Gold Metallic `#D6B0A0` anchor
- Brushed Dusty Steel is the only approved metallic-blue treatment.

## Immutable logo masters

The only authoritative logo masters are:

- `brand/source-logo/LuxSync_Logo_Horizontal_Combo.png`
- `brand/source-logo/LuxSync_Logo_Horizontal_Final.png`
- `brand/source-logo/LuxSync_Logo_Orb.png`

Never redraw, retype, recolor, soften, regenerate or approximate them.

## Visual approval archive

`brand/reference-boards/` is permanent approval evidence for approved non-logo visual concepts and brand applications.

Reference boards must not be deleted merely because a website implementation uses semantic HTML/CSS or because an old sliced export was retired. The boards are approval evidence, not production files to be grid-sliced mechanically.

The current element-level interpretation of all seven boards is recorded in `brand/audit/reference-board-visual-inventory.md`.

## Two complementary digital visual layers

### 1. Clean semantic/vector layer

`brand/assets/` remains the validated clean atomic delivery layer. It contains matching SVG, PNG and WebP files for:

- protected logo deliveries;
- 16 clean semantic vector icons;
- 12 clean semantic vector dividers/ornaments.

These assets are technically useful for scalable UI illustration and live application interfaces. They remain valid and are not deleted.

However, direct full-resolution comparison with the approval boards established that the icon and divider families are visually simplified. They must not be described as the only or fully faithful rendering of the approved LuxSync graphic archive.

### 2. Faithful approved-board visual layer

The approved metallic artwork recovered directly from the board pixels is governed by:

- `brand/manifests/approved-board-asset-manifest.json`
- `brand/masters/approved-board-raster/`
- `brand/exports/digital/approved/`
- `brand/audit/qa/approved-icons-board-derived.jpg`
- `brand/audit/qa/approved-dividers-board-derived.jpg`

Current Wave 1 faithful inventory:

- **16 approved metallic icons**
- **42 approved dividers/accents**
- **58 reusable approved artworks total**

Each has a raster-origin PNG master, matching PNG delivery export, lossless WebP export and an SVG fidelity container embedding the exact PNG.

Use this faithful layer when the approved metallic LuxSync artwork itself is part of the intended branded visual treatment. Do not substitute the simpler semantic vector merely because it shares the same icon meaning.

The SVG fidelity containers in this layer are not newly redrawn editable vectors. Do not describe them that way.

## Template/reference families

Direct board review also confirmed that not every approved board element should become a flattened production image.

Keep the following as semantic/template/reference systems unless a specific later deliverable requires a faithful composition:

- button and CTA states;
- section separators containing mutable titles;
- product-card compositions containing conceptual or mutable commerce content;
- stationery layouts containing placeholder identity/contact information;
- UI controls containing mutable content or example claims;
- hero/banner examples containing baked sample copy.

Web/app implementations should use live accessible HTML/CSS and validated data. Print/marketing templates should use current approved facts and identity data.

## Account-access derivative layer

The four production-approved text-free account-access ambient SVG masters are authoritative for that artwork. Governed PNG and lossless WebP derivatives live under `brand/exports/digital/account-access/` with provenance and QA recorded in `brand/manifests/omnichannel-brand-manifest.json`.

Supporting automation:

- `brand/manifests/digital-derivative-jobs.json`
- `scripts/render-brand-digital-derivatives.py`
- `scripts/reconcile-brand-wave1-state.py`
- `scripts/validate-brand-derivatives.py`
- `.github/workflows/build-brand-derivatives.yml`

## Omnichannel audit and recovery state

PR-BRAND-001 governs expansion, recovery and internal audit of the complete omnichannel brand system.

Durable governance/state locations:

- `prompts/branding/PR-BRAND-001-LuxSync-Omnichannel-Brand-System-Recovery-Audit.md`
- `brand/manifests/omnichannel-brand-manifest.json`
- `brand/manifests/approved-board-asset-manifest.json`
- `brand/audit/brand-build-state.json`
- `brand/audit/brand-build-report.md`
- `brand/audit/brand-exceptions.md`
- `brand/audit/reference-board-visual-inventory.md`

Do not force meaningless file types. True vector art may support SVG/PDF/EPS/AI plus PNG/WebP; raster-origin art should preserve a lossless high-quality master and add print/digital derivatives appropriate to its use.

## Canonical implementation references

- `docs/production-source-of-truth.md`
- `docs/production-asset-library.md`
- `website/asset-map.md`
- `website/implementation-manifest.json`
- `website/styles/design-system.md`

<!-- PR-BRAND-001-WAVE2-DIGITAL-MARKETING -->
## Wave 2 digital and marketing kit

PR-BRAND-001 Wave 2 adds a governed reusable digital-marketing layer without turning mutable campaign or commerce content into fixed artwork.

- Governed manifest: `brand/manifests/wave2-digital-marketing-manifest.json`
- Editable composition specs and live templates: `brand/templates/digital-marketing/`
- Raster-origin composition masters: `brand/masters/marketing-art/wave2/`
- PNG and lossless WebP channel exports: `brand/exports/digital/marketing/`
- QA contact sheet: `brand/audit/qa/wave2-digital-marketing.jpg`
- Hash-bound manual QA approval: `brand/audit/wave2-digital-marketing-qa-approval.json`

The kit contains ten text-safe static frames across social, presentations, campaigns and 4K video overlays, plus a live email-signature template and live semantic product-card treatment. Static frames use only exact approved LuxSync logo artwork. Mutable headlines, offers, product facts, prices, ratings, availability and customer information remain live/template-driven.

For new freeform compositions, clean transparent validated dividers under `brand/assets/dividers/` are used to avoid crop-edge seams. The faithful approval-board-derived ornament masters remain preserved separately and unchanged.

## Wave 3 - Print & Physical Brand System

The PR-BRAND-001 Wave 3 source layer is governed by `brand/manifests/wave3-print-physical-manifest.json`.

- Eight approved stationery/print composition templates are delivered as 300-DPI PNG source art, CMYK TIFF companions and exact-page-size PDFs.
- Template sources live under `brand/templates/print-physical/`; print exports live under `brand/exports/print/wave3/`.
- The stationery approval board remains composition evidence. Example identity/contact data from that board is not production data.
- Exact approved LuxSync logo artwork is used unchanged in full-color source compositions.
- Physical placements for signage, apparel, headwear, drinkware, vinyl, engraving and foil are governed by `brand/templates/print-physical/physical-production-specs.json`.
- Vendor-specific one-color, stitch, cut-line, engraving, screen-print and foil conversions are created only after actual production constraints are known. Do not invent them or generatively redraw the logo.
- All physical jobs require final vendor preflight before manufacture.

Wave 3 QA contact sheet: `brand/audit/qa/wave3-print-physical.jpg`.
