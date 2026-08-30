# LuxSync Typography

**Status:** Active / Authoritative  
**Company:** LuxSync LLC  
**Base brand system:** Plush Drift v2.1  
**Web visual treatment:** Luxury Orbit

<p align="center">
  <img src="assets/01-brand/luxsync-horizontal-lockup.png" alt="LuxSync LLC — Where Luxury Lives Intelligently" width="760">
</p>

## Typography Contract

LuxSync uses two distinct typography layers:

1. **Protected logo lettering:** the approved LuxSync `LS` monogram and `LUXSYNC` wordmark use a high-contrast **Didone / Bodoni-style serif treatment** as fixed artwork. This lettering is part of the logo identity and must not be substituted, re-typeset, simplified, or normalized to Manrope.
2. **Live website, UI, document, and graphic-copy typography:** Manrope + Inter remain authoritative everywhere outside the protected logo artwork.

### Live typography

- **Headings / display / navigation / CTA labels / graphic UI:** Manrope
- **Body copy / product descriptions / forms / supporting UI:** Inter

When another file, generated asset, fallback, or historical document conflicts with this file, this contract governs.

## Protected Logo Lettering

The logo artwork is intentionally different from the live-text system.

- `LS` monogram: approved Didone/Bodoni-style serif artwork
- `LUXSYNC` wordmark: matching approved Didone/Bodoni-style serif artwork
- Slogan within the approved lockup: preserve exactly as approved artwork
- Metallic treatment: Plush Drift-derived blush/rose/champagne highlights with restrained taupe shadowing
- Orbit light: Dusty Steel-derived icy light blue
- Accent sparkle/highlight placement: preserve the approved artwork treatment

Do **not** recreate the logo by choosing a system font. Bodoni, Didot, Libre Bodoni, or similar fonts may be used only as design references when reconstructing approved logo artwork, never as live LuxSync website or document typography.

## Headings, Display, Navigation, and Graphic UI

```css
font-family: "Manrope", system-ui, -apple-system, "Segoe UI", sans-serif;
```

Approved weights:

- 500 — standard display and section headings
- 600 — emphasis, hero headings, CTA labels, navigation emphasis

Do not introduce Century Gothic, Montserrat, Bodoni, Didot, Georgia, or another typeface as a LuxSync live-text heading font.

## Body Copy and Supporting UI

```css
font-family: "Inter", system-ui, -apple-system, "Segoe UI", sans-serif;
```

Approved weights:

- 400 — body copy and supporting text
- 500 — labels, controls, emphasized body/UI text

Do not introduce Candara or another typeface as a LuxSync live-text body font.

## Documentation Branding Rule

LuxSync LLC documentation is branded documentation, including Markdown files.

- Add an approved LuxSync logo/lockup near the beginning of durable documentation where rendering supports images.
- Identify **LuxSync LLC** in the document header or footer.
- Use the official slogan, **Where Luxury Lives Intelligently**, where a branded subtitle or footer is appropriate.
- Use Manrope/Inter for editable document text when the output format supports font control.
- Never redraw or re-typeset the protected logo merely to match document typography.

## Luxury Orbit Styling

Luxury Orbit may use spacing, tracking, scale, metallic treatment, orbit lighting, sparkle highlights, and editorial composition to create a luxury character, but live typography remains Manrope + Inter.

Use typography that feels airy, refined, calm, and highly legible. Avoid dense all-caps body copy and excessive letter spacing.

## Generation and Raster Rules

- `scripts/generate-luxury-orbit-assets.py` must emit Manrope/Inter for editable text.
- `scripts/normalize-luxury-orbit-fonts.py` is the enforcement layer for generated SVG text outside protected logo artwork.
- Build runners must install Manrope and Inter before raster rendering.
- Generated SVGs must fail validation if legacy Century Gothic, Candara, or unapproved live-text serif declarations remain.
- Protected logo files are exempt from live-text font normalization because they are approved artwork.
- Where copy can be HTML/CSS instead of baked into imagery, prefer semantic HTML/CSS.

**Official slogan:** Where Luxury Lives Intelligently

---

<p align="center"><strong>LuxSync LLC</strong><br><em>Where Luxury Lives Intelligently</em></p>
