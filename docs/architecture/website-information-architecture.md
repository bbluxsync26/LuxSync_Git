# LuxSync Launch Website Information Architecture

**Artifact:** ARC-001  
**Status:** Active / Approved baseline  
**Last updated:** 2026-08-31
**Repository:** `bbluxsync26/LuxSync_Git`  
**Governing branch:** `master`

## Purpose

Define the launch information architecture for LuxSync using the repository as the source of truth.

Current governing references include `brand/README.md`, `brand/colors.md`, `brand/typography.md`, `brand/voice-and-tone.md`, `website/pages/home.md`, and `website/styles/design-system.md`.

Where older generated assets or guidance conflict, the authoritative **Plush Drift v2.1** base system, active **Luxury Orbit** web treatment, Manrope/Inter typography contract, and current homepage blueprint govern.

## Launch Objective

The launch website is a **commerce-first luxury smart-home storefront**. It is not primarily a consulting brochure or a software/SaaS site.

A visitor should quickly understand what LuxSync sells, why the catalog is curated, which solution fits, why SmartThings compatibility matters, how to shop, and where to get help.

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

Commerce utilities remain independently visible:

```text
Search | Account | Cart
```

## Home

Required sequence:

1. **Hero**
   - Official slogan: **Where Luxury Lives Intelligently**
   - Hero message: **Smart Living. Elevated.**
   - Supporting copy: **Luxury smart-home technology designed for modern living, with curated hardware and thoughtful automation that bring comfort, control, and confidence to every space.**
   - Primary CTA: **Shop Smart Home**
   - Secondary CTA: **Get the ROI Guide**
2. **Featured Solutions** — Short-Term Rentals; Seniors & Caregivers; Smart Office & Property Management; Intentional Parents; Busy Professionals
3. **Why LuxSync** — Curated Catalog; SmartThings Compatibility; Simplified Buying; Premium Customer Experience
4. **Product Collections** — Comfort; Security; Energy; Hosting; Curated Bundles
5. **How It Works** — Discover; Choose; Set Up; Evolve
6. **Featured Products / Bundles** — validated commerce data only; editable placeholders during design
7. **Lead Magnet / Email Signup** — STR Smart Home ROI Guide when ready
8. **Footer** — Shop; Solutions; Guides; About; Support/Contact; legal placeholders

## Shop

```text
Shop
├── All Products
├── Curated Bundles
├── Comfort
├── Security
├── Energy
└── Hosting
```

Current product families include smart hubs, locks, lighting, shades, speakers, appliances, security devices, water management, and home entertainment.

Current bundle concepts include STR Property Automation, Guest Welcome & Keyless Entry, Smart Sleep Nursery, and Senior Independent Safety.

Do not expose supplier costs, margins, projections, or unvalidated prices/availability.

## Solutions

```text
Solutions
├── Short-Term Rentals
├── Seniors & Caregivers
├── Smart Office & Property Management
├── Intentional Parents
└── Busy Professionals
```

Each solution page should cover the customer need, desired outcome, relevant collections/products, example routines, SmartThings compatibility, and a shop/guidance CTA.

Do not imply third-party endorsement, make medical claims, expose unresolved pricing, or present roadmap capabilities as live.

## Guides

Launch content includes the STR Smart Home ROI Guide, compatibility guidance, SmartThings setup concepts, product-selection guidance, automation ideas, and FAQs.

Future SmartThings templates and LuxSync Grid documentation appear only after those products are released.

## About

Explain LuxSync through trusted curation, thoughtful automation, premium design, simplicity, and reliability. Luxury is confidence, not complexity.

Do not invent founder facts, awards, years in business, certifications, testimonials, press, or customer counts.

## Support

Provide contact, product/compatibility questions, order support, setup guidance, and FAQs without making the site feel service-heavy.

## Commerce Utilities

- **Search:** products, collections, guides, and solution pages where supported.
- **Account:** native commerce-platform customer-account capability where available.
- **Cart:** native cart/checkout; never a decorative duplicate disconnected from the commerce system of record.

## Brand Implementation Rules

### Base palette — Plush Drift v2.1

- Slate Navy `#0D1526`
- Dark Suede `#172036`
- Pale Driftwood `#D0BEB0`
- Warm Taupe Mauve `#9E8B85`
- Antique Rose Taupe `#967878`
- Dusty Steel `#7B96B2`
- Champagne Rose Gold Metallic `#D6B0A0` anchor

### Luxury Orbit treatment

Use the approved Champagne Rose Gold Metallic gradient, Dusty Steel-derived orbit light, spacious dark composition, soft architectural curves, and premium smart-living imagery. Metallic highlight/shadow stops and orbit tints are rendering effects, not additional standalone colors.

### Typography

- Headings / display / navigation / CTA labels / graphic UI: **Manrope 500/600**
- Body / product copy / forms / supporting UI: **Inter 400/500**

Approved exact logo artwork may preserve its own lettering as artwork and does not redefine site typography.

### Voice

**Intelligent Calm:** warm, confident, thoughtful, unhurried, professional, and human.

### Visual character

Deep Slate Navy/Dark Suede surfaces, restrained Champagne Rose Gold Metallic detail, Dusty Steel orbit light, Pale Driftwood copy, spacious composition, restrained atmospheric glow, and premium smart-living imagery.

Avoid cyberpunk neon, lavender as an unapproved base color, loud gradients, dense gadget-store grids, generic SaaS blue, excessive glassmorphism, and unnecessary motion.

## Responsive Architecture

- **Desktop:** editorial hero, controlled width, curated grids, restrained commerce utilities.
- **Tablet:** reduced columns and simplified navigation while preserving hierarchy.
- **Mobile:** compact navigation, immediate search/cart access, one-column flow, large touch targets, readable Manrope/Inter typography, and thumb-friendly product cards.

## Accessibility Baseline

Target WCAG 2.2 AA practices: semantic headings, keyboard navigation, visible focus, sufficient contrast, descriptive alt text, accessible labels, adequate touch targets, reduced-motion treatment, and no color-only meaning.

## Performance Baseline

Prefer approved SVG/raster logos as appropriate, SVG for icons/vector UI, optimized WebP for production scenes, responsive images, lazy loading, reserved image dimensions, efficient font loading, restrained effects, and minimal unnecessary JavaScript.

## Future Expansion Slots

Allow for SmartThings automation templates, LuxSync Grid, and elite architecture services without advertising them as currently available.

## Launch Acceptance Test

A first-time visitor should quickly answer:

- What is LuxSync?
- What can I buy?
- Why is this different from a generic electronics store?
- Which solution applies to me?
- How do I shop?
- How do I get help?
