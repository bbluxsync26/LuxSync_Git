# LuxSync Navigation and Footer Contract

**Status:** Active / Authoritative
**Brand system:** LuxSync Production Raster v5

## Header

Primary navigation:

- Shop → `/shop`
- Solutions → `/solutions`
- Guides → `/guides`
- About → `/about`
- FAQs → `/faqs`
- Contact → `/contact`

Persistent utilities where supported by the commerce implementation:

- Search
- Account → preferred LuxSync experience route `/account/login`, delegated to the actual production Commerce Plus/account flow when integrated
- Cart

The Account utility must feel like part of the LuxSync premium experience, not a generic external login handoff. Visual and interaction rules are governed by `website/pages/account-login.md` and `website/account-access-manifest.json`.

Do not collect real credentials in a static site or invent an authentication provider to make the preferred route work. The production route/redirect may change to match the supported account platform while preserving the LuxSync visual experience.

Primary header CTA: **LuxSync Concierge** → `/find-my-luxsync-solution`

## Solutions submenu

- Commercial Offices
- Senior Living & Nursing Homes
- Short-Term Rentals
- Residential Living
- Seniors, Caregivers & Aging in Place

## Footer

- Shop
- Solutions
- Guides
- About
- FAQs
- Contact
- Support → `/contact?intent=support`
- Account → production account route when integrated
- Privacy placeholder until approved legal copy exists
- Terms placeholder until approved legal copy exists
- Social links only for approved active channels

Do not create dead navigation, invented social accounts, unsupported commerce utilities, or unsupported authentication routes.

**Official slogan:** Where Luxury Lives Intelligently
