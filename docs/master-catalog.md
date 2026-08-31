# LuxSync Master Catalog

**Status:** Active  
**Repository:** `bbluxsync26/LuxSync_Git`  
**Default branch:** `master`  
**Last updated:** 2026-08-31

## Purpose

Repository index for approved LuxSync strategy, brand, website, prompt, architecture, decision, runbook, checklist, and validation artifacts.

The repository is the LuxSync source of truth. Conversation drafts or external copies do not override intentionally committed repository decisions.

## Source-of-Truth Precedence

1. Current explicit architecture/decision/runbook documents
2. Current authoritative brand standards
3. Current business and operating plans
4. Current website/content documents
5. Current prompts
6. Generated asset metadata and exports
7. Historical bootstrap scripts or superseded files

## Current Brand Tie-Breaker

When current LuxSync files disagree, apply these rules:

- **Base brand system:** Plush Drift v2.1
- **Active web/graphics treatment:** Luxury Orbit
- **Headings / display / navigation / graphic UI:** Manrope 500/600
- **Body / supporting UI:** Inter 400/500
- **Official slogan:** Where Luxury Lives Intelligently
- **Homepage hero:** Smart Living. Elevated.
- **Primary CTA:** Shop Smart Home
- **Secondary CTA:** Get the ROI Guide
- **Protected exact logo artwork:** the approved primary monogram and horizontal lockup remain exact artwork and are not re-typeset merely to enforce live-text typography
- **Approved metallic color:** Champagne Rose Gold Metallic uses the `#D6B0A0` anchor and approved light-to-dark metallic gradient

Luxury Orbit uses the approved Champagne Rose Gold Metallic treatment and may add restrained Dusty Steel-derived orbit light without replacing the Plush Drift palette or Manrope/Inter typography.

## Core Strategy Documents

| ID | Artifact | Path | Status |
|---|---|---|---|
| DOC-001 | Project Overview / Operating Baseline | `README.md` | Active |
| DOC-002 | Unified Business Plan v2.1 | `docs/business-plan.md` | Active / Reconciled |
| DOC-003 | Value Proposition v2.1 | `docs/value-proposition.md` | Active / Reconciled |
| DOC-004 | 3-Month Cookbook v2.0 | `docs/3-month-cookbook.md` | Active roadmap |
| DOC-005 | Financial Model | `docs/financial-model.md` | Active planning baseline |
| DOC-006 | Launch Plan | `docs/launch-plan.md` | Active |
| DOC-007 | LuxSync Project Runbook | `docs/project-runbook.md` | Active |

## Brand System

| ID | Artifact | Path | Status |
|---|---|---|---|
| BRAND-001 | Brand Guidelines | `brand/README.md` | Active — Plush Drift v2.1 + Luxury Orbit |
| BRAND-002 | Color System | `brand/colors.md` | Active — Plush Drift v2.1 base palette |
| BRAND-003 | Typography | `brand/typography.md` | Active — Manrope + Inter |
| BRAND-004 | Voice & Tone | `brand/voice-and-tone.md` | Active — Intelligent Calm |
| BRAND-005 | Asset Library | `brand/assets/` | Active — 104 logical assets |
| BRAND-006 | Vector Asset CSV | `brand/assets/asset-manifest.csv` | Active — 98 SVG-based graphics |
| BRAND-007 | Asset JSON Summary | `brand/assets/asset-manifest.json` | Active |
| BRAND-008 | Production Scene Manifest | `brand/assets/12-scenes/scene-manifest.csv` | Active — 6 text-free scenes |

## Architecture and Decisions

| ID | Artifact | Path | Status |
|---|---|---|---|
| ARC-001 | Launch Website Information Architecture | `docs/architecture/website-information-architecture.md` | Active / Approved baseline |
| DEC-004 | Commerce Plus and Airo Role | `docs/decisions/DEC-004-commerce-plus-and-airo-role.md` | Active |
| DEC-005 | Senior Service Pricing | `docs/decisions/DEC-005-senior-service-pricing.md` | Open / Decision Required |
| WEB-001 | Homepage Blueprint | `website/pages/home.md` | Active launch baseline |
| WEB-002 | Website Design System | `website/styles/design-system.md` | Active — Plush Drift + Luxury Orbit |
| WEB-003 | Website Source Area | `website/src/README.md` | Placeholder until first reviewed export |

## Runbooks

| ID | Artifact | Path | Status |
|---|---|---|---|
| RB-002 | GoDaddy Airo AI Builder | `docs/runbooks/RB-002-GoDaddy-Airo-AI-Builder.md` | Active |
| RB-004 | CI/CD | TBD | Planned |
| RB-005 | Production Deployment and Domain/DNS | TBD | Planned |
| RB-006 | Rollback | TBD | Planned |
| RB-007 | Brand Asset Raster Regeneration | `docs/runbooks/RB-007-Brand-Asset-Raster-Regeneration.md` | Superseded / Historical |
| RB-008 | Luxury Orbit Brand Asset Generation | `docs/runbooks/RB-008-Luxury-Orbit-Brand-Asset-Generation.md` | Active |
| RB-009 | Repository Consistency Validation | `docs/runbooks/RB-009-Repository-Consistency-Validation.md` | Active |

## Checklists

| ID | Artifact | Path | Status |
|---|---|---|---|
| CL-001 | Airo First-Pass Review | `docs/checklists/CL-001-Airo-First-Pass-Review.md` | Active / Reconciled |

## Prompt Catalog

| ID | Artifact | Path | Status | Use |
|---|---|---|---|---|
| PR-001 | LuxSync Airo Master Website Build Prompt | `prompts/website/PR-001-LuxSync-Airo-Master-Website-Build-Prompt.md` | Draft / Ready after consistency gate | Initial Airo staging build |
| PR-002 | Website Design Review Prompt | TBD | Planned | Brand/UX review |
| PR-003 | Deployment Validation Prompt | TBD | Planned | Pre-production validation |
| PR-CONTENT-001 | Content Writer | `prompts/content-writer.md` | Active | General LuxSync copy |
| PR-PRODUCT-001 | Product Description | `prompts/product-descriptions.md` | Active | Product copy |
| PR-EMAIL-001 | Email Writer | `prompts/email-writer.md` | Active | Marketing email copy |

## Automation and Validation

| Artifact | Path | Purpose |
|---|---|---|
| Brand Generator | `scripts/generate-luxury-orbit-assets.py` | Generate editable SVG-based graphics |
| Brand Normalizer | `scripts/normalize-luxury-orbit-fonts.py` | Enforce Manrope/Inter, base palette, and safe generated copy |
| Brand Renderer | `scripts/render-luxury-orbit-assets.py` | Render PNG/WebP derivatives and contact sheets while preserving approved logos |
| Asset Metadata Reconciler | `scripts/reconcile-asset-metadata.py` | Synchronize CSV/JSON/inventory/catalog metadata to committed assets |
| Repository Validator | `scripts/validate-repository-consistency.py` | Validate cross-repository source-of-truth consistency |
| Brand Generation Workflow | `.github/workflows/regenerate-brand-raster-assets.yml` | Generate/normalize/render/validate brand assets |
| Consistency Workflow | `.github/workflows/validate-repository-consistency.yml` | Gate pull requests and master on repository consistency |

## Launch Website Direction

- Commerce-first luxury smart-home storefront
- GoDaddy Commerce Plus remains production commerce system of record
- Airo AI Builder is used for staging/reference generation and code/design exploration
- Samsung SmartThings is the primary launch compatibility standard
- Mobile-first, accessible, performant experience
- Plush Drift v2.1 base brand system
- Luxury Orbit web/graphics treatment
- Manrope + Inter typography
- Intelligent Calm voice

Primary launch navigation:

```text
Home | Shop | Solutions | Guides | About | Support
```

Commerce utilities:

```text
Search | Account | Cart
```

## Open Decisions / Validation Items

1. **DEC-005:** Select and approve one senior-service pricing model before public display.
2. Validate live Commerce Plus product catalog and product data before publishing prices or availability.
3. Run the repository consistency gate and confirm canonical asset metadata is clean.
4. Run the first PR-001 generation in Airo AI Builder.
5. Review Airo output using CL-001 against ARC-001 and the authoritative brand contract.
6. Determine exported source structure after inspecting actual Airo output.
7. Define CI/CD, staging, production deployment/domain-DNS, and rollback runbooks.

## Maintenance Rules

1. Add an entry when a reusable prompt, runbook, architecture document, checklist, decision, or validation procedure becomes durable.
2. Mark work-in-progress artifacts `Draft`.
3. Mark the exact prompt/version used in production `Final / Used`.
4. Preserve superseded material where traceability matters.
5. Do not store passwords, API keys, payment credentials, private tokens, or other secrets in the repository.
6. Review this catalog after material architecture, brand, business-model, or production-deployment changes.
7. Repository paths in this catalog must correspond to actual committed files.
8. When an intentional decision changes a validator-enforced rule, update the governing document and validator in the same change set.

## Change Log

| Date | Change |
|---|---|
| 2026-08-29 | Repository master catalog established. |
| 2026-08-30 | Added DOC-007 and website/Airo architecture artifacts. |
| 2026-08-30 | Reconciled Plush Drift v2.1, Luxury Orbit, Manrope/Inter, asset counts, business-plan math, and repository consistency automation. |
| 2026-08-30 | Added DEC-005 to preserve unresolved senior-service pricing as an explicit publication guardrail. |
| 2026-08-31 | Added Champagne Rose Gold Metallic as the seventh approved color and reconciled palette inventory counts. |
