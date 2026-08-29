# LuxSync Typography

The Luxury Orbit refresh uses a three-part typography system: a fashion-luxury serif for the LuxSync wordmark, a geometric sans for display/UI, and a softer humanist sans for body copy.

## Brand Wordmark / Editorial Serif

Preferred stack:

```css
font-family: "Bodoni Moda", "Bodoni MT", Didot, Georgia, serif;
```

Use for:

- `LUXSYNC` wordmark treatment
- Select editorial headings
- Premium campaign or guide-cover accents

Do not use the serif for long body copy or dense interface text.

## Headings, Navigation, and Graphic UI

Preferred design reference: **Century Gothic**.

Web-safe stack:

```css
font-family: "Century Gothic", Montserrat, Arial, sans-serif;
```

Use for:

- Hero headlines
- Section headings
- Navigation
- CTA labels
- Product-card titles
- Graphic labels

Recommended weights: 400, 600, 700.

## Body Copy and Supporting UI

Preferred design reference: **Candara**.

Web-safe stack:

```css
font-family: Candara, Inter, "Segoe UI", Arial, sans-serif;
```

Use for:

- Body copy
- Product descriptions
- Helper text
- Form text
- Supporting captions

Recommended weights: 400 and 500.

## Styling Notes

- The LuxSync wordmark is normally uppercase with generous tracking.
- Graphic CTAs may use uppercase labels when the component is compact and highly visual.
- Website body copy should remain easy to scan and should not rely on all caps.
- Preserve strong contrast on Deep Navy surfaces.
- Keep typography airy and refined rather than dense or heavy.

## Fallback Behavior

The SVG library includes robust fallback stacks so the assets remain usable without proprietary fonts. Raster exports may use the closest available fallback font on the build runner.

**Official slogan:** Where Luxury Lives Intelligently
