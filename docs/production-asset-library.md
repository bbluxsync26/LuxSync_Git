# LuxSync Production Visual Library

**Status:** Active / Authoritative delivery-layer reference  
**Brand system:** LuxSync Production Raster v5  
**Omnichannel recovery/build prompt:** PR-BRAND-001

## Scope

LuxSync branding is omnichannel. No single website asset folder defines the whole brand system.

Authoritative supporting locations:

- protected logo masters: `brand/source-logo/`
- visual approval archive: `brand/reference-boards/`
- clean semantic/vector delivery layer: `brand/assets/`
- faithful approved-board masters: `brand/masters/approved-board-raster/`
- faithful approved-board digital exports: `brand/exports/digital/approved/`
- faithful approved-board manifest: `brand/manifests/approved-board-asset-manifest.json`
- account-access digital derivatives: `brand/exports/digital/account-access/`
- omnichannel manifest: `brand/manifests/omnichannel-brand-manifest.json`
- restart/audit state: `brand/audit/`
- governing recovery/build prompt: `prompts/branding/PR-BRAND-001-LuxSync-Omnichannel-Brand-System-Recovery-Audit.md`

## Protected logos

The protected logo masters remain authoritative under `brand/source-logo/`. Production PNG logo copies are byte-identical to those masters. Current logo SVG variants are embedded-raster fidelity containers that preserve exact approved artwork. They are not newly redrawn true-vector logo masters.

Never regenerate, redraw, retype, recolor or approximate LuxSync logo artwork.

## Clean semantic/vector layer

`brand/assets/` remains a validated technically clean delivery layer containing **31 atomic assets / 93 SVG-PNG-WebP files**:

- 3 protected logo deliveries;
- 16 semantic vector icons;
- 12 semantic vector dividers/ornaments.

The icon and divider vectors are useful for scalable interface illustration and live application contexts. They have semantic IDs and clean geometry, and they remain valid.

A full-resolution audit of the approval boards established that these icon/divider vectors are visually simplified. They are therefore a semantic/vector layer, not the sole faithful rendering of the approved LuxSync graphic archive.

## Faithful approved-board layer

Direct visual audit of the original board pixels produced a second, fidelity-first digital layer governed by `brand/manifests/approved-board-asset-manifest.json`.

Current Wave 1 inventory:

- **16 approved metallic icons**;
- **42 approved dividers/accents**;
- **58 reusable approved artworks total**.

Every asset has:

1. raster-origin master PNG under `brand/masters/approved-board-raster/`;
2. byte-identical PNG delivery export under `brand/exports/digital/approved/`;
3. lossless WebP delivery export;
4. SVG fidelity container embedding the exact approved PNG;
5. source-board hash and crop geometry;
6. dimensions and output hashes;
7. `qa_status: passed`;
8. visual QA contact-sheet evidence.

Use the faithful layer where the approved metallic LuxSync artwork itself is part of the intended brand expression. Do not substitute a simplified semantic icon merely because it represents the same concept.

The SVG fidelity containers are explicitly raster-embedded. Do not represent them as newly created editable vector masters.

## Approved-board visual audit

The element-level disposition of all seven boards is recorded in `brand/audit/reference-board-visual-inventory.md`.

The approved boards remain permanent evidence. The audit distinguishes reusable artwork from composition/template families:

- icons and text-free dividers/accents have faithful delivery assets;
- buttons and controls remain semantic live UI;
- section separators with mutable titles remain templates;
- product cards remain composition/marketing references until commerce facts are validated;
- stationery remains a Wave 3 template system because board identity/contact data is illustrative;
- hero/banner examples remain composition references and should use current live copy.

## UI boundary

Buttons, navigation, forms, toggles, cards, product cards, search, tabs and other interactive controls remain semantic HTML/CSS for websites/apps. Do not substitute screenshots for functional UI.

The approval boards define their design language and states. Mutable labels, prices, product facts, support claims, shipping/return statements and other changing facts must stay live and validated.

## Account-access derivative layer

Four text-free production-approved account ambient SVG masters are governed by `website/assets/auth/manifest.json`. Their PNG and lossless WebP derivatives live under `brand/exports/digital/account-access/` with hashes and QA evidence in the omnichannel manifest.

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

Semantic/vector contact sheets:

- `brand/assets/qa/icons-contact-sheet.jpg`
- `brand/assets/qa/dividers-contact-sheet.jpg`

Faithful approved-board contact sheets:

- `brand/audit/qa/approved-icons-board-derived.jpg`
- `brand/audit/qa/approved-dividers-board-derived.jpg`

Account-access derivative QA:

- `brand/audit/qa/account-access-derivatives.jpg`

Contact sheets are QA artifacts only, not deployable graphics.

Automated validation:

- `scripts/validate-production-brand.py`
- `scripts/validate-brand-derivatives.py`
- `scripts/validate-approved-board-assets.py`
- `scripts/validate-repository-consistency.py`

## Production visual strategy

Across channels, LuxSync should use:

- exact protected LuxSync logo artwork;
- faithful approved metallic LuxSync artwork when brand fidelity is intended;
- clean semantic vectors where a simpler scalable UI primitive is technically preferable;
- Slate Navy and Dark Suede architectural fields;
- Pale Driftwood copy;
- Dusty Steel intelligent-light states;
- restrained Champagne Rose Gold premium metallic detail;
- Manrope/Inter live typography where mutable text is appropriate;
- validated product/manufacturer imagery only when tied to validated commerce items;
- clean approved editorial imagery and compositions appropriate to their channel.

Do not bake mutable prices, availability, founder identities, support hours, customer information or unsupported claims into generic reusable brand imagery.

For route-level website usage, see `website/asset-map.md`.

<!-- PR-BRAND-001-WAVE2-DIGITAL-MARKETING -->
## Wave 2 digital marketing delivery layer

Wave 2 is governed by `brand/manifests/wave2-digital-marketing-manifest.json` and provides:

- four social composition frames;
- two presentation frames;
- two campaign frames;
- two 4K static video-overlay frames;
- a live placeholder-driven email signature;
- a live semantic product-card HTML/CSS treatment.

Raster composition masters live under `brand/masters/marketing-art/wave2/`; PNG and lossless WebP deliveries live under `brand/exports/digital/marketing/`. The static templates intentionally omit SVG because they combine protected raster logo artwork with atmospheric raster effects; `brand/templates/digital-marketing/template-specs.json` is the editable governed source.

All ten static frames are intentionally text-safe. Add current copy and validated commerce data at use time rather than baking mutable facts into reusable brand art.
