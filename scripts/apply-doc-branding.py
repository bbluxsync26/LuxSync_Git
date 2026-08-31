#!/usr/bin/env python3
"""Add the approved LuxSync LLC header to repository Markdown documents."""

from pathlib import Path
import os

ROOT = Path(__file__).resolve().parents[1]
LOGO = ROOT / "brand" / "brand-system-v4" / "01-logos" / "luxsync-horizontal-approved.png"
START = "<!-- LUXSYNC-BRAND-HEADER:START -->"
END = "<!-- LUXSYNC-BRAND-HEADER:END -->"


def header(path: Path) -> str:
    relative = Path(os.path.relpath(LOGO, path.parent)).as_posix()
    return (
        f"{START}\n"
        f'<p align="center"><img src="{relative}" alt="LuxSync LLC — Where Luxury Lives Intelligently" width="620"></p>\n'
        f"{END}\n\n"
    )


def main() -> None:
    changed = 0
    for path in sorted(ROOT.rglob("*.md")):
        if ".git" in path.parts:
            continue
        text = path.read_text(encoding="utf-8")
        if START in text and END in text:
            before, rest = text.split(START, 1)
            _, after = rest.split(END, 1)
            text = before.rstrip() + ("\n\n" if before.strip() else "") + after.lstrip("\n")
        branded = header(path) + text
        path.write_text(branded, encoding="utf-8")
        changed += 1
    print(f"Applied approved LuxSync branding to {changed} Markdown files")


if __name__ == "__main__":
    main()
