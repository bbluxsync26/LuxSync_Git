# LuxSync Production Visual Library

**Status:** Active / Authoritative delivery-layer reference  
**Brand system:** LuxSync Production Raster v5  
**Current digital delivery library:** 6.0 clean atomic triple-format  
**Omnichannel recovery/build prompt:** PR-BRAND-001

## Scope

LuxSync branding is omnichannel. The current `brand/assets/` tree is the validated clean **digital delivery layer**, not the entire brand universe.

The complete brand system also preserves approval evidence, future masters, print/physical exports, stationery, merchandise, marketing and motion-ready static artwork. The website consumes this system; it does not define or limit it.

Authoritative supporting locations:

- protected logo masters: `brand/source-logo/`
- visual approval archive: `brand/reference-boards/`
- current clean digital delivery layer: `brand/assets/`
- omnichannel manifest: `brand/manifests/omnichannel-brand-manifest.json`
- restart/audit state: `brand/audit/`
- governing recovery/build prompt: `prompts/branding/PR-BRAND-001-LuxSync-Omnichannel-Brand-System-Recovery-Audit.md`

## Current production-safe digital assets

Every reusable production graphic currently completed under `brand/assets/` has three corresponding files with the same semantic basename:

1. SVG
2. transparent PNG where appropriate
3. WebP

The current clean digital delivery library contains **31 approved atomic assets and 93 format-specific production files**.

Current completed families:

- `brand/assets/logos/`
- `brand/assets/icons/`
- `brand/assets/dividers/`

The protected logo masters remain authoritative under `brand/source-logo/`. Production PNG logo copies are byte-identical to those masters. Current logo SVG variants are **embedded-raster fidelity containers** that preserve the exact approved artwork rather than retyping or reconstructing the wordmark; they are not represented as newly redrawn true-vector logo masters.

## Atomic icon library

The icon family was rebuilt as clean semantic vector artwork. Each icon contains one intended symbol only, with consistent optical scale, padding, stroke treatment and approved LuxSync metallic colors.

No production icon may contain:

- a neighboring icon or partial neighboring icon;
- presentation-board labels or headings;
- crop borders or grid lines;
- malformed generated text;
- generated LuxSync logo approximations.

The old numbered grid-sliced icon files were retired.

## Dividers and ornamental accents

Dividers, badge underlines, corners and orbit strokes are true vector assets under `brand/assets/dividers/`, with matching PNG and WebP exports. They are decorative graphics only and contain no mutable business copy.

## Reference boards remain authoritative approval evidence

Retiring malformed sliced exports did **not** revoke the visual concepts approved on the boards under `brand/reference-boards/`.

Those boards are permanent approval evidence for the wider brand system, including concepts that may later become:

- print/stationery components;
- marketing compositions;
- merchandise/apparel artwork;
- signage/packaging elements;
- video-ready static overlays;
- email/social/presentation assets;
- website-supporting graphics;
- semantic UI references.

Do not grid-slice the boards into production files. Visually identify each intended element, reuse a matching clean asset when one exists, and create a new faithful master only when the approved element is genuinely missing.

## UI boundary

Buttons, navigation, forms, toggles, cards, product cards and other interactive controls remain semantic HTML/CSS for websites/apps. Do not substitute screenshots for functional UI.

Their approved appearance may still be durable brand reference and may inform other channels, marketing templates, presentations, video graphics or print collateral. Do not delete approval evidence merely because the website implementation is semantic.

## Omnichannel format strategy

Do not force every asset into every format.

### True vector artwork

Preferred chain where technically appropriate:

`AI or genuine vector master → SVG → PDF → EPS → PNG → WebP`

### Raster-origin artwork

Preferred chain where technically appropriate:

`highest-quality lossless raster master → high-resolution PNG/TIFF → print PDF → PNG/WebP delivery`

An SVG wrapper may be used around exact raster art when operationally useful, but it must be identified as embedded raster rather than a true editable vector.

### Specialty physical production

Create only when justified by the asset/use case:

- one-color black;
- reversed white;
- screen-print simplified art;
- embroidery-friendly art;
- engraving/etching art;
- vinyl/cut-line-friendly art;
- foil/spot-metallic production art.

Champagne Rose Gold used as a physical metallic finish should be handled as a production treatment such as foil, metallic ink or documented spot-color intent, not flattened casually into a peach substitute.

## Visual QA

Current rendered contact sheets are stored under:

- `brand/assets/qa/icons-contact-sheet.jpg`
- `brand/assets/qa/dividers-contact-sheet.jpg`

The contact sheets are QA artifacts only. They are not published as website graphics.

The current digital delivery manifest is `brand/assets/asset-manifest.json`. Every approved entry must retain `production_status: approved` and `qa_status: passed`, plus valid SVG, PNG and WebP hashes.

The broader omnichannel state and asset dispositions are governed by:

- `brand/manifests/omnichannel-brand-manifest.json`
- `brand/audit/brand-build-state.json`
- `brand/audit/brand-build-report.md`
- `brand/audit/brand-exceptions.md`

## Production visual strategy

Across channels, LuxSync should use:

- exact protected LuxSync logo artwork;
- clean LuxSync icons and ornaments;
- Slate Navy and Dark Suede architectural fields;
- Pale Driftwood copy;
- Dusty Steel intelligent-light states;
- restrained Champagne Rose Gold premium metallic detail;
- Manrope/Inter live typography where mutable text is appropriate;
- validated product/manufacturer imagery only when tied to validated commerce items;
- clean approved editorial imagery and compositions appropriate to their channel.

Do not bake mutable prices, availability, founder identities, support hours, customer information or unsupported claims into generic reusable brand imagery.

For route-level website usage, see `website/asset-map.md`.
