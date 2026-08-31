# LuxSync Master Catalog

**Status:** Active  
**Repository:** `bbluxsync26/LuxSync_Git`  
**Default branch:** `master`  
**Last updated:** 2026-08-31

## Purpose

Repository index and source-of-truth map for approved LuxSync strategy, brand, website, content, prompts, architecture, decision records, runbooks, product planning, and validation artifacts.

Conversation drafts and external copies do not override intentionally committed repository decisions.

## Source-of-Truth Precedence

When artifacts disagree, use this order unless a more specific current decision explicitly says otherwise:

1. Current decisions and architecture documents
2. Current authoritative brand standards
3. Current website page blueprints and shared UX/data contracts
4. Current canonical customer-facing content and product/solution catalog
5. Current runbooks and validation rules
6. Current prompts
7. Business and financial planning documents
8. Historical/superseded generators and legacy graphics

For merchandising specifically, `content/product-catalog.md` governs current product-family, bundle-concept, and LuxSync Experience terminology; validated GoDaddy Commerce Plus data governs exact live products, prices, stock, availability, and commerce facts.

## Current Brand and Product Tie-Breakers

- **Authoritative visual system:** LuxSync v3
- **Enduring design DNA:** Plush Drift
- **Brand architecture:** `brand/brand-architecture.md`
- **Headings / navigation / buttons / graphic UI:** Manrope 500/600
- **Body / supporting UI:** Inter 400/500
- **Sole approved public slogan / hero line:** **Where Luxury Lives Intelligently**
- **Retired slogan/hero treatments:** must not be regenerated or restored
- **Voice:** Intelligent Calm
- **Primary homepage CTA:** Find My LuxSync Solution
- **Secondary homepage CTA:** Shop Smart Home
- **Supporting homepage CTA:** Get the ROI Guide
- **Flagship experience:** LuxSync Intelligent Living Concierge
- **Personalized output:** My LuxSync Blueprint
- **Concierge model:** Lifestyle → Experience → Intelligence → Technology
- **Product planning catalog:** `content/product-catalog.md`
- **Support email:** `support@luxsync.net`
- **Information / consultation email:** `info@luxsync.net`
- **Primary launch compatibility standard:** Samsung SmartThings
- **Production commerce system of record:** GoDaddy Commerce Plus
- **Protected logo artwork:** approved logo masters remain immutable artwork

Approved colors:

- Slate Navy `#0D1526`
- Dark Suede `#172036`
- Pale Driftwood `#D0BEB0`
- Warm Taupe Mauve `#9E8B85`
- Antique Rose Taupe `#967878`
- Dusty Steel `#7B96B2`
- Champagne Rose Gold Metallic `#D6B0A0` anchor

## Core Strategy and Content

| ID | Artifact | Path | Status |
|---|---|---|---|
| DOC-001 | Project Overview / Operating Baseline | `README.md` | Active |
| DOC-002 | Unified Business Plan | `docs/business-plan.md` | Active / planning |
| DOC-003 | Value Proposition | `docs/value-proposition.md` | Active / reconciled |
| DOC-004 | 3-Month Cookbook | `docs/3-month-cookbook.md` | Active roadmap |
| DOC-005 | Financial Model | `docs/financial-model.md` | Active planning baseline |
| DOC-006 | Launch Plan | `docs/launch-plan.md` | Active |
| DOC-007 | LuxSync Project Runbook | `docs/project-runbook.md` | Active |
| DOC-008 | Bridgette Beardsley Leadership Biography | `docs/leadership/bridgette-beardsley.md` | Active / Approved |
| DOC-009 | Sheldon Bardol Leadership Biography | `docs/leadership/sheldon-bardol.md` | Active / Approved |
| CONTENT-001 | About LuxSync Website Copy | `content/about.md` | Active / Approved |
| CONTENT-002 | LuxSync Frequently Asked Questions | `content/faqs.md` | Active / Approved |
| CONTENT-003 | Contact Page Content | `content/contact.md` | Active / Approved |
| CONTENT-004 | Product & Solution Catalog | `content/product-catalog.md` | Active / Canonical planning catalog |
| CONTENT-005 | Homepage Content | `content/homepage.md` | Active / Reconciled |

## Brand System

| ID | Artifact | Path | Status |
|---|---|---|---|
| BRAND-001 | Brand Guidelines | `brand/README.md` | Active — LuxSync v3 |
| BRAND-002 | Color System | `brand/colors.md` | Active |
| BRAND-003 | Typography | `brand/typography.md` | Active — Manrope + Inter |
| BRAND-004 | Voice & Tone | `brand/voice-and-tone.md` | Active — Intelligent Calm |
| BRAND-005 | Brand Architecture / Plush Drift DNA | `brand/brand-architecture.md` | Active / Authoritative |
| BRAND-006 | Approved Asset Library | `brand/assets/` and current approved asset metadata | Active as governed by brand docs |
| BRAND-007 | Prior/generated visual libraries | legacy/historical locations | Superseded unless explicitly retained |

## Architecture and Website

| ID | Artifact | Path | Status |
|---|---|---|---|
| ARC-001 | Launch Website Information Architecture | `docs/architecture/website-information-architecture.md` | Active / Approved |
| ARC-002 | Intelligent Living Concierge Architecture | `docs/architecture/intelligent-living-concierge.md` | Active / Flagship |
| DEC-004 | Commerce Plus and Airo Role | `docs/decisions/DEC-004-commerce-plus-and-airo-role.md` | Active |
| DEC-005 | Senior Service Pricing | `docs/decisions/DEC-005-senior-service-pricing.md` | Open / Decision Required |
| WEB-001 | Homepage Blueprint | `website/pages/home.md` | Active |
| WEB-002 | Website Design System | `website/styles/design-system.md` | Active |
| WEB-003 | Website Source Area | `website/src/README.md` | Active source area |
| WEB-004 | About Page Blueprint | `website/pages/about.md` | Active |
| WEB-005 | FAQ Page Blueprint | `website/pages/faqs.md` | Active |
| WEB-006 | Contact Page Blueprint | `website/pages/contact.md` | Active / Adaptive form |
| WEB-007 | Intelligent Living Concierge Engine | `website/src/concierge/` | Active / v1 engine |

### Shared Property Profile Contract

The Contact page and Concierge share the same conceptual Property Profile. Reuse stable Concierge field concepts wherever practical:

- `property_type`
- `square_feet_exact`
- `square_feet_band`
- residence / STR / business subtype
- levels, units, or locations where relevant
- technology profile
- customer goals

Blueprint-to-Contact journeys should prepopulate relevant context when technically and legally appropriate.

## Concierge Engine

The flagship engine under `website/src/concierge/` contains the maintainable source for:

- questionnaire stages and branching
- stable field IDs
- LuxSync Experience catalog
- weighted recommendation scoring
- compatibility/foundation flags
- implementation paths
- consultation triggers
- CTA logic
- My LuxSync Blueprint schema
- reference evaluator and examples

Do not replace these rules with independently invented survey logic in an AI-generated website.

## Product and Solution Catalog

`content/product-catalog.md` separates:

1. **Physical product families**
2. **Curated bundle concepts**
3. **LuxSync Experiences / solution concepts**

Approved planning families include Foundation & Connectivity, Entry & Access, Lighting & Ambience, Comfort & Climate, Property Awareness, Water Protection, Energy & Power, Entertainment, Cleaning & Convenience, Outdoor Living, Hosting/STR, and Curated Bundles.

Concierge-linked Experience concepts include Welcome Home, Effortless Departure, Goodnight, Gentle Morning, Intelligent Evening, Cinema, Entertain, Relax, Away, Protect, Water Watch, Climate Intelligence, Energy Intelligence, Night Path, Guest Ready, Turnover, Property Pulse, Accessible Living, and Vacation Mode.

An Experience is not automatically a live SKU. Exact live products and bundles require validated Commerce Plus/manufacturer data.

## Runbooks and Checklists

| ID | Artifact | Path | Status |
|---|---|---|---|
| RB-002 | GoDaddy Airo AI Builder | `docs/runbooks/RB-002-GoDaddy-Airo-AI-Builder.md` | Active |
| RB-004 | CI/CD | TBD | Planned |
| RB-005 | Production Deployment and Domain/DNS | TBD | Planned |
| RB-006 | Rollback | TBD | Planned |
| RB-007 | Brand Asset Raster Regeneration | `docs/runbooks/RB-007-Brand-Asset-Raster-Regeneration.md` | Historical / Superseded |
| RB-008 | Prior Luxury Orbit Asset Generation | `docs/runbooks/RB-008-Luxury-Orbit-Brand-Asset-Generation.md` | Historical / Superseded |
| RB-009 | Repository Consistency Validation | `docs/runbooks/RB-009-Repository-Consistency-Validation.md` | Active |
| CL-001 | Airo First-Pass Review | `docs/checklists/CL-001-Airo-First-Pass-Review.md` | Active |

## Prompt Catalog

| ID | Artifact | Path | Status | Use |
|---|---|---|---|---|
| PR-001 | LuxSync Airo Master Website Build Prompt | `prompts/website/PR-001-LuxSync-Airo-Master-Website-Build-Prompt.md` | Active / Reconciled | Airo staging build |
| PR-002 | Website Design Review Prompt | TBD | Planned | Brand/UX review |
| PR-003 | Deployment Validation Prompt | TBD | Planned | Pre-production validation |
| PR-CONTENT-001 | LuxSync Content Writer | `prompts/content-writer.md` | Active / Reconciled | General approved copy |
| PR-PRODUCT-001 | LuxSync Product Description | `prompts/product-descriptions.md` | Active / Reconciled | Product/bundle/Experience copy |
| PR-EMAIL-001 | LuxSync Email Writer | `prompts/email-writer.md` | Active / Reconciled | Customer/marketing email copy |

All active prompts must inherit current company facts, exact founder titles, the sole approved slogan, Concierge/Blueprint naming, product-catalog guardrails, and Contact routing.

## Launch Website Direction

- Commerce-first premium intelligent-living storefront
- Guided discovery is a flagship journey, not a secondary quiz
- GoDaddy Commerce Plus remains production commerce authority
- Samsung SmartThings remains the primary launch compatibility standard
- Mobile-first, accessible, performant experience
- LuxSync v3 visual system with Plush Drift design DNA
- Manrope + Inter typography
- Intelligent Calm voice
- Approved logo artwork referenced directly, never regenerated

Primary launch navigation:

```text
Home | Shop | Solutions | Guides | About | Contact | Support
```

Commerce utilities:

```text
Search | Account | Cart
```

## Contact Routing

- Existing product/order/setup/troubleshooting support → `support@luxsync.net`
- Product information → `info@luxsync.net`
- Consultation → `info@luxsync.net`
- General question → `info@luxsync.net`
- Business / partnership → `info@luxsync.net`
- Other general contact → `info@luxsync.net`

Marketing consent is separate and optional.

## Publication Guardrails

Do not publish or invent:

- unvalidated prices, stock, shipping promises, availability, or compatibility
- unresolved senior-service pricing
- supplier terms, internal margins, or financial projections
- third-party endorsements
- awards, testimonials, press, customer counts, or founder facts not in approved sources
- medical claims
- claims that convenience/security-related smart-home products replace life-safety systems, emergency services, or professional monitoring
- unreleased SmartThings automation templates, LuxSync Grid, saved Blueprint functionality, or roadmap services as live

## Maintenance Rules

1. Add a catalog entry when a reusable prompt, runbook, architecture document, checklist, decision, content baseline, or shared product/UX contract becomes durable.
2. Mark work-in-progress artifacts Draft.
3. Preserve superseded material only where traceability matters, and mark it historical.
4. Never store passwords, API keys, payment credentials, private tokens, or other secrets.
5. Repository paths in this catalog must correspond to committed files.
6. Never recreate protected logo artwork.
7. New public slogan/hero language requires an explicit repository decision and cross-repository reconciliation.
8. Stable Concierge field and Experience IDs should not be changed casually after production launch.
9. Product-catalog changes should be mapped to relevant LuxSync Experiences and validated commerce data before public sale claims.
10. Run repository consistency validation after major cross-cutting changes.

## Change Log

| Date | Change |
|---|---|
| 2026-08-29 | Repository master catalog established. |
| 2026-08-30 | Reconciled website/Airo architecture and operating baseline. |
| 2026-08-31 | Added approved seven-color palette, Manrope/Inter contract, founder biographies, FAQs, and LuxSync v3 / Plush Drift governance. |
| 2026-08-31 | Added the Intelligent Living Concierge engine and My LuxSync Blueprint architecture as flagship product artifacts. |
| 2026-08-31 | Added the dedicated adaptive Contact page and shared Property Profile contract. |
| 2026-08-31 | Added the canonical Product & Solution Catalog with Concierge-linked Experience concepts. |
| 2026-08-31 | Reconciled all active reusable prompts around current founder facts, company facts, Contact routing, Concierge/Blueprint terminology, and commerce guardrails. |
| 2026-08-31 | Established **Where Luxury Lives Intelligently** as the sole approved public slogan/hero line and retired alternate slogan/hero treatments. |
