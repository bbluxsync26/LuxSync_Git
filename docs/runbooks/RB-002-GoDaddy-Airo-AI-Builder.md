# RB-002 — GoDaddy Airo AI Builder

**Status:** Active / Reconciled
**Last updated:** 2026-09-03
**Scope:** LuxSync website generation and staging workflow

## Purpose

Provide a repeatable Airo workflow without allowing generated output to override repository decisions, the Intelligent Living Concierge engine, the adaptive Contact architecture, or the GoDaddy Commerce Plus production boundary.

For the controlled GitHub → Airo → GitHub transport and branch process, use `docs/runbooks/RB-012-Airo-GitHub-Development-Loop.md`. The package contract is `docs/architecture/airo-source-package-contract.md`.

## Governing References

Review before each Airo build:

1. `docs/master-catalog.md`
2. `docs/project-runbook.md`
3. `docs/production-source-of-truth.md`
4. `docs/architecture/website-information-architecture.md`
5. `docs/architecture/intelligent-living-concierge.md`
6. `docs/architecture/airo-source-package-contract.md`
7. `docs/decisions/DEC-004-commerce-plus-and-airo-role.md`
8. `brand/README.md`
9. `brand/brand-architecture.md`
10. `brand/colors.md`
11. `brand/typography.md`
12. `brand/voice-and-tone.md`
13. `website/styles/design-system.md`
14. `website/pages/home.md`
15. `website/pages/about.md`
16. `website/pages/faqs.md`
17. `website/pages/contact.md`
18. `content/about.md`
19. `content/faqs.md`
20. `content/contact.md`
21. `content/product-catalog.md`
22. `docs/leadership/bridgette-beardsley.md`
23. `docs/leadership/sheldon-bardol.md`
24. `website/src/concierge/`
25. `prompts/website/PR-001-LuxSync-Airo-Master-Website-Build-Prompt.md`
26. `docs/runbooks/RB-012-Airo-GitHub-Development-Loop.md`

## Product Distinction

- **GoDaddy Commerce Plus:** production commerce system of record.
- **Airo AI Builder:** staging/reference website, application, store, design, and code-generation environment.
- **LuxSync Intelligent Living Concierge:** flagship guided recommendation architecture and rules engine governed by the repository.
- **Airo Plus:** supporting branding, SEO, content, marketing, accessibility/compliance assistance where available; not the governing architecture.
- **GitHub:** product source of truth and approval history.

## Preconditions

- Repository `master` is current.
- Repository consistency validation passes.
- Airo source-package selection validation passes.
- PR-001 is current and reconciled.
- LuxSync Production Raster v5 is the authoritative visual system.
- Plush Drift is the enduring design DNA.
- Manrope 500/600 is authoritative for headings/display/UI.
- Inter 400/500 is authoritative for body/supporting UI.
- Sole approved public slogan/hero line is `Where Luxury Lives Intelligently`.
- Primary homepage CTA is `LuxSync Concierge`.
- Secondary homepage CTA is `Shop Smart Home`.
- Supporting CTA is `Get the ROI Guide`.
- Contact routes support to `support@luxsync.net` and information/consultation to `info@luxsync.net`.
- The build is staging/reference until validation passes.
- Live payments and production DNS remain unchanged.

## Step 1 — Build the Governed Airo Source Package

Preferred local command:

```bash
python scripts/build-airo-source-package.py
```

Validation-only:

```bash
python scripts/build-airo-source-package.py --check
```

Default output:

`dist/airo/LuxSync-Airo-Source.zip`

You may instead run the GitHub Actions workflow **Build Airo source package** and download the resulting `luxsync-airo-source` artifact.

The package is allowlist-based. Do not replace it with a raw repository ZIP. It deliberately excludes financial planning, reference boards, protected logo source masters, print/vendor production files, audits, Git internals, and other material Airo does not need for website generation.

## Step 2 — Start the Staging Project

1. Sign in to GoDaddy.
2. Open Airo AI Builder.
3. Start or open a clearly non-production website project.
4. Upload `LuxSync-Airo-Source.zip` as source context.
5. Use the complete current PR-001 prompt as the controlling instruction.
6. Tell Airo to evolve the supplied source rather than inventing a disconnected second application.
7. Start the build.

## Step 3 — Structural Review

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

Confirm the sole slogan, CTAs, approved audiences, product collections, founder profiles, canonical FAQ content, adaptive Contact form, Concierge/Blueprint journey, and future-product guardrails match the repository.

Reject invented partnerships, awards, reviews, certifications, customer counts, prices, availability, financial data, or supplier claims.

## Step 4 — Concierge Review

Verify **LuxSync Concierge** is treated as a flagship journey rather than a novelty quiz.

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

## Step 5 — Contact Review

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

## Step 6 — Product Catalog Review

Use `content/product-catalog.md`.

Verify product-family architecture and solution concepts are represented without converting planning concepts into fake live SKUs.

Exact product names, prices, stock, shipping, availability, subscriptions, and compatibility require validated Commerce Plus/manufacturer data.

## Step 7 — Brand Calibration

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

Use LuxSync Production Raster v5 with restrained Plush Drift tactile illumination. Reject cyberpunk neon, unapproved lavender/purple base treatment, generic SaaS blue, dense gadget-store grids, excessive glassmorphism, aggressive popups, or retired slogan graphics.

## Step 8 — Commerce Representation

Represent catalog browsing, product details, search, account, cart, and checkout flow without treating Airo as approved production commerce authority.

Do not connect live payments, create an unmanaged live catalog, or use unvalidated product data.

## Step 9 — Responsive and Accessibility Review

Review desktop, tablet, and mobile navigation, hero, Concierge, adaptive forms, cards, cart, footer, typography, and touch targets.

Validate semantic headings, keyboard access, visible focus, contrast, labels, touch targets, reduced motion, and no color-only meaning. Dynamic form changes and error messages must be accessible.

## Step 10 — Content Integrity Review

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

## Step 11 — Export and Repository Review

When the Airo iteration is ready:

1. Export/download the full generated project.
2. Preserve an untouched reference snapshot.
3. Record the source-package commit SHA and Airo project/export identity when possible.
4. Inspect framework, dependencies, build commands, APIs, analytics, generated secrets, and configuration.
5. Reconcile accepted changes through a short-lived branch based on `website/airo-development` as defined in RB-012.
6. Never commit secrets or credentials.
7. Ensure Concierge engine and stable field IDs are not silently replaced by generated alternatives.
8. Run CL-001 and full repository CI before merge.

## Step 12 — Commerce Validation Gate

Before any Airo storefront could replace or bypass Commerce Plus, validate catalog, shipping, sales tax, payments, orders, refunds, accounts, fulfillment, recurring billing, analytics, accessibility, SEO, source-control/export, and rollback.

If any required capability is missing, Commerce Plus remains production authority.

## Step 13 — Publish Rules

Temporary staging publication is acceptable for review if it does not alter production DNS or commerce behavior.

Do not connect the production domain, enable live payments, or replace the production storefront during an Airo build cycle.

## Step 14 — Record the Result

Record prompt version, source-package commit SHA, Airo project name, date, deviations, approved/rejected screens, Contact/Concierge status, export status, reconciliation branch/commit, and commerce-validation status.

## Completion Criteria

A generation cycle is complete when CL-001 has been executed; structure, Concierge, Contact, catalog, brand, content, responsive behavior, accessibility, and commerce boundaries have been reviewed; exported source has been captured for repository review; and accepted changes have passed GitHub CI.

## Production Input Set

The Airo source package automatically supplies the governed website-build input set. Its selection contract is ARC-003.

The core operational priority remains:

1. `docs/production-source-of-truth.md`
2. `website/implementation-manifest.json`
3. `website/navigation.md`
4. `website/asset-map.md`
5. page blueprints under `website/pages/`
6. approved copy under `content/`
7. current production implementation under `site/`
8. PR-001 as the controlling Airo instruction

Use exact approved logo deliveries and live HTML/CSS. Do not import reference-only raster composites as public UI.
