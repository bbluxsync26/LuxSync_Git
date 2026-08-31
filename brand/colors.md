# LuxSync Color System

**Status:** Active / Authoritative  
**Base brand system:** Plush Drift v2.1  
**Web visual treatment:** Luxury Orbit

Luxury Orbit is the active website and web-graphics treatment. It is built on the **Plush Drift v2.1 seven-color approved palette** rather than replacing it.

## Authoritative Base Colors

| Role | Name | Hex |
|---|---|---|
| Primary background | Slate Navy | `#0D1526` |
| Elevated/card surface | Dark Suede | `#172036` |
| Primary light text / warm light surface | Pale Driftwood | `#D0BEB0` |
| Secondary text / neutral | Warm Taupe Mauve | `#9E8B85` |
| Warm decorative accent | Antique Rose Taupe | `#967878` |
| Interactive / cool technology accent | Dusty Steel | `#7B96B2` |
| Premium metallic accent | Champagne Rose Gold Metallic | `#D6B0A0` anchor |

These seven values are the source of truth for website, graphics, documentation, and generated assets. The first six are flat colors; Champagne Rose Gold Metallic is an approved metallic color anchored at `#D6B0A0`.

## Luxury Orbit Derived Treatments

Luxury Orbit adds restrained premium treatments without changing the base palette.

### Champagne Rose Gold Metallic Treatment

Champagne Rose Gold Metallic is the seventh approved brand color. Its flat anchor is `#D6B0A0`; use the following approved gradient when metallic depth is required:

`#FFF2EA → #EAC8B9 → #D6B0A0 → #9C675C → #F2D6C8 → #7D4E49`

Use the flat anchor where gradients are unsupported. The highlight and shadow stops render the metallic finish and are not additional standalone palette colors.

### Orbit / Cool-Light Treatment

Dusty Steel `#7B96B2` is the source color for the cool orbit/glow signature. Derived icy-blue highlight tints may be used inside gradients and light effects when necessary for depth.

The effect must remain soft and atmospheric rather than neon.

## Plush Drift Tactile Illumination

The Plush Drift aesthetic includes a tactile backlighting behavior for buttons, cards, selectable tiles, and similar controls.

Use a dark Slate Navy or Dark Suede foreground surface above a softer approved-color underlight. The underlight should feel concealed beneath the control rather than painted onto its face.

Preferred illumination hierarchy:

1. **Dusty Steel** — primary cool interaction/backlight color.
2. **Antique Rose Taupe** — warm luxury underlight for selected contexts.
3. **Pale Driftwood** — very soft luminous edge or ambient lift.
4. **Champagne Rose Gold Metallic** — restrained reflected edge or premium accent only, not the dominant halo.

Interaction behavior:

- **Rest:** faint, narrow underglow with clear dark-surface separation.
- **Hover/focus:** glow brightens and widens slightly while remaining controlled.
- **Pressed/active:** foreground surface visually compresses inward by about 1–2 px; outer shadow tightens; underlighting brightens modestly to suggest a physical backlit control being pressed.
- **Release:** return smoothly with calm easing.

Do not use neon bloom, hard luminous borders, flashing light, excessive glass effects, or color-only state communication. Accessibility and contrast take priority over decorative glow.

## Typography Relationship

Color treatments never redefine typography. The authoritative LuxSync type system remains:

- **Manrope 500/600** for headings, display, navigation, CTAs, and graphic UI.
- **Inter 400/500** for body copy and supporting UI.

See `brand/typography.md` for the complete typography contract.

## Design Rules

- Slate Navy is the default dark canvas.
- Dark Suede is the primary elevated surface.
- Pale Driftwood is the primary light text color on dark surfaces.
- Warm Taupe Mauve supports secondary information.
- Antique Rose Taupe provides warm decorative emphasis.
- Dusty Steel carries interactive emphasis and the cool intelligent-light cue.
- Champagne Rose Gold Metallic provides restrained premium emphasis and should not dominate large UI surfaces.
- Tactile backlighting should create depth beneath darker controls rather than flattening the control into a glowing shape.
- Avoid electric cyan, saturated magenta, lavender drift, or cyberpunk neon as new base colors.
- Use gradients and glows selectively so the interface stays calm, premium, and readable.

## Accessibility

Derived metallic, glow, and tactile-illumination treatments do not replace accessible text/background contrast. Interactive states must remain understandable without relying on glow or color alone. Honor reduced-motion preferences for press/release animation.

**Official slogan:** Where Luxury Lives Intelligently
