# LuxSync Intelligent Living Concierge Architecture

**Artifact:** ARC-002  
**Status:** Active / Flagship experience  
**Entry point:** **Find My LuxSync Solution**  
**Guided experience:** **LuxSync Intelligent Living Concierge**  
**Output:** **My LuxSync Blueprint**  
**Engine source:** `website/src/concierge/`  
**Official slogan:** **Where Luxury Lives Intelligently**

## Product Principle

The Concierge begins with how a customer wants a space to live, not with a device catalog.

The governing model is:

**Lifestyle → Experience → Intelligence → Technology**

Customer-facing copy should never reduce the Concierge to a novelty quiz.

## Core Journey

1. Inspiration / primary intent
2. Desired outcomes
3. Property Profile
4. Existing technology
5. Lifestyle discovery
6. Pain points
7. Priority ranking
8. Implementation preference
9. Rules-based recommendation
10. Blueprint reveal
11. Shop, customize, save, consult, or ask a question

## Reusable Property Profile

The Concierge and Contact page share the same conceptual Property Profile:

- property type
- residence / STR / business subtype
- approximate square footage or range
- levels where relevant
- unit/location count where relevant
- current smart-home ecosystem
- rooms/areas of interest

The Contact page should reuse or prepopulate these values when a visitor arrives from a Blueprint.

## Core LuxSync Experiences

Version 1 includes:

- Welcome Home
- Effortless Departure
- Goodnight
- Gentle Morning
- Intelligent Evening
- Cinema
- Entertain
- Relax
- Away
- Protect
- Water Watch
- Climate Intelligence
- Energy Intelligence
- Night Path
- Guest Ready
- Turnover
- Property Pulse
- Accessible Living
- Vacation Mode

Experience definitions and scoring are governed by the machine-readable engine in `website/src/concierge/`.

## Recommendation Contract

The engine evaluates:

**Property + Goals + Existing Technology + Lifestyle + Pain Points + Priorities + Implementation Preference**

and produces:

**Recommended Experiences + Foundation + Compatibility Flags + Implementation Path + Roadmap + Next Best Action**

Every displayed recommendation should explain **Why LuxSync Chose This**.

## Blueprint Reveal

My LuxSync Blueprint should reveal information progressively:

1. Your Space
2. What Matters Most
3. Your Intelligent Living Profile
4. Recommended LuxSync Experiences
5. Recommended Foundation
6. Implementation Path
7. Phased Roadmap
8. Technology Behind the Experience
9. Next Best Action

## Implementation Paths

Use:

- **Essential Intelligence** — highest-impact starting point
- **Elevated Living** — broader connected experience across major spaces
- **Complete LuxSync Experience** — comprehensive implementation of the Blueprint

Do not use Good / Better / Best language.

## Product Integration

Experiences resolve first to capability and product **categories**, then to validated exact products or bundles when available.

Canonical planning catalog: `content/product-catalog.md`.

Exact product names, prices, stock, availability, subscriptions, and compatibility must be validated before publication.

## Contact Integration

The Concierge may route customers to:

- **Build My Solution**
- **Start With Phase 1**
- **Review My Compatibility**
- **Request a LuxSync Consultation**
- **Build My Rental Solution**
- **Save My Blueprint**
- **Ask LuxSync a Question**

Support routes to `support@luxsync.net`; general information and consultations route to `info@luxsync.net`.

## Accessibility and Safety

The Concierge must be keyboard accessible, screen-reader friendly, mobile-first, and compatible with reduced-motion preferences.

Accessible Living recommendations are convenience/accessibility technology only. Do not present smart-home features as medical care, emergency response, professional security monitoring, or replacements for required life-safety equipment.

## Versioning

Stable field IDs and Experience IDs should be treated as API contracts once production launches.

Saved Blueprints should retain the configuration version used to generate them.

## North-Star Test

The experience succeeds when a visitor arrives thinking:

**I need some smart-home products.**

and leaves thinking:

**This is how I want my space to live.**
