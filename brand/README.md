# LuxSync Brand Guidelines

**Plush Drift v2.1 — Authoritative Brand System**  
**Luxury Orbit — Active Web Visual Treatment**

> Where Luxury Lives Intelligently

## Direction

Luxury Orbit is the active website and web-graphics direction layered on the authoritative **Plush Drift v2.1** brand system. It combines architectural navy, warm metallic rose, restrained Dusty Steel orbit light, tactile dark surfaces, and calm premium smart-living photography.

The desired impression is **luxury interior design with intelligent technology quietly underneath it**.

Luxury Orbit does not replace the Plush Drift base palette or the Manrope/Inter typography contract.

## Authoritative Plush Drift v2.1 Palette

- Slate Navy `#0D1526`
- Dark Suede `#172036`
- Pale Driftwood `#D0BEB0`
- Warm Taupe Mauve `#9E8B85`
- Antique Rose Taupe `#967878`
- Dusty Steel `#7B96B2`

Derived highlight and shadow tints may be used for metallic rose and orbit-light effects, but the six colors above remain the base palette.

See [colors.md](colors.md) for implementation details.

## Typography

- **Manrope 500/600** — headings, display text, navigation, CTA labels, and graphic UI
- **Inter 400/500** — body copy, controls, forms, product descriptions, and supporting UI

Do not use Century Gothic, Candara, Montserrat, Bodoni-family, Didot, Georgia, or other legacy font declarations as current LuxSync website-system typography.

Approved logo artwork may preserve its exact visual lettering as artwork. Logo artwork does not redefine the website typography system.

See [typography.md](typography.md) for implementation details.

## Asset Library

The library contains **103 logical assets**:

- **97 SVG-based graphics**, each with generated PNG and WebP siblings
- **6 production raster scenes**, each supplied as optimized PNG and WebP

Assets live under [assets/](assets/):

- `01-brand/` logos and brand marks
- `02-icons-brand/` decorative and brand-principle icons
- `03-icons-website/` functional web icons
- `04-icons-social/` social icons
- `05-palette/` palette and texture tiles
- `06-gradients/` atmospheric backgrounds
- `07-components/` buttons, badges, controls, trust components
- `08-cards/` brand and content cards
- `09-illustrations/` smart-home and visual-system illustrations
- `10-product-cards/` commerce category cards
- `11-banners/` vector hero, shop, and guide treatments
- `12-scenes/` production smart-living photography for website compositing

## Generator Boundary

The vector/UI generation path is:

```text
scripts/generate-luxury-orbit-assets.py
scripts/normalize-luxury-orbit-fonts.py
scripts/render-luxury-orbit-assets.py
```

The normalization step enforces Manrope/Inter and the Plush Drift v2.1 base palette before raster rendering.

The approved primary monogram and horizontal lockup are protected exact artwork and must be preserved by the generation pipeline unless a later explicit logo decision replaces them.

SVG files do not need to be sent through an image generator. Photographic scenes are intentionally raster assets and should contain no baked-in website copy, navigation, buttons, or unapproved logo recreations. Render those elements natively in HTML/CSS or use approved vector/raster brand assets.

## Brand Voice

Keep **Intelligent Calm**: warm, confident, thoughtful, unhurried, professional, and human.

## Status

**Brand system:** Plush Drift v2.1  
**Web visual treatment:** Luxury Orbit  
**Typography:** Manrope + Inter  
**Status:** Active  
**Updated:** August 30, 2026
