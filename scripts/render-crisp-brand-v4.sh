#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
brand_root="$repo_root/brand/brand-system-v4"

command -v inkscape >/dev/null
command -v convert >/dev/null

while IFS= read -r -d '' svg; do
  png="${svg%.svg}.png"
  webp="${svg%.svg}.webp"
  inkscape "$svg" --export-filename="$png" --export-overwrite >/dev/null 2>&1
  sync "$png" 2>/dev/null || true
  sleep 0.1
  convert "$png" null: >/dev/null 2>&1 || {
    inkscape "$svg" --export-filename="$png" --export-overwrite >/dev/null 2>&1
    sync "$png" 2>/dev/null || true
    sleep 0.2
    convert "$png" null: >/dev/null 2>&1
  }
  convert "$png" -quality 88 "$webp"
done < <(find "$brand_root" -name '*.svg' -print0)

echo "Rendered Brand System 4.0 PNG and WebP outputs"
