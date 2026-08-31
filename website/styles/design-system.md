# LuxSync Website Design System

**Status:** Active  
**Brand system:** LuxSync v3  
**Primary asset source:** `brand/assets-v3/`

LuxSync v3 is the active website treatment. It is crisp, architectural, premium, calm, and restrained. The approved logo artwork is immutable and all editable website UI uses Manrope/Inter and the approved palette only.

## Approved Colors

- Slate Navy `#0D1526` — primary dark background
- Dark Suede `#172036` — elevated dark surfaces
- Pale Driftwood `#D0BEB0` — primary light text / warm light surface
- Warm Taupe Mauve `#9E8B85` — secondary neutral text/details
- Antique Rose Taupe `#967878` — warm decorative accent
- Dusty Steel `#7B96B2` — interactive/cool accent
- Champagne Rose Gold Metallic, `#D6B0A0` anchor — premium metallic accent

No lavender, purple, orange, electric blue, neon blue, or other unapproved brand colors may be introduced into website UI, icons, borders, overlays, or branded graphics.

Natural photography may contain natural scene color.

## Typography

- **Headings / display / navigation / CTA labels / graphic UI:** Manrope 500/600
- **Body / product copy / forms / supporting UI:** Inter 400/500
- **Logo lettering:** protected artwork only, never recreated with a font

## Approved Logo Masters

Reference the protected logo artwork directly:

- `brand/assets/01-brand/luxsync-monogram-orb.png`
- `brand/assets/01-brand/luxsync-horizontal-lockup.png`

Do not redraw, retype, recolor, soften, cartoonize, or regenerate either logo.

## Active Website Assets

Use:

- `brand/assets-v3/02-ui/buttons-and-ctas.svg`
- `brand/assets-v3/02-ui/badges.svg`
- `brand/assets-v3/02-ui/ecommerce-controls.svg`
- `brand/assets-v3/03-icons/core-line-icons.svg`
- `brand/assets-v3/04-heroes/hero-smart-living-elevated.svg`
- `brand/assets-v3/04-heroes/hero-roi-guide.svg`
- `brand/assets-v3/05-ecommerce/product-card-template.svg`
- `brand/assets-v3/05-ecommerce/trust-bar.svg`

## Component Language

- Slate Navy / Dark Suede foundations
- Pale Driftwood primary copy
- Antique Rose Taupe detail and borders
- Dusty Steel controls and selected cool accents
- Champagne Rose Gold only as a metallic premium accent
- generous spacing and editorial negative space
- refined rounded corners
- clear focus states and large touch targets
- native HTML/CSS text wherever practical

## Plush Drift Tactile Illumination

LuxSync v3 carries forward Plush Drift's physical, backlit interaction language. Buttons, cards, selectable product tiles, recommendation choices, navigation controls, and other actionable surfaces should feel like refined architectural controls rather than flat software rectangles.

### Layering

Build the component as a darker foreground surface above a softer illuminated layer:

- foreground: Slate Navy or Dark Suede;
- primary cool underlight: Dusty Steel;
- optional warm underlight: Antique Rose Taupe or a very restrained Pale Driftwood lift;
- Champagne Rose Gold Metallic may appear as a subtle reflected edge or premium accent, never as the dominant halo.

The softer color should read as **light coming from behind or beneath the darker surface**.

### Interaction states

**Rest**
- Keep the dark surface visually dominant.
- Use only a faint narrow halo/underlight and a soft dimensional shadow.

**Hover**
- Increase underlight brightness and spread slightly.
- Preserve text contrast and dark-surface dominance.
- Avoid abrupt scaling or exaggerated lift.

**Keyboard focus**
- Use an unmistakable accessible focus indicator in addition to any backlight increase.
- Never rely on glow alone to indicate focus.

**Pressed / active**
- Move or visually compress the foreground surface inward by approximately `1px–2px`.
- Tighten/reduce the outer shadow to make the control feel physically depressed.
- Increase the underlight modestly, as though pressing the surface exposes more concealed light.
- Do not create a flash or neon burst.

**Release**
- Return smoothly with restrained easing.
- Keep transitions short and calm.

### Suggested implementation behavior

Use native CSS effects where practical, such as layered pseudo-elements, `box-shadow`, `transform`, and opacity transitions. Favor GPU-light, low-cost interactions over complex JavaScript animation.

A typical implementation may use:

- `transform: translateY(1px)` or equivalent on active state;
- slightly reduced shadow offset/blur on active state;
- increased pseudo-element glow opacity on hover/focus/active;
- transition durations roughly in the `120ms–220ms` range with a calm ease-out curve.

These are implementation targets, not permission to sacrifice responsiveness or accessibility.

### Accessibility and restraint

- Preserve WCAG contrast on the actual foreground surface.
- Do not communicate state through glow/color alone.
- Honor `prefers-reduced-motion` and reduce or remove positional press animation when requested.
- Keep glow soft, atmospheric, and localized.
- Avoid hard luminous outlines, arcade/neon effects, excessive bloom, glassmorphism overload, or glowing every static card on the page.

Use tactile illumination most strongly on **interactive controls**. Static containers may use much subtler backlighting for layered depth.

## Hero Language

Preferred visual treatment:

- premium interior or architectural photography
- dark refined field with warm light
- controlled branded overlays from the approved palette
- editorial negative space for native copy
- approved logo artwork only

Approved hero line:

**Smart Living. Elevated.**

Official slogan:

**Where Luxury Lives Intelligently**

## Image Rules

- Production photography should be text-free wherever practical.
- Do not bake live prices, ratings, stock, scarcity, navigation, or promotional claims into photographs.
- Use approved v3 SVG compositions for branded graphics.
- Prefer SVG for vector UI and WebP for production scene imagery.

## Avoid

- cartoonized or softened logo treatments
- regenerated logo lettering
- cyberpunk neon
- lavender/purple drift
- orange/copper drift outside the approved metallic treatment
- loud electric gradients
- generic SaaS blue
- dense gadget-store grids
- cartoon UI
- excessive glassmorphism
- hard glowing borders
- flashing animation
- flat controls that ignore the approved tactile backlighting language
- text baked into photography when it can be rendered natively
