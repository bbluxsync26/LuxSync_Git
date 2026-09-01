# RB-011 — LuxSync Staging and Production Release Gate

**Status:** Active
**Staging branch:** `staging`
**Production branch:** `master`
**Production publication:** Manual only

## Purpose

Allow LuxSync to be completely built, validated, and reviewed without publishing the site to the public production host.

## Staging Contract

The `staging` branch is the review branch for complete website candidates.

Every push to `staging` runs `.github/workflows/stage-luxsync-site.yml` and must:

1. validate the production brand library;
2. validate repository source-of-truth contracts;
3. verify that the tracked Concierge engine is current;
4. build all governed website routes;
5. run website validation; and
6. upload a `luxsync-staging` artifact.

The staging workflow contains no hosting deployment step. Producing the artifact does not publish LuxSync publicly.

Optional staging integrations can be supplied through repository variables:

- `LUXSYNC_STAGING_COMMERCE_URL`
- `LUXSYNC_STAGING_CONTACT_ENDPOINT`
- `LUXSYNC_STAGING_SITE_URL`

Blank staging integration values are allowed. The site must continue to use its safe fallbacks and must not invent live commerce or successful contact-submission behavior.

## Production Release Contract

A push or merge to `master` builds and packages a validated `luxsync-production-candidate` artifact. It does not publish the website.

Production publication can happen only from a manual `workflow_dispatch` of `.github/workflows/deploy-luxsync-site.yml` with the `publish` input explicitly set to `true`.

The publish job also requires all GoDaddy deployment secrets. If any required deployment secret is missing, the publish job fails rather than reporting a false deployment success.

Required production deployment secrets:

- `GODADDY_FTP_URL`
- `GODADDY_FTP_USER`
- `GODADDY_FTP_PASSWORD`
- `GODADDY_REMOTE_DIR`

## Review Flow

1. Merge finished implementation work to `master` only after CI is green.
2. Fast-forward or recreate `staging` from the desired reviewed `master` commit.
3. Let the staging workflow create the full review artifact.
4. Review content, responsive layouts, Concierge, Blueprint, Contact branching, catalog handoff, accessibility, legal copy, and integration configuration.
5. Repeat on `staging` until approved.
6. When publication is explicitly authorized, manually run the production release workflow with `publish=true`.

## Rule

**No automatic production publication is permitted.** Building, testing, packaging, or staging LuxSync is not authorization to publish it.
