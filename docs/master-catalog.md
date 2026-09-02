# LuxSync Master Catalog

**Status:** Active  
**Repository:** `bbluxsync26/LuxSync_Git`  
**Default branch:** `master`  
**Last updated:** 2026-09-02

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

- **Authoritative visual system:** LuxSync Production Raster v5
- **Enduring design DNA:** Plush Drift
- **Brand architecture:** `brand/brand-architecture.md`
- **Omnichannel brand governance:** `brand/README.md` + `brand/manifests/omnichannel-brand-manifest.json`
- **Permanent visual approval archive:** `brand/reference-boards/`
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
- **Approved logo paths:** `brand/assets/logos/png/luxsync-horizontal-combo.png`, `brand/assets/logos/png/luxsync-horizontal.png`, `brand/assets/logos/png/luxsync-orb.png`
- **Account experience principle:** every customer receives the same high-care, VIP-level welcome and service experience

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
| DOC-004 | Conditional 3-Month Operating Roadmap | `docs/3-month-cookbook.md` | Active / gated roadmap |
| DOC-005 | Financial Model | `docs/financial-model.md` | Active planning baseline |
| DOC-006 | Six-Day Launch Plan | `docs/launch-plan.md` | Active / gated production checklist |
| DOC-007 | LuxSync Project Runbook | `docs/project-runbook.md` | Active |
| DOC-008 | Bridgette Beardsley — Co-Founder & Chief Technology and Strategy Officer | `docs/leadership/bridgette-beardsley.md` | Active / Approved |
| DOC-009 | Sheldon Bardol — Co-Founder & Chief Customer and Operations Officer | `docs/leadership/sheldon-bardol.md` | Active / Approved |
| CONTENT-001 | About LuxSync Website Copy | `content/about.md` | Active / Approved |
| CONTENT-002 | LuxSync Frequently Asked Questions | `content/faqs.md` | Active / Approved |
| CONTENT-003 | Contact Page Content | `content/contact.md` | Active / Approved |
| CONTENT-004 | Product & Solution Catalog | `content/product-catalog.md` | Active / Canonical planning catalog |
| CONTENT-005 | Homepage Content | `content/homepage.md` | Active / Reconciled |
| CONTENT-006 | ROI Guide Library Index and Methodology | `content/guides/roi/README.md` | Active / Customer education |

## ROI Guide Library

| ID | Audience | Path | Status |
|---|---|---|---|
| GUIDE-ROI-001 | Commercial Offices | `content/guides/roi/commercial-offices.md` | Active |
| GUIDE-ROI-002 | Nursing Homes | `content/guides/roi/nursing-homes.md` | Active / Non-clinical guardrails |
| GUIDE-ROI-003 | Senior Living Communities | `content/guides/roi/senior-living-communities.md` | Active / Non-clinical guardrails |
| GUIDE-ROI-004 | STR Owners | `content/guides/roi/str-owners.md` | Active |
| GUIDE-ROI-005 | STR Operators | `content/guides/roi/str-operators.md` | Active |
| GUIDE-ROI-006 | STR Managers | `content/guides/roi/str-managers.md` | Active |
| GUIDE-ROI-007 | Residential Homeowners | `content/guides/roi/residential-homeowners.md` | Active |
| GUIDE-ROI-008 | Busy Professionals | `content/guides/roi/residential-busy-professionals.md` | Active |
| GUIDE-ROI-009 | Intentional Parents and Families | `content/guides/roi/residential-intentional-parents.md` | Active |
| GUIDE-ROI-010 | Seniors, Caregivers, and Aging in Place | `content/guides/roi/residential-seniors-caregivers.md` | Active / Non-medical guardrails |

## Brand System

| ID | Artifact | Path | Status |
|---|---|---|---|
| BRAND-001 | Brand Guidelines / Omnichannel Brand Contract | `brand/README.md` | Active — LuxSync Production Raster v5 / Omnichannel |
| BRAND-002 | Color System | `brand/colors.md` | Active |
| BRAND-003 | Typography | `brand/typography.md` | Active — Manrope + Inter |
| BRAND-004 | Voice & Tone | `brand/voice-and-tone.md` | Active — Intelligent Calm |
| BRAND-005 | Brand Architecture / Plush Drift DNA | `brand/brand-architecture.md` | Active / Authoritative |
| BRAND-006 | Clean Atomic Digital Delivery Library | `brand/assets/` and `brand/assets/asset-manifest.json` | Active / 31 approved atomic assets / 93 files |
| BRAND-007 | Prior/generated visual libraries | legacy/historical locations | Superseded unless explicitly retained |
| BRAND-008 | VIP Account Access Vector Mini-Library | `website/assets/auth/` | Active / Mixed publication status per manifest |
| BRAND-009 | VIP Account Access Asset Manifest | `website/assets/auth/manifest.json` | Active / Authoritative for auth vectors |
| BRAND-010 | Omnichannel Brand Manifest | `brand/manifests/omnichannel-brand-manifest.json` | Active / Phase 0 state and asset dispositions |
| BRAND-011 | Omnichannel Brand Build State | `brand/audit/brand-build-state.json` | Active / Restart checkpoint |
| BRAND-012 | Omnichannel Brand Audit Report | `brand/audit/brand-build-report.md` | Active / Internal audit |
| BRAND-013 | Omnichannel Brand Exceptions | `brand/audit/brand-exceptions.md` | Active / Exception log |
| BRAND-014 | Visual Approval Archive | `brand/reference-boards/` | Active / Permanent approval evidence |

### Omnichannel brand rule

LuxSync branding is not limited to the website. The validated `brand/assets/` tree is the current clean digital delivery layer; the complete brand system may also produce technically appropriate masters and exports for print, video-ready static graphics, stationery, merchandise, apparel, embroidery, signage, packaging, email, social and marketing.

The approval boards under `brand/reference-boards/` are durable visual evidence. Retiring malformed grid-sliced files does not revoke the approved concepts represented on those boards.

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
| WEB-008 | ROI Guides Library Page Blueprint | `website/pages/guides.md` | Active |
| WEB-009 | VIP Account Access / Login Production Specification | `website/pages/account-login.md` | Active / Production-ready visual baseline; auth integration pending |
| WEB-010 | VIP Account Access Implementation Manifest | `website/account-access-manifest.json` | Active |
| WEB-011 | VIP Account Access Interaction Tokens | `website/styles/account-access-tokens.css` | Active / Implementation reference |

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

## Account Experience

LuxSync account access is a high-care customer experience, not a generic utility form.

Governing artifacts:

- `website/pages/account-login.md`
- `website/account-access-manifest.json`
- `website/styles/account-access-tokens.css`
- `website/assets/auth/manifest.json`
- `docs/checklists/CL-002-Account-Access-Review.md`

Key principles:

- every ordinary customer receives the same VIP-level welcome and service treatment;
- use only the three approved immutable logo masters under `brand/assets/logos/png/`;
- use Plush Drift tactile illumination for login card, fields, and primary CTA;
- keep authentication calm, private, and friction-light;
- Dusty Steel is the preferred cool concealed underlight;
- Champagne Rose Gold is restrained premium reflected detail;
- production ambient auth graphics remain text-free and live authentication content is semantic HTML/CSS;
- do not invent identity providers, social login, MFA, passkeys, session policy, or account capabilities that the production platform does not support;
- GoDaddy Commerce Plus remains the current production commerce/account authority unless a later architecture decision changes it;
- preferred UX route family begins at `/account/login`, but final production routing must follow the supported account integration.

## Runbooks and Checklists

| ID | Artifact | Path | Status |
|---|---|---|---|
| RB-002 | GoDaddy Airo AI Builder | `docs/runbooks/RB-002-GoDaddy-Airo-AI-Builder.md` | Active |
| RB-004 | CI/CD | TBD | Planned |
| RB-005 | Production Deployment and Domain/DNS | TBD | Planned |
| RB-006 | Rollback | TBD | Planned |
| RB-009 | Repository Consistency Validation | `docs/runbooks/RB-009-Repository-Consistency-Validation.md` | Active |
| CL-001 | Airo First-Pass Review | `docs/checklists/CL-001-Airo-First-Pass-Review.md` | Active |
| CL-002 | VIP Account Access Review | `docs/checklists/CL-002-Account-Access-Review.md` | Active |

## Prompt Catalog

| ID | Artifact | Path | Status | Use |
|---|---|---|---|---|
| PR-001 | LuxSync Airo Master Website Build Prompt | `prompts/website/PR-001-LuxSync-Airo-Master-Website-Build-Prompt.md` | Active / Reconciled | Airo staging build |
| PR-002 | Website Design Review Prompt | TBD | Planned | Brand/UX review |
| PR-003 | Deployment Validation Prompt | TBD | Planned | Pre-production validation |
| PR-BRAND-001 | LuxSync Omnichannel Brand System Recovery, Build & Audit Prompt | `prompts/branding/PR-BRAND-001-LuxSync-Omnichannel-Brand-System-Recovery-Audit.md` | Active / Promptless / Restart-Safe / Self-Healing | Omnichannel brand build, recovery and internal audit |
| PR-CONTENT-001 | LuxSync Content Writer | `prompts/content-writer.md` | Active / Reconciled | General approved copy |
| PR-PRODUCT-001 | LuxSync Product Description | `prompts/product-descriptions.md` | Active / Reconciled | Product/bundle/Experience copy |
| PR-EMAIL-001 | LuxSync Email Writer | `prompts/email-writer.md` | Active / Reconciled | Customer/marketing email copy |

All active prompts must inherit current company facts, exact founder titles, the sole approved slogan, Concierge/Blueprint naming, product-catalog guardrails, Contact routing, and the VIP account-access experience when account pages are generated.

## Launch Website Direction

- Commerce-first premium intelligent-living storefront
- Guided discovery is a flagship journey, not a secondary quiz
- GoDaddy Commerce Plus remains production commerce authority
- Samsung SmartThings remains the primary launch compatibility standard
- Mobile-first, accessible, performant experience
- LuxSync Production Raster v5 visual system with Plush Drift design DNA
- Manrope + Inter typography
- Intelligent Calm voice
- Approved logo artwork referenced directly, never regenerated
- Website graphics consume validated omnichannel brand assets; the website does not redefine the brand masters
- Account/login experience should feel like private, premium service while remaining simple and accessible

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
- unsupported authentication providers, social logins, verification methods, passkeys, session behaviors, or account features
- real customer credentials or authentication secrets in static prototypes or repository content

## Maintenance Rules

1. Add a catalog entry when a reusable prompt, runbook, architecture document, checklist, decision, content baseline, shared product/UX contract, or durable brand audit/governance artifact becomes durable.
2. Mark work-in-progress artifacts Draft.
3. Preserve superseded material only where traceability matters, and mark it historical.
4. Never store passwords, API keys, payment credentials, private tokens, or other secrets.
5. Repository paths in this catalog must correspond to committed files.
6. Never recreate protected logo artwork.
7. New public slogan/hero language requires an explicit repository decision and cross-repository reconciliation.
8. Stable Concierge field and Experience IDs should not be changed casually after production launch.
9. Product-catalog changes should be mapped to relevant LuxSync Experiences and validated commerce data before public sale claims.
10. Run repository consistency validation after major cross-cutting changes.
11. ROI examples must use customer inputs or clearly labeled scenarios; never publish promised returns, invented benchmarks, or unvalidated savings percentages.
12. Account/authentication UX must remain subordinate to the capabilities and security requirements of the selected production account platform.
13. Auth asset publication status is governed by `website/assets/auth/manifest.json`; reference diagrams are never functional UI.
14. Preserve `brand/reference-boards/` as permanent visual approval evidence; never treat a production-library cleanup as revocation of approved brand concepts.
15. Run PR-BRAND-001 idempotently for omnichannel brand recovery/build work: audit first, skip validated completed work, self-heal deterministic drift, and never creatively overwrite approved masters.

## Change Log

| Date | Change |
|---|---|
| 2026-08-29 | Repository master catalog established. |
| 2026-08-30 | Reconciled website/Airo architecture and operating baseline. |
| 2026-08-31 | Added approved seven-color palette, Manrope/Inter contract, founder biographies, FAQs, and LuxSync Production Raster v5 / Plush Drift governance. |
| 2026-08-31 | Added the Intelligent Living Concierge engine and My LuxSync Blueprint architecture as flagship product artifacts. |
| 2026-08-31 | Added the dedicated adaptive Contact page and shared Property Profile contract. |
| 2026-08-31 | Added the canonical Product & Solution Catalog with Concierge-linked Experience concepts. |
| 2026-08-31 | Reconciled all active reusable prompts around current founder facts, company facts, Contact routing, Concierge/Blueprint terminology, and commerce guardrails. |
| 2026-08-31 | Established **Where Luxury Lives Intelligently** as the sole approved public slogan/hero line and retired alternate slogan/hero treatments. |
| 2026-08-31 | Added ten audience-specific ROI Guides, a shared measurement standard, and the ROI Guides website library blueprint. |
| 2026-09-01 | Added the VIP Account Access / Login blueprint and made VIP-level welcome/service an account-experience requirement. |
| 2026-09-01 | Reconciled the three-month roadmap and six-day launch plan, connected production output to governed content sources, completed adaptive Contact property branching, and strengthened repository/site regression checks. |
| 2026-09-01 | Promoted VIP Account Access to a production-ready visual/interaction package with exact approved-logo mapping, dedicated ambient vectors, interaction tokens, implementation manifest, and CL-002 review gate. |
| 2026-09-02 | Added PR-BRAND-001 and established restart-safe, promptless, self-healing omnichannel brand governance. |
| 2026-09-02 | Added the omnichannel brand manifest, restart state, audit report and exception log; preserved the seven reference boards as permanent approval evidence and clarified `brand/assets/` as the validated digital delivery layer rather than the full brand scope. |

## Production Completion Baseline

**Authoritative visual system:** LuxSync Production Raster v5  
**Official slogan:** Where Luxury Lives Intelligently

Canonical website implementation references:

- `docs/production-source-of-truth.md`
- `website/implementation-manifest.json`
- `website/account-access-manifest.json`
- `website/asset-map.md`
- `website/navigation.md`
- `website/pages/`
- `website/styles/account-access-tokens.css`
- `website/assets/auth/manifest.json`
- `website/src/concierge/luxsync-concierge-engine.v1.json`

Canonical omnichannel brand references:

- `brand/README.md`
- `brand/reference-boards/`
- `brand/manifests/omnichannel-brand-manifest.json`
- `brand/audit/brand-build-state.json`
- `brand/audit/brand-build-report.md`
- `brand/audit/brand-exceptions.md`
- `prompts/branding/PR-BRAND-001-LuxSync-Omnichannel-Brand-System-Recovery-Audit.md`

The old malformed grid-sliced production assets remain retired. Auth vectors may be published only when their current website asset manifest explicitly marks them `production-approved`. The wider approved brand remains governed by the visual approval archive and omnichannel manifest, not by whether an asset is currently used on the website.
