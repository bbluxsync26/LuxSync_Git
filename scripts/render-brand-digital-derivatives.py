#!/usr/bin/env python3
"""Render verified LuxSync SVG masters into deterministic digital derivatives.

This script is intentionally idempotent. It verifies approval state and existing
hashes before rendering, skips already-valid derivatives, writes PNG/WebP
outputs only for approved SVG masters, creates QA contact sheets, and updates
the omnichannel manifest with provenance and hashes.
"""

from __future__ import annotations

import hashlib
import json
import os
import subprocess
from pathlib import Path

from PIL import Image, ImageDraw
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
JOBS_PATH = ROOT / "brand/manifests/digital-derivative-jobs.json"
OMNI_PATH = ROOT / "brand/manifests/omnichannel-brand-manifest.json"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def git_sha() -> str:
    env_sha = os.environ.get("GITHUB_SHA")
    if env_sha:
        return env_sha
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=ROOT, text=True
        ).strip()
    except Exception:
        return "unknown"


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


def approval_map(path: Path):
    data = load_json(path)
    return {item.get("path"): item for item in data.get("assets", [])}


def existing_record_valid(record: dict, source: Path, png: Path, webp: Path) -> bool:
    if not record:
        return False
    if record.get("source_sha256") != sha256(source):
        return False
    files = record.get("files", {})
    expected = (("png", png), ("webp", webp))
    for fmt, path in expected:
        meta = files.get(fmt, {})
        if not path.exists():
            return False
        if meta.get("path") != path.relative_to(ROOT).as_posix():
            return False
        if meta.get("sha256") != sha256(path):
            return False
        if meta.get("bytes") != path.stat().st_size:
            return False
    return True


def render_svg(page, source: Path, png: Path, width: int, height: int) -> None:
    svg = source.read_text(encoding="utf-8")
    html = (
        "<html><head><style>"
        "html,body{margin:0;padding:0;background:transparent;overflow:hidden}"
        "svg{display:block}"
        "</style></head><body>" + svg + "</body></html>"
    )
    page.set_viewport_size({"width": width, "height": height})
    page.set_content(html, wait_until="load")
    png.parent.mkdir(parents=True, exist_ok=True)
    page.screenshot(
        path=str(png),
        omit_background=True,
        clip={"x": 0, "y": 0, "width": width, "height": height},
    )


def make_contact_sheet(batch_id: str, jobs: list[dict], target: Path) -> None:
    tile_w, tile_h = 640, 420
    cols = 2
    rows = (len(jobs) + cols - 1) // cols
    sheet = Image.new("RGB", (tile_w * cols, tile_h * rows), (20, 20, 20))
    draw = ImageDraw.Draw(sheet)
    for i, job in enumerate(jobs):
        png = ROOT / job["output_png"]
        im = Image.open(png).convert("RGBA")
        preview = im.copy()
        preview.thumbnail((tile_w - 50, tile_h - 80))
        tile = Image.new("RGBA", (tile_w, tile_h), (20, 20, 20, 255))
        x = (tile_w - preview.width) // 2
        y = 18 + (tile_h - 80 - preview.height) // 2
        tile.alpha_composite(preview, (x, y))
        sheet.paste(tile.convert("RGB"), ((i % cols) * tile_w, (i // cols) * tile_h))
        draw.text(
            ((i % cols) * tile_w + 20, (i // cols) * tile_h + tile_h - 36),
            job["id"],
            fill=(235, 235, 235),
        )
    target.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(target, "JPEG", quality=92, optimize=True)


def main() -> None:
    cfg = load_json(JOBS_PATH)
    omni = load_json(OMNI_PATH)
    generated = omni.setdefault("generated_derivative_batches", {})
    source_commit = git_sha()

    rendered_any = False
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, args=["--no-sandbox", "--disable-dev-shm-usage"])
        page = browser.new_page()

        for batch in cfg.get("batches", []):
            batch_id = batch["id"]
            approval_path = ROOT / batch["approval_manifest"]
            approvals = approval_map(approval_path)
            required_status = batch["publication_status_required"]
            previous = generated.get(batch_id, {})
            previous_by_id = {a.get("id"): a for a in previous.get("assets", [])}
            records = []
            batch_rendered = False

            for job in batch.get("jobs", []):
                source = ROOT / job["source"]
                png = ROOT / job["output_png"]
                webp = ROOT / job["output_webp"]
                width = int(job["width"])
                height = int(job["height"])

                if not source.exists():
                    raise SystemExit(f"Missing approved SVG source: {job['source']}")
                approval = approvals.get(job["source"], {})
                if approval.get("publication_status") != required_status:
                    raise SystemExit(
                        f"{job['source']} is not {required_status} in {batch['approval_manifest']}"
                    )
                if approval.get("text_free") is not True:
                    raise SystemExit(f"{job['source']} must remain text-free for this derivative batch")

                old = previous_by_id.get(job["id"], {})
                if existing_record_valid(old, source, png, webp):
                    records.append(old)
                    print(f"SKIP already valid: {job['id']}")
                    continue

                render_svg(page, source, png, width, height)
                im = Image.open(png).convert("RGBA")
                if im.size != (width, height):
                    raise SystemExit(
                        f"{job['id']} PNG size mismatch: {im.size} != {(width, height)}"
                    )
                webp.parent.mkdir(parents=True, exist_ok=True)
                im.save(
                    webp,
                    "WEBP",
                    lossless=bool(job.get("webp_lossless", True)),
                    method=6,
                    exact=True,
                )
                if Image.open(webp).size != (width, height):
                    raise SystemExit(f"{job['id']} WebP dimensions changed during export")

                alpha_min, alpha_max = im.getchannel("A").getextrema()
                record = {
                    "id": job["id"],
                    "source": job["source"],
                    "source_sha256": sha256(source),
                    "master_type": "true-vector-svg",
                    "publication_status": required_status,
                    "text_free": True,
                    "width": width,
                    "height": height,
                    "transparency": alpha_min < 255,
                    "alpha_extrema": [alpha_min, alpha_max],
                    "files": {
                        "png": {
                            "path": job["output_png"],
                            "bytes": png.stat().st_size,
                            "sha256": sha256(png),
                        },
                        "webp": {
                            "path": job["output_webp"],
                            "bytes": webp.stat().st_size,
                            "sha256": sha256(webp),
                            "lossless": bool(job.get("webp_lossless", True)),
                        },
                    },
                    "qa_status": "passed",
                }
                records.append(record)
                batch_rendered = True
                rendered_any = True
                print(f"RENDERED: {job['id']}")

            qa = ROOT / batch["qa_contact_sheet"]
            if batch_rendered or not qa.exists():
                make_contact_sheet(batch_id, batch.get("jobs", []), qa)

            generated[batch_id] = {
                "renderer": cfg.get("renderer"),
                "approval_manifest": batch["approval_manifest"],
                "source_commit": source_commit,
                "qa_contact_sheet": batch["qa_contact_sheet"],
                "qa_contact_sheet_sha256": sha256(qa),
                "qa_status": "passed",
                "assets": records,
            }

        browser.close()

    omni["last_derivative_render_source_commit"] = source_commit
    write_json(OMNI_PATH, omni)
    print("Derivative manifest updated.")
    if not rendered_any:
        print("No binary derivatives required regeneration.")


if __name__ == "__main__":
    main()
