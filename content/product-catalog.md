# LuxSync Product & Solution Catalog

**Status:** Active planning catalog / customer-facing publication requires validated Commerce Plus data
**Last updated:** 2026-08-31
**Commerce system of record:** GoDaddy Commerce Plus
**Primary compatibility standard:** Samsung SmartThings
**Official slogan:** **Where Luxury Lives Intelligently**

## Purpose

This file is the canonical repository catalog for LuxSync product families, curated bundle concepts, and Concierge-linked solution concepts.

It does **not** establish live price, stock, supplier availability, shipping promises, ratings, reviews, or exact compatibility. Those values must come from validated Commerce Plus and manufacturer/integration data before publication.

## Catalog Model

LuxSync merchandises in three layers:

1. **Physical product families** — the compatible hardware categories customers may purchase.
2. **Curated bundles** — groups of validated products assembled around a clear use case.
3. **LuxSync Experiences** — outcome-first recommendation concepts produced by the Intelligent Living Concierge. An Experience is not automatically a standalone SKU. It may map to one or more bundles, device categories, setup guidance, and automation recommendations.

The governing customer journey is:

**Lifestyle Goal → LuxSync Experience → Capability Requirements → Compatible Products / Bundles → Setup & Guidance**

---

# 1. Physical Product Families

## Foundation & Connectivity

Potential catalog categories:

- SmartThings-compatible hubs and hub-enabled controllers
- Matter-compatible controllers where appropriate
- Network-support products when needed for reliable smart-home operation
- Bridges required by supported product ecosystems

## Entry & Access

- Smart locks
- Smart garage/entry controllers
- Door/window contact sensors
- Keypad or code-based access products
- Compatible doorbell and entry-awareness products

## Lighting & Ambience

- Smart bulbs
- Smart switches and dimmers
- Smart plugs
- Architectural and decorative smart lighting
- Accent and pathway lighting
- Outdoor lighting
- Smart shades and blinds where validated

## Comfort & Climate

- Smart thermostats
- Temperature sensors
- Humidity and environmental sensors
- Smart shades/blinds used for comfort routines
- Compatible fans or climate-control accessories where validated

## Property Awareness & Security-Related Technology

- Cameras
- Motion/presence sensors
- Door/window sensors
- Smart doorbells
- Property-status sensors

LuxSync must not describe convenience-oriented security technology as a guaranteed substitute for professional monitoring, emergency services, or required life-safety systems.

## Water Protection

- Leak sensors
- Water sensors
- Smart water shut-off products
- Freeze/temperature awareness devices where appropriate

## Energy & Power

- Smart plugs and outlets
- Energy-monitoring devices
- Lighting controls
- Climate controls
- Power-management accessories where compatibility is validated

## Entertainment & Ambience

- Smart televisions
- Smart speakers
- Compatible streaming/entertainment devices
- Lighting and shade products used in entertainment scenes

## Cleaning & Convenience

- Robotic vacuums/mops
- Selected smart appliances
- Convenience devices that fit the supported ecosystem and LuxSync experience model

## Outdoor Living

- Outdoor smart lighting
- Outdoor-compatible smart plugs
- Property-awareness sensors
- Outdoor entertainment products where validated

---

# 2. Existing Curated Bundle Concepts

These concepts remain part of the LuxSync planning catalog:

- **STR Property Automation Kit**
- **STR Guest Welcome & Keyless Entry Bundle**
- **Smart Sleep Nursery Kit**
- **Senior Independent Safety Bundle** — pricing remains unresolved and must not be published until explicitly approved

Exact contents and pricing require Commerce Plus validation.

---

# 3. Concierge-Linked Solution Concepts

The following concepts are added to the planning catalog because they are now generated or supported by the **LuxSync Intelligent Living Concierge**.

Each item is a **solution concept**, not automatically a live SKU. Development should map each concept to validated hardware categories, compatibility requirements, optional enhancements, guides, and automation instructions before publication.

## Residential Experience Concepts

### Welcome Home
Purpose: coordinate an intelligent arrival experience.

Potential capability categories:
- entry/presence awareness
- interior and exterior lighting
- climate
- selected entry systems
- optional entertainment

### Effortless Departure
Purpose: reduce repetitive leaving-home tasks.

Potential capability categories:
- lighting shutdown
- climate setback
- entry-status awareness
- selected device/power controls
- Away state

### Goodnight
Purpose: coordinate the home's transition to overnight mode.

Potential capability categories:
- lighting
- climate
- selected entry-status checks
- device shutdown
- night lighting

### Gentle Morning
Purpose: create a gradual morning transition.

Potential capability categories:
- lighting
- shades
- climate
- optional audio/information routines

### Intelligent Evening
Purpose: coordinate evening lighting, comfort, shades, and ambience.

### Night Path
Purpose: provide context-aware low-level pathway lighting for nighttime movement.

### Climate Intelligence
Purpose: coordinate comfort and energy-conscious climate routines.

### Energy Intelligence
Purpose: reduce unnecessary lighting, climate, and device energy use.

### Water Watch
Purpose: improve leak/water-event awareness and, where compatible, water-control response.

### Away
Purpose: coordinate energy-conscious and awareness-oriented behavior when a property is unoccupied.

### Protect
Purpose: group non-life-safety property-awareness capabilities around the customer's priorities.

### Property Pulse
Purpose: provide a remote property-status concept using compatible sensors and notifications.

### Vacation Mode
Purpose: coordinate extended-away routines for vacation or secondary residences.

### Cinema
Purpose: coordinate entertainment, lighting, shades, and ambience.

### Entertain
Purpose: coordinate lighting, music, dining/living spaces, and optional outdoor ambience for guests.

### Relax
Purpose: create a comfort-oriented lighting and ambience experience.

### Accessible Living
Purpose: simplify everyday tasks through appropriate lighting, voice control, routines, entry, climate, and other convenience technology.

This is a convenience/accessibility solution concept and must not be represented as medical care, emergency response, or a substitute for required safety equipment.

---

# 4. Short-Term Rental Solution Concepts

## Guest Ready
Purpose: transition a property into a guest-ready state before arrival.

Potential capability categories:
- guest access
- lighting
- climate
- property status
- guest-comfort settings

## Turnover
Purpose: support the transition between checkout, cleaning, and the next guest-ready state.

Potential capability categories:
- access-state changes
- climate changes
- cleaner coordination
- property-status checks

## STR Property Pulse
Purpose: provide remote property awareness between and during stays using compatible technology and privacy-conscious configuration.

## STR Water Watch
Purpose: prioritize leak/water awareness for remotely managed properties.

## STR Energy Intelligence
Purpose: reduce avoidable energy use during vacant, turnover, and occupied states without compromising reasonable guest comfort.

The Concierge may combine these with the existing **STR Property Automation Kit** and **Guest Welcome & Keyless Entry Bundle** once exact components are validated.

---

# 5. Business / Commercial Solution Concepts

## Intelligent Opening
Potential capabilities: lighting, climate, access-related routines, shared-space preparation.

## Intelligent Closing
Potential capabilities: lighting shutdown, climate setback, selected device shutdown, property-status awareness.

## Business Energy Intelligence
Potential capabilities: occupancy-aware lighting, climate routines, and selected power controls.

## Business Property Pulse
Potential capabilities: remote awareness for selected locations and supported sensors.

Commercial scope and multi-location projects may require consultation before final component selection.

---

# 6. Recommendation-to-Catalog Mapping

The Concierge engine in `website/src/concierge/` should recommend **Experiences first**.

The website or commerce layer should then resolve the Experience into:

- required capability categories
- compatible product families
- existing customer devices that may be reused
- optional enhancements
- validated bundle/SKU references when available
- required hubs, bridges, apps, or accounts
- subscription dependencies
- installation requirements
- related setup guides

Do not hard-code one exact product into an Experience unless that product has been validated and the recommendation logic can tolerate discontinuation or replacement.

---

# 7. Catalog Status Rules

Use these statuses internally:

- **Validated Live Product** — exact commerce item verified in Commerce Plus
- **Validated Bundle** — bundle contents and public commerce data verified
- **Planning Product Family** — category approved, exact live items still being selected
- **Solution Concept** — experience-led concept awaiting final product mapping
- **Roadmap** — not available for sale
- **Retired** — no longer recommended or sold

The website must never convert a Planning Product Family, Solution Concept, or Roadmap item into a claim of current stock or availability.

---

# 8. Roadmap Boundary

The following remain roadmap capabilities until explicitly released:

- downloadable or installable SmartThings automation templates
- LuxSync Grid SaaS/dashboard capabilities
- advanced AI-generated automation deployment
- elite architecture/integration services not yet commercially approved

The Concierge itself may describe automation **possibilities and recommended experiences**, but it must not claim that unreleased automation-template products are available.

---

# 9. Maintenance

When products or bundles are added:

1. Validate SmartThings/Matter/manufacturer compatibility.
2. Validate supplier and Commerce Plus data.
3. Assign a catalog status.
4. Map the item to relevant LuxSync Experiences.
5. Add guides/support dependencies.
6. Confirm subscription and installation requirements.
7. Update the Concierge product mapping without changing stable Experience IDs unnecessarily.
8. Update `docs/master-catalog.md` when the change is durable.

## Website Display Contract

The shop implementation is `website/pages/shop.md`. Product and collection surfaces are built live. The imported files under `brand/assets/06-product-cards/` are reference-only and must not supply product names, prices, ratings, inventory or imagery for live commerce.
