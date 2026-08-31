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
6. Active asset metadata and exports
7. Historical/superseded generators and legacy graphics

## Current Brand Tie-Breaker

When current LuxSync files disagree, apply these rules:

- **Authoritative visual system:** LuxSync v3
- **Active asset root:** `brand/assets-v3/`
- **Headings / navigation / buttons / graphic UI:** Manrope 500/600
- **Body / supporting UI:** Inter 400/500
- **Official slogan:** Where Luxury Lives Intelligently
- **Homepage hero:** Smart Living. Elevated.
- **Protected exact logo artwork:** approved monogram and horizontal lockup remain immutable artwork
- **Approved colors only:** Slate Navy, Dark Suede, Pale Driftwood, Warm Taupe Mauve, Antique Rose Taupe, Dusty Steel, Champagne Rose Gold Metallic
- **Champagne Rose Gold Metallic:** `#D6B0A0` anchor with approved metallic rendering

Do not redraw, retype, recolor, soften, cartoonize, or regenerate the approved logo artwork.

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
| DOC-008 | Bridgette Beardsley Leadership Biography | `docs/leadership/bridgette-beardsley.md` | Active / Approved |
| DOC-009 | Sheldon Bardol Leadership Biography | `docs/leadership/sheldon-bardol.md` | Active / Approved |

## Brand System

| ID | Artifact | Path | Status |
|---|---|---|---|
| BRAND-001 | Brand Guidelines | `brand/README.md` | Active — LuxSync v3 |
| BRAND-002 | Color System | `brand/colors.md` | Active — approved seven-color palette |
| BRAND-003 | Typography | `brand/typography.md` | Active — Manrope + Inter |
| BRAND-004 | Voice & Tone | `brand/voice-and-tone.md` | Active — Intelligent Calm |
| BRAND-005 | v3 Asset System | `brand/assets-v3/` | Active / Authoritative |
| BRAND-006 | v3 Brand Board | `brand/assets-v3/00-reference/brand-board.svg` | Active reference |
| BRAND-007 | v3 Asset Manifest | `brand/assets-v3/08-docs/asset-manifest.json` | Active |
| BRAND-008 | v3 Migration Guide | `brand/assets-v3/08-docs/MIGRATION.md` | Active |
| BRAND-009 | Legacy Asset Library | `brand/assets/` | Legacy / Compatibility only |
| BRAND-010 | Production Scene Manifest | `brand/assets/12-scenes/scene-manifest.csv` | Retained source photography |

## v3 Asset Groups

| Area | Path | Purpose |
|---|---|---|
| Reference | `brand/assets-v3/00-reference/` | authoritative brand board |
| Foundation | `brand/assets-v3/01-foundation/` | approved palette |
| UI | `brand/assets-v3/02-ui/` | buttons, CTAs, badges, ecommerce controls |
| Icons | `brand/assets-v3/03-icons/` | smart-living line icons |
| Heroes | `brand/assets-v3/04-heroes/` | homepage and ROI-guide hero compositions |
| Ecommerce | `brand/assets-v3/05-ecommerce/` | product-card and trust components |
| Stationery | `brand/assets-v3/06-stationery/` | business cards, letterhead, invoice |
| Marketing | `brand/assets-v3/07-marketing/` | social, email, flyer templates |
| Docs | `brand/assets-v3/08-docs/` | manifest and migration policy |

## Architecture and Website

| ID | Artifact | Path | Status |
|---|---|---|---|
| ARC-001 | Launch Website Information Architecture | `docs/architecture/website-information-architecture.md` | Active / Approved baseline |
| DEC-004 | Commerce Plus and Airo Role | `docs/decisions/DEC-004-commerce-plus-and-airo-role.md` | Active |
| DEC-005 | Senior Service Pricing | `docs/decisions/DEC-005-senior-service-pricing.md` | Open / Decision Required |
| WEB-001 | Homepage Blueprint | `website/pages/home.md` | Active launch baseline |
| WEB-002 | Website Design System | `website/styles/design-system.md` | Active — LuxSync v3 |
| WEB-003 | Website Source Area | `website/src/README.md` | Placeholder until first reviewed export |

## Runbooks

| ID | Artifact | Path | Status |
|---|---|---|---|
| RB-002 | GoDaddy Airo AI Builder | `docs/runbooks/RB-002-GoDaddy-Airo-AI-Builder.md` | Active |
| RB-004 | CI/CD | TBD | Planned |
| RB-005 | Production Deployment and Domain/DNS | TBD | Planned |
| RB-006 | Rollback | TBD | Planned |
| RB-007 | Brand Asset Raster Regeneration | `docs/runbooks/RB-007-Brand-Asset-Raster-Regeneration.md` | Superseded / Historical |
| RB-008 | Luxury Orbit Brand Asset Generation | `docs/runbooks/RB-008-Luxury-Orbit-Brand-Asset-Generation.md` | Superseded / Historical |
| RB-009 | Repository Consistency Validation | `docs/runbooks/RB-009-Repository-Consistency-Validation.md` | Active |

## Prompt Catalog

| ID | Artifact | Path | Status | Use |
|---|---|---|---|---|
| PR-001 | LuxSync Airo Master Website Build Prompt | `prompts/website/PR-001-LuxSync-Airo-Master-Website-Build-Prompt.md` | Draft / Requires v3 asset references | Initial Airo staging build |
| PR-002 | Website Design Review Prompt | TBD | Planned | Brand/UX review |
| PR-003 | Deployment Validation Prompt | TBD | Planned | Pre-production validation |
| PR-CONTENT-001 | Content Writer | `prompts/content-writer.md` | Active | General LuxSync copy |
| PR-PRODUCT-001 | Product Description | `prompts/product-descriptions.md` | Active | Product copy |
| PR-EMAIL-001 | Email Writer | `prompts/email-writer.md` | Active | Marketing email copy |

## Automation and Validation

The previous Luxury Orbit generators remain historical tooling for the legacy `brand/assets/` library. They do **not** define LuxSync v3.

| Artifact | Path | Status |
|---|---|---|
| Legacy Brand Generator | `scripts/generate-luxury-orbit-assets.py` | Historical / legacy assets only |
| Legacy Brand Renderer | `scripts/render-luxury-orbit-assets.py` | Historical / legacy assets only |
| Repository Validator | `scripts/validate-repository-consistency.py` | Active; update for v3 as needed |
| Consistency Workflow | `.github/workflows/validate-repository-consistency.yml` | Active |

## Launch Website Direction

- Commerce-first luxury smart-home storefront
- GoDaddy Commerce Plus remains production commerce system of record
- Samsung SmartThings remains the primary launch compatibility standard
- Mobile-first, accessible, performant experience
- LuxSync v3 visual system
- Manrope + Inter typography
- Intelligent Calm voice
- Approved logo artwork referenced directly, never regenerated

Primary launch navigation:

```text
Home | Shop | Solutions | Guides | About | Support
```

Commerce utilities:

```text
Search | Account | Cart
```

## Maintenance Rules

1. Add an entry when a reusable prompt, runbook, architecture document, checklist, decision, or validation procedure becomes durable.
2. Mark work-in-progress artifacts `Draft`.
3. Preserve superseded material where traceability matters, but clearly mark it legacy.
4. Do not store passwords, API keys, payment credentials, private tokens, or other secrets in the repository.
5. Repository paths in this catalog must correspond to actual committed files.
6. New visual assets must use `brand/assets-v3/`.
7. Never recreate protected logo artwork.
8. Branded vector/UI work may use only the approved palette.

## Change Log

| Date | Change |
|---|---|
| 2026-08-29 | Repository master catalog established. |
| 2026-08-30 | Reconciled website/Airo architecture and operating baseline. |
| 2026-08-31 | Added Champagne Rose Gold Metallic as the seventh approved color. |
| 2026-08-31 | Established LuxSync v3 as the authoritative brand asset system and moved the generated Luxury Orbit library to legacy compatibility status. |
| 2026-08-31 | Added approved branded leadership biographies and titles for Bridgette Beardsley and Sheldon Bardol. |
