# LuxSync ROI guides and saved work

The library at `/guides/` contains ten audience-specific PDFs and online guides. The content is derived from `src/roi/source/`, copied from the supplied ROI Markdown directory. The supplied cover was edited to remove its subtitle placeholder; each audience title is overlaid in the PDF and web cover.

Online guides support named worksheets, notes, measurement periods, correcting existing periods, and side-by-side comparisons. Values are displayed as entered. Automatic ROI, savings, payback, and calculated differences are intentionally deferred.

`/account/` and `/account/create/` start Sites' ChatGPT sign-in. `/account/welcome/` lists the current user's saved guides and Concierge journeys. Anonymous save actions preserve a temporary draft during sign-in and prompt for sign-in or account creation. PDFs remain available without an account.

## Persistence

Production uses the logical D1 binding `DB`. Generated Drizzle migrations in `drizzle/` create `saved_items`. Every read and write is scoped to the Sites-authenticated user ID; clients cannot set ownership. Updates use versions to detect conflicting saves. Do not change already-applied migrations.

Local preview runs with `npm run dev` on `http://localhost:4177`. It uses Node 22.13 or later and stores records in `.local-data/accounts.sqlite`. Local sign-in deliberately uses one clearly labeled test workspace; it does not authenticate a real customer or connect to hosted account data. This development server must never be used as the public deployment entrypoint. Hosted code uses `server/worker.mjs` instead.

`LUXSYNC_LOCAL_DB` optionally selects a separate SQLite file for local testing. Runtime data is ignored by Git. Back up that file before clearing local preview records.

## Building and validation

Run `npm test` for the site build and existing content checks, and `npm run test:accounts` for ownership, persistence, input validation, and conflicting-update checks. Build output is `dist/client/`, `dist/server/index.js`, and `dist/.openai/`.

PDFs are prebuilt in `src/roi/pdfs/`. To regenerate, run `scripts/prepare-roi.py` and `scripts/build-roi-pdfs.py` using Python with ReportLab and pypdf; the current print typography uses the Windows Inter font. Render and visually inspect regenerated PDFs before release.

Published with the LuxSync site. Hosted ChatGPT sign-in is owned by Sites, and account records use D1. Local preview uses a separate SQLite test workspace.
