# LuxSync Color System

**Status:** Active / Authoritative  
**Brand system:** LuxSync Production Raster v5  
**Design DNA:** Plush Drift  
**Voice:** Intelligent Calm

This file defines the authoritative LuxSync color contract for production website UI, branded graphics, documentation, and approved visual assets.

## Authoritative Colors

| Role | Name | Hex |
|---|---|---|
| Primary background | Slate Navy | `#0D1526` |
| Elevated/card surface | Dark Suede | `#172036` |
| Primary light text / warm light surface | Pale Driftwood | `#D0BEB0` |
| Secondary text / neutral | Warm Taupe Mauve | `#9E8B85` |
| Warm decorative accent | Antique Rose Taupe | `#967878` |
| Interactive / cool intelligent-light accent | Dusty Steel | `#7B96B2` |
| Premium metallic accent | Champagne Rose Gold Metallic | `#D6B0A0` anchor |

These seven colors are the source of truth. The first six are flat colors. Champagne Rose Gold Metallic is an approved metallic color anchored at `#D6B0A0`.

## Champagne Rose Gold Metallic

Use `#D6B0A0` where a flat color is required. Where metallic depth is appropriate, the approved dimensional treatment may use:

`#FFF2EA → #EAC8B9 → #D6B0A0 → #9C675C → #F2D6C8 → #7D4E49`

The highlight and shadow stops render metallic depth. They are not additional standalone brand colors.

Use Champagne Rose Gold Metallic selectively for premium trim, fine borders, dividers, icon detail, reflected edges, and other controlled emphasis. Do not turn large interface surfaces into metallic gradients.

## Brushed Dusty Steel

Dusty Steel `#7B96B2` is the source color for the approved cool intelligent-light treatment.

**Brushed Dusty Steel is the only approved metallic-blue treatment.** Do not introduce electric blue, cyan, icy-blue substitutions, or additional branded blue hues.

Cool-light effects should remain soft, atmospheric, and architectural rather than neon.

## Plush Drift Tactile Illumination

Plush Drift is the enduring interaction and material design DNA beneath Production Raster v5.

Use a Slate Navy or Dark Suede foreground surface above a softer approved-color underlight. The light should feel concealed beneath or behind the control rather than painted onto its face.

Preferred illumination hierarchy:

1. **Dusty Steel** — primary cool interaction/backlight color.
2. **Antique Rose Taupe** — warm luxury underlight for selected contexts.
3. **Pale Driftwood** — soft luminous edge or ambient lift.
4. **Champagne Rose Gold Metallic** — restrained reflected edge or premium detail, never the dominant halo.

Interaction behavior:

- **Rest:** faint localized underlight with clear dark-surface separation.
- **Hover:** underlight brightens and widens modestly.
- **Keyboard focus:** preserve an explicit accessible focus indicator in addition to any illumination.
- **Pressed/active:** foreground compresses inward approximately `1px–2px`, the outer shadow tightens, and concealed light becomes modestly more visible.
- **Release:** return smoothly with calm easing.

Do not use neon bloom, hard luminous borders, flashing light, excessive glass effects, or glow as the only state indicator.

## Design Rules

- Slate Navy is the default dark canvas.
- Dark Suede is the primary elevated surface.
- Pale Driftwood is the primary light text color on dark surfaces.
- Warm Taupe Mauve supports secondary information.
- Antique Rose Taupe provides restrained warm emphasis.
- Dusty Steel carries interactive emphasis and the intelligent-light cue.
- Champagne Rose Gold Metallic provides selective premium emphasis.
- Natural photography may contain natural scene color, but branded UI and overlays use the approved palette.
- Accessibility and contrast take priority over decorative glow or metallic treatment.

## Production Asset Relationship

The current visual implementation is **LuxSync Production Raster v5**.

- Authoritative brand guidance: `brand/README.md`
- Production assets: `brand/assets/`
- Immutable logo masters: `brand/source-logo/`
- Website publication mapping: `website/asset-map.md`
- Website implementation contract: `website/styles/design-system.md`

Imported raster slices are reference-only unless a current asset manifest explicitly marks them `production-approved`.

## Typography Relationship

Color never redefines typography.

- **Manrope 500/600** for headings, display, navigation, CTAs, and graphic UI.
- **Inter 400/500** for body copy, forms, product copy, and supporting UI.

See `brand/typography.md`.

**Official slogan:** Where Luxury Lives Intelligently
