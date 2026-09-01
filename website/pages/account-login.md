# LuxSync Account Access — Production Specification

**Status:** Active / Production-ready visual and interaction baseline  
**Experience:** VIP Account Access  
**Brand:** LuxSync Production Raster v5 with Plush Drift design DNA  
**Typography:** Manrope + Inter  
**Official slogan:** Where Luxury Lives Intelligently  
**Implementation manifest:** `website/account-access-manifest.json`  
**Interaction tokens:** `website/styles/account-access-tokens.css`

## Purpose

The LuxSync login and account-access experience must feel like entry into a private luxury service environment, not a generic authentication form. Every customer should feel recognized, welcomed, and important from the first account interaction.

The experience must remain simple, secure, accessible, commerce-oriented, and visually consistent with Plush Drift: layered dark surfaces, concealed light, tactile controls, restrained metallic detail, and Intelligent Calm voice.

## Non-Negotiable Brand Rules

1. Use **only** the approved logo masters in `brand/assets/01-logos/`.
2. Never redraw, retype, recolor, regenerate, simplify, or reinterpret the LuxSync logo.
3. Desktop/header brand use: `brand/assets/logos/png/luxsync-horizontal-combo.png`.
4. Alternate extended horizontal use: `brand/assets/logos/png/luxsync-horizontal.png`.
5. Compact/mobile/account emblem use: `brand/assets/logos/png/luxsync-orb.png`.
6. Live headings and controls use Manrope 500/600.
7. Live body, helper, form, and supporting copy use Inter 400/500.
8. Decorative metallic and illumination effects must never replace accessible contrast, focus, labels, or state text.

## Experience Principle

**Every LuxSync customer is treated like a VIP.**

VIP means:

- the interface feels considered and personal;
- the customer is welcomed rather than processed;
- access is calm, clear, and friction-light;
- assistance is always easy to find;
- account information feels private and well cared for;
- every ordinary customer receives the same high-care experience.

VIP does **not** mean artificial status tiers, velvet-rope language, scarcity, or implying that some ordinary customers matter less.

## Route Architecture

Preferred route family:

- `/account/login`
- `/account/create`
- `/account/forgot-password`
- `/account/reset-password`
- `/account/verify`
- `/account/verification-code`
- `/account/locked`
- `/account/welcome`

These are UX route targets. Final production route names must follow the actual GoDaddy Commerce Plus/account implementation or a later approved identity architecture decision.

## Desktop Architectural Drawing

### Overall canvas

- Full viewport minimum height: `100svh` where supported.
- Content max width: `1440px` visual composition, with the auth card constrained independently.
- Base canvas: Slate Navy `#0D1526`.
- Elevated surfaces: Dark Suede `#172036`.
- Primary light copy: Pale Driftwood `#D0BEB0`.
- Soft secondary copy: Warm Taupe Mauve `#9E8B85`.
- Interactive concealed light: Dusty Steel `#7B96B2`.
- Premium micro-detail: Champagne Rose Gold Metallic anchored at `#D6B0A0`.

### Two-zone composition

Use a 58/42 desktop split at wide viewports. The layout may relax toward 55/45 between 1024px and 1279px.

#### Zone A — VIP welcome atmosphere

**Placement:** left side, approximately 52–58% width.

Contains, in order:

1. approved LuxSync logo artwork;
2. restrained architectural smart-living visual or abstract Plush Drift illumination graphic;
3. optional eyebrow: `MEMBER ACCESS`;
4. headline: **Welcome Back**;
5. support line: **Your LuxSync experience is ready.**;
6. supporting copy: `Sign in to continue to your orders, saved preferences, curated recommendations, and LuxSync support.`;
7. optional small trust/service cue.

Use `website/assets/auth/login-vip-hero.svg` as a text-free ambient layer behind live HTML content. Do not bake welcome copy, authentication fields, customer data, or mutable account claims into the background graphic.

#### Zone B — account access card

**Placement:** right side, vertically centered, visually anchored slightly inside the right half rather than against the browser edge.

Recommended card geometry:

- width: `clamp(360px, 32vw, 480px)`;
- minimum interior padding: `32px` desktop;
- corner radius: `22–26px`;
- border: restrained Dusty Steel / Pale Driftwood blend;
- concealed underlight behind the card, not a hard glowing outline;
- card should float 20–32px above its optical background plane.

Card content order:

1. `Member Login`
2. `Access your LuxSync account.`
3. Email address field
4. Password field with accessible show/hide control
5. Remember-me option only when supported by the real platform
6. `Forgot Password?`
7. Primary `Sign In` action
8. `Create Your LuxSync Account`
9. Support pathway
10. optional security/trust text only when factually supported

Do not invent Apple, Google, Microsoft, passkey, biometric, SSO, MFA, or social-login options unless the production account platform actually supports them.

## VIP Welcome Messaging

### Preferred login copy

**Eyebrow:** `MEMBER ACCESS`  
**Headline:** `Welcome Back`  
**Support line:** `Your LuxSync experience is ready.`

Preferred helper copy:

- `Welcome to your LuxSync account.`
- `Your home. Your preferences. Your LuxSync.`
- `Need assistance? LuxSync Support is here.`

Use the official slogan as a brand signature where compositionally appropriate:

**Where Luxury Lives Intelligently**

Avoid:

- `Elite members only`
- `Exclusive access` unless a genuinely restricted feature exists
- invented loyalty/status terminology
- scarcity or urgency language
- exaggerated security claims

## Input Architecture and States

All fields use live semantic HTML labels. Placeholder text never substitutes for a visible or programmatically associated label.

### Default

- Dark Suede inset field.
- Low-contrast border visible against the card.
- Pale Driftwood input text.
- Warm Taupe Mauve placeholder/help text.
- No bright halo.

### Hover

- Border becomes slightly clearer.
- Concealed Dusty Steel underlight may become visible at low intensity.
- No size shift.

### Focus

- Visible WCAG-oriented focus ring.
- Dusty Steel underlight brightens modestly.
- Fine Champagne Rose Gold reflection may appear along one edge.
- No large bloom or animation that competes with typing.

### Filled / valid

- Preserve normal text contrast.
- Optional check/status icon plus readable text where validation feedback is needed.
- Never communicate success through color alone.

### Error

- Accessible error text linked to the field.
- Error icon or textual cue in addition to color.
- No shake animation.
- No flashing red border.
- Error state must remain legible in reduced-motion and high-contrast contexts.

### Disabled

- Reduced contrast while retaining legibility.
- No illumination response.
- Cursor and semantics must accurately communicate disabled state.

## Button Architecture and States

### Primary Sign In

Rest:

- dark premium foreground surface;
- restrained Champagne Rose Gold edge/reflection;
- faint Dusty Steel concealed light behind the button;
- readable Pale Driftwood label.

Hover:

- concealed light widens slightly;
- shadow lifts subtly;
- border/reflection becomes a little clearer;
- do not scale the button up.

Focus:

- visible focus ring plus restrained illumination;
- keyboard focus must be at least as clear as mouse hover.

Pressed:

- visual compression of approximately `1–2px`;
- outer shadow tightens;
- underlight becomes slightly brighter and more concentrated;
- the interaction should feel like pressing a softly backlit architectural control.

Release:

- return smoothly over approximately `140–220ms`;
- use calm easing;
- avoid spring/bounce effects.

Disabled:

- lower contrast;
- no glow expansion;
- no metallic emphasis;
- retain readable label where possible.

## Plush Drift Tactile Illumination

The auth experience is a flagship expression of Plush Drift tactile illumination.

### Layer stack

1. Slate Navy environmental field.
2. Text-free ambient orbit/architectural layer.
3. low-opacity warm/cool atmospheric wash.
4. Dark Suede foreground card or control.
5. concealed Dusty Steel underlight.
6. restrained Champagne Rose Gold reflected edge.
7. live content and accessible focus/state layer.

### Intensity guidance

- Rest: barely perceptible illumination.
- Hover: +10–20% perceived light.
- Focus: +20–30% perceived light plus clear focus ring.
- Press: narrower, brighter concealed light with 1–2px compression.
- Success: calm, brief confirmation, not celebratory fireworks.

### Prohibited effects

- neon tubes
- cyberpunk cyan/magenta glow
- flashing
- pulsing authentication fields
- exaggerated bloom
- hard glowing outlines around every card
- animation used as the only state cue

## Mobile Architectural Drawing

### Breakpoint behavior

At `<= 767px`, collapse to a single-column experience.

Order:

1. approved Orb logo
2. `Welcome Back`
3. short support line
4. login card
5. password recovery / account creation links
6. support pathway
7. optional ambient art behind or below the primary content

### Mobile geometry

- horizontal page padding: `20–24px`;
- card width: `100%` with a practical max of `440px`;
- form controls: minimum 44px touch target, preferably 48–52px;
- no split-screen treatment;
- no horizontally scrolling decorative art;
- ambient background uses `website/assets/auth/login-vip-hero-mobile.svg`;
- Orb logo should remain comfortably separated from the card so it reads as brand, not field decoration.

### Keyboard and viewport

- page must remain usable with the software keyboard open;
- primary action must not be trapped below an inaccessible fixed viewport;
- use `100dvh`/`100svh` carefully and allow vertical scrolling;
- preserve password-manager and autofill behavior.

## Account Flow Architecture

### Login

`Email → Password → Sign In → authenticated destination`

On authentication failure, retain the entered email where security policy permits and show a calm, field-associated message.

### Forgot password

Heading: **Reset Your Access**

Support line:

`Enter the email associated with your LuxSync account and we’ll help you restore access.`

Submit confirmation:

**Check Your Email**

`If an account matches that address, you’ll receive the next step shortly.`

This wording avoids unnecessarily disclosing account existence.

### Create account

Heading: **Create Your LuxSync Account**

Support line:

`Save preferences, follow orders, revisit recommendations, and keep your LuxSync experience connected.`

Collect only fields required by the actual production account/commerce platform. Do not add demographic or property-profile questions to the credential-creation step merely for marketing convenience.

### Verification / two-step access

Only display if the production account platform requires or supports it.

- Prefer platform-native verification controls.
- Six-code visual treatment is acceptable when technically appropriate.
- Support paste/autofill.
- Provide resend guidance.
- Do not use pressure language or aggressive countdown animation.

### Locked / recovery-required

- Explain the next safe action clearly.
- Provide Support path.
- Do not expose internal security rules or account-enumeration details.

### Post-login welcome

Heading:

**Welcome Back, [First Name]**

Only show modules supported by real account data, such as:

- Orders
- Saved products
- Saved recommendations
- Recently viewed items
- Support
- Account preferences

Do not invent personalized values or saved-state capabilities.

## Production Graphic Mini-Library

The approved auth graphics live under `website/assets/auth/`.

### Production-approved ambient graphics

| Asset | Purpose | Placement |
|---|---|---|
| `login-vip-hero.svg` | text-free desktop VIP atmosphere | Zone A background / ambient layer |
| `login-vip-hero-mobile.svg` | text-free mobile ambient treatment | mobile page background / lower atmosphere |
| `member-access-ambient.svg` | reusable abstract underlight/orbit layer | behind login card, recovery card, verification card |
| `account-welcome-banner.svg` | text-free post-login banner base | authenticated account welcome area |

### Design-reference graphics

| Asset | Purpose | Publication rule |
|---|---|---|
| `auth-card-reference.svg` | login card geometry and illumination reference | reference only; build live HTML/CSS |
| `auth-input-states.svg` | input-state visual reference | reference only; build live semantic controls |
| `auth-button-states.svg` | button-state visual reference | reference only; build live semantic controls |

The auth asset manifest is `website/assets/auth/manifest.json`.

## Exact Logo Placement

| Context | Approved asset | Rule |
|---|---|---|
| Desktop welcome/header | `brand/assets/logos/png/luxsync-horizontal-combo.png` | primary desktop lockup |
| Extended marketing/auth email visual | `brand/assets/logos/png/luxsync-horizontal.png` | only where horizontal space supports it |
| Mobile / compact auth | `brand/assets/logos/png/luxsync-orb.png` | compact brand mark |

Never generate a logo inside an auth background, illustration, icon set, or AI image. Place the approved file directly.

## CSS / Token Contract

Use `website/styles/account-access-tokens.css` for the implementation-level values and interaction timing. That file complements, not replaces, `website/styles/design-system.md`.

Core variables include:

- `--auth-canvas`
- `--auth-surface`
- `--auth-text`
- `--auth-muted`
- `--auth-underlight`
- `--auth-metal`
- `--auth-radius-card`
- `--auth-radius-control`
- `--auth-focus-ring`
- `--auth-motion-fast`
- `--auth-motion-standard`

## Security / Platform Boundary

GoDaddy Commerce Plus remains the current production commerce/account authority unless a later repository decision changes it.

This specification defines visual behavior, page architecture, responsive behavior, copy, interaction states, and production-safe brand assets. It does **not** define:

- authentication provider;
- password storage;
- password policy;
- MFA method;
- social-login provider;
- passkey implementation;
- session/token policy;
- customer identity database;
- authorization rules.

Do not build a custom credential backend merely to reproduce the design. Adapt the real production account component or redirect/delegated login flow to this visual system once the supported integration contract is known.

## Accessibility Requirements

- WCAG 2.2 AA-oriented contrast and interaction patterns.
- Semantic labels and instructions.
- Full keyboard operation.
- Visible keyboard focus.
- Touch targets at least 44px.
- Password manager/autofill compatibility.
- Accessible show/hide-password labeling.
- Field errors connected programmatically to fields.
- Reduced-motion support.
- No authentication state communicated by glow, animation, or color alone.
- Decorative SVGs use empty alt / `aria-hidden` when placed as atmosphere.
- Logo images use meaningful LuxSync alt text where they communicate brand identity.

## Acceptance Criteria

The account-access experience passes LuxSync review when:

- every customer is welcomed with a VIP-quality experience;
- the approved logo masters are used directly and exclusively;
- Manrope and Inter are used correctly;
- desktop uses a calm two-zone composition;
- mobile collapses cleanly to one column;
- card, input, and button states visibly express Plush Drift tactile illumination;
- Champagne Rose Gold remains restrained;
- password recovery uses security-safe copy;
- unsupported authentication providers or features are not invented;
- accessibility remains complete without glow or motion;
- text-free ambient graphics stay behind live HTML/CSS content;
- the account integration preserves Commerce Plus/security boundaries;
- the visual result matches the approved LuxSync VIP login direction rather than a generic SaaS login template.
