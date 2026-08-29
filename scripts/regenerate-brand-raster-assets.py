#!/usr/bin/env python3
"""Normalize LuxSync SVG typography and regenerate text-bearing PNG/WebP siblings.

Source of truth:
- Headlines/display: Manrope
- Body/UI: Inter

Legacy mappings:
- Century Gothic -> Manrope
- Candara -> Inter

The script intentionally regenerates only SVGs that contain actual <text> elements and
already have PNG and/or WebP siblings. Existing raster dimensions are preserved.
"""

from __future__ import annotations

import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ASSET_ROOT = ROOT / "brand" / "assets"

LEGACY_FONT_REPLACEMENTS = (
    ("Century Gothic", "Manrope"),
    ("Candara", "Inter"),
)

TEXT_RE = re.compile(r"<text\b", re.IGNORECASE)


def run(*args: str) -> str:
    result = subprocess.run(
        list(args),
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    return result.stdout.strip()


def raster_dimensions(path: Path) -> tuple[int, int]:
    value = run("magick", "identify", "-format", "%w %h", str(path))
    width, height = value.split()
    return int(width), int(height)


def normalize_svg_text(svg_text: str) -> tuple[str, bool]:
    normalized = svg_text
    for old, new in LEGACY_FONT_REPLACEMENTS:
        normalized = normalized.replace(old, new)
    return normalized, normalized != svg_text


def has_text(svg_text: str) -> bool:
    return bool(TEXT_RE.search(svg_text))


def render_png(svg: Path, output: Path, width: int, height: int) -> None:
    run(
        "inkscape",
        str(svg),
        "--export-type=png",
        f"--export-filename={output}",
        f"--export-width={width}",
        f"--export-height={height}",
        "--export-background-opacity=0",
    )


def regenerate(svg: Path, png: Path | None, webp: Path | None) -> None:
    reference = png if png and png.exists() else webp
    if reference is None or not reference.exists():
        return

    width, height = raster_dimensions(reference)

    with tempfile.TemporaryDirectory(prefix="luxsync-raster-") as tmpdir:
        rendered_png = Path(tmpdir) / "rendered.png"
        render_png(svg, rendered_png, width, height)

        if png and png.exists():
            shutil.copyfile(rendered_png, png)

        if webp and webp.exists():
            run(
                "magick",
                str(rendered_png),
                "-strip",
                "-quality",
                "92",
                str(webp),
            )

        # Verify regenerated dimensions before accepting the outputs.
        for candidate in (png, webp):
            if candidate and candidate.exists():
                candidate_size = raster_dimensions(candidate)
                if candidate_size != (width, height):
                    raise RuntimeError(
                        f"Dimension mismatch for {candidate}: {candidate_size} != {(width, height)}"
                    )


def main() -> int:
    if not ASSET_ROOT.exists():
        raise RuntimeError(f"Asset root not found: {ASSET_ROOT}")

    normalized_svgs: list[Path] = []
    regenerated: list[Path] = []

    for svg in sorted(ASSET_ROOT.rglob("*.svg")):
        # Catalog contact sheets are raster-only; skip any future catalog SVG helpers.
        if "00-catalog" in svg.parts:
            continue

        original = svg.read_text(encoding="utf-8")
        normalized, changed = normalize_svg_text(original)
        if changed:
            svg.write_text(normalized, encoding="utf-8")
            normalized_svgs.append(svg)

        # Regenerate only files with visible SVG text and existing raster siblings.
        if not has_text(normalized):
            continue

        png = svg.with_suffix(".png")
        webp = svg.with_suffix(".webp")
        if not png.exists() and not webp.exists():
            continue

        regenerate(
            svg,
            png if png.exists() else None,
            webp if webp.exists() else None,
        )
        regenerated.append(svg)

    # No legacy typography may remain in text-bearing SVG sources after normalization.
    leftovers: list[str] = []
    for svg in sorted(ASSET_ROOT.rglob("*.svg")):
        text = svg.read_text(encoding="utf-8")
        if not has_text(text):
            continue
        for old, _new in LEGACY_FONT_REPLACEMENTS:
            if old in text:
                leftovers.append(f"{svg.relative_to(ROOT)}: {old}")

    if leftovers:
        raise RuntimeError("Legacy fonts remain:\n" + "\n".join(leftovers))

    print(f"Normalized SVG masters: {len(normalized_svgs)}")
    print(f"Regenerated text-bearing raster sets: {len(regenerated)}")
    for svg in regenerated:
        print(f"  - {svg.relative_to(ROOT)}")

    return 0


if __name__ == "__main__":
    sys.exit(main())

# Workflow trigger marker: 2026-08-29 raster-font regeneration
