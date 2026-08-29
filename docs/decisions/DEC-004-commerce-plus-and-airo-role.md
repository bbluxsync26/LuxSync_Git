# DEC-004 — Commerce Plus and Airo Role

**Status:** Active  
**Date:** 2026-08-29

## Decision

For the LuxSync launch, **GoDaddy Commerce Plus remains the commerce system of record**.

**GoDaddy Airo AI Builder is approved as a design, prototyping, and custom-site generation tool, but it does not replace the production commerce system of record unless a later repository decision explicitly approves that migration after functional validation.**

GoDaddy Airo Plus is treated separately from Airo AI Builder. Airo Plus may support brand, SEO, accessibility/content optimization, marketing, and compliance-assistant workflows where available, but it is not the governing website architecture.

## Why

The current LuxSync repository defines:

- GoDaddy Commerce Plus as the commerce platform.
- A zero-inventory physical-product storefront.
- Product catalog and fulfillment requirements.
- Future subscription-based services.
- SmartThings-compatible curated bundles and standalone products.

Current GoDaddy documentation confirms that Airo AI Builder can create online stores and connect to GoDaddy Payments or Stripe. However, GoDaddy also notes that Airo AI Builder sites using GoDaddy Payments may not support certain ecommerce capabilities such as tax calculation, shipping, or recurring billing.

Those capabilities are material to the documented LuxSync business model.

Therefore the launch architecture must not silently migrate checkout, shipping, tax, inventory, or subscription responsibilities away from Commerce Plus.

## Approved Use of Airo AI Builder

Airo AI Builder may be used to:

- Generate the initial LuxSync website experience from PR-001.
- Prototype page layouts and responsive behavior.
- Explore code-level implementation.
- Generate reusable presentation components.
- Create a staging/reference implementation.
- Export code for repository review where supported.
- Validate the visual and UX direction before production implementation.

## Not Approved Without a New Decision

Do not:

- Replace Commerce Plus checkout without validated feature parity.
- Duplicate live product inventory in an unmanaged second catalog.
- Connect live payments during initial generation.
- Publish an Airo-generated store as the LuxSync production commerce site before tax, shipping, order, fulfillment, customer account, and recurring-service requirements are validated.
- Treat Airo-generated content as authoritative when it conflicts with repository documentation.

## Production Principle

**The repository governs the experience. Commerce Plus governs launch commerce. Airo accelerates design and implementation.**

## Validation Gate for Any Future Airo Commerce Migration

A future decision may approve Airo AI Builder as the full production storefront only after validating:

1. Product catalog synchronization
2. Shipping calculation
3. Sales-tax behavior
4. Payment processing
5. Order management
6. Customer account behavior
7. Refund/cancellation workflow
8. Supplier/fulfillment workflow
9. Recurring billing where required
10. Analytics and conversion tracking
11. Accessibility
12. SEO
13. Code export/source-control workflow
14. Rollback capability

Until that gate is passed, Commerce Plus remains authoritative for live commerce.