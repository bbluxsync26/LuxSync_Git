# DEC-005 — Senior Service Pricing

**Status:** Open / Decision Required  
**Date opened:** 2026-08-30  
**Scope:** Senior Independent Safety hardware/service pricing

## Context

Current LuxSync planning material historically contained two competing senior-service pricing concepts:

1. A bundle/service concept described as starting at **$149/month**.
2. A **$249 hardware + $49/month service** concept.

The repository does not currently contain enough validated commercial, supplier, fulfillment, support-cost, recurring-billing, or market-test evidence to select one model as authoritative.

## Decision

**No senior-service price is currently approved for public display.**

Until this decision record is updated to an approved final model:

- Do not publish either candidate price on the website.
- Do not place either candidate price in PR-001, Airo staging copy, ads, lead magnets, product cards, or customer-facing support content.
- Do not imply that recurring monitoring/service pricing is finalized.
- Use editable placeholders or inquiry language where a design requires a pricing location.
- Any live Commerce Plus listing must remain unpublished or price-suppressed until the commercial decision is approved.

## Candidate Models Under Review

### Candidate A — Subscription-led

- Historical planning reference: starting at $149/month.
- Requires validation of included hardware, service scope, fulfillment economics, support burden, cancellation terms, and recurring-billing capability.

### Candidate B — Hardware + recurring service

- Historical planning reference: $249 hardware + $49/month service.
- Requires validation of hardware COGS, margin, service scope, payment/recurring-billing fees, support burden, and cancellation terms.

These are **planning candidates only**, not approved customer prices.

## Approval Criteria

A final decision should document at minimum:

1. Exact hardware contents and validated supplier costs.
2. Fulfillment/shipping economics.
3. Recurring service scope and customer support obligations.
4. Payment and recurring-billing platform capability.
5. Refund, cancellation, and replacement policy implications.
6. Target gross margin and acceptable acquisition cost.
7. Competitive/market validation.
8. Customer-facing terms and compliance review where appropriate.
9. Final approved one-time and/or recurring price.
10. Effective date and Commerce Plus catalog record.

## Public-Site Guardrail

ARC-001, PR-001, RB-002, CL-001, and the business plan must continue to treat senior pricing as unresolved until this record is changed to **Active / Approved** with one final model.

## Follow-Up

When the pricing model is approved:

1. Update this decision record with the final model and rationale.
2. Update `docs/business-plan.md` and any affected financial forecast.
3. Validate/update the Commerce Plus product/service record.
4. Update customer-facing website/content only from the validated commerce data.
5. Run `scripts/validate-repository-consistency.py` and update its pricing rule to match the newly approved decision.
6. Update `docs/master-catalog.md`.
