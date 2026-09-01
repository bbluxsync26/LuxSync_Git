# LuxSync Production Visual Library

**Status:** Active / Authoritative
**Brand system:** LuxSync Production Raster v5
**Production asset library:** 6.0 clean atomic triple-format

## Production-safe assets

The deployable LuxSync graphic library is `brand/assets/`.

Every reusable production graphic has three corresponding files with the same semantic basename:

1. SVG
2. transparent PNG where appropriate
3. WebP

The current clean production families are:

- `brand/assets/logos/`
- `brand/assets/icons/`
- `brand/assets/dividers/`

The protected logo masters remain authoritative under `brand/source-logo/`. Production PNG logo copies are byte-identical to those masters. The SVG logo variants are fidelity containers that preserve the exact approved artwork rather than retyping or reconstructing it.

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

## UI boundary

Buttons, navigation, forms, toggles, cards, product cards and other interactive controls remain semantic HTML/CSS. Do not substitute screenshots for live UI.

## Visual QA

Rendered contact sheets are stored under:

- `brand/assets/qa/icons-contact-sheet.jpg`
- `brand/assets/qa/dividers-contact-sheet.jpg`

The contact sheets are QA artifacts only. They are not published as website graphics.

The production manifest is `brand/assets/asset-manifest.json`. Every approved entry must have `production_status: approved` and `qa_status: passed`, plus valid SVG, PNG and WebP hashes.

## Production visual strategy

The launch website should compose its visual language live using:

- exact LuxSync logo artwork;
- clean LuxSync SVG icons and ornaments;
- Slate Navy and Dark Suede architectural fields;
- Pale Driftwood copy;
- Dusty Steel interaction states;
- restrained Champagne Rose Gold premium detail;
- Manrope/Inter live typography;
- CSS-built cards, controls, forms and responsive layouts;
- validated product/manufacturer imagery only when tied to a validated commerce item;
- clean text-free editorial photography only after explicit approval.

This prevents prices, availability, founder identities, support hours, slogans or other mutable information from being baked into production imagery.

See `website/asset-map.md` for route-level usage rules.
