# LuxSync VIP Account Access Assets

**Status:** Active  
**Experience:** VIP Account Access  
**Design DNA:** Plush Drift tactile illumination  
**Brand system:** LuxSync Production Raster v5

This folder contains the dedicated account/login visual mini-library. It intentionally lives under `website/assets/auth/` because `brand/assets/` is the governed Production Raster v5 library and must not contain SVGs.

## Logo rule

No logo is recreated in this folder.

Use only the production-approved masters:

- `../../../brand/assets/01-logos/LuxSync_Logo_Horizontal_Combo.png`
- `../../../brand/assets/01-logos/LuxSync_Logo_Horizontal_Final.png`
- `../../../brand/assets/01-logos/LuxSync_Logo_Orb.png`

The auth graphics are designed to sit behind or beside those exact logo files.

## Production-approved ambient graphics

These files contain no mutable authentication copy and can be used as decorative atmosphere behind live HTML/CSS once the site delivery layer supports these assets:

- `login-vip-hero.svg`
- `login-vip-hero-mobile.svg`
- `member-access-ambient.svg`
- `account-welcome-banner.svg`

## Design-reference graphics

These files document visual states only. Build the real controls as semantic HTML/CSS using `website/styles/account-access-tokens.css`:

- `auth-card-reference.svg`
- `auth-input-states.svg`
- `auth-button-states.svg`

Do not publish the reference diagrams as functional controls.

## Placement

Desktop login:

- Horizontal Combo logo is placed live over `login-vip-hero.svg`.
- `member-access-ambient.svg` may sit behind the auth card at low opacity.
- The auth card, fields, buttons, labels, and links are live HTML/CSS.

Mobile login:

- Orb logo is placed live above the card.
- `login-vip-hero-mobile.svg` may be used as a fixed or absolute background layer.

Post-login welcome:

- Use `account-welcome-banner.svg` as a text-free base and render customer-specific welcome copy live.

## Accessibility

Decorative assets should use `aria-hidden="true"` or empty alt text when embedded as images. Never bake customer names, email addresses, verification codes, authentication errors, or other account data into graphics.

## Source of truth

- Page spec: `website/pages/account-login.md`
- Account manifest: `website/account-access-manifest.json`
- Interaction tokens: `website/styles/account-access-tokens.css`
- Asset manifest: `website/assets/auth/manifest.json`
