#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WAVE2 = ROOT / "brand/manifests/wave2-digital-marketing-manifest.json"
OMNI = ROOT / "brand/manifests/omnichannel-brand-manifest.json"
BRAND_README = ROOT / "brand/README.md"
ASSET_GUIDE = ROOT / "docs/production-asset-library.md"
CATALOG = ROOT / "docs/master-catalog.md"
REPORT = ROOT / "brand/audit/brand-build-report.md"

MARKER = "<!-- PR-BRAND-001-WAVE2-DIGITAL-MARKETING -->"


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def append_once(path: Path, block: str) -> None:
    text = path.read_text(encoding="utf-8")
    if MARKER in text:
        return
    path.write_text(text.rstrip() + "\n\n" + block.strip() + "\n", encoding="utf-8")


def reconcile_omnichannel(manifest: dict) -> None:
    omni = json.loads(OMNI.read_text(encoding="utf-8"))
    omni["wave2_digital_marketing"] = {
        "status": "qa-passed",
        "manifest": "brand/manifests/wave2-digital-marketing-manifest.json",
        "manifest_sha256": sha256(WAVE2),
        "static_template_count": manifest["static_asset_count"],
        "live_template_count": len(manifest["live_templates"]),
        "channels": sorted({item["channel"] for item in manifest["static_assets"]}),
        "master_root": "brand/masters/marketing-art/wave2/",
        "digital_export_root": "brand/exports/digital/marketing/",
        "template_root": "brand/templates/digital-marketing/",
        "qa_contact_sheet": manifest["qa"]["contact_sheet"],
        "qa_contact_sheet_sha256": manifest["qa"]["sha256"],
        "qa_approval_record": manifest["qa"].get("approval_record"),
        "guardrail": "Mutable copy and commerce facts remain live/template-driven. Exact approved LuxSync logos only.",
    }
    OMNI.write_text(json.dumps(omni, indent=2) + "\n", encoding="utf-8")


def reconcile_catalog() -> None:
    text = CATALOG.read_text(encoding="utf-8")
    if "| BRAND-015 | Wave 2 Digital Marketing Manifest |" in text:
        return
    rows = (
        "| BRAND-015 | Wave 2 Digital Marketing Manifest | `brand/manifests/wave2-digital-marketing-manifest.json` | Active / QA-passed |\n"
        "| BRAND-016 | Wave 2 Digital Marketing Templates & Channel Kit | `brand/templates/digital-marketing/` + `brand/exports/digital/marketing/` | Active / PR-BRAND-001 Wave 2 |\n"
    )
    needle = "| BRAND-014 | Visual Approval Archive | `brand/reference-boards/` | Active / Permanent approval evidence |\n"
    if needle in text:
        text = text.replace(needle, needle + rows, 1)
    else:
        text = text.rstrip() + "\n\n" + MARKER + "\n## Wave 2 Digital Marketing\n\n" + rows
    CATALOG.write_text(text, encoding="utf-8")


def main() -> None:
    if not WAVE2.exists():
        raise SystemExit("Wave 2 manifest missing")
    manifest = json.loads(WAVE2.read_text(encoding="utf-8"))
    if manifest.get("status") != "qa-passed":
        raise SystemExit("Wave 2 manifest must be qa-passed before governance reconciliation")

    reconcile_omnichannel(manifest)
    reconcile_catalog()

    append_once(
        BRAND_README,
        f"""
{MARKER}
## Wave 2 digital and marketing kit

PR-BRAND-001 Wave 2 adds a governed reusable digital-marketing layer without turning mutable campaign or commerce content into fixed artwork.

- Governed manifest: `brand/manifests/wave2-digital-marketing-manifest.json`
- Editable composition specs and live templates: `brand/templates/digital-marketing/`
- Raster-origin composition masters: `brand/masters/marketing-art/wave2/`
- PNG and lossless WebP channel exports: `brand/exports/digital/marketing/`
- QA contact sheet: `brand/audit/qa/wave2-digital-marketing.jpg`
- Hash-bound manual QA approval: `brand/audit/wave2-digital-marketing-qa-approval.json`

The kit contains ten text-safe static frames across social, presentations, campaigns and 4K video overlays, plus a live email-signature template and live semantic product-card treatment. Static frames use only exact approved LuxSync logo artwork. Mutable headlines, offers, product facts, prices, ratings, availability and customer information remain live/template-driven.

For new freeform compositions, clean transparent validated dividers under `brand/assets/dividers/` are used to avoid crop-edge seams. The faithful approval-board-derived ornament masters remain preserved separately and unchanged.
""",
    )

    append_once(
        ASSET_GUIDE,
        f"""
{MARKER}
## Wave 2 digital marketing delivery layer

Wave 2 is governed by `brand/manifests/wave2-digital-marketing-manifest.json` and provides:

- four social composition frames;
- two presentation frames;
- two campaign frames;
- two 4K static video-overlay frames;
- a live placeholder-driven email signature;
- a live semantic product-card HTML/CSS treatment.

Raster composition masters live under `brand/masters/marketing-art/wave2/`; PNG and lossless WebP deliveries live under `brand/exports/digital/marketing/`. The static templates intentionally omit SVG because they combine protected raster logo artwork with atmospheric raster effects; `brand/templates/digital-marketing/template-specs.json` is the editable governed source.

All ten static frames are intentionally text-safe. Add current copy and validated commerce data at use time rather than baking mutable facts into reusable brand art.
""",
    )

    append_once(
        REPORT,
        f"""
{MARKER}
## Wave 2 digital and marketing checkpoint

Wave 2 built and visually reviewed a reusable channel kit rather than a set of one-off flattened ads.

Completed:

- 10 deterministic text-safe static compositions: 4 social, 2 presentation, 2 campaign and 2 4K video-overlay frames;
- exact approved LuxSync logo artwork used in every logo-bearing composition;
- clean transparent validated divider assets used for seamless freeform compositing while faithful approval-board crop masters remain preserved;
- live placeholder-driven email signature;
- live semantic product-card HTML/CSS treatment with no baked product or price claims;
- PNG and lossless WebP exports plus raster-origin masters;
- manual contact-sheet QA recorded against an exact SHA256 approval record;
- deterministic builder, validator and governance reconciliation tooling.

The first QA pass found rectangular board-crop seams around some ornaments. That was repaired objectively by using the clean transparent validated divider delivery layer for new compositions rather than altering the faithful board-derived masters. The second contact sheet passed visual review.

Wave 2 remains pending pull-request and post-merge repository CI before being marked complete.
""",
    )

    print("Wave 2 governance reconciliation complete")


if __name__ == "__main__":
    main()
