# STAGE-001 - GoDaddy Airo First-Pass Build

**Status:** Ready for execution  
**Date:** 2026-09-01  
**Branch:** `airo-first-pass-20260901`  
**Production branch:** `master`  
**Production publishing:** Not authorized by this packet

## Objective

Generate the first complete LuxSync staging/reference website in GoDaddy Airo AI Builder using the current repository source of truth. This run is for visual, structural, content, Concierge, Contact, accessibility, and commerce-boundary review only.

## Locked Inputs

Use these sources in this order:

1. `docs/production-source-of-truth.md`
2. `prompts/website/PR-001-LuxSync-Airo-Master-Website-Build-Prompt.md`
3. `website/implementation-manifest.json`
4. `website/navigation.md`
5. `website/asset-map.md`
6. `website/styles/design-system.md`
7. `website/pages/`
8. `content/`
9. `docs/leadership/`
10. `website/src/concierge/`
11. `docs/checklists/CL-001-Airo-First-Pass-Review.md`

## Locked Brand and Product Facts

- Official slogan: **Where Luxury Lives Intelligently**
- Primary CTA: **Find My LuxSync Solution**
- Secondary CTA: **Shop Smart Home**
- Supporting CTA: **Get the ROI Guide**
- Visual system: **LuxSync Production Raster v5**
- Design DNA: **Plush Drift**
- Voice: **Intelligent Calm**
- Headings/UI: **Manrope 500/600**
- Body/supporting UI: **Inter 400/500**
- Primary launch ecosystem: **Samsung SmartThings**
- Commerce/account authority: **GoDaddy Commerce Plus**
- Concierge: **LuxSync Intelligent Living Concierge**
- Personalized output: **My LuxSync Blueprint**
- Support email: `support@luxsync.net`
- Information/consultation email: `info@luxsync.net`

## First-Pass Airo Procedure

1. Sign in to GoDaddy and open Airo AI Builder.
2. Create a new project named `LuxSync First Pass - 2026-09-01` or another clearly non-production equivalent.
3. Do not import or inherit a prior generated LuxSync site.
4. Paste the complete current contents of `prompts/website/PR-001-LuxSync-Airo-Master-Website-Build-Prompt.md`.
5. Generate the first-pass site.
6. Do not connect production DNS.
7. Do not connect live payments.
8. Do not create an unmanaged duplicate live catalog.
9. Do not enter real customer credentials into a prototype.
10. Preserve the first generated result before making cosmetic edits.

## Required Route Set

The first pass should represent:

- `/`
- `/find-my-luxsync-solution`
- `/my-luxsync-blueprint`
- `/solutions`
- `/solutions/commercial-offices`
- `/solutions/senior-living`
- `/solutions/short-term-rentals`
- `/solutions/residential`
- `/solutions/aging-in-place`
- `/shop`
- `/guides`
- `/about`
- `/faqs`
- `/contact`
- preferred account/login experience beginning at `/account/login`, subject to actual Commerce Plus routing

The canonical FAQ route is `/faqs`.

## Flagship Experience Gate

`Find My LuxSync Solution` must be treated as a primary customer journey, not a quiz.

The first pass should visibly support:

- outcome-first discovery;
- reusable Property Profile;
- private residence, STR, business/commercial, and Other branching;
- approximate square footage or range;
- existing technology discovery;
- lifestyle/routine and pain-point discovery;
- prioritization;
- Essential Intelligence / Elevated Living / Complete LuxSync Experience paths;
- recommended LuxSync Experiences before exact products;
- My LuxSync Blueprint reveal;
- concise `Why LuxSync Chose This` explanations.

The rules under `website/src/concierge/` remain authoritative. Airo must not invent a replacement scoring model.

## Adaptive Contact Gate

The first choice must include:

- Support
- Product Information
- Consultation
- General Question
- Business / Partnership
- Other

Only relevant follow-up fields should appear. Relevant Contact paths reuse Property Profile concepts and may receive Blueprint context when technically and legally appropriate.

Support routes to `support@luxsync.net`. Product information, consultation, general questions, business/partnership, and Other general inquiries route to `info@luxsync.net`.

Marketing consent remains separate and optional.

## Commerce Gate

Use `content/product-catalog.md` for category and concept architecture. Do not fabricate exact products, prices, inventory, stock, shipping, warranties, ratings, subscriptions, or compatibility.

LuxSync Experiences are solution concepts unless validated live Commerce Plus entries exist.

Senior recurring-service pricing remains unpublished while DEC-005 is open.

## Capture After Generation

Record:

- Airo project name
- date/time generated
- prompt version / repository commit
- preview URL if one is created
- screenshots or export location
- routes created
- missing routes
- invented content found
- Concierge status
- Contact status
- product/catalog status
- brand deviations
- accessibility concerns
- mobile concerns
- account/login behavior
- export availability
- next corrective prompt

Use `docs/checklists/CL-001-Airo-First-Pass-Review.md` immediately after generation.

## Exit Criteria

This staging run is complete when the generated site has been reviewed against CL-001 and one of these outcomes is recorded:

- **Pass for source export / deeper integration**
- **Revise in Airo and review again**
- **Reject generation and restart from PR-001**

No result from this packet authorizes production publication.