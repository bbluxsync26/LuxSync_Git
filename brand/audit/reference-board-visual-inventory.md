# LuxSync Reference-Board Visual Inventory

**Prompt:** PR-BRAND-001  
**Status:** Wave 1 visual audit complete  
**Visual source:** full-resolution originals under `brand/reference-boards/`  
**Audit branch:** `feature/brand-board-visual-audit`

## Purpose

This inventory records what the seven approved LuxSync reference boards actually contain and how each family should be preserved or implemented. The boards are approval evidence. They are not permission to restore malformed legacy grid slices, bake mutable text into images, invent product facts, or approximate protected logos.

## 1. Approved brand board

`brand/reference-boards/approved_brand_board.png`

Approved visual direction includes the protected LuxSync logo family, palette and metallic language, metallic capability icons, Plush Drift button examples, product-card composition examples, hero/banner composition examples, divider/accent examples, stationery examples, and UI examples.

Disposition:

- Protected logos remain governed only by `brand/source-logo/` masters.
- Reusable metallic icon and divider art is produced from the dedicated icon/divider boards.
- Hero examples are composition references because their copy is baked into the board; use current live copy in production.
- Product-card, stationery, button, and UI examples remain composition/template references where content is mutable.

## 2. Icons board

`brand/reference-boards/icons_board.png`

The board contains 16 approved metallic icons:

1. Security
2. Lighting
3. Climate
4. Music
5. Shades
6. Locks
7. Concierge
8. Installation
9. Support
10. Automation
11. Energy
12. Camera
13. FAQ
14. Phone
15. Calendar
16. Location

Direct visual comparison found that the earlier 16 clean semantic icons are semantically aligned but visually simplified. They are not faithful reproductions of the approved metallic board artwork.

Wave 1 therefore creates 16 faithful board-derived raster-origin masters and matching PNG, lossless WebP, and SVG fidelity-container exports. Stable IDs remain aligned with the semantic names already used by the website.

## 3. Dividers board

`brand/reference-boards/dividers_board.png`

The board contains a substantially broader approved decorative system than the earlier 12 simplified production dividers.

Wave 1 identifies 42 reusable text-free divider/accent artworks:

- 8 horizontal divider treatments;
- 3 standalone sparkle treatments;
- 6 sparkle-divider treatments;
- 7 metallic line/bar treatments;
- 4 badge-underline treatments;
- 4 orbit treatments;
- 10 corner/standalone ornament treatments.

The same board also contains 4 section-separator compositions with placeholder `SECTION` text. Those remain template/reference-only. Production separators should preserve the approved layout language while rendering real section titles as live text.

## 4. Buttons board

`brand/reference-boards/buttons_board.png`

Approved language includes primary, secondary, outline, ghost, inverted and disabled buttons; default/hover/pressed states; icon buttons; pill CTAs; text links; and a supporting value-proposition icon band.

Disposition: semantic live UI/reference. Do not ship flattened button screenshots with baked copy. Implement with current Plush Drift tokens, live accessible text, keyboard/focus states, and reduced-motion behavior. Reusable non-UI ornaments may be promoted separately if needed.

## 5. Product cards board

`brand/reference-boards/product_cards_board.png`

Approved composition direction includes six smart-home category cards: Smart Hubs, Lighting, Security, Shades, Climate and Audio.

Disposition: marketing/composition template. The board demonstrates LuxSync visual treatment, not validated live commerce inventory. Conceptual device imagery, descriptions, pricing, availability or other mutable commerce facts must not be promoted as real catalog data without validation from the commerce/manufacturer source of truth.

## 6. Stationery board

`brand/reference-boards/stationery_board.png`

Approved composition direction includes business-card front/back, letterhead, envelope, note card, invoice/header treatments and document-cover accents.

Disposition: Wave 3 print/template system. The board contains example/placeholder identity and contact information, so the board itself is not a production stationery file. Rebuild templates with current approved LuxSync identity and real data, then produce print-ready formats appropriate to the specific piece.

## 7. UI controls board

`brand/reference-boards/ui_controls_board.png`

Approved interface direction includes quantity controls, dropdowns, tabs, pagination, search, chips, toggles, accordion/FAQ rows, modal/header patterns, breadcrumbs, form states, radios/select chips and product-meta/value-proposition examples.

Disposition: semantic live UI/reference. Some example merchandising/service claims on the board are not validated business facts. They must not be baked into production graphics or published unless separately confirmed.

## Board-fidelity conclusion

The prior clean 31-asset library remains useful as a semantic/vector delivery layer and is not deleted by this audit. However, direct visual review invalidates the assumption that its simplified icon and divider families fully represent the approved visual archive.

The faithful approved visual layer is now governed separately by:

- `brand/manifests/approved-board-asset-manifest.json`
- `brand/masters/approved-board-raster/`
- `brand/exports/digital/approved/`
- `brand/audit/qa/approved-icons-board-derived.jpg`
- `brand/audit/qa/approved-dividers-board-derived.jpg`

The Wave 1 board-derived set contains **58 reusable approved artworks: 16 metallic icons and 42 dividers/accents**.

## Format note

These 58 masters are raster-origin because the approved boards are the available visual authority. Their SVG files are explicitly labeled embedded-raster fidelity containers. They are not represented as newly redrawn editable vector art.

Where transparency, true vectors, one-color production, embroidery, engraving, foil, EPS/PDF/TIFF or other specialty output is required, create a technically justified derivative in the appropriate later wave without altering the approved master appearance.
