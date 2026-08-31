# LuxSync Brand Architecture

**Status:** Active / Authoritative  
**Company:** LuxSync LLC  
**Current visual system:** LuxSync v3  
**Design DNA:** Plush Drift  
**Typography:** Manrope + Inter  
**Official slogan:** Where Luxury Lives Intelligently

## Purpose

This document defines the underlying LuxSync brand architecture. It explains which elements are foundational brand DNA, which are current implementation layers, and which visual behaviors must remain recognizable as the brand evolves.

When a website, graphic, asset library, campaign, or future design-system version is created, it should inherit the principles in this document unless an explicit later brand decision supersedes them.

## Brand Architecture

LuxSync is organized in layers:

1. **Brand promise and voice** — intelligent luxury expressed through calm, useful, human-centered technology.
2. **Plush Drift design DNA** — tactile depth, softened luxury, concealed illumination, layered dark surfaces, warm/cool balance, and quiet physicality.
3. **Authoritative palette** — Slate Navy, Dark Suede, Pale Driftwood, Warm Taupe Mauve, Antique Rose Taupe, Dusty Steel, and Champagne Rose Gold Metallic.
4. **Typography** — Manrope 500/600 for headings/display/navigation/controls and Inter 400/500 for body/supporting UI.
5. **Current visual implementation** — LuxSync v3 and `brand/assets-v3/`.
6. **Protected identity artwork** — approved LuxSync logo masters, preserved exactly and not reconstructed from live type.

LuxSync v3 is therefore the current implementation of the brand, while **Plush Drift is the enduring interaction and material design language underneath it**.

## Plush Drift Design DNA

Plush Drift should feel like premium interior architecture with intelligent technology built into the material itself.

The aesthetic is not flat minimalism and not futuristic neon. It uses **soft depth, concealed light, restrained texture, calm movement, and tactile visual feedback** to make digital controls feel integrated into a luxurious physical environment.

### Core characteristics

- layered Slate Navy and Dark Suede surfaces;
- soft warm neutrals rather than stark white;
- controlled cool illumination from Dusty Steel;
- restrained Antique Rose Taupe warmth;
- Champagne Rose Gold Metallic as a polished premium finish;
- generous negative space;
- refined rounded geometry;
- low-noise shadows and atmospheric depth;
- interactive controls that appear physically touchable;
- motion that is subtle enough to feel architectural rather than animated.

## Plush Drift Tactile Illumination

Tactile illumination is a **core Plush Drift behavior**, not an optional website effect.

Buttons, cards, selectable tiles, recommendation choices, ecommerce controls, and similar interactive elements may be composed as a darker foreground control sitting above or within a softly illuminated backing layer.

The visual metaphor is a premium physical switch or architectural control with concealed light behind it.

### Rest state

- Slate Navy or Dark Suede remains the dominant foreground surface.
- A faint, localized underglow creates separation from the background.
- The control should look dimensional and touchable without appearing luminous for its own sake.

### Hover state

- The concealed underlight brightens slightly.
- The illuminated area may widen or soften modestly.
- The foreground surface remains dark and visually dominant.

### Keyboard focus

- Backlighting may increase, but an explicit accessible focus indicator must also be present.
- Glow alone never communicates focus.

### Pressed / active state

The control should create the impression that the user is physically pressing into the illuminated surface:

- foreground depth compresses or moves inward approximately `1px–2px`;
- the outer shadow tightens or reduces;
- the concealed underlight becomes modestly brighter or more visible around the compressed edge;
- the effect remains calm, with no flash, bounce, neon burst, or exaggerated scale change.

### Release state

- Return smoothly to rest using restrained easing.
- Typical transition behavior may fall around `120ms–220ms` where appropriate.
- Honor `prefers-reduced-motion`; positional movement may be reduced or removed while preserving clear state feedback.

## Illumination Color Hierarchy

### Dusty Steel

`#7B96B2`

Primary intelligent-light color. Use for cool underlighting, active technology cues, focus enhancement, and subtle concealed illumination.

### Antique Rose Taupe

`#967878`

Warm luxury underlight for selected lifestyle, comfort, or premium contexts. Use more sparingly than Dusty Steel.

### Pale Driftwood

`#D0BEB0`

Very soft luminous edge, reflected warmth, or ambient lift. It should not turn controls into pale glowing boxes.

### Champagne Rose Gold Metallic

Flat anchor: `#D6B0A0`

Champagne Rose Gold Metallic is a premium material treatment. It may appear as a fine reflected edge, highlight, trim, icon detail, or polished accent around tactile controls.

It is **not the primary backlight color** and should not become a broad rose-gold halo.

Approved metallic rendering follows the gradient defined in `brand/colors.md`.

## Layered Surface Model

A typical Plush Drift interactive component may be understood as four visual layers:

1. **Environment** — Slate Navy page/background field.
2. **Underlight** — soft Dusty Steel or approved warm illumination behind the control.
3. **Control surface** — Dark Suede or Slate Navy foreground button/tile/card.
4. **Detail layer** — Manrope/Inter text, iconography, focus treatment, and optionally a restrained Champagne Rose Gold Metallic accent.

This structure should remain recognizable even when exact border radius, spacing, shadows, or component dimensions evolve.

## Static vs. Interactive Surfaces

Interactive surfaces receive the strongest tactile illumination.

Static cards and containers may use a much softer version for depth, but they should not appear clickable unless they actually are. Avoid surrounding every rectangle with a glow.

Visual affordance must remain truthful.

## Metallic Integration

Metallic treatments enhance Plush Drift rather than competing with it.

Use Champagne Rose Gold Metallic to suggest polished material, reflected light, and premium hardware detail. The strongest metallic treatments belong in identity accents, premium labels, dividers, icon details, fine borders, and selected high-value interface moments.

Do not convert the entire interface into metallic gradients. The dark tactile surfaces and soft underlighting must remain the visual foundation.

## Typography Relationship

Plush Drift does not use a separate decorative website font.

- **Manrope 500/600** — headings, display, navigation, CTA labels, buttons, badges, graphic UI.
- **Inter 400/500** — body copy, product descriptions, forms, captions, and supporting UI.

Protected logo artwork is an exception because it is identity artwork, not live website typography.

## Motion Character

Motion should reinforce physicality and calm:

- short press/release transitions;
- subtle opacity changes;
- soft shadow compression;
- restrained light expansion;
- minimal positional movement;
- no bouncing, pulsing, flashing, elastic overshoot, or continuous decorative movement on ordinary controls.

The interface should feel responsive immediately but never restless.

## Accessibility

The Plush Drift effect system must remain usable when glow, color, or motion is unavailable.

- Maintain sufficient text/background contrast on the actual foreground surface.
- Use explicit focus indicators.
- Do not use color alone to communicate state.
- Respect reduced-motion preferences.
- Preserve large enough touch targets.
- Ensure tactile effects never obscure labels or control boundaries.

## What Plush Drift Is Not

Avoid:

- cyberpunk neon;
- hard luminous outlines;
- arcade-style glow;
- lavender or purple drift;
- electric cyan or generic SaaS blue;
- excessive glassmorphism;
- glossy skeuomorphism;
- heavy beveling;
- glitter effects;
- full-surface metallic gradients;
- flat controls with no tactile hierarchy;
- excessive animation.

## Relationship to LuxSync v3

LuxSync v3 is the current authoritative visual and asset implementation. New production design work uses `brand/assets-v3/`.

The v3 system should preserve the Plush Drift DNA described here even as individual assets, logo baselines, component drawings, or marketing compositions are refined.

A future LuxSync v4 may alter execution details without losing the core principles of **layered dark surfaces, tactile illumination, intelligent calm, softened luxury, and restrained metallic polish** unless an explicit brand architecture decision changes them.

## Related Authoritative Files

- `brand/README.md` — current LuxSync brand guidelines
- `brand/colors.md` — authoritative palette and metallic treatment
- `brand/typography.md` — Manrope/Inter typography contract
- `brand/voice-and-tone.md` — Intelligent Calm voice
- `website/styles/design-system.md` — website implementation rules
- `prompts/website/PR-001-LuxSync-Airo-Master-Website-Build-Prompt.md` — staging-generation instructions
- `docs/checklists/CL-001-Airo-First-Pass-Review.md` — implementation review gate

**Brand principle:** the technology should feel present when needed and quietly integrated when it is not.