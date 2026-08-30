# LuxSync Project Runbook

**Artifact:** DOC-007  
**Status:** Active  
**Last updated:** 2026-08-30  
**Repository:** `bbluxsync26/LuxSync_Git`  
**Default branch:** `master`

## Purpose

Maintain the operational record for how LuxSync is designed, documented, generated, integrated, tested, deployed, and recovered.

The repository is the source of truth. Conversation drafts and external copies become authoritative only after they are reconciled with current repository decisions and committed.

## Operating Rules

1. Record meaningful setup, integration, generation, deployment, configuration, and recovery procedures.
2. Prefer exact, repeatable steps over assumptions.
3. Record when a procedure was last validated.
4. Link prompts, decisions, checklists, architecture, vendor guidance, and related runbooks.
5. Mark superseded procedures instead of silently erasing history.
6. Never store passwords, API keys, payment credentials, private tokens, or other secrets in project documentation.
7. Keep experiments and staging work separate from production-impacting procedures.
8. Update `docs/master-catalog.md` whenever a durable artifact is added or materially changed.

## Workstream Map

| Workstream | Scope | Durable output |
|---|---|---|
| Integration Setup | GitHub, GoDaddy, domain/DNS, platform connections | Integration and deployment runbooks |
| Website Design & CI/CD | IA, UX/UI, source, testing, preview, deployment, rollback | Architecture, decisions, website source, CI/CD runbooks |
| Prompts & Docs | Prompts, runbooks, checklists, catalog, decision records | `docs/`, `prompts/`, and catalog updates |

## Environment Map

| Area | Platform | Purpose | Current status |
|---|---|---|---|
| Source control | GitHub | Authoritative repository | Active |
| Production commerce | GoDaddy Commerce Plus | Product catalog, cart, checkout, orders | System of record |
| Website generation | GoDaddy Airo AI Builder | Staging/reference design and code generation | Ready for first PR-001 pass |
| Optimization | GoDaddy Airo Plus | SEO, content, marketing, accessibility/compliance assistance where supported | Planned |
| AI architecture and documentation | ChatGPT | Planning, prompting, review, and documentation | Active |
| Domain/DNS | GoDaddy | Public domain and DNS | Deployment runbook pending |
| Brand system | Luxury Orbit | Website and web-graphics direction | Active |
| CI/CD | GitHub plus selected GoDaddy deployment path | Build, test, staging, and release | Runbook pending |

## Source-of-Truth Order

Use the precedence defined in `docs/master-catalog.md`. For current website visual work:

- Visual system: **Luxury Orbit**
- Official slogan: **Where Luxury Lives Intelligently**
- Homepage hero: **Smart Living. Elevated.**
- Primary CTA: **Shop Smart Home**
- Secondary CTA: **Get the ROI Guide**
- Wordmark/editorial: Bodoni-family serif stack
- Headings/UI: Century Gothic / Montserrat stack
- Body/UI: Candara / Inter / Segoe UI stack
- Voice: **Intelligent Calm**

## Core Delivery Flow

1. Define the requirement in the appropriate workstream.
2. Check the master catalog and current governing artifacts.
3. Create or update the prompt, specification, architecture, or decision.
4. Generate or edit the website in staging.
5. Review with the applicable checklist.
6. Validate responsive behavior, accessibility, content integrity, and commerce boundaries.
7. Commit approved changes to GitHub.
8. Deploy to preview/staging using the approved deployment path.
9. Record validation results.
10. Promote to production only after the production gate passes.
11. Update this runbook and the master catalog.

## Current Artifact Map

| ID | Artifact | Path | Status |
|---|---|---|---|
| ARC-001 | Launch Website Information Architecture | `docs/architecture/website-information-architecture.md` | Active baseline |
| DEC-004 | Commerce Plus and Airo Role | `docs/decisions/DEC-004-commerce-plus-and-airo-role.md` | Active |
| RB-002 | GoDaddy Airo AI Builder | `docs/runbooks/RB-002-GoDaddy-Airo-AI-Builder.md` | Active |
| RB-008 | Luxury Orbit Brand Asset Generation | `docs/runbooks/RB-008-Luxury-Orbit-Brand-Asset-Generation.md` | Active |
| CL-001 | Airo First-Pass Review | `docs/checklists/CL-001-Airo-First-Pass-Review.md` | Active |
| PR-001 | Airo Master Website Build Prompt | `prompts/website/PR-001-LuxSync-Airo-Master-Website-Build-Prompt.md` | Ready for first staging generation |

## Current Readiness

### Completed

- [x] GitHub repository and `master` branch confirmed
- [x] Workstreams separated
- [x] Master catalog established
- [x] Launch information architecture established
- [x] Commerce Plus/Airo boundary decided
- [x] Luxury Orbit active brand system committed
- [x] PR-001 reconciled to Luxury Orbit
- [x] First-pass review checklist reconciled to Luxury Orbit

### Next

- [ ] Run the first staging generation with PR-001
- [ ] Review the result with CL-001
- [ ] Record accepted and rejected output
- [ ] Inspect any exported source before choosing framework/build assumptions
- [ ] Create RB-004 CI/CD
- [ ] Create RB-005 Production Deployment, including domain/DNS
- [ ] Create RB-006 Rollback
- [ ] Validate Commerce Plus catalog data before publishing prices or availability

## Production Protection

During the first Airo generation and review cycle:

- Do not connect live payments.
- Do not modify production DNS.
- Do not replace Commerce Plus as the commerce system of record.
- Do not create a second unmanaged production catalog.
- Do not commit secrets.
- Do not present roadmap products as live.

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

## Change Log

| Date | Change |
|---|---|
| 2026-08-29 | Initial project runbook created. |
| 2026-08-30 | Reconciled operational baseline to the committed Luxury Orbit system and current website architecture. |
