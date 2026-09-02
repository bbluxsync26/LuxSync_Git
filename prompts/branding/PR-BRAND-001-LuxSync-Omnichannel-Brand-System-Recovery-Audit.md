# PR-BRAND-001 — LuxSync Omnichannel Brand System Recovery, Build & Audit Prompt

**Status:** Active / Restart-Safe / Promptless / Self-Healing  
**Purpose:** Resume, build, validate, repair, and audit the complete LuxSync omnichannel brand-asset system without unnecessary user interaction or rework.  
**Repository:** `bbluxsync26/LuxSync_Git`  
**Default branch:** `master`  
**Primary local workspace when available:** `C:\LuxSync_Git`  
**Official slogan:** **Where Luxury Lives Intelligently**

---

# HOW TO USE THIS PROMPT

Run this entire prompt as the operating instruction for LuxSync branding work.

Do **not** ask the user where to resume. Do **not** assume prior work failed. Do **not** restart completed phases merely because this prompt was invoked again.

Instead:

1. inspect the current repository and local workspace if available;
2. determine what work is already complete and valid;
3. repair objective inconsistencies that are safe to repair;
4. resume from the first incomplete or invalid checkpoint;
5. validate each completed phase before advancing;
6. preserve all approved originals and masters;
7. commit durable work using the repository workflow;
8. produce an audit summary showing completed, repaired, pending, blocked, and intentionally skipped items.

This prompt is designed to be **idempotent**: running it repeatedly should converge on the same correct brand system rather than recreate, duplicate, rename, or degrade completed work.

---

# EXECUTION MODE — PROMPTLESS BY DEFAULT

Operate autonomously unless a true brand-approval decision is required.

## Do not ask for confirmation when you can safely determine the answer from:

- the current `master` branch;
- `brand/reference-boards/`;
- protected logo masters;
- authoritative brand documentation;
- existing validated manifests;
- hashes, dimensions, metadata, or file structure;
- prior completed QA evidence;
- deterministic format conversion/export rules.

## Automatically continue after ordinary successes.

Do not stop between phases to ask whether to continue.

## Only stop for user input when at least one of these is true:

1. two different visual masters both appear explicitly approved and there is no authoritative tie-breaker;
2. an element visible on an approval board cannot be reconstructed or extracted faithfully without creative reinterpretation;
3. a protected logo master is missing or corrupted and no verified identical copy exists;
4. a requested production treatment changes the approved visual identity rather than merely adapting it technically;
5. a vendor-specific requirement requires a subjective design compromise that is not already governed;
6. an irreversible destructive action would be required and a safe non-destructive alternative does not exist.

When blocked, finish every unrelated safe task first. Then report the smallest possible decision needed from the user.

---

# CORE PRINCIPLE

LuxSync branding is **not a website asset collection**.

It is a durable omnichannel brand system intended for use across:

- websites and web apps;
- mobile and desktop digital experiences;
- social media;
- email signatures and campaigns;
- presentations;
- video and motion graphics;
- digital advertising;
- business cards;
- letterhead and stationery;
- brochures, guides, flyers, posters, and print collateral;
- signage and environmental graphics;
- packaging;
- apparel and shirts;
- hats and embroidery;
- mugs and drinkware;
- promotional merchandise and swag;
- decals, vinyl, engraving, etching, and laser production;
- screen printing;
- commercial printing;
- future media and channels not yet selected.

The website consumes the brand system. The website does **not** define, limit, or own the brand system.

---

# AUTHORITATIVE SOURCES AND PRECEDENCE

Use this precedence when determining what is approved.

## 1. Protected LuxSync logo masters

Protected logo masters are immutable and always outrank generated, traced, retyped, redrawn, recolored, simplified, or reconstructed versions.

Current protected/source locations must be discovered from the repository rather than hard-coded blindly. Expected governing areas include:

- `brand/source-logo/`
- current approved production logo exports under `brand/assets/logos/`

Never recreate a protected LuxSync logo from a screenshot or reference board if the verified master exists.

## 2. Visual approval archive

`brand/reference-boards/` is the authoritative visual approval archive for approved non-logo brand imagery and design elements.

At the time this prompt was established, the archive included:

- `approved_brand_board.png`
- `buttons_board.png`
- `dividers_board.png`
- `icons_board.png`
- `product_cards_board.png`
- `stationery_board.png`
- `ui_controls_board.png`

Automatically discover additional future files in `brand/reference-boards/` rather than assuming this list will remain exhaustive.

Treat these boards as **approval evidence**, not as final production files to be sliced blindly.

## 3. Authoritative brand rules

Use the current active versions of:

- `brand/README.md`
- `brand/brand-architecture.md`
- `brand/colors.md`
- `brand/typography.md`
- `brand/voice-and-tone.md`
- current production source-of-truth and master catalog

Current known identity baseline includes:

- visual system: LuxSync Production Raster v5 or its later explicitly approved successor;
- design DNA: Plush Drift;
- voice: Intelligent Calm;
- display/UI typography: Manrope 500/600;
- body/supporting UI typography: Inter 400/500;
- official slogan: **Where Luxury Lives Intelligently**.

Current approved palette baseline:

- Slate Navy `#0D1526`
- Dark Suede `#172036`
- Pale Driftwood `#D0BEB0`
- Warm Taupe Mauve `#9E8B85`
- Antique Rose Taupe `#967878`
- Dusty Steel `#7B96B2`
- Champagne Rose Gold Metallic anchor `#D6B0A0`

If a later explicit repository decision supersedes one of these, use the later authoritative decision and document the reconciliation.

## 4. Existing clean production assets

Reuse existing assets that pass visual and technical QA. Do not rebuild good work merely because this prompt was restarted.

## 5. Historical/reference exports

Old numbered crops, board slices, prior generated images, and historical exports may help reconstruct approved art but do not outrank the approval boards or protected masters.

---

# NON-NEGOTIABLE LOGO RULE

Only approved protected LuxSync logo artwork may represent the LuxSync logo.

Never:

- redraw it;
- retype it;
- recolor it without an explicitly approved production variant;
- simplify it casually;
- ask generative AI to recreate it;
- substitute initials or a lookalike monogram;
- treat an AI approximation as a valid master;
- trace a low-resolution screenshot when a protected master exists.

For alternate production techniques such as embroidery, engraving, foil, one-color print, or screen printing, preserve the identity and create a technical production variant only when necessary. Label that variant clearly and retain the original master unchanged.

---

# TARGET OMNICHANNEL LIBRARY ARCHITECTURE

The final system should evolve toward this conceptual structure. Reconcile with existing repository structure instead of destructively forcing a rename if a current equivalent already exists.

```text
brand/
├── masters/
│   ├── logos/
│   ├── icons/
│   ├── ornaments/
│   ├── illustrations/
│   ├── patterns-backgrounds/
│   ├── marketing-art/
│   └── raster-art/
│
├── exports/
│   ├── digital/
│   │   ├── svg/
│   │   ├── png/
│   │   └── webp/
│   ├── print/
│   │   ├── pdf/
│   │   ├── eps/
│   │   └── tiff/
│   ├── merchandise/
│   ├── stationery/
│   ├── email/
│   ├── social/
│   └── video/
│
├── reference-boards/
├── source-logo/
├── audit/
└── manifests/
```

Existing validated `brand/assets/` content may remain as a production-delivery layer if that is the current architecture. Do not perform broad folder migrations merely for cosmetic conformity. Prefer compatibility aliases/documentation or an incremental migration plan.

---

# MASTER FORMAT STRATEGY

Do not force every asset through the same master format.

## True vector artwork

Examples:

- logos when a genuine vector master exists;
- icons;
- dividers;
- ornaments;
- simple badges;
- line art;
- geometric marks;
- certain stationery components;
- merchandise marks.

Preferred production chain:

`AI or genuine vector master → SVG → PDF → EPS → PNG → WebP`

Use AI only when there is an actual Illustrator/editable master or when a faithful vector master is intentionally created and validated. Never claim an embedded raster file is a true editable vector.

## Raster-origin artwork

Examples:

- photography;
- richly textured hero imagery;
- environmental scenes;
- complex raster illustrations;
- photographic marketing compositions;
- artwork whose approved appearance depends on raster texture/effects.

Preferred production chain:

`highest-quality lossless raster master → high-resolution PNG/TIFF → print PDF where appropriate → PNG delivery → WebP delivery`

An SVG may be provided as a **fidelity container** around exact raster artwork when an SVG wrapper is operationally useful, but it must be labeled `embedded-raster-svg` or equivalent. Do not misrepresent it as infinitely scalable vector art.

---

# REQUIRED DELIVERY FORMATS

## Standard digital exports

For every approved asset where technically appropriate:

- SVG
- PNG
- WebP

## Major vector brand artwork

Where appropriate also provide:

- PDF
- EPS
- AI/editable master when a genuine editable master exists or is intentionally created

## Major raster/print artwork

Where appropriate also provide:

- high-resolution PNG
- TIFF
- print-ready PDF

Do not create meaningless format duplicates. Record why a format is omitted.

---

# COLOR AND PRODUCTION VARIANTS

For major brand assets, evaluate and create only the variants that are technically justified.

## Digital

- sRGB full color
- transparent background where appropriate
- dark-background use
- light-background use

## Print

- print-ready PDF
- CMYK-compatible treatment when commercially appropriate
- 300 DPI raster output when raster printing requires it
- bleed-safe layouts for actual print compositions, not isolated logos

## Specialty production

When appropriate:

- one-color black
- one-color white/reversed
- simplified screen-print version
- embroidery-friendly version
- engraving/etching version
- vinyl/cut-line-friendly version
- foil/spot-metallic production artwork

Do not simulate metallic Champagne Rose Gold with a random flat color when a physical metallic production process is intended. Where a print vendor needs spot-color, foil, or metallic-ink specifications, document that production intent separately.

---

# VIDEO / MOTION BRANDING BOUNDARY

The static omnichannel brand system must be motion-ready, but do not create every possible video file during the static brand rebuild.

Prepare static source assets suitable for future motion work:

- genuine vectors where appropriate;
- large transparent PNG exports;
- 4K-capable raster assets for overlays;
- safe-zone guidance for logos and lower-third use.

Future dedicated motion-kit work may include:

- animated logo sting;
- title cards;
- lower thirds;
- transitions;
- end cards;
- transparent alpha-channel video exports;
- Premiere / After Effects templates where supported.

Record these as future outputs rather than fabricating unnecessary motion formats during static asset production.

---

# PHASE MODEL

The process has three major production waves plus an audit bootstrap.

## Phase 0 — Audit and State Detection

Estimated human-equivalent effort: 1.5–2.5 hours.

Tasks:

1. Refresh current `master`.
2. Inventory `brand/reference-boards/`.
3. Inventory protected logo masters.
4. Inventory current `brand/assets/`, current manifests, QA sheets, and related website auth assets.
5. Compare current assets against approved board elements.
6. Identify which approved elements already have valid masters and exports.
7. Identify duplicates, obsolete crops, broken references, missing formats, and stale paths.
8. Classify every approved visual element as one of:
   - protected-logo;
   - true-vector;
   - raster-origin;
   - composition/template;
   - semantic live-UI reference;
   - production-technique variant;
   - approval-board-only reference;
   - blocked-needs-human-decision.
9. Create or update the durable brand manifest and audit state.

Do not render/rebuild an asset until Phase 0 determines whether valid work already exists.

## Wave 1 — Website-Critical Brand Set

Estimated human-equivalent effort after audit: 3–5 hours.

Prioritize assets needed for the first GoDaddy Airo / staging website build while preserving their broader omnichannel usability:

- approved logos;
- core icons;
- dividers and ornaments;
- key decorative elements;
- hero-supporting approved graphics;
- Concierge-supporting graphics;
- account/login supporting graphics;
- primary backgrounds/patterns needed for visual identity;
- core digital variants.

Wave 1 is complete only when its assets are also valid masters for future channels. Do not create website-only dead ends.

## Wave 2 — Broader Digital and Marketing Library

Estimated human-equivalent effort: 5–7 hours.

Include as approved/appropriate:

- social-ready brand elements;
- email-signature components;
- presentation assets;
- video-overlay static assets;
- product-card visual treatments;
- reusable promotional ornaments;
- campaign-support graphics;
- digital marketing compositions and templates that are truly approved.

## Wave 3 — Print and Physical Brand System

Estimated human-equivalent effort: 7–10 hours.

Include as approved/appropriate:

- business-card components;
- stationery and letterhead components;
- print collateral assets;
- high-resolution print exports;
- merchandise marks;
- apparel/shirt assets;
- hat/embroidery variants;
- mug/drinkware variants;
- signage-ready versions;
- one-color and reversed artwork;
- screen-print and engraving variants;
- commercial print PDF/EPS/TIFF outputs;
- physical-production guidance.

Overall expected human-equivalent effort for the complete initial omnichannel rebuild is approximately **15–22 hours**, depending on how much approved artwork needs reconstruction versus clean reuse.

---

# CHECKPOINT / STATE SYSTEM

Maintain durable state so the process can resume after interruption.

Preferred state artifacts:

- `brand/manifests/omnichannel-brand-manifest.json`
- `brand/audit/brand-build-state.json`
- `brand/audit/brand-build-report.md`
- `brand/audit/brand-exceptions.md`

If the repository already has equivalent files under different current paths, reuse and extend them rather than creating duplicate competing manifests.

## Every approved asset record should include, where applicable:

- stable asset ID;
- semantic asset name;
- approval source board(s);
- approval evidence/location;
- master type;
- master path;
- master hash;
- dimensions / viewBox;
- transparency status;
- color space when known;
- production variants;
- export paths;
- export hashes;
- intended channels;
- permitted backgrounds;
- publication status;
- QA status;
- last validated commit;
- notes about embedded raster SVGs or technical compromises;
- dependency relationships;
- blocked reason if incomplete.

## Phase state values

Use explicit states such as:

- `not_started`
- `inventory_complete`
- `in_progress`
- `blocked`
- `qa_failed`
- `complete`
- `complete_with_exceptions`

Never infer completion merely from file existence. Completion requires required QA evidence.

---

# IDEMPOTENCE RULES — PREVENT REWORK

Before creating or converting any asset:

1. search the current manifest for a matching stable asset ID;
2. verify the expected master exists;
3. compare hashes when available;
4. verify required export formats exist;
5. verify current QA state;
6. verify the approval source still exists;
7. verify no later authoritative decision supersedes the asset.

If all checks pass, mark the item `already_complete` and skip production.

Do not regenerate an asset merely to refresh timestamps.

Do not duplicate an asset under a new name when a semantically equivalent validated asset already exists.

Do not downgrade a high-quality master by deriving a new master from a lower-quality export.

Always derive downstream files from the highest-authority/highest-quality master available.

---

# SELF-HEALING RULES

Self-healing means **deterministic repair**, not creative redesign.

## SAFE AUTO-REPAIRS — perform automatically

When objective evidence permits, automatically:

- regenerate a missing PNG/WebP/PDF/EPS/TIFF derivative from a verified master;
- regenerate an SVG export from a verified genuine vector master;
- recreate an embedded-raster SVG fidelity container from the exact approved raster master when that wrapper is intentionally required;
- restore a missing manifest entry from verified files and approval evidence;
- repair stale repository paths after a documented asset migration;
- repair broken internal documentation links;
- rebuild contact sheets / QA sheets from validated assets;
- recompute hashes and dimensions;
- reconcile duplicate exact files by preserving the canonical path and documenting aliases/migrations;
- restore expected directory structure without deleting valid work;
- rerun format validation;
- rerun transparency checks;
- rerun naming validation;
- rerun source-of-truth validation;
- update audit state after successful repair;
- retry a failed deterministic export once when failure appears transient;
- resume an interrupted batch at the first incomplete asset rather than restarting the batch.

## UNSAFE AUTO-REPAIRS — never perform without an authoritative basis

Never automatically:

- redesign approved art;
- redraw or regenerate a protected logo;
- choose between conflicting approved-looking masters with no tie-breaker;
- invent a missing graphic that appears on no approval board;
- change composition because a tool prefers a different crop;
- simplify a logo solely for convenience;
- replace typography inside protected logo artwork;
- alter brand colors because an export tool changes them;
- trace a low-resolution raster into a new vector and silently declare it the new master;
- flatten a genuine editable vector master and make the flattened file authoritative;
- overwrite an approved master with a derivative;
- delete historical approval evidence;
- promote an old malformed board crop to production simply because it exists;
- claim an embedded-raster SVG is a true vector.

If a required repair is unsafe, record it in `brand/audit/brand-exceptions.md`, continue all unrelated safe work, and report it at the end.

---

# REFERENCE-BOARD EXTRACTION RULES

The reference boards are visual approval evidence, not crop grids to be sliced mechanically.

For every visible approved element:

1. identify the intended element boundaries;
2. determine whether a clean equivalent already exists;
3. if a clean equivalent exists and matches the board, reuse it;
4. if no clean equivalent exists, reconstruct/extract the element faithfully;
5. remove board labels, neighboring elements, grid lines, crop artifacts, and presentation-only framing unless those are themselves part of the approved asset;
6. preserve exact approved logos by inserting the verified protected logo master rather than extracting/redrawing it from the board;
7. verify the resulting isolated asset visually against the approval board;
8. record the board name and element location/description as approval evidence in the manifest.

Do not use OCR or automated slicing as the primary method when direct visual analysis is sufficient.

---

# UI CONTROLS, BUTTONS, AND PRODUCT CARDS

Approval boards may contain visual examples of buttons, controls, cards, toggles, or product cards.

Distinguish between:

1. **brand artwork** that should be preserved as an omnichannel asset;
2. **visual design reference** for a live semantic UI component;
3. **marketing composition/template** intended for print/digital collateral.

For website/app implementation, buttons/forms/toggles/cards should normally remain semantic HTML/CSS rather than image screenshots.

However, their approved appearance must still be documented and preserved as brand reference material because the same visual language may influence presentations, video graphics, print collateral, packaging, and campaigns.

Never delete approved board evidence simply because the website uses live CSS instead.

---

# FILE NAMING

Use durable semantic names, not anonymous sequence-only names such as `button_07` or `icon_12`, unless the historical name must be preserved as an alias.

Preferred pattern:

`luxsync-<family>-<semantic-name>-<variant>.<ext>`

Examples:

- `luxsync-logo-orb-fullcolor.png`
- `luxsync-icon-lighting-bulb.svg`
- `luxsync-divider-orbit-03.webp`
- `luxsync-mark-orb-onecolor-white.eps`
- `luxsync-stationery-corner-rose-gold.svg`

Keep names lowercase, hyphenated, stable, and channel-neutral when the artwork itself is channel-neutral.

---

# QA GATES

No asset is complete until the applicable checks pass.

## Visual QA

Verify:

- matches the approved reference board/master;
- no neighboring board fragments;
- no labels accidentally baked in;
- no unintended crop lines;
- no fake or approximated logo;
- approved colors preserved;
- transparency correct;
- edges clean;
- proportions correct;
- metallic treatment consistent with approved visual intent;
- no purple/lavender/orange drift;
- no accidental typography substitution.

## Technical QA

Verify where applicable:

- file opens successfully;
- MIME/extension matches content;
- dimensions/viewBox valid;
- SVG parses;
- PNG transparency works;
- WebP renders;
- PDF/EPS/TIFF exports are non-empty and usable;
- color-space intent documented;
- vector assets do not contain accidental rasterization unless explicitly allowed;
- embedded-raster SVGs are labeled as such;
- hashes recorded;
- duplicate hashes reconciled;
- master is higher or equal quality than derivatives;
- 300 DPI intent is used for raster print deliverables where appropriate;
- no secrets, personal data, prices, mutable product facts, or unsupported claims are baked into generic reusable brand assets.

## Cross-channel QA

For major assets, review suitability for:

- small digital use;
- dark background;
- light background;
- print;
- video overlay;
- merchandise;
- embroidery/screen print if relevant;
- engraving/one-color if relevant.

Do not force one complex full-color asset to serve every physical process. Use intentional production variants where required.

---

# WEBSITE BUILD COORDINATION

The initial GoDaddy Airo website build may proceed once Wave 1 website-critical assets are complete and validated.

Do not wait for all print/merchandise outputs before beginning the website if Wave 1 has passed QA.

Conversely, do not declare the omnichannel brand project complete merely because the first website is generated.

The Airo build prompt is expected under:

`prompts/website/PR-001-LuxSync-Airo-Master-Website-Build-Prompt.md`

The website prompt should consume validated brand assets and current brand rules. It must not redefine or overwrite the omnichannel brand masters.

---

# VERSION CONTROL BEHAVIOR

Before writes:

1. refresh/read current `master`;
2. check whether another branch or recent merge changed the relevant source-of-truth;
3. reconcile against current files rather than using stale remembered paths.

For substantial changes:

- create/use a feature branch;
- make logically grouped commits;
- run available brand/repository validation;
- open a PR when supported;
- merge only after applicable checks pass;
- verify post-merge `master`.

Do not force-push over unrelated work.

Do not delete approved reference boards.

Do not remove valid masters merely because the active website does not use them.

---

# INTERNAL AUDIT / SANITY CHECK MODE

Every invocation begins with an audit, even if the apparent goal is production.

Answer these questions from the repository before producing new art:

1. Are all reference boards present?
2. Are protected logo masters present and intact?
3. Does the current logo delivery library match the protected masters?
4. Which approved board elements already have valid clean masters?
5. Which approved board elements are missing?
6. Which required digital formats are missing?
7. Which print/specialty formats are missing?
8. Are any files duplicated under conflicting names?
9. Are any paths stale after prior migrations?
10. Are any assets marked production-approved without QA evidence?
11. Are any reference-only assets being used as production masters?
12. Are any approved assets being treated as website-only when they should be channel-neutral?
13. Are any format labels misleading, especially raster-in-SVG containers?
14. Are any current brand documents contradicting the approval archive?
15. Did a recent cleanup accidentally remove an approved asset family?
16. Can missing derivatives be deterministically regenerated from a verified master?
17. Is any requested repair subjective enough that it must be escalated rather than auto-healed?

Record the answers in the current brand audit report.

---

# COMPLETION DEFINITION

The initial omnichannel brand rebuild is complete when:

1. every approved visual element visible in the authoritative reference boards has a manifest disposition;
2. every protected logo is preserved exactly;
3. every approved reusable asset has a verified master or an explicit documented reason why it is composition/reference-only;
4. every applicable asset has standard digital exports;
5. major assets have appropriate print/physical-production exports;
6. specialty variants exist where technically required rather than merely desired;
7. website-critical Wave 1 assets pass QA;
8. digital/marketing Wave 2 assets pass QA;
9. print/physical Wave 3 assets pass QA or are explicitly blocked with documented vendor-dependent requirements;
10. all manifests and hashes are current;
11. approval boards remain intact;
12. brand documentation clearly states that the asset library is omnichannel;
13. the website consumes the brand system without redefining it;
14. a clean audit run reports no unresolved objective errors.

---

# FINAL REPORT FORMAT FOR EACH RUN

At the end of each invocation, produce a concise status report with these sections:

## Brand System Status

- current repository commit inspected;
- current phase/wave;
- overall state.

## Already Complete

List validated work skipped to avoid rework.

## Self-Healed

List deterministic repairs performed automatically.

## Newly Completed

List new masters, exports, manifests, QA, or documentation completed during the run.

## Pending

List the next unfinished deterministic tasks.

## Exceptions / Human Decision Required

List only genuine subjective or authority conflicts. If none, say `None`.

## Validation

List tests/checks run and whether they passed.

## Resume Point

State the exact next checkpoint so another run can resume without asking the user what happened previously.

---

# SHORT EXECUTION COMMAND

When this prompt is already installed in the LuxSync repository, the user may simply say:

**Run PR-BRAND-001.**

Interpret that as:

> Load the current `prompts/branding/PR-BRAND-001-LuxSync-Omnichannel-Brand-System-Recovery-Audit.md` from the current repository `master`, execute it in promptless restart-safe self-healing mode, audit before producing, skip validated completed work, repair safe objective inconsistencies automatically, resume from the first incomplete checkpoint, preserve protected masters and approval boards, run applicable validations, and report the exact resume point.

Do not ask the user to paste the prompt again when the repository is accessible.
