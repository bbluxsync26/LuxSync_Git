# LuxSync Project Runbook

**Artifact:** DOC-007
**Status:** Active / Reconciled
**Last updated:** 2026-08-31
**Repository:** `bbluxsync26/LuxSync_Git`
**Default branch:** `master`

## Purpose

Maintain the operational record for how LuxSync is designed, documented, generated, integrated, tested, deployed, and recovered.

The repository is the source of truth. Conversation drafts and external copies become authoritative only after reconciliation with current repository decisions and commit to `master` or an approved release branch.

## Operating Rules

1. Record meaningful setup, integration, generation, deployment, configuration, validation, and recovery procedures.
2. Prefer exact, repeatable steps over assumptions.
3. Record when a procedure was last validated.
4. Link prompts, decisions, checklists, architecture, content, product-catalog, and related runbooks.
5. Mark superseded procedures instead of silently treating them as current.
6. Never store passwords, API keys, payment credentials, private tokens, or other secrets.
7. Keep staging/experiments separate from production-impacting procedures.
8. Update `docs/master-catalog.md` whenever a durable artifact is added or materially changed.
9. Run repository consistency validation after major cross-cutting changes.
10. Preserve stable Concierge field and Experience IDs after production launch unless a versioned migration is intentionally designed.

## Workstream Map

| Workstream | Scope | Durable output |
|---|---|---|
| Integration Setup | GitHub, GoDaddy, domain/DNS, platform connections | Integration/deployment runbooks |
| Website Design & CI/CD | IA, UX/UI, source, testing, preview, deployment, rollback | Architecture, website source, CI/CD runbooks |
| Content & Guides | FAQs, Contact, setup/education, product content | `content/`, `website/pages/`, guides |
| Prompts & Docs | Prompts, runbooks, checklists, catalog, decisions | `docs/`, `prompts/`, Master Catalog |
| Concierge | Find My LuxSync Solution, engine, Blueprint, product mapping | `docs/architecture/intelligent-living-concierge.md`, `website/src/concierge/` |
| Brand & Graphics | Logos, vector/UI graphics, imagery, asset metadata | `brand/`, asset tooling/runbooks |

## Environment Map

| Area | Platform / Artifact | Purpose | Current status |
|---|---|---|---|
| Source control | GitHub | Authoritative repository | Active / private |
| Production commerce | GoDaddy Commerce Plus | Product catalog, cart, checkout, orders | System of record |
| Website generation | GoDaddy Airo AI Builder | Staging/reference design and code generation | Governed by PR-001 |
| Optimization | GoDaddy Airo Plus | SEO/content/marketing/accessibility assistance where supported | Supporting only |
| Domain/DNS | GoDaddy | Public domain and DNS | Deployment runbook pending |
| Visual system | LuxSync Production Raster v5 | Current website/brand implementation | Active / authoritative |
| Design DNA | Plush Drift | Tactile illumination and enduring interaction language | Active / authoritative |
| Concierge | `website/src/concierge/` | Rules-based guided recommendation engine | Active / v1 |
| Product planning | `content/product-catalog.md` | Product families, bundles, Experience concepts | Active / canonical planning catalog |
| Contact | `website/pages/contact.md` | Adaptive customer-intent routing | Active design baseline |
| ROI Guide Library | `content/guides/roi/` + `website/pages/guides.md` | Audience-specific ROI education and measurement worksheets | Active |
| CI/CD | GitHub plus selected GoDaddy deployment path | Build/test/staging/release | Runbook pending |
| Repository validation | GitHub Actions + Python validator | Cross-repo consistency gate | Active |

## Current Source-of-Truth Tie-Breaker

Use `docs/master-catalog.md` for precedence.

Current implementation rules:

- Visual system: **LuxSync Production Raster v5**
- Design DNA: **Plush Drift**
- Sole approved public slogan / hero line: **Where Luxury Lives Intelligently**
- Primary homepage CTA: **Find My LuxSync Solution**
- Secondary homepage CTA: **Shop Smart Home**
- Supporting CTA: **Get the ROI Guide**
- Headings / display / navigation / graphic UI: **Manrope 500/600**
- Body / supporting UI: **Inter 400/500**
- Voice: **Intelligent Calm**
- Flagship guided experience: **LuxSync Intelligent Living Concierge**
- Personalized output: **My LuxSync Blueprint**
- Concierge model: **Lifestyle → Experience → Intelligence → Technology**
- Product planning catalog: `content/product-catalog.md`
- Support email: `support@luxsync.net`
- Information / consultation email: `info@luxsync.net`
- Protected logo artwork remains exact artwork
- Champagne Rose Gold Metallic uses `#D6B0A0` as the approved anchor

Retired visual systems, generators, hero language, and slogan treatments do not override the rules above.

## Core Delivery Flow

1. Define the requirement in the appropriate workstream.
2. Check Master Catalog and governing artifacts.
3. Create/update the prompt, specification, architecture, decision, page blueprint, content baseline, product mapping, or business rule.
4. Reconcile dependent files when the decision crosses workstreams.
5. Run repository consistency validation.
6. Generate/edit the website in staging.
7. Review with the applicable checklist.
8. Validate responsive behavior, accessibility, content integrity, Concierge/Contact behavior, and commerce boundaries.
9. Commit approved changes.
10. Deploy to preview/staging using the approved path.
11. Record validation results.
12. Promote to production only after the production gate passes.
13. Update this runbook and Master Catalog.

## Current Artifact Map

| ID | Artifact | Path | Status |
|---|---|---|---|
| ARC-001 | Launch Website Information Architecture | `docs/architecture/website-information-architecture.md` | Active |
| ARC-002 | Intelligent Living Concierge Architecture | `docs/architecture/intelligent-living-concierge.md` | Active / Flagship |
| DEC-004 | Commerce Plus and Airo Role | `docs/decisions/DEC-004-commerce-plus-and-airo-role.md` | Active |
| DEC-005 | Senior Service Pricing | `docs/decisions/DEC-005-senior-service-pricing.md` | Open / Decision Required |
| WEB-001 | Homepage Blueprint | `website/pages/home.md` | Active |
| WEB-006 | Contact Page Blueprint | `website/pages/contact.md` | Active |
| WEB-007 | Concierge Engine | `website/src/concierge/` | Active / v1 |
| CONTENT-003 | Contact Content | `content/contact.md` | Active |
| CONTENT-004 | Product & Solution Catalog | `content/product-catalog.md` | Active |
| RB-002 | GoDaddy Airo AI Builder | `docs/runbooks/RB-002-GoDaddy-Airo-AI-Builder.md` | Active |
| RB-009 | Repository Consistency Validation | `docs/runbooks/RB-009-Repository-Consistency-Validation.md` | Active |
| CL-001 | Airo First-Pass Review | `docs/checklists/CL-001-Airo-First-Pass-Review.md` | Active |
| PR-001 | Airo Master Website Build Prompt | `prompts/website/PR-001-LuxSync-Airo-Master-Website-Build-Prompt.md` | Active / Reconciled |

## Current Readiness

### Completed

- [x] GitHub repository and `master` branch established
- [x] Master Catalog and project runbook established
- [x] Launch information architecture established
- [x] Commerce Plus/Airo boundary established
- [x] LuxSync Production Raster v5 / Plush Drift governance established
- [x] Manrope/Inter typography contract established
- [x] Approved logo artwork protected
- [x] Founder biographies and exact leadership titles established
- [x] Canonical FAQs established
- [x] Intelligent Living Concierge architecture and rules engine established
- [x] My LuxSync Blueprint output architecture established
- [x] Dedicated adaptive Contact page architecture established
- [x] Shared Property Profile concept established across Contact and Concierge
- [x] Canonical Product & Solution Catalog established
- [x] Reusable content/product/email prompts reconciled to current company facts
- [x] `Where Luxury Lives Intelligently` established as sole public slogan/hero line
- [x] Senior-service pricing conflict preserved as DEC-005 rather than guessed

### Next

- [ ] Complete DEC-005 before publishing senior-service pricing
- [ ] Validate Commerce Plus product data before publishing exact prices/stock/availability
- [ ] Map validated live products to LuxSync Experience capability requirements
- [ ] Run Airo staging generation using current PR-001
- [ ] Review with CL-001
- [ ] Inspect exported source before choosing build/deployment assumptions
- [ ] Create RB-004 CI/CD
- [ ] Create RB-005 Production Deployment and Domain/DNS
- [ ] Create RB-006 Rollback

## Production Protection

During staging/review:

- do not connect live payments
- do not modify production DNS
- do not replace Commerce Plus as commerce authority
- do not create a second unmanaged production catalog
- do not commit secrets
- do not present roadmap products as live
- do not publish unresolved senior-service pricing
- do not replace protected logo artwork
- do not replace repository Concierge logic with generated survey logic
- do not restore retired slogan/hero language

## Validation

From repository root:

```bash
python scripts/validate-repository-consistency.py
```

The validation should verify current source-of-truth files, sole slogan usage, founder titles, Contact routing, Concierge naming/contracts, prompt synchronization, and parseable Concierge configuration.

## Validation / Troubleshooting Log Template

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
| DEC-002 | 2026-08-29 | Separate operational workstreams | Active |
| DEC-003 | 2026-08-29 | Maintain Master Catalog and Project Runbook | Active |
| DEC-004 | 2026-08-29 | Commerce Plus governs launch commerce; Airo accelerates staging/design | Active |
| DEC-005 | 2026-08-30 | Do not publish senior-service pricing until explicitly approved | Open |
| ARCH-001 | 2026-08-31 | Find My LuxSync Solution / Intelligent Living Concierge is a flagship customer journey | Active |
| ARCH-002 | 2026-08-31 | Contact and Concierge share a reusable Property Profile | Active |
| BRAND-001 | 2026-08-31 | Where Luxury Lives Intelligently is the sole public slogan/hero line | Active |

## Change Log

| Date | Change |
|---|---|
| 2026-08-29 | Initial project runbook created. |
| 2026-08-30 | Reconciled commerce/Airo architecture and pricing guardrails. |
| 2026-08-31 | Established current LuxSync Production Raster v5 / Plush Drift / Manrope + Inter governance. |
| 2026-08-31 | Added approved founder profiles and canonical FAQs. |
| 2026-08-31 | Added Intelligent Living Concierge, My LuxSync Blueprint, adaptive Contact, shared Property Profile, and Product & Solution Catalog. |
| 2026-08-31 | Reconciled reusable prompts and retired alternate slogan/hero treatments in favor of Where Luxury Lives Intelligently. |

## Production Source-of-Truth Handoff

The current website source-of-truth baseline is `LuxSync Production Raster v5` with the implementation manifest at `website/implementation-manifest.json`. Use `docs/production-source-of-truth.md` as the first operational reference and `website/asset-map.md` for visual publication rules.
