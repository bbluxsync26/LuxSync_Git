# LuxSync Brand Asset Migration to v3

**LuxSync LLC** · *Where Luxury Lives Intelligently*

## Objective

Replace the previous generated graphics system with a clean, human-governed v3 asset system while preserving the approved logo masters and curated text-free photography.

## Source of truth

New work must use `brand/assets-v3/`.

The legacy `brand/assets/` directory remains only for:

1. protected approved logo master PNGs,
2. curated text-free scene photography in `12-scenes/`, and
3. temporary compatibility while references are migrated.

Do not use the legacy generated logo, banner, icon, component, card, or product-card assets for new work.

## Replacement map

| Legacy area | v3 replacement |
|---|---|
| `assets/05-palette/` | `assets-v3/01-foundation/approved-palette.svg` |
| `assets/07-components/` | `assets-v3/02-ui/` |
| `assets/02-icons-brand/` + `03-icons-website/` | `assets-v3/03-icons/core-line-icons.svg` |
| `assets/11-banners/` | `assets-v3/04-heroes/` |
| `assets/10-product-cards/` | `assets-v3/05-ecommerce/` |
| ad-hoc stationery/mockups | `assets-v3/06-stationery/` |
| ad-hoc marketing graphics | `assets-v3/07-marketing/` |

## Logo handling

Never regenerate the logo. v3 compositions reference:

- `brand/assets/01-brand/luxsync-monogram-orb.png`
- `brand/assets/01-brand/luxsync-horizontal-lockup.png`

These are treated as immutable raster masters.

## Palette

Only the approved palette is allowed for branded UI/vector graphics:

- Slate Navy `#0D1526`
- Dark Suede `#172036`
- Pale Driftwood `#D0BEB0`
- Warm Taupe Mauve `#9E8B85`
- Antique Rose Taupe `#967878`
- Dusty Steel `#7B96B2`
- Champagne Rose Gold Metallic, `#D6B0A0` anchor

## Typography

- Manrope 500/600 for headings, navigation, buttons, badges, and editable display/UI text.
- Inter 400/500 for body copy, forms, captions, descriptions, and supporting UI.
- Logo lettering is artwork, not a live font.

## Documentation rule

Durable LuxSync documentation, including Markdown, should identify **LuxSync LLC** and reference the v3 branding system where appropriate. Do not embed re-created logos in documentation.
