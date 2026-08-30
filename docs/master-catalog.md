# LuxSync Master Catalog

**Status:** Active  
**Repository:** `bbluxsync26/LuxSync_Git`  
**Default branch:** `master`  
**Last updated:** 2026-08-30

## Purpose

Repository index for approved LuxSync strategy, brand, website, prompt, architecture, decision, runbook, and checklist artifacts.

The repository is the LuxSync source of truth. Conversation drafts or external copies do not override intentionally committed repository decisions.

## Source-of-Truth Precedence

1. Current explicit architecture/decision/runbook documents
2. Current brand standards
3. Current business and operating plans
4. Current website/content documents
5. Current prompts
6. Generated asset metadata and legacy exports
7. Historical bootstrap scripts or superseded files

Current visual-system tie-breaker:

- Brand/editorial wordmark: **Bodoni Moda / Bodoni MT / Didot / Georgia**
- Headings and graphic UI: **Century Gothic / Montserrat**
- Body and supporting UI: **Candara / Inter / Segoe UI**
- Active web visual system: **Luxury Orbit**

Official slogan:

**Where Luxury Lives Intelligently**

## Core Strategy Documents

| ID | Artifact | Path | Status |
|---|---|---|---|
| DOC-001 | Project Overview / Operating Baseline | `README.md` | Active |
| DOC-002 | Unified Business Plan v2.0 | `docs/business-plan.md` | Active |
| DOC-003 | Value Proposition v2.0 | `docs/value-proposition.md` | Active |
| DOC-004 | 3-Month Cookbook v2.0 | `docs/3-month-cookbook.md` | Active |
| DOC-005 | Financial Model | `docs/financial-model.md` | Active |
| DOC-006 | Launch Plan | `docs/launch-plan.md` | Active |
| DOC-007 | LuxSync Project Runbook | `docs/project-runbook.md` | Active |

## Brand System

| ID | Artifact | Path | Status |
|---|---|---|---|
| BRAND-001 | Brand Guidelines | `brand/README.md` | Active — Luxury Orbit |
| BRAND-002 | Color System | `brand/colors.md` | Active — Luxury Orbit |
| BRAND-003 | Typography | `brand/typography.md` | Active — Luxury Orbit |
| BRAND-004 | Voice & Tone | `brand/voice-and-tone.md` | Active |
| BRAND-005 | Asset Library | `brand/assets/` | Active — 97 generated SVG masters |
| BRAND-006 | Canonical Asset CSV | `brand/assets/asset-manifest.csv` | Active |
| BRAND-007 | Asset JSON Summary | `brand/assets/asset-manifest.json` | Active |

## Website Architecture and Decisions

| ID | Artifact | Path | Status |
|---|---|---|---|
| ARC-001 | Launch Website Information Architecture | `docs/architecture/website-information-architecture.md` | Active / Approved baseline |
| DEC-004 | Commerce Plus and Airo Role | `docs/decisions/DEC-004-commerce-plus-and-airo-role.md` | Active |
| WEB-001 | Homepage Blueprint | `website/pages/home.md` | Active launch baseline |
| WEB-002 | Website Design System | `website/styles/design-system.md` | Active — Luxury Orbit |
| WEB-003 | Website Source Objectives | `website/src/README.md` | Active |

## Runbooks

| ID | Artifact | Path | Status |
|---|---|---|---|
| RB-002 | GoDaddy Airo AI Builder | `docs/runbooks/RB-002-GoDaddy-Airo-AI-Builder.md` | Active |
| RB-004 | CI/CD | TBD | Planned |
| RB-005 | Production Deployment and Domain/DNS | TBD | Planned |
| RB-006 | Rollback | TBD | Planned |
| RB-007 | Brand Asset Raster Regeneration | `docs/runbooks/RB-007-Brand-Asset-Raster-Regeneration.md` | Superseded by RB-008 for current graphics |
| RB-008 | Luxury Orbit Brand Asset Generation | `docs/runbooks/RB-008-Luxury-Orbit-Brand-Asset-Generation.md` | Active |

## Checklists

| ID | Artifact | Path | Status |
|---|---|---|---|
| CL-001 | Airo First-Pass Review | `docs/checklists/CL-001-Airo-First-Pass-Review.md` | Active — Luxury Orbit reconciled |

## Prompt Catalog

| ID | Artifact | Path | Status | Use |
|---|---|---|---|---|
| PR-001 | LuxSync Airo Master Website Build Prompt | `prompts/website/PR-001-LuxSync-Airo-Master-Website-Build-Prompt.md` | Draft / Ready for first Airo generation | Initial Airo staging build |
| PR-002 | Website Design Review Prompt | TBD | Planned | Brand/UX review |
| PR-003 | Deployment Validation Prompt | TBD | Planned | Pre-production validation |
| PR-CONTENT-001 | Content Writer | `prompts/content-writer.md` | Active | General LuxSync copy |
| PR-PRODUCT-001 | Product Description | `prompts/product-descriptions.md` | Active | Product copy |
| PR-EMAIL-001 | Email Writer | `prompts/email-writer.md` | Active | Marketing email copy |

## Launch Website Direction

- Commerce-first luxury smart-home storefront
- GoDaddy Commerce Plus remains production commerce system of record
- Airo AI Builder is used for staging/reference generation and code/design exploration
- Samsung SmartThings is the primary launch compatibility standard
- Mobile-first, accessible, performant experience
- **Luxury Orbit** visual system
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

1. Run the first PR-001 generation in Airo AI Builder.
2. Review Airo output using CL-001 against ARC-001 and the active Luxury Orbit standards.
3. Validate live Commerce Plus product catalog and product data before publishing prices or availability.
4. Resolve conflicting senior-service pricing before public display.
5. Determine exported source structure after inspecting actual Airo output.
6. Define CI/CD, staging, production deployment/domain-DNS, and rollback runbooks.

## Maintenance Rules

1. Add an entry when a reusable prompt, runbook, architecture document, checklist, or decision becomes durable.
2. Mark work-in-progress artifacts `Draft`.
3. Mark the exact prompt/version used in production `Final / Used`.
4. Preserve superseded material where traceability matters.
5. Do not store passwords, API keys, payment credentials, or other secrets in the repository.
6. Review this catalog after material architecture changes and production deployments.
7. Repository paths in this catalog must correspond to actual committed files.

## Change Log

| Date | Change |
|---|---|
| 2026-08-29 | Repository master catalog established. |
| 2026-08-30 | Added DOC-007 and reconciled PR-001, ARC-001, RB-002, and CL-001 to Luxury Orbit. |
