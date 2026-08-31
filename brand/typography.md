<!-- LUXSYNC-BRAND-HEADER:START -->
<p align="center"><img src="brand-system-v4/01-logos/luxsync-horizontal-approved.png" alt="LuxSync LLC — Where Luxury Lives Intelligently" width="620"></p>
<!-- LUXSYNC-BRAND-HEADER:END -->

# LuxSync Typography

**Status:** Active / Authoritative
**Base brand system:** Plush Drift v2.1
**Web visual treatment:** Crisp Dimensional

## Typography Contract

LuxSync uses one authoritative website and graphic-UI typography system:

- **Headings / display / navigation / CTA labels / graphic UI:** Manrope
- **Body copy / product descriptions / forms / supporting UI:** Inter

When another file, generated asset, fallback, or historical document conflicts with this file, **Manrope and Inter govern**.

## Headings, Display, Navigation, and Graphic UI

```css
font-family: "Manrope", system-ui, -apple-system, "Segoe UI", sans-serif;
```

Approved weights:

- 500 — standard display and section headings
- 600 — emphasis, hero headings, CTA labels, navigation emphasis

Do not introduce Century Gothic, Montserrat, Bodoni, Didot, Georgia, or another typeface as a LuxSync website-system heading font.

## Body Copy and Supporting UI

```css
font-family: "Inter", system-ui, -apple-system, "Segoe UI", sans-serif;
```

Approved weights:

- 400 — body copy and supporting text
- 500 — labels, controls, emphasized body/UI text

Do not introduce Candara or another typeface as a LuxSync website-system body font.

## Approved Logo Artwork Exception

The approved LuxSync logo/monogram files are artwork. Their exact visual lettering may be preserved as approved raster/vector artwork and does **not** redefine the website typography system.

Do not recreate, re-typeset, or modify protected exact logo artwork merely to force live-text typography into the logo.

## Crisp Dimensional Styling

Crisp Dimensional may use spacing, tracking, scale, metallic treatment, orbit lighting, and editorial composition to create a luxury character, but typography remains Manrope + Inter.

Use typography that feels airy, refined, calm, and highly legible. Avoid dense all-caps body copy and excessive letter spacing.

## Generation and Raster Rules

- `scripts/generate-crisp-brand-v4.py` must emit Manrope/Inter for editable text.
- `scripts/validate-crisp-brand-v4.py` is the enforcement layer for generated SVGs.
- Build runners must install Manrope and Inter before raster rendering.
- Generated SVGs must fail validation if legacy Century Gothic, Candara, Bodoni-family, Didot, or Georgia system declarations remain in editable text.
- Where copy can be HTML/CSS instead of baked into imagery, prefer semantic HTML/CSS.

**Official slogan:** Where Luxury Lives Intelligently
