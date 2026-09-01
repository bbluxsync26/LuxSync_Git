# RB-010 — LuxSync Website Build and Deployment

**Status:** Active
**Website implementation:** `site/`
**Production branch:** `master`
**Commerce system of record:** GoDaddy Commerce Plus
**Official slogan:** **Where Luxury Lives Intelligently**

## Purpose

Build, validate, package, and deploy the LuxSync website without allowing the deployment layer to become a second source of truth for brand, Concierge logic, catalog status, or commerce data.

## Local Build

```bash
cd site
npm run build
npm test
```

`site/dist/` is generated output and is not committed.

The build copies the exact protected LuxSync logo masters, the tracked Concierge engine, FAQ content derived from `content/faqs.md`, and the approved planning catalog structure into a deployable static site.

## Runtime Integrations

The build accepts:

- `LUXSYNC_COMMERCE_URL` — GoDaddy Commerce Plus customer storefront URL.
- `LUXSYNC_CONTACT_ENDPOINT` — HTTPS endpoint that accepts the adaptive Contact form JSON payload.
- `LUXSYNC_SITE_URL` — canonical public site URL.

If the Commerce Plus URL is not configured, Shop does not invent a destination. Product CTAs fall back to the product-information Contact path.

If the Contact endpoint is not configured, the site does not falsely display a successful web submission. It prepares an email to `support@luxsync.net` or `info@luxsync.net`, according to the selected intent.

## Concierge and Blueprint

The browser implementation loads `website/src/concierge/luxsync-concierge-engine.v1.json`, renders the governed questionnaire, applies conditional visibility, evaluates the governed scoring rules, and stores the active-session profile and Blueprint in browser local storage.

The Contact page can reuse Blueprint context when a customer arrives from My LuxSync Blueprint.

## CI

The repository consistency workflow must run:

1. Production brand validation.
2. Repository source-of-truth validation.
3. Concierge engine drift validation.
4. Website build and site validation.
5. Whitespace validation.

The website test validates all governed routes, exact logo equality, approved palette usage, retired-slogan absence, and the absence of active placeholder/reference SVG wiring.

## Production Deployment

The deployment workflow always produces a validated `luxsync-site` artifact from `site/dist/`.

When classic GoDaddy hosting with FTP/FTPS access is used, configure these repository secrets:

- `GODADDY_FTP_URL` — full FTP or FTPS server URL.
- `GODADDY_FTP_USER`
- `GODADDY_FTP_PASSWORD`
- `GODADDY_REMOTE_DIR` — production document-root directory such as `/public_html`.

The deployment job mirrors `site/dist/` to the configured remote directory only when all required hosting secrets are present.

If the selected GoDaddy product does not expose FTP/FTPS deployment, keep the build artifact as the release package and document the supported publishing mechanism before enabling automatic production deployment. Do not invent or bypass a hosting API.

## Commerce Boundary

GoDaddy Commerce Plus remains authoritative for exact live products, prices, inventory, shipping, tax, checkout, order management, and other commerce facts. The LuxSync site may present the approved collection and solution structure, but it must not duplicate mutable Commerce Plus facts unless a validated integration is implemented.

## Rollback

1. Identify the last known-good merge commit on `master`.
2. Rebuild that commit using `site/build.mjs`.
3. Run `site/test.mjs` and repository validation.
4. Redeploy the resulting `site/dist/` artifact.
5. Record the rollback reason in the Website Design & CICD workstream and update this runbook if a durable process change is required.
