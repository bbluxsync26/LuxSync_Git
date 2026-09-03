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
