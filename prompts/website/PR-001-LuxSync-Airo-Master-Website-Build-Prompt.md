# PR-001 — LuxSync Airo Master Website Build Prompt

**Status:** Draft / Ready for first Airo generation after repository consistency validation  
**Updated:** 2026-08-31
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
5. Find My LuxSync Solution: a premium outcome-first guided recommendation path.
6. How It Works: Discover; Choose; Set Up; Evolve.
7. Featured Products/Bundles using validated catalog data or clearly editable placeholders.
8. Meet the Founders using the approved compact biographies and exact titles.
9. Frequently Asked Questions preview using the six approved homepage questions.
10. STR Smart Home ROI Guide and calm email signup.
11. Footer with Shop, Solutions, Guides, About, Support/Contact, and legal placeholders.

### Shop

Create a curated Shop landing page with All Products, Curated Bundles, Comfort, Security, Energy, and Hosting.

Product families may include smart hubs, locks, lighting, shades, speakers, appliances, security devices, water management, and home entertainment.

Bundle concepts include STR Property Automation, Guest Welcome & Keyless Entry, Smart Sleep Nursery, and Senior Independent Safety.

Do not invent prices, stock, ratings, reviews, scarcity, supplier relationships, margins, costs, or financial projections.

### Solutions

Create pages for the five approved audiences. Each page should cover the need, desired outcome, relevant products/collections, example routines, SmartThings compatibility, and a shop/guidance CTA.

Do not imply Samsung, SmartThings, Airbnb, VRBO, or other endorsement unless later documented.

### Guides

Create space for the STR Smart Home ROI Guide, compatibility guidance, SmartThings setup concepts, product-selection guidance, automation ideas, and a dedicated FAQ page at `/guides/faqs`.

Build the FAQ page from `content/faqs.md` and `website/pages/faqs.md`. Use the approved categories, accessible accordion behavior, stable question links, optional lightweight search, FAQPage structured data limited to visibly rendered answers, and calm pathways to Find My LuxSync Solution, shopping, information, or support. Do not invent or materially rewrite FAQ answers.

Do not present SmartThings templates or LuxSync Grid as currently available.

### About and Support

About must follow `content/about.md` and `website/pages/about.md`. Emphasize trusted curation, thoughtful automation, premium design, simplicity, and reliability. Luxury is confidence, not complexity.

Use these exact leadership identities and the approved Compact Biographies from `docs/leadership/`:

- **Bridgette Beardsley — Co-Founder & Chief Technology and Strategy Officer**
- **Sheldon Bardol — Co-Founder & Chief Customer and Operations Officer**

Give both profiles equal visual authority. Do not generate photographic likenesses; use approved portraits only when supplied, otherwise use a refined branded placeholder or monogram treatment.

Support should cover product/compatibility questions, order support, setup guidance, FAQ, and general contact without making the site feel service-heavy. Route general information to `info@luxsync.net` and existing-order/product support to `support@luxsync.net`.

Do not invent awards, certifications, testimonials, press, customer counts, years in business, or founder facts.

### Technology and commerce boundary

Samsung SmartThings is the primary launch compatibility standard. Emphasize compatibility before customization, simplicity before complexity, reliability before novelty, and customer experience before technology.

GoDaddy Commerce Plus remains the production commerce system of record. Represent storefront UX in staging, but do not connect live payments, alter production DNS, replace Commerce Plus, or create a second unmanaged live catalog.

### LuxSync v3 brand system

Use **LuxSync v3** as the authoritative website, ecommerce, and branded-graphics system. New visual work must use `brand/assets-v3/`. The prior generated Luxury Orbit library is legacy compatibility content and must not be used for new website design.

Base colors:

- Slate Navy `#0D1526`
- Dark Suede `#172036`
- Pale Driftwood `#D0BEB0`
- Warm Taupe Mauve `#9E8B85`
- Antique Rose Taupe `#967878`
- Dusty Steel `#7B96B2`
- Champagne Rose Gold Metallic `#D6B0A0` anchor

Use Champagne Rose Gold Metallic sparingly for premium detail and Dusty Steel for clear interactive states. Keep effects controlled, crisp, and architectural.

Typography:

- **Headings / display / navigation / CTA labels / graphic UI:** Manrope 500/600
- **Body / product copy / forms / supporting UI:** Inter 400/500

Do not use Century Gothic, Candara, Montserrat, Bodoni-family, Didot, or Georgia as website-system fonts.

Approved exact LuxSync logo artwork may retain its exact visual lettering as artwork. Do not recreate or re-typeset protected logo art merely to force live-text typography into the logo.

Visual direction:

- Layered Slate Navy / Dark Suede surfaces
- Restrained Champagne Rose Gold Metallic detail
- Clear Dusty Steel interaction accents
- Pale Driftwood copy
- Premium smart-living/interior imagery
- Spacious editorial composition
- Refined rounded cards
- Selective atmospheric glow
- Minimal organic motion

Avoid cyberpunk neon, unapproved lavender/cyan/magenta base colors, loud gradients, generic SaaS blue, dense gadget-store grids, cartoon UI, excessive glassmorphism, hard glowing borders, flashing animation, aggressive popups, and text baked into photographs when native text is possible.

### Voice

Use **Intelligent Calm**: warm, confident, thoughtful, unhurried, professional, human, refined, and approachable.

Avoid hype, fear-based security language, jargon, technical showing-off, urgency, excessive exclamation marks, and unsupported superlatives.

### Responsive, accessibility, and performance

Design mobile first. Mobile uses compact navigation, accessible search/cart, large touch targets, readable Manrope/Inter type, scannable sections, and thumb-friendly product cards. Tablet reduces columns; desktop may use wider editorial layouts.

Target WCAG 2.2 AA practices: semantic headings, keyboard access, visible focus, sufficient contrast, labels, meaningful alt text, adequate targets, reduced-motion behavior, and no color-only meaning.

Use responsive images, modern formats, lazy loading, stable layouts, efficient font loading, minimal unnecessary JavaScript, and restrained effects.

### Repository assets

Use current approved website assets beneath `brand/assets-v3/`.

- Use protected approved primary logo artwork exactly as supplied.
- Logo masters remain under `brand/assets/01-brand/` and are immutable artwork.
- Prefer SVG for icons/vector UI and optimized WebP for larger scene imagery.
- Production scenes under `brand/assets/12-scenes/` are text-free backgrounds intended for native HTML/CSS copy and approved branding overlays.
- Do not use retired generated graphics or recreate repository SVG assets through an image generator.

### Future roadmap

Leave clean expansion points for SmartThings automation templates, LuxSync Grid, and elite architecture services. Do not advertise them as live.

### Final quality standard

A first-time visitor should quickly understand that LuxSync is a premium curated smart-home commerce brand; products and bundles are selected to work together; SmartThings compatibility reduces complexity; shopping is intentionally curated; the technology belongs in a beautifully designed home or property; Bridgette Beardsley and Sheldon Bardol are the accountable co-founders; and customers can find clear answers or a guided recommendation without becoming smart-home experts.

Every important design, content, and commerce decision should reinforce:

**Where Luxury Lives Intelligently.**
