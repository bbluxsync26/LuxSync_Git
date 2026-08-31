# LuxSync Launch Website Information Architecture

**Artifact:** ARC-001  
**Status:** Active / Approved baseline  
**Last updated:** 2026-08-31  
**Repository:** `bbluxsync26/LuxSync_Git`  
**Governing branch:** `master`

## Purpose

Define the launch information architecture for LuxSync using the repository as the source of truth.

Governing references include `brand/README.md`, `brand/colors.md`, `brand/typography.md`, `brand/voice-and-tone.md`, `website/styles/design-system.md`, `website/pages/home.md`, `website/pages/contact.md`, `content/product-catalog.md`, and `docs/architecture/intelligent-living-concierge.md`.

Where older generated assets or guidance conflict, **LuxSync v3**, Plush Drift design DNA, the current approved asset library, Manrope/Inter typography, and current page/architecture blueprints govern.

## Launch Objective

The launch website is a **commerce-first premium intelligent-living storefront with guided discovery as a flagship journey**.

A visitor should quickly understand what LuxSync offers, why the catalog is curated, how **Find My LuxSync Solution** can create a personalized **My LuxSync Blueprint**, why SmartThings compatibility matters, how to shop, and where to get help.

## Primary Navigation

```text
LuxSync
├── Home
├── Shop
├── Solutions
├── Guides
├── About
├── Contact
└── Support
```

Commerce utilities remain independently visible:

```text
Search | Account | Cart
```

On compact/mobile navigation, Contact and Support may be grouped carefully if needed, but both destinations must remain obvious.

## Home

Required sequence:

1. **Hero**
   - Official slogan / hero line: **Where Luxury Lives Intelligently**
   - Supporting copy: premium smart-home technology, curated hardware, and thoughtful automation for modern living
   - Primary CTA: **Find My LuxSync Solution**
   - Secondary CTA: **Shop Smart Home**
   - Supporting CTA: **Get the ROI Guide**
2. **Featured Solutions** — Short-Term Rentals; Seniors & Caregivers / Accessible Living; Smart Office & Property Management; Intentional Parents; Busy Professionals
3. **Why LuxSync** — Curated Catalog; SmartThings Compatibility; Intelligent Discovery; Simplified Buying; Premium Customer Experience
4. **Find My LuxSync Solution** — flagship Intelligent Living Concierge with Blueprint output
5. **Product Collections** — current categories from `content/product-catalog.md`
6. **How It Works** — Discover; Design; Choose; Evolve
7. **Featured Products / Bundles** — validated commerce data only; solution concepts clearly labeled
8. **Meet the Founders** — compact approved profiles for Bridgette Beardsley and Sheldon Bardol
9. **FAQ Preview** — six canonical questions with a View All FAQs link
10. **Contact / Support Gateway**
11. **Lead Magnet / Email Signup** — STR Smart Home ROI Guide when ready
12. **Footer**

## Find My LuxSync Solution

This is a primary website journey, governed by `docs/architecture/intelligent-living-concierge.md` and `website/src/concierge/`.

Customer-facing naming:

- Entry point: **Find My LuxSync Solution**
- Experience: **LuxSync Intelligent Living Concierge**
- Output: **My LuxSync Blueprint**

The journey follows:

**Lifestyle → Experience → Intelligence → Technology**

It should capture property profile, approximate square footage, existing technology, desired outcomes, routines, pain points, priorities, and implementation preference. It should return recommended LuxSync Experiences, foundation, compatibility notes, implementation path, phased roadmap, and next best action.

Do not implement it as a novelty quiz or require customers to understand protocols before receiving value.

## Shop

```text
Shop
├── All Products
├── Curated Bundles
├── Foundation & Connectivity
├── Entry & Access
├── Lighting & Ambience
├── Comfort & Climate
├── Property Awareness
├── Water Protection
├── Energy & Power
├── Entertainment
└── Hosting / STR
```

Canonical planning catalog: `content/product-catalog.md`.

Exact public product names, prices, stock, compatibility, shipping, and availability require validated Commerce Plus/manufacturer data.

Concierge-generated LuxSync Experiences are solution concepts unless/until mapped to validated live products or bundles.

## Solutions

```text
Solutions
├── Short-Term Rentals
├── Seniors & Caregivers / Accessible Living
├── Smart Office & Property Management
├── Intentional Parents
└── Busy Professionals
```

Each solution page should cover the customer need, desired outcome, relevant LuxSync Experiences, collections/products, SmartThings compatibility, and a Concierge/shop/guidance CTA.

Do not imply third-party endorsement, make medical claims, expose unresolved pricing, or present roadmap capabilities as live.

## Guides

Launch content includes the STR Smart Home ROI Guide, compatibility guidance, SmartThings setup concepts, product-selection guidance, automation ideas, FAQ content, and future Experience-specific setup guidance.

The FAQ page follows `website/pages/faqs.md` and `content/faqs.md`.

Future downloadable SmartThings automation templates and LuxSync Grid documentation appear only after those products are explicitly released.

## About

Follow `website/pages/about.md` and `content/about.md`.

Approved leadership identities:

- **Bridgette Beardsley — Co-Founder & Chief Technology and Strategy Officer**
- **Sheldon Bardol — Co-Founder & Chief Customer and Operations Officer**

Full biography sources are `docs/leadership/bridgette-beardsley.md` and `docs/leadership/sheldon-bardol.md`.

Do not invent founder facts, awards, years in business, certifications, testimonials, press, or customer counts.

## Contact

The dedicated Contact page is governed by `website/pages/contact.md` and `content/contact.md`.

Initial branch choices:

- Support
- Product Information
- Consultation
- General Question
- Business / Partnership
- Other

The form uses adaptive conditional logic and the same conceptual Property Profile as the Concierge, including property type and approximate square footage.

When technically and legally appropriate, visitors coming from My LuxSync Blueprint should have relevant property/Blueprint context prepopulated.

Routing:

- Support → `support@luxsync.net`
- Product Information / Consultation / General Question / Business-Partnership / Other → `info@luxsync.net`

## Support

Support remains a clear pathway for existing products, orders, setup, compatibility, SmartThings connection, troubleshooting, and related questions.

The Support path may launch the Contact form preselected to **Support**.

## Commerce Utilities

- **Search:** products, collections, guides, Experiences, and solution pages where supported.
- **Account:** native commerce-platform customer-account capability where available.
- **Cart:** native cart/checkout; never a decorative duplicate disconnected from the commerce system of record.

## Brand Implementation Rules

### Official slogan

**Where Luxury Lives Intelligently**

This is the sole approved public slogan/hero line. Retired alternate slogan/hero treatments must not be generated or restored.

### Palette

- Slate Navy `#0D1526`
- Dark Suede `#172036`
- Pale Driftwood `#D0BEB0`
- Warm Taupe Mauve `#9E8B85`
- Antique Rose Taupe `#967878`
- Dusty Steel `#7B96B2`
- Champagne Rose Gold Metallic `#D6B0A0` anchor

### Typography

- Headings / display / navigation / CTA labels / graphic UI: **Manrope 500/600**
- Body / product copy / forms / supporting UI: **Inter 400/500**

Approved exact logo artwork may preserve its own lettering as artwork and does not redefine site typography.

### Voice

**Intelligent Calm:** warm, confident, thoughtful, unhurried, professional, and human.

### Visual character

Use LuxSync v3 with Plush Drift tactile illumination: deep Slate Navy/Dark Suede surfaces, restrained Champagne Rose Gold Metallic detail, Dusty Steel interaction states, Pale Driftwood copy, spacious composition, controlled lighting, and premium imagery.

Avoid cyberpunk neon, unapproved lavender/purple base treatments, loud gradients, dense gadget-store grids, generic SaaS blue, excessive glassmorphism, and unnecessary motion.

## Responsive Architecture

- **Desktop:** editorial hero, controlled width, strong Concierge feature, curated grids, restrained commerce utilities.
- **Tablet:** reduced columns while preserving hierarchy.
- **Mobile:** compact navigation, immediate search/cart access, one-column flow, large touch targets, readable Manrope/Inter typography, and thumb-friendly Concierge choices/product cards.

## Accessibility Baseline

Target WCAG 2.2 AA practices: semantic headings, keyboard navigation, visible focus, sufficient contrast, descriptive alt text, accessible labels, adequate touch targets, reduced-motion treatment, and no color-only meaning.

Adaptive Contact and Concierge forms must expose field labels, required state, errors, and conditional changes accessibly.

## Performance Baseline

Prefer approved SVG/raster logos as appropriate, SVG for icons/vector UI, optimized WebP for production scenes, responsive images, lazy loading, reserved image dimensions, efficient font loading, restrained effects, and minimal unnecessary JavaScript.

## Future Expansion Slots

Allow for saved Blueprints, customer accounts, deeper product mapping, room-by-room planning, natural-language Concierge input, SmartThings automation templates, LuxSync Grid, and approved architecture services without advertising unreleased capabilities as live.

## Launch Acceptance Test

A first-time visitor should quickly answer:

- What is LuxSync?
- What can I buy?
- What could my space do?
- How does Find My LuxSync Solution help me decide?
- Why is LuxSync different from a generic electronics store?
- How do I shop?
- How do I ask a question or request a consultation?
- How do I get support?
