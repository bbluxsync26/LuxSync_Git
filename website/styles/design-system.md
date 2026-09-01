# LuxSync Website Design System

**Status:** Active / Reconciled  
**Brand system:** LuxSync Production Raster v5
**Design DNA:** Plush Drift

LuxSync Production Raster v5 is the active website treatment: crisp, architectural, premium, calm, restrained, and tactile. Approved logo artwork is immutable; editable UI uses Manrope/Inter and the approved palette.

## Official Brand Language

**Sole approved public slogan / hero line:**

# Where Luxury Lives Intelligently

Do not use or regenerate retired alternate slogan/hero treatments.

## Approved Colors

- Slate Navy `#0D1526` — primary dark background
- Dark Suede `#172036` — elevated dark surfaces
- Pale Driftwood `#D0BEB0` — primary light text / warm light surface
- Warm Taupe Mauve `#9E8B85` — secondary neutral
- Antique Rose Taupe `#967878` — warm accent
- Dusty Steel `#7B96B2` — interactive/cool accent
- Champagne Rose Gold Metallic `#D6B0A0` anchor — premium metallic accent

No lavender, purple, orange, electric blue, neon blue, or other unapproved brand colors may be introduced into branded website UI. Natural photography may contain natural scene color.

## Typography

- **Headings / display / navigation / CTA labels / graphic UI:** Manrope 500/600
- **Body / product copy / forms / supporting UI:** Inter 400/500
- **Logo lettering:** protected artwork only, never recreated with a font

Do not use Montserrat, Century Gothic, Candara, Bodoni-family, Didot, or Georgia as website-system fonts.

## Approved Logo Treatment

Reference protected logo artwork directly. Do not redraw, retype, recolor, soften, cartoonize, or regenerate the logo.

## Component Language

- Slate Navy / Dark Suede foundations
- Pale Driftwood primary copy
- Antique Rose Taupe detail and borders
- Dusty Steel controls and selected cool accents
- Champagne Rose Gold only as restrained premium metallic detail
- generous spacing and editorial negative space
- refined rounded corners
- clear focus states and large touch targets
- native HTML/CSS text wherever practical

## Plush Drift Tactile Illumination

Buttons, cards, Concierge choices, Contact-form intent cards, product tiles, navigation controls, and other actionable surfaces should feel like refined architectural controls rather than flat software rectangles.

### Layering

Build a darker foreground surface above a softer illuminated layer:

- foreground: Slate Navy or Dark Suede
- primary cool underlight: Dusty Steel
- optional warm underlight: Antique Rose Taupe or restrained Pale Driftwood
- Champagne Rose Gold Metallic: subtle reflected edge/premium accent only

### States

**Rest**
- dark surface remains dominant
- faint localized underlight

**Hover**
- modestly increase underlight brightness/spread
- avoid aggressive scaling

**Keyboard focus**
- explicit accessible focus indicator in addition to illumination
- never rely on glow alone

**Pressed / active**
- visually compress/move foreground inward approximately 1–2 px
- tighten outer shadow
- modestly increase concealed underlight

**Release**
- short, calm easing back to rest

### Accessibility

- preserve WCAG contrast on the foreground surface
- do not communicate state through color/glow alone
- honor `prefers-reduced-motion`
- avoid hard luminous borders, neon effects, excessive bloom, flashing, or glowing every static card

## Concierge Components

The **LuxSync Intelligent Living Concierge** is a flagship interaction surface.

Use:

- large outcome-oriented selectable cards
- progressive disclosure rather than long forms
- descriptive progress states such as `Understanding Your Space`, `Designing Your Experience`, and `Creating Your Blueprint`
- strong selected states with accessible non-color cues
- comfortable touch targets
- clear Back / Continue behavior without data loss
- Blueprint reveal cards that explain `Why LuxSync Chose This`

The Concierge must not visually resemble a cheap online quiz.

## My LuxSync Blueprint

Blueprint visual hierarchy:

1. Your Space
2. What Matters Most
3. Intelligent Living Profile
4. Recommended LuxSync Experiences
5. Foundation / compatibility context
6. Implementation path
7. Phased roadmap
8. Technology behind the experience
9. Next best action

Recommended paths use:

- Essential Intelligence
- Elevated Living
- Complete LuxSync Experience

## Adaptive Contact Components

The dedicated Contact page uses the same premium card language as the Concierge.

Initial intent cards:

- Support
- Product Information
- Consultation
- General Question
- Business / Partnership
- Other

Reveal approximately 3–6 relevant fields at a time. Do not render a wall of every possible field.

Use the same visual treatment for shared Property Profile selections such as property type and square-footage ranges.

Conditional changes and validation errors must be accessible to assistive technologies.

## Forms

- persistent visible labels
- clear required/optional state
- helpful, non-punitive validation copy
- large inputs and controls on mobile
- Not Sure option where exact property measurements are unnecessary
- marketing consent separate and optional
- no full street-address requirement for initial Contact/Concierge discovery

## Hero Treatment

Use:

- approved logo artwork
- **Where Luxury Lives Intelligently** as the public hero line
- premium interior / architectural imagery or approved branded composition
- restrained dark field and warm/cool lighting
- native text rather than baked-in copy when practical
- primary CTA: **Find My LuxSync Solution**
- secondary CTA: **Shop Smart Home**

Do not use assets that embed retired slogan/hero copy.

## Product and Solution Cards

Differentiate clearly between:

- validated live product
- validated bundle
- planning product family
- LuxSync Experience / solution concept

Do not make a solution concept look purchasable unless a validated commerce item exists.

## Image Rules

- production photography should be text-free where practical
- do not bake live prices, ratings, stock, scarcity, navigation, or promotional claims into photographs
- use the approved finished PNG/WebP graphics for branded visual assets; build live interactive UI with accessible HTML/CSS rather than baking interaction into image files
- retired slogan artwork must not be reused

## Avoid

- regenerated logo lettering
- cyberpunk neon
- lavender/purple drift
- generic SaaS blue
- dense gadget-store grids
- cartoon UI
- excessive glassmorphism
- hard glowing borders
- flashing animation
- flat controls that ignore tactile backlighting
- text baked into photography when it can be native
- novelty-quiz styling for the Concierge
- bureaucratic ticket-system styling for Contact
