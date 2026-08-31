# RB-002 — GoDaddy Airo AI Builder

**Status:** Active / Reconciled  
**Last updated:** 2026-08-31  
**Scope:** LuxSync website generation and staging workflow

## Purpose

Provide a repeatable Airo workflow without allowing generated output to override repository decisions, the Intelligent Living Concierge engine, the adaptive Contact architecture, or the GoDaddy Commerce Plus production boundary.

## Governing References

Review before each Airo build:

1. `docs/master-catalog.md`
2. `docs/project-runbook.md`
3. `docs/architecture/website-information-architecture.md`
4. `docs/architecture/intelligent-living-concierge.md`
5. `docs/decisions/DEC-004-commerce-plus-and-airo-role.md`
6. `brand/README.md`
7. `brand/brand-architecture.md`
8. `brand/colors.md`
9. `brand/typography.md`
10. `brand/voice-and-tone.md`
11. `website/styles/design-system.md`
12. `website/pages/home.md`
13. `website/pages/about.md`
14. `website/pages/faqs.md`
15. `website/pages/contact.md`
16. `content/about.md`
17. `content/faqs.md`
18. `content/contact.md`
19. `content/product-catalog.md`
20. `docs/leadership/bridgette-beardsley.md`
21. `docs/leadership/sheldon-bardol.md`
22. `website/src/concierge/`
23. `prompts/website/PR-001-LuxSync-Airo-Master-Website-Build-Prompt.md`

## Product Distinction

- **GoDaddy Commerce Plus:** production commerce system of record.
- **Airo AI Builder:** staging/reference website, application, store, design, and code-generation environment.
- **LuxSync Intelligent Living Concierge:** flagship guided recommendation architecture and rules engine governed by the repository.
- **Airo Plus:** supporting branding, SEO, content, marketing, accessibility/compliance assistance where available; not the governing architecture.

## Preconditions

- Repository `master` is current.
- Repository consistency validation passes.
- PR-001 is current and reconciled.
- LuxSync v3 is the authoritative visual system.
- Plush Drift is the enduring design DNA.
- Manrope 500/600 is authoritative for headings/display/UI.
- Inter 400/500 is authoritative for body/supporting UI.
- Sole approved public slogan/hero line is `Where Luxury Lives Intelligently`.
- Primary homepage CTA is `Find My LuxSync Solution`.
- Secondary homepage CTA is `Shop Smart Home`.
- Supporting CTA is `Get the ROI Guide`.
- Contact routes support to `support@luxsync.net` and information/consultation to `info@luxsync.net`.
- The build is staging/reference until validation passes.
- Live payments and production DNS remain unchanged.

## Step 1 — Start the Staging Project

1. Sign in to GoDaddy.
2. Open Airo AI Builder.
3. Start a staging/reference project with an obvious non-production name.
4. Paste the complete current PR-001 prompt.
5. Start the build.

## Step 2 — Structural Review

Before cosmetic edits, verify:

- Home
- Shop
- Solutions
- Guides
- About
- Contact
- Support
- Search
- Account
- Cart

Confirm the sole slogan, CTAs, five approved audiences, product collections, founder profiles, canonical FAQ content, adaptive Contact form, Concierge/Blueprint journey, and future-product guardrails match the repository.

Reject invented partnerships, awards, reviews, certifications, customer counts, prices, availability, financial data, or supplier claims.

## Step 3 — Concierge Review

Verify **Find My LuxSync Solution** is treated as a flagship journey rather than a novelty quiz.

Confirm:

- experience name: LuxSync Intelligent Living Concierge
- output name: My LuxSync Blueprint
- Lifestyle → Experience → Intelligence → Technology model
- Property Profile includes property type and approximate square footage
- existing technology and lifestyle/pain-point discovery are represented
- implementation paths use Essential Intelligence, Elevated Living, and Complete LuxSync Experience
- Blueprint reveals recommended Experiences, foundation, compatibility context, roadmap, and next best action
- recommendations explain Why LuxSync Chose This
- stable engine logic comes from `website/src/concierge/` rather than invented Airo rules

Do not claim save/account functionality is live unless implemented.

## Step 4 — Contact Review

Verify the dedicated Contact page follows `website/pages/contact.md`.

Initial branches must include:

- Support
- Product Information
- Consultation
- General Question
- Business / Partnership
- Other

Confirm conditional questions appear after the first selection rather than exposing one giant form.

Confirm shared Property Profile concepts include Private Residence / STR / Business / Other and approximate square footage.

Confirm support routes to `support@luxsync.net`; all other general/consultation paths route to `info@luxsync.net`.

If Blueprint context is passed into Contact, ensure it is reused appropriately rather than forcing duplicate entry.

Marketing consent must remain separate and optional.

## Step 5 — Product Catalog Review

Use `content/product-catalog.md`.

Verify product-family architecture and solution concepts are represented without converting planning concepts into fake live SKUs.

Exact product names, prices, stock, shipping, availability, subscriptions, and compatibility require validated Commerce Plus/manufacturer data.

## Step 6 — Brand Calibration

Approved palette:

- Slate Navy `#0D1526`
- Dark Suede `#172036`
- Pale Driftwood `#D0BEB0`
- Warm Taupe Mauve `#9E8B85`
- Antique Rose Taupe `#967878`
- Dusty Steel `#7B96B2`
- Champagne Rose Gold Metallic `#D6B0A0` anchor

Typography:

- headings / display / navigation / CTA labels / graphic UI: Manrope 500/600
- body / product copy / forms / supporting UI: Inter 400/500

Preserve approved logo artwork exactly. Do not infer website fonts from logo art.

Use LuxSync v3 with restrained Plush Drift tactile illumination. Reject cyberpunk neon, unapproved lavender/purple base treatment, generic SaaS blue, dense gadget-store grids, excessive glassmorphism, aggressive popups, or retired slogan graphics.

## Step 7 — Commerce Representation

Represent catalog browsing, product details, search, account, cart, and checkout flow without treating Airo as approved production commerce authority.

Do not connect live payments, create an unmanaged live catalog, or use unvalidated product data.

## Step 8 — Responsive and Accessibility Review

Review desktop, tablet, and mobile navigation, hero, Concierge, adaptive forms, cards, cart, footer, typography, and touch targets.

Validate semantic headings, keyboard access, visible focus, contrast, labels, touch targets, reduced motion, and no color-only meaning. Dynamic form changes and error messages must be accessible.

## Step 9 — Content Integrity Review

Every claim must trace to repository-supported content.

Verify:

- exact founder names/titles and approved compact biographies
- FAQ answers preserve approved source meaning
- sole slogan is `Where Luxury Lives Intelligently`
- no retired hero/slogan treatment appears
- correct contact routing
- product/solution terminology matches `content/product-catalog.md`
- no unreleased SmartThings templates or LuxSync Grid presented as live
- no medical claims or life-safety substitution claims

## Step 10 — Export and Repository Review

If code export is available:

1. Export generated source.
2. Preserve an untouched reference snapshot.
3. Inspect framework, dependencies, build commands, APIs, analytics, and generated secrets.
4. Place reviewed source beneath `website/` only after the structure is understood.
5. Never commit secrets or credentials.
6. Ensure Concierge engine and stable field IDs are not silently replaced by generated alternatives.

## Step 11 — Commerce Validation Gate

Before any Airo storefront could replace or bypass Commerce Plus, validate catalog, shipping, sales tax, payments, orders, refunds, accounts, fulfillment, recurring billing, analytics, accessibility, SEO, source-control/export, and rollback.

If any required capability is missing, Commerce Plus remains production authority.

## Step 12 — Publish Rules

Temporary staging publication is acceptable for review if it does not alter production DNS or commerce behavior.

Do not connect the production domain, enable live payments, or replace the production storefront during the first pass.

## Step 13 — Record the Result

Record prompt version, Airo project name, date, deviations, approved/rejected screens, Contact/Concierge status, export status, branch/commit, and commerce-validation status.

## Completion Criteria

A generation cycle is complete when CL-001 has been executed; structure, Concierge, Contact, catalog, brand, content, responsive behavior, accessibility, and commerce boundaries have been reviewed; and exported source, if any, has been captured for repository review.
