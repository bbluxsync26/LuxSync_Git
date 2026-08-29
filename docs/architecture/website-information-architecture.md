# LuxSync Launch Website Information Architecture

**Artifact:** ARC-001  
**Status:** Active / Approved baseline  
**Date:** 2026-08-29  
**Repository:** `bbluxsync26/LuxSync_Git`  
**Governing branch:** `master`

## Purpose

Define the launch information architecture for LuxSync using the current repository as the source of truth.

This architecture is derived from:

- `README.md`
- `docs/business-plan.md`
- `docs/value-proposition.md`
- `docs/3-month-cookbook.md`
- `brand/README.md`
- `brand/colors.md`
- `brand/typography.md`
- `brand/voice-and-tone.md`
- `content/homepage.md`
- `content/about.md`
- `website/pages/home.md`
- `website/styles/design-system.md`
- `brand/assets/asset-manifest.csv`

Where older generated assets conflict with active brand standards, Manrope and Inter are authoritative.

---

## Launch Objective

The launch website is a **commerce-first luxury smart-home storefront**.

It must help a visitor quickly understand:

1. What LuxSync sells.
2. Why LuxSync curates products rather than presenting an overwhelming electronics catalog.
3. Which solutions fit the visitor's needs.
4. Why SmartThings compatibility matters.
5. How to shop curated collections and standalone products.
6. Where to get guidance and support.

The launch site is **not** primarily a consulting-services brochure and is **not** a software/SaaS site.

---

## Primary Navigation

```text
LuxSync
├── Home
├── Shop
├── Solutions
├── Guides
├── About
└── Support
```

Commerce utilities remain visible independently of the primary navigation:

```text
Search | Account | Cart
```

Keep the primary navigation compact. Do not expose every product category at the top level.

---

## 1. Home

**Purpose:** Establish LuxSync, communicate the curated-commerce value proposition, and move customers into product collections or relevant solutions.

### Required homepage sequence

1. **Hero**
   - Brand: LuxSync
   - Official slogan: **Where Luxury Lives Intelligently**
   - Hero message: **Technology That Feels Like Home**
   - Supporting copy from `content/homepage.md`
   - Primary CTA: **Shop Collections**
   - Secondary CTA: **Explore Solutions**

2. **Featured Solutions**
   - Short-Term Rentals
   - Seniors & Caregivers
   - Smart Office & Property Management
   - Intentional Parents
   - Busy Professionals

3. **Why LuxSync**
   - Curated Catalog
   - SmartThings Compatibility
   - Simplified Buying
   - Premium Customer Experience

4. **Product Collections**
   - Comfort
   - Security
   - Energy
   - Hosting
   - Curated Bundles

5. **How It Works**
   - Discover the need
   - Choose a curated collection or product
   - Follow guided setup and compatibility guidance
   - Expand the experience over time

6. **Featured Products / Bundles**
   - Product data must come from validated commerce catalog data.
   - Do not hard-code unverified availability or pricing.

7. **Lead Magnet / Email Signup**
   - STR Smart Home ROI Guide when ready
   - General LuxSync updates / educational content

8. **Footer**
   - Shop
   - Solutions
   - Guides
   - About
   - Support / Contact
   - Privacy / Terms placeholders until approved legal copy exists

---

## 2. Shop

**Purpose:** Primary commerce destination.

### Shop landing page

Provide a curated path into the catalog instead of presenting an undifferentiated product wall.

### Shop structure

```text
Shop
├── All Products
├── Curated Bundles
├── Comfort
├── Security
├── Energy
└── Hosting
```

The repository's current brand asset library already contains category cards for Comfort, Security, Energy, and Hosting.

### Product families represented in the current business plan

- Smart Hubs & Core
- Smart Locks
- Smart Lighting & Decorative Lighting
- Smart Shades
- Smart Speakers
- Smart Appliances
- Security Devices
- Water Management Systems
- Home Entertainment Products

Product merchandising may place individual products into one or more customer-facing collections when the commerce platform supports it.

### Curated bundles represented in the current repository

- STR Property Automation
- Guest Welcome & Keyless Entry
- Smart Sleep Nursery
- Senior Independent Safety

Do not expose internal margins, projected profitability, supplier costs, or founder financial targets.

---

## 3. Solutions

**Purpose:** Let customers begin with an outcome or life situation rather than a device specification.

```text
Solutions
├── Short-Term Rentals
├── Seniors & Caregivers
├── Smart Office & Property Management
├── Intentional Parents
└── Busy Professionals
```

Each solution page should use this structure:

1. Customer need
2. Desired experience/outcome
3. Relevant LuxSync collections or products
4. Example automations or routines
5. SmartThings compatibility explanation
6. CTA to shop or get guidance

### Guardrails

- Do not imply Airbnb, VRBO, Samsung, or other third-party endorsement unless documented.
- Do not make medical claims for senior/caregiver solutions.
- Do not represent future LuxSync Grid capabilities as currently available.
- Do not publish unresolved subscription pricing.

---

## 4. Guides

**Purpose:** Education, trust, lead generation, and self-service support.

### Launch content

- STR Smart Home ROI Guide
- Compatibility guidance
- SmartThings setup concepts
- Product selection guidance
- Automation ideas
- Frequently asked questions

### Future content

- Digital setup guides
- SmartThings template guidance after Month 2 launch
- LuxSync Grid documentation only after the product is released

---

## 5. About

**Purpose:** Explain why LuxSync exists and how it approaches smart living.

Use `content/about.md`, the mission in `README.md`, and the repository-defined business model.

Core themes:

- Luxury is confidence, not complexity.
- Trusted curation.
- Thoughtful automation.
- Premium design.
- Simplicity and reliability.

Founder details may be used only where the current repository explicitly supports them.

---

## 6. Support

**Purpose:** Give customers an obvious path to help without making the site feel service-heavy.

Launch functions:

- Contact LuxSync
- Product / compatibility questions
- Order support
- Setup guidance
- FAQ
- AI receptionist contact path when approved for public display

---

## Commerce Utilities

### Search

Search products, collections, guides, and solution pages where supported by the platform.

### Account

Use the commerce platform's native customer-account capability where available.

### Cart

Use the commerce platform's native cart and checkout flow. Do not create a decorative duplicate cart disconnected from the system of record.

---

## Homepage UX Priorities

1. Brand and value proposition before specifications.
2. Commerce action visible above the fold.
3. Outcome-oriented solution paths before long product grids.
4. Curated choice rather than endless choice.
5. Mobile-first shopping behavior.
6. Accessibility and performance from the first build.

---

## Brand Implementation Rules

### Palette: Plush Drift v2.1

- Slate Navy `#0D1526`
- Dark Suede `#172036`
- Pale Driftwood `#D0BEB0`
- Warm Taupe Mauve `#9E8B85`
- Antique Rose Taupe `#967878`
- Dusty Steel `#7B96B2`

### Typography

- Headings / display: **Manrope 500/600**
- Body / UI: **Inter 400/500**

### Voice

**Intelligent Calm**

Warm, confident, thoughtful, unhurried, professional.

### Brand pillars

- Tactile Luxury
- Intelligent Calm
- Warm Futurism
- Effortless Sophistication

---

## Responsive Architecture

### Desktop

- Strong editorial hero
- Curated collection grids
- Controlled content width
- Persistent but restrained commerce utilities

### Tablet

- Two-column collection / solution layouts where space allows
- Simplified navigation

### Mobile

- Compact navigation
- Search/cart immediately accessible
- One-column content flow
- Large tap targets
- Product cards optimized for thumb use
- Avoid desktop layouts merely scaled down

---

## Accessibility Baseline

Target WCAG 2.2 AA practices:

- Semantic heading order
- Keyboard navigation
- Visible focus states
- Sufficient text/background contrast
- Descriptive alt text
- Accessible form labels
- Adequate touch-target sizing
- Reduced-motion treatment for decorative animation
- No information communicated by color alone

---

## Performance Baseline

- Prefer SVG for logos and interface icons.
- Prefer WebP for large raster graphics where appropriate.
- Use responsive images.
- Lazy-load non-critical imagery.
- Keep decorative effects restrained.
- Avoid unnecessary JavaScript.
- Prevent layout shifts by reserving image dimensions.

---

## Future Expansion Slots

The IA must allow later addition of:

- SmartThings automation templates
- LuxSync Grid SaaS dashboard
- Elite integration / architecture services

These are roadmap items and must not be shown as currently available until the governing repository says they are live.

---

## Launch Acceptance Test

A first-time visitor should be able to answer these questions within a short visit:

- What is LuxSync?
- What can I buy here?
- Why are these products different from a generic electronics store?
- Which solution applies to me?
- How do I shop?
- How do I get help?

If the site cannot answer those questions clearly, the information architecture has failed.