<!-- LUXSYNC-BRAND-HEADER:START -->
<p align="center"><img src="../../brand/brand-system-v4/01-logos/luxsync-horizontal-approved.png" alt="LuxSync LLC — Where Luxury Lives Intelligently" width="620"></p>
<!-- LUXSYNC-BRAND-HEADER:END -->

# RB-002 — GoDaddy Airo AI Builder

**Status:** Active
**Last updated:** 2026-08-31
**Scope:** LuxSync website generation and staging workflow

## Purpose

Provide a repeatable Airo workflow without allowing generated output to override the repository or prematurely replace GoDaddy Commerce Plus.

## Governing References

Review before each Airo build:

1. `docs/project-runbook.md`
2. `docs/master-catalog.md`
3. `docs/architecture/website-information-architecture.md`
4. `docs/decisions/DEC-004-commerce-plus-and-airo-role.md`
5. `brand/README.md`
6. `brand/colors.md`
7. `brand/typography.md`
8. `brand/voice-and-tone.md`
9. `website/pages/home.md`
10. `website/styles/design-system.md`
11. `prompts/website/PR-001-LuxSync-Airo-Master-Website-Build-Prompt.md`
12. `docs/runbooks/RB-008-Luxury-Orbit-Brand-Asset-Generation.md`

## Product Distinction

- **Commerce Plus / Websites + Marketing:** launch commerce platform and system of record.
- **Airo AI Builder:** staging/reference website, application, store, design, and code-generation environment.
- **Airo Plus:** supporting branding, SEO, content, marketing, accessibility, and compliance-assistant capabilities where available; not the governing architecture.

## Preconditions

- Repository `master` is current and repository consistency validation passes.
- PR-001 is the approved draft for the first generation pass.
- Plush Drift v2.1 is the authoritative base brand system.
- Crisp Dimensional is the active web/graphics treatment.
- Manrope 500/600 is authoritative for headings/display/UI.
- Inter 400/500 is authoritative for body/supporting UI.
- Official slogan is `Where Luxury Lives Intelligently`.
- Homepage hero is `Smart Living. Elevated.`.
- Primary CTA is `Shop Smart Home`; secondary CTA is `Get the ROI Guide`.
- The build is staging/reference until the validation gate passes.
- Live payments and production DNS remain unchanged.

## Step 1 — Start the Staging Project

1. Sign in to GoDaddy.
2. Open **Airo AI Builder**, not the legacy AI Website Builder.
3. Start a website/store project named clearly, such as `LuxSync Storefront Staging`.
4. Paste the complete current PR-001 prompt.
5. Start the build.

## Step 2 — Structural Review

Before cosmetic edits, verify Home, Shop, Solutions, Guides, About, Support, Search, Account, and Cart.

Confirm the hero, slogan, calls to action, five approved audiences, product collections, and future-product guardrails match ARC-001 and the homepage blueprint.

Reject invented partnerships, awards, reviews, certifications, customer counts, prices, availability, financial data, or supplier claims.

## Step 3 — Brand Calibration

### Base palette — Plush Drift v2.1

- Slate Navy `#0D1526`
- Dark Suede `#172036`
- Pale Driftwood `#D0BEB0`
- Warm Taupe Mauve `#9E8B85`
- Antique Rose Taupe `#967878`
- Dusty Steel `#7B96B2`
- Champagne Rose Gold Metallic — approved palette-derived treatment

### Typography

- Headings / display / navigation / CTA labels / graphic UI: **Manrope 500/600**
- Body / product copy / forms / supporting UI: **Inter 400/500**

Approved logo artwork may preserve its exact lettering as artwork; do not infer website fonts from the logo.

### Crisp Dimensional character

Use layered dark surfaces, restrained Champagne Rose Gold Metallic accents, soft Dusty Steel light accents, Pale Driftwood copy, premium imagery, generous negative space, and minimal organic motion.

Use the approved metallic gradient from approved palette colors. Metallic highlight/shadow stops and Dusty Steel-derived icy-blue tints are rendering effects, not additional standalone colors.

Reject cyberpunk neon, lavender as an unapproved base color, loud gradients, generic SaaS blue, dense gadget-store grids, excessive glassmorphism, and aggressive popups.

## Step 4 — Load Repository Assets

Use current approved assets beneath `brand/brand-system-v4/`. The `brand/assets/` directory contains protected source logos and text-free photography only.

- Preserve the approved exact primary monogram and horizontal lockup.
- Use SVG for icons/vector UI and optimized WebP for larger raster scenes where supported.
- Production scenes under `12-scenes/` are text-free backgrounds intended for native website copy and approved branding overlays.
- Follow RB-008 when generated assets change.

## Step 5 — Commerce Representation

Represent catalog browsing, product details, search, account, cart, and checkout flow without treating Airo as the approved production commerce engine.

Do not connect live payments, create an unmanaged live catalog, or use unvalidated product data.

## Step 6 — Responsive Review

Review desktop, tablet, and mobile navigation, hero crop, CTA visibility, cards, forms, cart, footer, typography, and touch targets. Mobile must be intentionally composed.

## Step 7 — Accessibility Review

Validate semantic headings, keyboard access, visible focus, contrast, alt text, labels, touch targets, reduced motion, and no color-only meaning. Generated output is not presumed compliant.

## Step 8 — Content Review

Every claim must trace to repository-supported content. Reject unsupported awards, certifications, testimonials, savings, compatibility, supplier relationships, endorsements, or medical outcomes.

## Step 9 — Export and Repository Review

If code export is available:

1. Export the generated source.
2. Preserve an untouched reference snapshot.
3. Inspect the actual framework, dependencies, build commands, APIs, analytics, and generated secrets.
4. Place reviewed source beneath `website/` only after the structure is understood.
5. Never commit secrets or credentials.

## Step 10 — Commerce Validation Gate

Before any Airo storefront could replace or bypass Commerce Plus, validate catalog, shipping, sales tax, payments, orders, refunds, customer accounts, fulfillment, recurring billing, analytics, accessibility, SEO, source-control/export, and rollback.

If any required capability is missing, Commerce Plus remains production authority.

## Step 11 — Publish Rules

Temporary staging publication is acceptable for review if it does not alter production DNS or commerce behavior.

Do not connect the production domain, enable live payments, or replace the production storefront during the first pass.

## Step 12 — Record the Result

Record prompt version, Airo project name, date, deviations, approved/rejected screens, export status, branch/commit, and commerce-validation status.

## Completion Criteria

A generation cycle is complete when CL-001 has been executed; structure, brand, content, responsive behavior, accessibility, and commerce boundaries have been reviewed; and exported source, if any, has been captured for repository review.
