#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
W3=ROOT/"brand/manifests/wave3-print-physical-manifest.json"
OMNI=ROOT/"brand/manifests/omnichannel-brand-manifest.json"
STATE=ROOT/"brand/audit/brand-build-state.json"
BRAND_README=ROOT/"brand/README.md"
ASSET_GUIDE=ROOT/"docs/production-asset-library.md"
CATALOG=ROOT/"docs/master-catalog.md"
REPORT=ROOT/"brand/audit/brand-build-report.md"


def sha256(path:Path)->str:
    h=hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda:f.read(1024*1024),b""): h.update(chunk)
    return h.hexdigest()


def append_once(path:Path, marker:str, block:str)->None:
    text=path.read_text()
    if marker not in text:
        path.write_text(text.rstrip()+"\n\n"+block.strip()+"\n")


def main()->None:
    w3=json.loads(W3.read_text())
    if w3.get("status")!="qa-passed":
        raise SystemExit("Wave 3 manifest must be qa-passed before governance reconciliation")
    w3hash=sha256(W3)

    omni=json.loads(OMNI.read_text())
    omni["version"]="1.5-wave3-print-physical-integrated"
    omni["status"]="wave3-print-physical-qa-passed-pending-pr-validation"
    omni["wave3_print_physical"]={
      "status":"qa-passed",
      "manifest":"brand/manifests/wave3-print-physical-manifest.json",
      "manifest_sha256":w3hash,
      "static_print_asset_count":w3["static_asset_count"],
      "physical_placement_spec_count":w3["physical_spec"]["placement_count"],
      "formats":["300-dpi-png","cmyk-tiff-companion","exact-page-pdf"],
      "master_root":"brand/masters/print-physical/wave3/",
      "print_export_root":"brand/exports/print/wave3/",
      "template_root":"brand/templates/print-physical/",
      "qa_contact_sheet":w3["qa"]["contact_sheet"],
      "qa_contact_sheet_sha256":w3["qa"]["sha256"],
      "qa_approval_record":"brand/audit/wave3-print-physical-qa-approval.json",
      "specialty_production_boundary":"Vendor-specific one-color, embroidery, engraving, vinyl, screen-print and foil conversions remain pending actual production constraints; do not invent them generatively."
    }
    OMNI.write_text(json.dumps(omni,indent=2)+"\n")

    state=json.loads(STATE.read_text())
    state["schema_version"]="1.5"
    state["overall_state"]="wave3-qa-complete-pending-pr-validation"
    state["current_phase"]="wave3"
    wave3=state["phases"]["wave3"]
    wave3["state"]="qa_complete_pending_pr_validation"
    wave3["manifest"]="brand/manifests/wave3-print-physical-manifest.json"
    wave3["manifest_status"]="qa-passed"
    wave3["latest_successful_build_run"]=33714772180
    wave3["completed_checks"]=[
      "approved stationery board treated as composition evidence rather than a source of production contact data",
      "eight 300-DPI print/stationery source compositions generated",
      "high-resolution PNG masters and matching PNG delivery files generated",
      "CMYK TIFF companions generated without unsupported vendor ICC claims",
      "exact-page-size PDF source files generated and independently render-reviewed",
      "eight vendor-neutral physical placement specifications created for signage, apparel, headwear, drinkware, vinyl, engraving and foil use",
      "exact approved LuxSync raster logo artwork used without redraw, recolor or retyping",
      "mutable personal/contact/invoice/campaign data kept out of flattened source art",
      "Wave 3 contact-sheet visual QA passed",
      "all eight PDF pages rendered and visually checked for clipping, distortion and broken render artifacts",
      "manual QA approval bound to exact contact-sheet SHA256",
      "vendor-specific specialty conversion deferred until actual production constraints are supplied"
    ]
    wave3["known_gaps"]=[
      "full repository PR validation must pass with Wave 3 validator enabled before PR-BRAND-001 is closed",
      "actual specialty manufacturing artwork remains vendor-dependent and intentionally outside the generic master kit"
    ]
    state["idempotence"]["wave3_static_print_asset_count"]=w3["static_asset_count"]
    state["idempotence"]["wave3_static_delivery_file_count"]=w3["static_asset_count"]*3
    state["idempotence"]["wave3_physical_placement_spec_count"]=w3["physical_spec"]["placement_count"]
    state["next_checkpoint"]="Wire Wave 3 validation into standard repository CI, open the Wave 3 PR, pass full PR validation, merge, verify master, then mark PR-BRAND-001 complete with vendor-specific specialty conversions intentionally deferred until production requirements exist."
    STATE.write_text(json.dumps(state,indent=2)+"\n")

    append_once(BRAND_README,"## Wave 3 - Print & Physical Brand System",f'''## Wave 3 - Print & Physical Brand System

The PR-BRAND-001 Wave 3 source layer is governed by `brand/manifests/wave3-print-physical-manifest.json`.

- Eight approved stationery/print composition templates are delivered as 300-DPI PNG source art, CMYK TIFF companions and exact-page-size PDFs.
- Template sources live under `brand/templates/print-physical/`; print exports live under `brand/exports/print/wave3/`.
- The stationery approval board remains composition evidence. Example identity/contact data from that board is not production data.
- Exact approved LuxSync logo artwork is used unchanged in full-color source compositions.
- Physical placements for signage, apparel, headwear, drinkware, vinyl, engraving and foil are governed by `brand/templates/print-physical/physical-production-specs.json`.
- Vendor-specific one-color, stitch, cut-line, engraving, screen-print and foil conversions are created only after actual production constraints are known. Do not invent them or generatively redraw the logo.
- All physical jobs require final vendor preflight before manufacture.

Wave 3 QA contact sheet: `brand/audit/qa/wave3-print-physical.jpg`.''')

    append_once(ASSET_GUIDE,"## Wave 3 print and physical source layer",'''## Wave 3 print and physical source layer

Use `brand/manifests/wave3-print-physical-manifest.json` as the authoritative Wave 3 inventory.

The layer contains eight 300-DPI stationery/print compositions across business cards, letterhead, #10 envelope, note card, invoice/header, document cover and one-page print collateral. Each composition has a governed PNG source, CMYK TIFF companion and exact-page PDF. Live-content zones are recorded in the manifest so mutable data stays editable.

Physical-production placement guidance lives in `brand/templates/print-physical/physical-production-specs.json`. It does not fabricate printer/fabricator settings. Validate material, process, minimum feature size, decoration area, ink/thread/foil constraints, cut lines, registration, trapping and vendor file requirements before creating specialty manufacturing artwork.''')

    cat=CATALOG.read_text()
    if "| BRAND-017 | Wave 3 Print & Physical Manifest" not in cat:
        needle="| BRAND-016 | Wave 2 Digital Marketing Templates & Channel Kit | `brand/templates/digital-marketing/` + `brand/exports/digital/marketing/` | Active / PR-BRAND-001 Wave 2 |"
        addition=needle+"\n| BRAND-017 | Wave 3 Print & Physical Manifest | `brand/manifests/wave3-print-physical-manifest.json` | Active / QA-passed |\n| BRAND-018 | Wave 3 Print, Stationery & Physical Production Kit | `brand/templates/print-physical/` + `brand/exports/print/wave3/` | Active / PR-BRAND-001 Wave 3 |"
        if needle not in cat:
            raise SystemExit("Master catalog insertion anchor missing")
        CATALOG.write_text(cat.replace(needle,addition,1))

    append_once(REPORT,"## Wave 3 print and physical checkpoint",f'''## Wave 3 print and physical checkpoint

Status: QA complete; pending repository PR validation.

- 8 print/stationery compositions at 300 DPI.
- 8 PNG masters + 8 PNG deliveries + 8 CMYK TIFF companions + 8 exact-page PDFs.
- 8 vendor-neutral physical placement specifications.
- Contact-sheet QA passed and is hash-bound.
- All 8 PDFs were independently render-reviewed before approval.
- No example identity/contact/invoice data from the stationery board was promoted as production data.
- Specialty manufacturing conversions remain intentionally deferred until actual vendor constraints exist.

Wave 3 manifest SHA256: `{w3hash}`.''')

    print("Wave 3 governance and discovery reconciliation complete")

if __name__=="__main__": main()
