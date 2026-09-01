# DEC-006 — VIP Account Access Experience

**Status:** Accepted  
**Date:** 2026-09-01

## Decision

LuxSync account access will be designed as a high-care VIP experience while remaining equally available to every ordinary LuxSync customer.

The approved visual and interaction baseline is governed by:

- `website/pages/account-login.md`
- `website/account-access-manifest.json`
- `website/styles/account-access-tokens.css`
- `website/assets/auth/manifest.json`
- `docs/checklists/CL-002-Account-Access-Review.md`

## Brand Contract

Only the approved logo masters may be used:

- `brand/assets/01-logos/LuxSync_Logo_Horizontal_Combo.png`
- `brand/assets/01-logos/LuxSync_Logo_Horizontal_Final.png`
- `brand/assets/01-logos/LuxSync_Logo_Orb.png`

No authentication graphic, generated visual, implementation, or future design pass may redraw, retype, recolor, regenerate, simplify, or substitute the LuxSync logo.

The experience uses:

- LuxSync Production Raster v5
- Plush Drift tactile illumination
- Manrope + Inter
- Slate Navy / Dark Suede foundations
- Dusty Steel concealed underlighting
- restrained Champagne Rose Gold metallic detail
- Intelligent Calm voice

## UX Contract

Desktop uses a calm two-zone welcome/auth composition. Mobile collapses to one column.

Preferred language includes:

- `MEMBER ACCESS`
- `Welcome Back`
- `Your LuxSync experience is ready.`

The VIP principle means considered service and presentation, not artificial membership tiers or exclusionary status language.

## Authentication Boundary

GoDaddy Commerce Plus remains the current production commerce/account authority unless a later explicit architecture decision changes it.

This decision does not approve:

- a custom credential backend;
- a new identity provider;
- social login providers;
- passkeys;
- a particular MFA method;
- password/session/token policy;
- custom authorization architecture.

Final production routes and authentication mechanisms must follow the supported account integration while preserving the approved LuxSync visual and interaction experience.

## Asset Boundary

The approved exact logos remain under `brand/assets/01-logos/`.

The clean vector account-access mini-library lives under `website/assets/auth/`, not `brand/assets/`, so the Production Raster v5 asset validator remains PNG-only.

Production ambient auth vectors must be text-free. Reference-only UI diagrams must never be used as functional controls.

## Consequences

- Account/login is now a durable LuxSync website experience rather than a generic commerce utility.
- Future builders must pass CL-002 before production account release.
- The source-of-truth validator must detect logo substitutions, obsolete auth paths, missing account artifacts, unsafe publication status, and auth assets placed inside the Production Raster library.
- A live login route is not considered integrated until the actual Commerce Plus/account contract is validated and connected.
