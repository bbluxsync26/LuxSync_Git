# LuxSync Project Runbook

**Artifact:** DOC-007  
**Status:** Active  
**Last updated:** 2026-08-31
**Repository:** `bbluxsync26/LuxSync_Git`  
**Default branch:** `master`

## Purpose

Maintain the operational record for how LuxSync is designed, documented, generated, integrated, tested, deployed, and recovered.

The repository is the source of truth. Conversation drafts and external copies become authoritative only after they are reconciled with current repository decisions and committed.

## Operating Rules

1. Record meaningful setup, integration, generation, deployment, configuration, validation, and recovery procedures.
2. Prefer exact, repeatable steps over assumptions.
3. Record when a procedure was last validated.
4. Link prompts, decisions, checklists, architecture, vendor guidance, and related runbooks.
5. Mark superseded procedures instead of silently erasing history.
6. Never store passwords, API keys, payment credentials, private tokens, or other secrets in project documentation.
7. Keep experiments and staging work separate from production-impacting procedures.
8. Update `docs/master-catalog.md` whenever a durable artifact is added or materially changed.
9. Run repository consistency validation before treating a major cross-cutting change as release-ready.

## Workstream Map

| Workstream | Scope | Durable output |
|---|---|---|
| Integration Setup | GitHub, GoDaddy, domain/DNS, platform connections | Integration and deployment runbooks |
| Website Design & CI/CD | IA, UX/UI, source, testing, preview, deployment, rollback | Architecture, decisions, website source, CI/CD runbooks |
| Prompts & Docs | Prompts, runbooks, checklists, catalog, decision records | `docs/`, `prompts/`, and catalog updates |
| Brand & Graphics | Logos, vector/UI graphics, scene imagery, asset metadata | `brand/`, generation scripts, asset runbooks |

## Environment Map

| Area | Platform | Purpose | Current status |
|---|---|---|---|
| Source control | GitHub | Authoritative repository | Active |
| Production commerce | GoDaddy Commerce Plus | Product catalog, cart, checkout, orders | System of record |
| Website generation | GoDaddy Airo AI Builder | Staging/reference design and code generation | Ready after consistency gate |
| Optimization | GoDaddy Airo Plus | SEO, content, marketing, accessibility/compliance assistance where supported | Planned |
| AI architecture and documentation | ChatGPT | Planning, prompting, review, and documentation | Active |
| Domain/DNS | GoDaddy | Public domain and DNS | Deployment runbook pending |
| Base brand system | Plush Drift v2.1 | Palette, typography, voice, core design rules | Active / Authoritative |
| Web visual treatment | Luxury Orbit | Website and web-graphics composition/effects | Active |
| CI/CD | GitHub plus selected GoDaddy deployment path | Build, test, staging, and release | Runbook pending |
| Repository validation | GitHub Actions + Python validator | Cross-repo consistency gate | Active |

## Source-of-Truth Order

Use the precedence defined in `docs/master-catalog.md`.

Current implementation tie-breaker:

- Base brand system: **Plush Drift v2.1**
- Web/graphics treatment: **Luxury Orbit**
- Official slogan: **Where Luxury Lives Intelligently**
- Homepage hero: **Smart Living. Elevated.**
- Primary CTA: **Shop Smart Home**
- Secondary CTA: **Get the ROI Guide**
- Headings / display / navigation / graphic UI: **Manrope 500/600**
- Body / supporting UI: **Inter 400/500**
- Voice: **Intelligent Calm**
- Approved primary monogram and horizontal lockup: **protected exact artwork**
- Champagne Rose Gold Metallic: **approved seventh color, `#D6B0A0` anchor with the approved metallic gradient**

Luxury Orbit uses the approved Champagne Rose Gold Metallic treatment and does not replace the Plush Drift v2.1 palette or Manrope/Inter typography.

## Core Delivery Flow

1. Define the requirement in the appropriate workstream.
2. Check the master catalog and current governing artifacts.
3. Create or update the prompt, specification, architecture, decision, or business rule.
4. Reconcile dependent documents when the decision crosses workstream boundaries.
5. Run automated repository consistency validation.
6. Generate or edit the website in staging.
7. Review with the applicable checklist.
8. Validate responsive behavior, accessibility, content integrity, and commerce boundaries.
9. Commit approved changes to GitHub.
10. Deploy to preview/staging using the approved deployment path.
11. Record validation results.
12. Promote to production only after the production gate passes.
13. Update this runbook and the master catalog.

## Current Artifact Map

| ID | Artifact | Path | Status |
|---|---|---|---|
| ARC-001 | Launch Website Information Architecture | `docs/architecture/website-information-architecture.md` | Active baseline |
| DEC-004 | Commerce Plus and Airo Role | `docs/decisions/DEC-004-commerce-plus-and-airo-role.md` | Active |
| DEC-005 | Senior Service Pricing | `docs/decisions/DEC-005-senior-service-pricing.md` | Open / Decision Required |
| RB-002 | GoDaddy Airo AI Builder | `docs/runbooks/RB-002-GoDaddy-Airo-AI-Builder.md` | Active |
| RB-007 | Brand Asset Raster Regeneration | `docs/runbooks/RB-007-Brand-Asset-Raster-Regeneration.md` | Historical / Superseded |
| RB-008 | Luxury Orbit Brand Asset Generation | `docs/runbooks/RB-008-Luxury-Orbit-Brand-Asset-Generation.md` | Active |
| RB-009 | Repository Consistency Validation | `docs/runbooks/RB-009-Repository-Consistency-Validation.md` | Active |
| CL-001 | Airo First-Pass Review | `docs/checklists/CL-001-Airo-First-Pass-Review.md` | Active |
| PR-001 | Airo Master Website Build Prompt | `prompts/website/PR-001-LuxSync-Airo-Master-Website-Build-Prompt.md` | Ready after consistency gate |

## Current Readiness

### Completed

- [x] GitHub repository and `master` branch confirmed
- [x] Workstreams separated
- [x] Master catalog established
- [x] Launch information architecture established
- [x] Commerce Plus/Airo boundary decided
- [x] Plush Drift v2.1 base system established
- [x] Luxury Orbit web treatment established
- [x] Manrope/Inter typography contract established
- [x] Approved exact primary logo artwork protected
- [x] PR-001 reconciled to the current brand contract
- [x] First-pass review checklist reconciled
- [x] Automated repository consistency validation defined
- [x] Asset metadata reconciliation defined
- [x] Senior-service pricing conflict captured as DEC-005 rather than silently resolved

### Next

- [ ] Complete DEC-005 with one approved senior-service pricing model before public display
- [ ] Confirm repository consistency validation passes on the reconciled baseline
- [ ] Validate Commerce Plus catalog data before publishing prices or availability
- [ ] Run the first staging generation with PR-001
- [ ] Review the result with CL-001
- [ ] Record accepted and rejected output
- [ ] Inspect any exported source before choosing framework/build assumptions
- [ ] Create RB-004 CI/CD
- [ ] Create RB-005 Production Deployment, including domain/DNS
- [ ] Create RB-006 Rollback

## Production Protection

During the first Airo generation and review cycle:

- Do not connect live payments.
- Do not modify production DNS.
- Do not replace Commerce Plus as the commerce system of record.
- Do not create a second unmanaged production catalog.
- Do not commit secrets.
- Do not present roadmap products as live.
- Do not publish unresolved senior-service pricing.
- Do not replace protected approved logo artwork with a generic regenerated version.

## Validation Commands

From the repository root:

```bash
python scripts/reconcile-asset-metadata.py
python scripts/validate-repository-consistency.py
```

Asset metadata reconciliation should leave no uncommitted changes when the repository is clean.

## Validation and Troubleshooting Log Template

**Date:**  
**Component:**  
**Environment:**  
**Symptom:**  
**Cause:**  
**Resolution:**  
**Validation:**  
**Related artifact:**  
**Commit/deployment:**  

## Decision Log

| ID | Date | Decision | Status |
|---|---|---|---|
| DEC-001 | 2026-08-29 | Reuse `bbluxsync26/LuxSync_Git` | Active |
| DEC-002 | 2026-08-29 | Separate Integration, Website/CI/CD, and Prompts/Docs workstreams | Active |
| DEC-003 | 2026-08-29 | Maintain the master catalog and project runbook as durable records | Active |
| DEC-004 | 2026-08-29 | Commerce Plus governs launch commerce; Airo accelerates staging/design | Active |
| DEC-005 | 2026-08-30 | Do not publish senior-service pricing until one candidate model is explicitly approved | Open / Decision Required |

## Change Log

| Date | Change |
|---|---|
| 2026-08-29 | Initial project runbook created. |
| 2026-08-30 | Reconciled operational baseline to Plush Drift v2.1 + Luxury Orbit and current website architecture. |
| 2026-08-30 | Added Manrope/Inter tie-breaker, protected-logo rules, asset metadata reconciliation, and repository consistency validation. |
| 2026-08-30 | Added DEC-005 to preserve the unresolved senior-pricing conflict as an explicit publication guardrail. |
| 2026-08-31 | Promoted Champagne Rose Gold Metallic to the seventh approved color and reconciled palette guidance and asset counts. |
| 2026-08-31 | Added branded website biographies and approved leadership titles for both LuxSync co-founders. |
| 2026-08-31 | Integrated the approved founder profiles and canonical FAQs into the About, FAQ, homepage, architecture, Airo prompt, and review workflow. |
