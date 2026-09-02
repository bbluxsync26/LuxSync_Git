# LuxSync Typography

**Status:** Active / Authoritative  
**Brand system:** LuxSync Production Raster v5  
**Design DNA:** Plush Drift

## Typography Contract

LuxSync uses one authoritative website and graphic-UI typography system:

- **Headings / display / navigation / CTA labels / graphic UI:** Manrope
- **Body copy / product descriptions / forms / supporting UI:** Inter

When another active file, generated asset, fallback, or historical document conflicts with this file, **Manrope and Inter govern**.

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

The approved LuxSync logo files are identity artwork. Their exact lettering is preserved as supplied and does **not** redefine the live website typography system.

Authoritative logo sources:

- `brand/source-logo/LuxSync_Logo_Horizontal_Combo.png`
- `brand/source-logo/LuxSync_Logo_Horizontal_Final.png`
- `brand/source-logo/LuxSync_Logo_Orb.png`

Production-approved PNG delivery copies are mapped under `brand/assets/logos/png/` and `website/asset-map.md`.

Do not recreate, re-typeset, redraw, or modify protected logo artwork merely to force live-text typography into the logo.

## Production Raster v5 Styling

Production Raster v5 may use spacing, tracking, scale, metallic treatment, concealed illumination, and editorial composition to create the LuxSync luxury character, but typography remains Manrope + Inter.

Use typography that feels airy, refined, calm, and highly legible. Avoid dense all-caps body copy, excessive letter spacing, decorative type substitutions, and novelty display fonts.

## Website and Raster Rules

- Prefer semantic HTML/CSS for mutable website copy, prices, forms, navigation, authentication text, support information, and calls to action.
- Do not bake mutable website copy into production imagery when live text is practical.
- Production UI must follow `website/styles/design-system.md`.
- Imported raster slices are reference-only unless a current manifest explicitly marks them `production-approved`.
- Text rendered into approved fixed graphics must use Manrope and/or Inter unless the text is part of immutable approved logo artwork.
- Accessibility and readability take priority over decorative tracking, glow, or metallic effects.

## Responsive Typography

- Preserve clear heading hierarchy at desktop, tablet, and mobile widths.
- Allow long founder titles and CTA labels to wrap naturally rather than shrinking them into unreadable type.
- Maintain comfortable line length and line height for body copy.
- Ensure form labels remain persistent and readable.

## Related Authoritative Files

- `brand/README.md`
- `brand/colors.md`
- `brand/voice-and-tone.md`
- `website/styles/design-system.md`
- `docs/production-source-of-truth.md`

**Official slogan:** Where Luxury Lives Intelligently
