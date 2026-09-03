# LuxSync Project Runbook

**Artifact:** DOC-007
**Status:** Active / Reconciled
**Last updated:** 2026-09-03
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
| Website Design & CI/CD | IA, UX/UI, source, testing, preview, Airo handoff/reconciliation, deployment, rollback | Architecture, website source, CI/CD runbooks |
| Content & Guides | FAQs, Contact, setup/education, product content | `content/`, `website/pages/`, guides |
| Prompts & Docs | Prompts, runbooks, checklists, catalog, decisions | `docs/`, `prompts/`, Master Catalog |
| Concierge | Find My LuxSync Solution, engine, Blueprint, product mapping | `docs/architecture/intelligent-living-concierge.md`, `website/src/concierge/` |
| Brand & Graphics | Logos, vector/UI graphics, imagery, asset metadata | `brand/`, asset tooling/runbooks |

## Environment Map

| Area | Platform / Artifact | Purpose | Current status |
|---|---|---|---|
| Source control | GitHub | Authoritative repository | Active / private |
| Production commerce | GoDaddy Commerce Plus | Product catalog, cart, checkout, orders | System of record |
| Website generation | GoDaddy Airo AI Builder | Staging/reference design and code generation | Governed by PR-001 + ARC-003 + RB-012 |
| Airo source transport | `scripts/build-airo-source-package.py` | Deterministic repo → Airo ZIP | Active |
| Website development branch | `website/airo-development` | Persistent controlled Airo-backed integration baseline | Created after pipeline PR merge |
| Optimization | GoDaddy Airo Plus | SEO/content/marketing/accessibility assistance where supported | Supporting only |
| Domain/DNS | GoDaddy | Public domain and DNS | Deployment runbook pending |
| Visual system | LuxSync Production Raster v5 | Current website/brand implementation | Active / authoritative |
| Design DNA | Plush Drift | Tactile illumination and enduring interaction language | Active / authoritative |
| Concierge | `website/src/concierge/` | Rules-based guided recommendation engine | Active / v1 |
| Product planning | `content/product-catalog.md` | Product families, bundles, Experience concepts | Active / canonical planning catalog |
| Contact | `website/pages/contact.md` | Adaptive customer-intent routing | Active design baseline |
| ROI Guide Library | `content/guides/roi/` + `website/pages/guides.md` | Audience-specific ROI education and measurement worksheets | Active |
| CI/CD | GitHub plus selected GoDaddy deployment path | Build/test/staging/release | Existing validation/release workflows active; consolidated runbook still planned |
| Repository validation | GitHub Actions + Python validators | Cross-repo consistency gate | Active |

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
- GitHub `master` owns product truth; Airo is a staging/design/code-generation participant, not a second authority

Retired visual systems, generators, hero language, and slogan treatments do not override the rules above.

## Core Delivery Flow

1. Define the requirement in the appropriate workstream.
2. Check Master Catalog and governing artifacts.
3. Create/update the prompt, specification, architecture, decision, page blueprint, content baseline, product mapping, or business rule.
4. Reconcile dependent files when the decision crosses workstreams.
5. Run repository consistency validation.
6. Build the governed Airo source ZIP when Airo is part of the cycle.
7. Generate/edit the website in Airo staging or the repository implementation.
8. Review with the applicable checklist.
9. Export Airo output when applicable and reconcile it through a GitHub website branch rather than copying it directly to `master`.
10. Validate responsive behavior, accessibility, content integrity, Concierge/Contact behavior, and commerce boundaries.
11. Commit approved changes and open a PR.
12. Require green CI.
13. Deploy to preview/staging using the approved path.
14. Record validation results.
15. Promote to production only after the production gate passes.
16. Update this runbook and Master Catalog.

## Current Artifact Map

| ID | Artifact | Path | Status |
|---|---|---|---|
| ARC-001 | Launch Website Information Architecture | `docs/architecture/website-information-architecture.md` | Active |
| ARC-002 | Intelligent Living Concierge Architecture | `docs/architecture/intelligent-living-concierge.md` | Active / Flagship |
| ARC-003 | Airo Source Package Contract | `docs/architecture/airo-source-package-contract.md` | Active / Authoritative |
| DEC-004 | Commerce Plus and Airo Role | `docs/decisions/DEC-004-commerce-plus-and-airo-role.md` | Active |
| DEC-005 | Senior Service Pricing | `docs/decisions/DEC-005-senior-service-pricing.md` | Open / Decision Required |
| WEB-001 | Homepage Blueprint | `website/pages/home.md` | Active |
| WEB-006 | Contact Page Blueprint | `website/pages/contact.md` | Active |
| WEB-007 | Concierge Engine | `website/src/concierge/` | Active / v1 |
| CONTENT-003 | Contact Content | `content/contact.md` | Active |
| CONTENT-004 | Product & Solution Catalog | `content/product-catalog.md` | Active |
| RB-002 | GoDaddy Airo AI Builder | `docs/runbooks/RB-002-GoDaddy-Airo-AI-Builder.md` | Active |
| RB-009 | Repository Consistency Validation | `docs/runbooks/RB-009-Repository-Consistency-Validation.md` | Active |
| RB-012 | Airo ↔ GitHub Development Loop | `docs/runbooks/RB-012-Airo-GitHub-Development-Loop.md` | Active |
| TOOL-AIRO-001 | Deterministic Airo Source Package Builder | `scripts/build-airo-source-package.py` | Active |
| CI-AIRO-001 | Build Airo Source Package Workflow | `.github/workflows/build-airo-source-package.yml` | Active / Manual artifact build |
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
- [x] Repository-wide image cleanup and validation completed
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
- [x] Airo source-package contract established
- [x] Deterministic repo → Airo ZIP builder established
- [x] GitHub Actions Airo package artifact workflow established
- [x] Airo export → GitHub reconciliation runbook established

### Next

- [ ] Create/refresh `website/airo-development` from the validated pipeline merge commit
- [ ] Generate the first source package from that baseline
- [ ] Start a clean Airo build with the package + current PR-001
- [ ] Review with CL-001
- [ ] Export the full Airo project
- [ ] Reconcile accepted changes through a per-cycle website branch
- [ ] Complete DEC-005 before publishing senior-service pricing
- [ ] Validate Commerce Plus product data before publishing exact prices/stock/availability
- [ ] Map validated live products to LuxSync Experience capability requirements
- [ ] Create/refresh consolidated RB-004 CI/CD documentation
- [ ] Create RB-005 Production Deployment and Domain/DNS
- [ ] Create RB-006 Rollback

## Production Protection

During staging/review:

- do not connect live payments
- do not modify production DNS
- do not replace Commerce Plus as commerce authority
- do not create a second unmanaged production catalog
- do not commit secrets
- do not put secrets in the Airo source ZIP
- do not upload internal financial planning or protected approval/source assets merely because they exist in the repository
- do not present roadmap products as live
- do not publish unresolved senior-service pricing
- do not replace protected logo artwork
- do not replace repository Concierge logic with generated survey logic
- do not restore retired slogan/hero language
- do not merge raw Airo exports directly into `master`

## Validation

From repository root:

```bash
python scripts/validate-repository-consistency.py
python scripts/build-airo-source-package.py --check
```

The first command verifies current source-of-truth files, sole slogan usage, founder titles, Contact routing, Concierge naming/contracts, prompt synchronization, and parseable Concierge configuration.

The second verifies the governed Airo handoff allowlist, required sources, forbidden paths, and secret-like filename protections.

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
| ARC-003 | 2026-09-03 | Airo receives an allowlisted source package and returns exports through GitHub reconciliation | Active |
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
| 2026-09-03 | Added the governed GitHub → Airo source-package contract, deterministic ZIP builder, artifact workflow, and Airo → GitHub reconciliation branch model. |

## Production Source-of-Truth Handoff

The current website source-of-truth baseline is `LuxSync Production Raster v5` with the implementation manifest at `website/implementation-manifest.json`. Use `docs/production-source-of-truth.md` as the first operational reference and `website/asset-map.md` for visual publication rules.

For Airo-backed development, use `docs/architecture/airo-source-package-contract.md` and `docs/runbooks/RB-012-Airo-GitHub-Development-Loop.md`. The generated ZIP is transport material only; GitHub remains authoritative.
