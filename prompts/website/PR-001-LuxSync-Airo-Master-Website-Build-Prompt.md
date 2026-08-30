# PR-001 — LuxSync Airo Master Website Build Prompt

**Status:** Draft / Ready for first Airo generation  
**Updated:** 2026-08-30  
**Purpose:** Generate the LuxSync launch storefront in GoDaddy Airo AI Builder while preserving the repository source of truth and Commerce Plus production boundary.

## Prompt to paste into GoDaddy Airo AI Builder

Build a polished, mobile-first luxury smart-home storefront for **LuxSync LLC**.

This is a **staging/reference build**. Do not connect live payments, production DNS, or publish it as the production commerce site during the first generation pass.

The LuxSync GitHub repository is the source of truth. Do not invent a different business model, target audience, visual identity, product strategy, pricing model, technology ecosystem, or company history.

### Company and positioning

LuxSync is a luxury smart-home automation and commerce company launching with a retail-first, zero-inventory curated-commerce model.

LuxSync helps customers create smarter, safer, more elegant environments through carefully selected SmartThings-compatible products, curated bundles, thoughtful automation guidance, and a premium customer experience.

LuxSync is not a discount electronics retailer, generic DIY marketplace, traditional on-site installer, or software-first startup. The experience should feel like luxury interior design with intelligent technology quietly underneath it.

### Official brand language

- Company: **LuxSync**
- Official slogan: **Where Luxury Lives Intelligently**
- Homepage hero: **Smart Living. Elevated.**
- Supporting copy: **Luxury smart-home technology designed for modern living, with curated hardware and thoughtful automation that bring comfort, control, and confidence to every space.**
- Primary CTA: **Shop Smart Home**
- Secondary CTA: **Get the ROI Guide**

Do not replace these with older LuxSync slogan, hero, or CTA treatments.

### Primary audiences

1. **Short-Term Rental Operators** — remote property awareness, keyless entry, guest experience, and operational efficiency.
2. **Seniors & Caregivers** — independent-living support, home awareness, leak detection, pathway lighting, and caregiver notifications. Do not make medical claims.
3. **Smart Office & Property Managers** — centralized oversight of lighting, HVAC, security, and multi-property environments.
4. **Intentional Parents** — sleep routines, smart nursery environments, household comfort, and safety-focused automation.
5. **Busy Professionals** — convenience, premium experiences, elegant technology, and simplicity.

Do not add unsupported target segments.

### Navigation

Primary: Home; Shop; Solutions; Guides; About; Support.

Keep Search, Account, and Cart separate and easy to reach. Do not create an oversized top navigation.

### Homepage sequence

1. Hero with the exact slogan, hero message, supporting copy, and CTAs above.
2. Featured Solutions for the five approved audiences.
3. Why LuxSync: Curated Catalog; SmartThings Compatibility; Simplified Buying; Premium Customer Experience.
4. Product Collections: Comfort; Security; Energy; Hosting; Curated Bundles.
5. How It Works: Discover; Choose; Set Up; Evolve.
6. Featured Products/Bundles using validated catalog data or clearly editable placeholders.
7. STR Smart Home ROI Guide and calm email signup.
8. Footer with Shop, Solutions, Guides, About, Support/Contact, and legal placeholders.

### Shop

Create a curated Shop landing page with All Products, Curated Bundles, Comfort, Security, Energy, and Hosting.

Product families may include smart hubs, locks, lighting, shades, speakers, appliances, security devices, water management, and home entertainment.

Bundle concepts include STR Property Automation, Guest Welcome & Keyless Entry, Smart Sleep Nursery, and Senior Independent Safety.

Do not invent prices, stock, ratings, reviews, scarcity, supplier relationships, margins, costs, or financial projections.

### Solutions

Create pages for the five approved audiences. Each page should cover the need, desired outcome, relevant products/collections, example routines, SmartThings compatibility, and a shop/guidance CTA.

Do not imply Samsung, SmartThings, Airbnb, VRBO, or other endorsement unless later documented.

### Guides

Create space for the STR Smart Home ROI Guide, compatibility guidance, SmartThings setup concepts, product-selection guidance, automation ideas, and FAQs.

Do not present SmartThings templates or LuxSync Grid as currently available.

### About and Support

About should emphasize trusted curation, thoughtful automation, premium design, simplicity, and reliability. Luxury is confidence, not complexity.

Support should cover product/compatibility questions, order support, setup guidance, FAQ, and general contact without making the site feel service-heavy.

Do not invent awards, certifications, testimonials, press, customer counts, years in business, or founder facts.

### Technology and commerce boundary

Samsung SmartThings is the primary launch compatibility standard. Emphasize compatibility before customization, simplicity before complexity, reliability before novelty, and customer experience before technology.

GoDaddy Commerce Plus remains the production commerce system of record. Represent storefront UX in staging, but do not connect live payments, alter production DNS, replace Commerce Plus, or create a second unmanaged live catalog.

### Luxury Orbit visual system

Use **Luxury Orbit**, which replaces the older Plush Drift direction for current website work.

Colors:

- Deep Navy `#0B1D3A` — primary dark canvas
- Midnight Blue `#172846` — elevated surfaces
- Pale Blush `#F3ECE8` — warm light surfaces and primary light text
- Taupe `#A69A8E` — secondary neutral
- Dusty Rose `#E7B5B8` — warm atmospheric accent
- Soft Powder Blue `#A6B9CE` — restrained orbit/glow accent
- Rose Gold base `#D6B0A0` — metallic CTA, line, rim, and logo accent using champagne/copper highlights and shadows

Typography:

- Wordmark/editorial: `Bodoni Moda`, `Bodoni MT`, Didot, Georgia, serif
- Headings/navigation/UI: `Century Gothic`, Montserrat, Arial, sans-serif
- Body/supporting UI: Candara, Inter, `Segoe UI`, Arial, sans-serif

Visual direction:

- Deep architectural navy
- Warm rose-gold metal
- Soft powder-blue orbit light
- Pale blush copy and surfaces
- Premium smart-living/interior imagery
- Spacious editorial composition
- Refined rounded dark cards
- Selective atmospheric glow
- Minimal organic motion

Avoid cyberpunk neon, saturated cyan/magenta, loud gradients, generic SaaS blue, dense gadget-store grids, cartoon UI, excessive glassmorphism, hard glowing borders, flashing animation, aggressive popups, and text baked into photographs when native text is possible.

### Voice

Use **Intelligent Calm**: warm, confident, thoughtful, unhurried, professional, human, refined, and approachable.

Avoid hype, fear-based security language, jargon, technical showing-off, urgency, excessive exclamation marks, and unsupported superlatives.

### Responsive, accessibility, and performance

Design mobile first. Mobile uses compact navigation, accessible search/cart, large touch targets, readable type, scannable sections, and thumb-friendly product cards. Tablet reduces columns; desktop may use wider editorial layouts.

Target WCAG 2.2 AA practices: semantic headings, keyboard access, visible focus, sufficient contrast, labels, meaningful alt text, adequate targets, reduced-motion behavior, and no color-only meaning.

Use responsive images, modern formats, lazy loading, stable layouts, efficient font loading, minimal unnecessary JavaScript, and restrained effects.

### Repository assets

Prefer current assets beneath `brand/assets/`, including the brand, website-icon, component, card, illustration, product-card, and banner folders. Prefer SVG for logos/icons and optimized WebP for larger imagery.

The current SVG masters are generated from the repository's Luxury Orbit asset generator. Do not recreate them through an image generator unless a photographic/interior scene is intentionally required.

### Future roadmap

Leave clean expansion points for SmartThings automation templates, LuxSync Grid, and elite architecture services. Do not advertise them as live.

### Final quality standard

A first-time visitor should quickly understand that LuxSync is a premium curated smart-home commerce brand; products and bundles are selected to work together; SmartThings compatibility reduces complexity; shopping is intentionally curated; the technology belongs in a beautifully designed home or property; and customers can shop without becoming smart-home experts.

Every important design, content, and commerce decision should reinforce:

**Where Luxury Lives Intelligently.**
