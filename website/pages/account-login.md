# LuxSync Account Access Blueprint

**Status:** Active / Pre-build UX baseline  
**Experience:** VIP Account Access  
**Brand:** LuxSync v3 with Plush Drift tactile illumination  
**Typography:** Manrope + Inter  
**Official slogan:** Where Luxury Lives Intelligently

## Purpose

The LuxSync login and account-access experience must feel like entry into a private luxury service environment, not a generic authentication form. Every customer should feel recognized, welcomed, and important from the first account interaction.

The account experience must remain simple, secure, accessible, and commerce-oriented while carrying the Plush Drift design DNA: layered dark surfaces, concealed light, tactile controls, restrained metallic detail, and Intelligent Calm voice.

## Primary Experience Principle

**Every LuxSync customer is treated like a VIP.**

VIP does not mean flashy, exclusive in a socially exclusionary way, or overloaded with luxury language. It means:

- the interface feels considered and personal;
- the customer is welcomed rather than processed;
- access is calm, clear, and friction-light;
- assistance is easy to find;
- account information feels private and well cared for;
- the visual environment communicates polish, trust, and attention.

## Recommended Page Route

Primary route: `/account/login`

Related account states should remain visually consistent:

- `/account/create`
- `/account/forgot-password`
- `/account/reset-password`
- `/account/verify`
- `/account/verification-code`
- `/account/locked`
- `/account/welcome`

Do not assume these exact production routes until the actual Commerce Plus/account implementation is confirmed. Preserve them as UX blueprint routes/placeholders.

## Desktop Layout

Use a balanced two-zone composition.

### Welcome / VIP atmosphere zone

Approximately 52–58% of the desktop width.

Contains:

1. approved LuxSync logo artwork;
2. restrained architectural smart-living visual or abstract Plush Drift illumination graphic;
3. warm welcome statement;
4. short value message;
5. optional small trust/service cue.

Suggested hierarchy:

**Welcome Back**

**Your LuxSync experience is ready.**

Supporting copy:

`Sign in to continue to your orders, saved preferences, curated recommendations, and LuxSync support.`

Optional eyebrow:

`PRIVATE MEMBER ACCESS`

Avoid overly formal club language, velvet-rope language, status tiers, or claims that imply some normal customers are less valued.

### Account-access zone

Approximately 42–48% of the desktop width.

Use a vertically centered elevated access card with generous breathing room.

The card should include:

- Email address
- Password
- Show/hide password control
- Remember me option where appropriate
- Primary `Sign In` CTA
- `Forgot password?`
- `Create your LuxSync account`
- clear Support pathway

If third-party sign-in is later supported by the actual account platform, add it only after implementation validation. Do not invent social-login providers in the design baseline.

## Mobile Layout

Use a single-column experience.

Priority order:

1. compact approved logo
2. `Welcome Back`
3. short VIP-oriented supporting copy
4. login card
5. account creation / password support
6. customer-support pathway
7. restrained visual atmosphere below or behind the main card

Do not force a split-screen composition onto mobile.

The form must fit comfortably without horizontal scrolling or oversized decorative elements.

## Plush Drift Tactile Illumination

The login page is a flagship use case for Plush Drift tactile illumination.

### Login card

- Dark Suede surface over a Slate Navy field.
- Very soft Pale Driftwood / Warm Taupe Mauve atmospheric lift behind the card.
- Optional restrained Champagne Rose Gold reflected edge detail.
- Card should appear elevated and softly backlit, not glassy or neon.

### Input fields

Rest:

- Dark surface
- readable Pale Driftwood/Inter text
- subtle border or inset depth

Focus:

- Dusty Steel concealed underlight becomes slightly more visible
- accessible focus outline remains clearly identifiable
- field may lift optically but should not jump or resize

Valid/success:

- communicate with icon/text as well as color
- keep the overall palette restrained

Error:

- use accessible error messaging and iconography
- never rely only on red/color
- do not use aggressive flashing or shake animation

### Primary Sign In button

Rest:

- dark premium foreground surface
- faint concealed Dusty Steel underlight
- optional metallic micro-highlight at edge or icon

Hover:

- underlight expands and brightens modestly
- no dramatic scale-up

Pressed:

- surface compresses visually inward approximately 1–2 px
- outer shadow tightens
- concealed light becomes slightly stronger
- release returns smoothly

Keyboard focus:

- clear focus indicator plus restrained illumination

Reduced motion:

- remove physical travel if needed
- retain non-motion focus/pressed differentiation

## Metallic Integration

Champagne Rose Gold Metallic is used as jewelry, not wallpaper.

Approved uses:

- tiny divider accent
- fine edge reflection
- small member-access emblem
- micro-icon detail
- restrained headline ornament

Do not use metallic gradients as large text fills, full form backgrounds, or dominant button fills.

## Dedicated Login Visual Asset Set

Create an account-access mini-library under the active v3 asset system.

Recommended assets:

1. `login-vip-hero.webp` — text-free premium background / atmosphere image
2. `login-vip-hero-mobile.webp` — mobile-safe crop or alternate composition
3. `member-access-ambient.svg` — restrained abstract underlight/orbit composition
4. `account-access-emblem.svg` — optional small metallic/Dusty Steel decorative mark, not a new logo
5. `auth-card-reference.svg` — visual reference for backlit account card states
6. `auth-input-states.svg` — rest/focus/error/success field treatment reference
7. `auth-button-states.svg` — rest/hover/focus/pressed button treatment reference
8. `account-welcome-banner.svg` — reusable post-login welcome banner treatment

Do not create alternate LuxSync logos for the auth experience. Use the canonical approved logo artwork once the final baseline is confirmed.

## VIP Language System

Preferred phrases:

- `Welcome Back`
- `Your LuxSync experience is ready.`
- `Welcome to your LuxSync account.`
- `Your home. Your preferences. Your LuxSync.`
- `Need assistance? LuxSync Support is here.`

Use `Member Access` sparingly as an eyebrow or utility label. The customer should feel personally valued without the interface sounding like a private club.

Avoid:

- `Elite members only`
- `Exclusive access` unless a genuinely restricted feature exists
- invented loyalty status
- artificial scarcity
- status hierarchy among ordinary customers

## Create Account Experience

The account-creation page should feel like a warm invitation.

Suggested heading:

**Create Your LuxSync Account**

Suggested support line:

`Save preferences, follow orders, revisit recommendations, and keep your LuxSync experience connected.`

Do not require unnecessary profile information at account creation. Collect only what the production commerce/account system actually needs.

## Password Recovery

Password recovery should be calm and reassuring.

Suggested heading:

**Reset Your Access**

Suggested support line:

`Enter the email associated with your LuxSync account and we’ll help you restore access.`

Success state:

**Check Your Email**

`If an account matches that address, you’ll receive the next step shortly.`

Use security-safe wording that does not unnecessarily reveal whether an email address has an account.

## Verification / Two-Step Access

If verification is required by the production platform:

- use six clearly readable code positions or the platform-native control;
- support paste/autofill where available;
- preserve keyboard usability;
- provide resend guidance;
- avoid countdown pressure language;
- use the same tactile illumination language as other auth controls.

## Post-Login Welcome

The first authenticated screen should continue the VIP feeling rather than abruptly dropping into generic ecommerce UI.

Recommended welcome area:

**Welcome Back, [First Name]**

Supporting modules may include, when supported by real data:

- Orders
- Saved products
- Saved recommendations
- Recently viewed items
- Support
- Account preferences

Do not invent personalization data that the real platform cannot provide.

## Accessibility and Security UX

- WCAG 2.2 AA-oriented contrast and interaction patterns
- semantic labels, not placeholder-only fields
- full keyboard operation
- visible focus
- touch targets sized for mobile use
- password manager/autofill compatibility
- show/hide password control with accessible label
- errors linked to relevant fields
- reduced-motion support
- no authentication state communicated by glow/color alone
- no sensitive information baked into decorative graphics

## Commerce / Implementation Boundary

GoDaddy Commerce Plus remains the current production commerce/account authority unless a later repository decision changes it.

This blueprint defines UX and visual behavior. It does not select an authentication provider, identity platform, password policy, MFA mechanism, session policy, social login provider, or customer-data architecture.

Those choices must follow the actual production platform and security implementation.

## Acceptance Criteria

The account-access experience passes LuxSync review when:

- the customer is welcomed, not merely presented with a form;
- the page feels visually related to the storefront but quieter and more private;
- Plush Drift tactile illumination is visible on card/input/button interaction states;
- Champagne Rose Gold is restrained;
- Manrope + Inter are used correctly;
- the approved logo is not regenerated or altered;
- mobile remains simple and fast;
- password/account recovery is calm and security-safe;
- accessibility does not depend on glow, motion, or color;
- no unsupported authentication capabilities are invented;
- every ordinary LuxSync customer receives the same high-care, VIP-level experience.
