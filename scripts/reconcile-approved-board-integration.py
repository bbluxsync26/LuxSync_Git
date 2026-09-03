#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OMNI = ROOT / "brand/manifests/omnichannel-brand-manifest.json"
STATE = ROOT / "brand/audit/brand-build-state.json"
BOARD_MANIFEST = ROOT / "brand/manifests/approved-board-asset-manifest.json"


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def write(path: Path, data) -> None:
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


board = load(BOARD_MANIFEST)
if board.get("asset_count") != 58 or board.get("counts") != {"icons": 16, "dividers": 42}:
    raise SystemExit("Approved-board asset manifest is not at the validated 58-asset Wave 1 baseline")

omni = load(OMNI)
omni["version"] = "1.3-wave1-faithful-layer-integrated"
omni["status"] = "wave1-faithful-approved-board-layer-integrated-pending-final-ci"
omni["approved_board_delivery_layer"] = {
    "manifest": "brand/manifests/approved-board-asset-manifest.json",
    "visual_inventory": "brand/audit/reference-board-visual-inventory.md",
    "status": "faithful-approved-visual-layer",
    "asset_count": 58,
    "families": {"metallic_icons": 16, "dividers_accents": 42},
    "master_root": "brand/masters/approved-board-raster/",
    "digital_export_root": "brand/exports/digital/approved/",
    "format_contract": ["master-png", "png", "lossless-webp", "svg-fidelity-container"],
    "usage_rule": "Prefer this layer when the approved metallic LuxSync artwork itself is intended. Retain clean semantic vectors for compact/scalable live UI where technically appropriate.",
    "idempotence_rule": "Skip regeneration when source-board hash, crop geometry, output hashes and QA evidence remain valid."
}

updated = []
for item in omni.get("approval_family_dispositions", []):
    board_name = item.get("board")
    if board_name == "approved_brand_board.png":
        item["current_disposition"] = "Full-resolution visual audit complete. Protected logos remain master-governed; hero/composition examples remain reference/template families with live current copy."
        item["state"] = "visual-audit-complete"
    elif board_name == "icons_board.png":
        item["classification"] = ["raster-origin-approved-art", "semantic-live-ui-reference"]
        item["current_disposition"] = "16 faithful metallic board-derived assets generated and QA-passed. Earlier clean vectors remain as simplified semantic UI primitives and are not the sole faithful brand rendering."
        item["state"] = "complete-faithful-layer-integrated"
    elif board_name == "dividers_board.png":
        item["classification"] = ["raster-origin-approved-art", "composition-template"]
        item["current_disposition"] = "42 faithful text-free divider/accent assets generated and QA-passed. Four SECTION separator examples remain template/reference-only because their titles are mutable."
        item["state"] = "complete-faithful-layer-integrated"
    elif board_name == "buttons_board.png":
        item["current_disposition"] = "Approved visual/state language retained as semantic live UI reference. Do not flatten mutable button labels into production images."
        item["state"] = "visual-audit-complete-template-reference"
    elif board_name == "ui_controls_board.png":
        item["current_disposition"] = "Approved visual/state language retained as semantic live UI reference. Mutable data and example claims remain live and require validation."
        item["state"] = "visual-audit-complete-template-reference"
    elif board_name == "product_cards_board.png":
        item["current_disposition"] = "Approved category-card composition retained for Wave 2 template/marketing work. Conceptual imagery or commerce content is not validated live catalog data."
        item["state"] = "visual-audit-complete-wave2-template"
    elif board_name == "stationery_board.png":
        item["current_disposition"] = "Approved stationery composition retained for Wave 3 print/template work. Placeholder identity/contact data on the board is not production data."
        item["state"] = "visual-audit-complete-wave3-template"
    updated.append(item)
omni["approval_family_dispositions"] = updated
omni["known_omnichannel_gaps"] = [
    "Wave 2 broader digital/marketing compositions remain to be built with current live copy and validated data.",
    "Wave 3 print/physical production remains to be built, including stationery, merchandise/apparel/signage and technically justified PDF/EPS/TIFF or specialty variants.",
    "Board-derived raster-origin artworks retain their approved dark-board-background masters; transparency or specialty-production variants must be created only when technically justified without altering the approved masters."
]
omni["next_checkpoint"] = "Run full repository CI with approved-board validation enabled. If green, mark Wave 1 complete and resume PR-BRAND-001 at Wave 2 without regenerating the validated 58-asset faithful layer."
write(OMNI, omni)

state = load(STATE)
state["overall_state"] = "wave1-integration-complete-pending-final-ci"
state["current_phase"] = "wave1"
wave1 = state.setdefault("phases", {}).setdefault("wave1", {})
wave1["state"] = "integration-complete-pending-final-ci"
completed = wave1.setdefault("completed_checks", [])
for check in (
    "faithful approved-board visual layer documented in brand/README.md and docs/production-asset-library.md",
    "website/asset-map.md updated to prefer faithful metallic artwork for branded visual moments while retaining semantic vectors for compact live UI",
    "private short-retention board visual-audit workflow made reusable across brand feature branches",
    "omnichannel icon/divider dispositions reconciled to the completed full-resolution visual audit",
):
    if check not in completed:
        completed.append(check)
wave1["known_gaps"] = [
    "full repository CI must pass with scripts/validate-approved-board-assets.py enabled before Wave 1 is closed",
    "Wave 2 and Wave 3 remain intentionally pending"
]
state["execution_constraints"] = [
    "The 58 faithful board-derived assets are raster-origin because the approved boards are the current visual authority; their SVGs are fidelity containers rather than newly redrawn editable vectors.",
    "Do not generatively redraw approved LuxSync artwork merely to obtain vector paths.",
    "Do not flatten mutable button, product, stationery, hero or UI copy into production assets when live/template implementation is appropriate."
]
state["next_checkpoint"] = "Run full repository CI on the Wave 1 branch. If green, seal validation into state, merge, and resume future PR-BRAND-001 runs at Wave 2."
write(STATE, state)

print("LuxSync approved-board integration state reconciled")
