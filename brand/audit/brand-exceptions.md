# LuxSync Omnichannel Brand Exceptions

**Prompt:** PR-BRAND-001  
**Current phase:** Phase 0

## Open execution exceptions

### EX-001 — Reference-board pixels unavailable to current execution tooling

**Type:** Environment/tool-access limitation  
**Human brand decision required:** No  
**Blocks:** Fresh element-level extraction/reconstruction from approval boards  
**Does not block:** Repository audit, path repairs, manifest/state creation, governance reconciliation, reuse of already validated assets, CI validation

The seven authoritative files under `brand/reference-boards/` are present in the GitHub repository, but the current repository connector exposes their metadata without providing binary image pixels for direct model inspection. The connected creative preview service also rejected the authenticated GitHub raw URL host during this run.

**Required behavior:**

- Do not infer board contents from filenames alone.
- Do not resurrect old numbered crops as if they were approved production masters.
- Do not recreate unseen artwork generatively.
- Continue every deterministic nonvisual task.
- Resume visual board inventory automatically when the workspace or connector exposes the board pixels.

### EX-002 — Print/specialty exports require asset-specific suitability review

**Type:** Technical production dependency  
**Human brand decision required:** No at Phase 0  
**Blocks:** Blanket creation of meaningless PDF/EPS/TIFF/AI variants

PR-BRAND-001 intentionally does not require every format for every asset. True vectors, protected raster logos, photographs, stationery layouts, embroidery art and print compositions have different technically appropriate master/export chains.

**Required behavior:** Determine format requirements asset by asset during Waves 1–3 and record any intentionally omitted format in the omnichannel manifest.

## Brand approval conflicts

None detected.

## Protected-master exceptions

None detected. All three protected logo masters are present, and their current production PNG copies match by Git blob SHA.
