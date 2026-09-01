# LuxSync Website Production Source of Truth

**Status:** FINAL launch source-of-truth baseline
**Brand system:** LuxSync Production Raster v5
**Official slogan:** Where Luxury Lives Intelligently

This file is the shortest path through the repository. When two active files appear to conflict, this hierarchy wins:

1. `brand/README.md`, `brand/colors.md`, `brand/typography.md`, `brand/voice-and-tone.md`
2. `website/styles/design-system.md`
3. `website/implementation-manifest.json`, `website/account-access-manifest.json`, and `website/asset-map.md`
4. page blueprints under `website/pages/`
5. approved copy under `content/`
6. architecture and operational detail under `docs/`
7. reusable prompts under `prompts/`

## Locked identity

- Official slogan: **Where Luxury Lives Intelligently**
- Primary CTA: **Find My LuxSync Solution**
- Secondary CTA: **Shop Smart Home**
- Concierge: **LuxSync Intelligent Living Concierge**
- Result: **My LuxSync Blueprint**
- Bridgette Beardsley: **Co-Founder & Chief Technology and Strategy Officer**
- Sheldon Bardol: **Co-Founder & Chief Customer and Operations Officer**
- Account principle: **every customer receives the same high-care, VIP-level account experience**

## Locked website model

LuxSync begins with lifestyle outcomes and compatible intelligent-living experiences, then recommends technology categories and validated products. It is not positioned as a traditional on-site installation company unless a future approved decision changes the model.

## Canonical page set

- Home
- Find My LuxSync Solution / Concierge
- My LuxSync Blueprint
- Solutions hub
- Commercial Offices
- Senior Living / Nursing Homes
- Short-Term Rentals
- Residential Living
- Seniors / Caregivers / Aging in Place
- Shop / product collections
- Guides / ROI library
- About / founders
- FAQs
- Contact / Support
- VIP Account Access / Login route family, subject to final Commerce Plus authentication-route integration

## Contact contract

The adaptive Contact page begins with Support, Product Information, Consultation, General Question, Business / Partnership, or Other. It reveals only the fields needed for the selected path and shares Property Profile conventions with the Concierge.

## Commerce and account contract

Names, prices, inventory, ratings, availability, subscriptions, compatibility and product imagery must come from validated commerce/manufacturer data. Never invent ratings, scarcity, stock status, warranties, shipping promises, testimonials or prices.

GoDaddy Commerce Plus remains the current production commerce/account authority unless a later approved decision changes it. The VIP account-access specification defines visual and interaction behavior only; it does not authorize a custom credential backend, identity provider, password policy, MFA mechanism, passkey flow, social-login provider, session policy, or authorization model.

## Visual contract

Use exact logo masters plus live HTML/CSS for the active site. The imported raster slices outside `brand/assets/01-logos/` are reference-only except for assets explicitly marked `production-approved` in a current asset manifest.

For account access, production-approved ambient graphics are governed by `website/assets/auth/manifest.json`. Authentication copy, customer data, fields, buttons and state messaging remain live HTML/CSS.

Do not publish generated logo approximations, baked support hours, fake founder identities, retired copy, board-crop fragments, customer-specific auth text baked into graphics, or reference-only control diagrams.

## VIP Account Access contract

Primary references:

- `website/pages/account-login.md`
- `website/account-access-manifest.json`
- `website/styles/account-access-tokens.css`
- `website/assets/auth/manifest.json`
- `docs/checklists/CL-002-Account-Access-Review.md`

Locked account visual rules:

- only the three approved logos under `brand/assets/01-logos/` may be used;
- desktop uses a calm welcome/auth two-zone composition;
- mobile collapses to one column and prefers the approved Orb logo;
- Plush Drift tactile illumination governs card, input and button interaction states;
- Dusty Steel is the preferred cool underlight;
- Champagne Rose Gold remains restrained metallic detail;
- Manrope + Inter remain authoritative;
- every customer receives the same VIP-quality welcome;
- no unsupported authentication capability may be invented merely to match the visual design.

## Implementation handoff

A site builder should begin with:

1. `website/implementation-manifest.json`
2. `website/navigation.md`
3. `website/asset-map.md`
4. `prompts/website/PR-001-LuxSync-Airo-Master-Website-Build-Prompt.md`
5. `docs/checklists/CL-001-Airo-First-Pass-Review.md`

For account/login implementation, additionally use:

6. `website/account-access-manifest.json`
7. `website/pages/account-login.md`
8. `website/styles/account-access-tokens.css`
9. `website/assets/auth/manifest.json`
10. `docs/checklists/CL-002-Account-Access-Review.md`

The Concierge implementation source is `website/src/concierge/`, including the generated `luxsync-concierge-engine.v1.json` configuration.
