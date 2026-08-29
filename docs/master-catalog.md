# LuxSync Master Catalog

**Status:** Active  
**Repository:** `bbluxsync26/LuxSync_Git`  
**Default branch:** `master`  
**Last updated:** 2026-08-29

## Purpose

This file is the repository index for approved LuxSync strategy, brand, website, prompt, architecture, decision, runbook, and checklist artifacts.

The repository is the LuxSync source of truth. Conversation drafts or external copies do not override the current repository unless they are intentionally reconciled and committed.

---

## Source-of-Truth Precedence

When repository materials conflict, use this order unless a later explicit decision says otherwise:

1. Current explicit architecture/decision/runbook documents
2. Current brand standards
3. Current business and operating plans
4. Current website/content documents
5. Current prompts
6. Generated asset metadata and legacy exports
7. Historical bootstrap scripts or superseded files

Typography tie-breaker:

- Headings / display: **Manrope**
- Body / UI: **Inter**

Official slogan:

**Where Luxury Lives Intelligently**

---

## Core Strategy Documents

| ID | Artifact | Path | Status |
|---|---|---|---|
| DOC-001 | Project Overview / Operating Baseline | `README.md` | Active |
| DOC-002 | Unified Business Plan v2.0 | `docs/business-plan.md` | Active |
| DOC-003 | Value Proposition v2.0 | `docs/value-proposition.md` | Active |
| DOC-004 | 3-Month Cookbook v2.0 | `docs/3-month-cookbook.md` | Active |
| DOC-005 | Financial Model | `docs/financial-model.md` | Active |
| DOC-006 | Launch Plan | `docs/launch-plan.md` | Active |

---

## Brand System

| ID | Artifact | Path | Status |
|---|---|---|---|
| BRAND-001 | Brand Guidelines | `brand/README.md` | Active |
| BRAND-002 | Plush Drift v2.1 Colors | `brand/colors.md` | Active |
| BRAND-003 | Typography | `brand/typography.md` | Active |
| BRAND-004 | Voice & Tone | `brand/voice-and-tone.md` | Active |
| BRAND-005 | Asset Library | `brand/assets/` | Active |
| BRAND-006 | Canonical Asset CSV | `brand/assets/asset-manifest.csv` | Active |
| BRAND-007 | Asset JSON Summary | `brand/assets/asset-manifest.json` | Active |

---

## Website Architecture and Decisions

| ID | Artifact | Path | Status |
|---|---|---|---|
| ARC-001 | Launch Website Information Architecture | `docs/architecture/website-information-architecture.md` | Active / Approved baseline |
| DEC-004 | Commerce Plus and Airo Role | `docs/decisions/DEC-004-commerce-plus-and-airo-role.md` | Active |
| WEB-001 | Homepage Blueprint | `website/pages/home.md` | Active launch baseline |
| WEB-002 | Website Design System | `website/styles/design-system.md` | Active |
| WEB-003 | Website Source Objectives | `website/src/README.md` | Active |

---

## Runbooks

| ID | Artifact | Path | Status |
|---|---|---|---|
| RB-002 | GoDaddy Airo AI Builder | `docs/runbooks/RB-002-GoDaddy-Airo-AI-Builder.md` | Active |
| RB-004 | CI/CD | TBD | Planned |
| RB-005 | Production Deployment | TBD | Planned |
| RB-006 | Rollback | TBD | Planned |

---

## Checklists

| ID | Artifact | Path | Status |
|---|---|---|---|
| CL-001 | Airo First-Pass Review | `docs/checklists/CL-001-Airo-First-Pass-Review.md` | Active |

---

## Prompt Catalog

| ID | Artifact | Path | Status | Use |
|---|---|---|---|---|
| PR-001 | LuxSync Airo Master Website Build Prompt | `prompts/website/PR-001-LuxSync-Airo-Master-Website-Build-Prompt.md` | Draft / Ready for first generation | Initial Airo staging build |
| PR-002 | Website Design Review Prompt | TBD | Planned | Brand/UX review |
| PR-003 | Deployment Validation Prompt | TBD | Planned | Pre-production validation |
| PR-CONTENT-001 | Content Writer | `prompts/content-writer.md` | Active | General LuxSync copy |
| PR-PRODUCT-001 | Product Description | `prompts/product-descriptions.md` | Active | Product copy |
| PR-EMAIL-001 | Email Writer | `prompts/email-writer.md` | Active | Marketing email copy |

---

## Launch Website Direction

Current launch direction:

- Commerce-first luxury smart-home storefront
- GoDaddy Commerce Plus remains production commerce system of record
- Airo AI Builder is used for staging/reference generation and code/design exploration
- Samsung SmartThings is the primary launch compatibility standard
- Mobile-first, accessible, performant experience
- Plush Drift v2.1 visual system
- Intelligent Calm voice

Primary launch navigation:

```text
Home | Shop | Solutions | Guides | About | Support
```

Commerce utilities:

```text
Search | Account | Cart
```

---

## Open Decisions / Validation Items

1. Validate live Commerce Plus product catalog and product data before publishing prices/availability.
2. Resolve conflicting senior-service pricing before public display.
3. Run first PR-001 generation in Airo AI Builder.
4. Review Airo output using CL-001 against ARC-001 and brand standards.
5. Determine exported source structure after inspecting actual Airo output.
6. Define CI/CD only after the generated/selected implementation technology is known.
7. Define staging, production deployment, and rollback runbooks.
8. Regenerate text-bearing PNG/WebP assets where legacy typography is visually embedded.

---

## Maintenance Rules

1. Add an entry when a reusable prompt, runbook, architecture document, checklist, or decision becomes durable.
2. Mark work-in-progress artifacts `Draft`.
3. Mark the exact prompt/version used in production `Final / Used`.
4. Preserve superseded material where traceability matters.
5. Do not store passwords, API keys, payment credentials, or other secrets in the repository.
6. Review this catalog after material architecture changes and production deployments.
7. Repository paths in this catalog must correspond to actual committed files.