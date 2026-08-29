# LuxSync Brand Asset Library

**Plush Drift v2.1 — Web Graphics Collection**

> Where warmth meets intelligence. Where luxury feels like home.

## Authority and precedence

The current LuxSync brand standards in `brand/` are authoritative. For typography, **Manrope** is the headline/display font and **Inter** is the body/UI font. Any older generated asset metadata or embedded SVG declarations that reference Century Gothic or Candara are legacy implementation artifacts and do not override the active brand standard.

The official LuxSync slogan is **Where Luxury Lives Intelligently**.

## Current library

The library contains **97 logical graphics** across 11 numbered asset categories. Most graphics are supplied in SVG, PNG, and WebP formats.

The original 96-graphic pack was expanded by the later `hero-where-luxury-lives-intelligently` banner set.

## Color palette

| Role | Color | Hex |
|---|---|---|
| Primary Background | Slate Navy | `#0D1526` |
| Card Surface | Dark Suede | `#172036` |
| Primary Text | Pale Driftwood | `#D0BEB0` |
| Secondary Text | Warm Taupe Mauve | `#9E8B85` |
| Tertiary Accent | Antique Rose Taupe | `#967878` |
| Primary Accent | Dusty Steel | `#7B96B2` |

## Typography

| Role | Standard | Recommended weights |
|---|---|---|
| Headlines / Display | Manrope | 500, 600 |
| Body / UI | Inter | 400, 500 |

For website implementation, render important text in HTML/CSS with these fonts whenever practical. Do not treat legacy font names embedded in older generated assets as current standards.

## Actual repository structure

```text
brand/assets/
├── 00-catalog/          Catalogs, contact sheets, QA documentation
├── 01-brand/            Logos, wordmarks, lockups, brand identifiers
├── 02-icons-brand/      Brand principle and decorative icons
├── 03-icons-website/    Functional website icons
├── 04-icons-social/     Social-platform icons
├── 05-palette/          Palette and texture assets
├── 06-gradients/        Gradient/background assets
├── 07-components/       Buttons, badges, controls, trust components
├── 08-cards/            Brand/content cards
├── 09-illustrations/    Illustrations and UI concepts
├── 10-product-cards/    Commerce category cards
├── 11-banners/          Website and campaign banners
├── asset-manifest.csv   Canonical detailed asset inventory
└── asset-manifest.json  Lightweight machine-readable library metadata
```

## Category counts

| Category | Logical graphics |
|---|---:|
| 01-brand | 8 |
| 02-icons-brand | 12 |
| 03-icons-website | 14 |
| 04-icons-social | 6 |
| 05-palette | 8 |
| 06-gradients | 4 |
| 07-components | 17 |
| 08-cards | 13 |
| 09-illustrations | 7 |
| 10-product-cards | 4 |
| 11-banners | 4 |
| **Total** | **97** |

## Format guidance

- **SVG:** preferred for logos, icons, controls, badges, gradients, and other vector graphics.
- **WebP:** preferred for larger banners, cards, textures, and illustrations where raster delivery is appropriate.
- **PNG:** compatibility/export fallback, especially where transparency is needed.

Because some PNG/WebP files were generated before the current typography standard was fully normalized, verify text-bearing raster assets visually before production use. Prefer current SVGs or HTML/CSS-rendered text when typography fidelity matters.

## Manifest guidance

`asset-manifest.csv` is the canonical detailed per-asset inventory until an automated manifest generator is introduced.

`asset-manifest.json` provides valid machine-readable library metadata and points consumers to the canonical CSV inventory. Do not add hand-edited duplicate per-asset data to both files unless they are generated from the same source.

## Asset management

When adding or updating an asset:

1. Place it in the appropriate numbered directory.
2. Update `asset-manifest.csv`.
3. Update catalog/contact-sheet outputs when applicable.
4. Verify Manrope/Inter typography for text-bearing assets.
5. Verify the official slogan where brand-line text appears.
6. Commit the change with a clear message.

## Web implementation principles

Use the assets in support of the active Plush Drift v2.1 system:

- Intelligent Calm
- Warm and premium
- Functional beauty
- Generous breathing space
- Layered depth
- Restrained ambient glow
- Consistent quality

See also:

- `../README.md` for brand-system guidance
- `../typography.md` for authoritative typography
- `../colors.md` for authoritative colors
- `../../website/styles/design-system.md` for website implementation guidance

**Version:** Plush Drift v2.1  
**Updated:** August 29, 2026  
**Status:** Active
