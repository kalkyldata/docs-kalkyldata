#!/usr/bin/env python3
"""Check documentation link targets and duplicate permalinks after a Jekyll build."""

import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[2]
SITE = ROOT / "_site"
LINK = re.compile(
    r"""\]\(\s*\{\{\s*(['"])(/[^'"]*)\1\s*\|\s*relative_url\s*\}\}\s*\)"""
)
ROOT_LINK = re.compile(r"\]\((/[^)\s]*)")
PERMALINK = re.compile(r"^permalink:\s*['\"]?([^'\"\s]+)", re.MULTILINE)

errors = []
permalinks = {}
for source in sorted((ROOT / "docs").rglob("*.md")):
    text = source.read_text(encoding="utf-8")
    frontmatter = text.split("---", 2)
    if len(frontmatter) >= 3 and not frontmatter[0].strip():
        match = PERMALINK.search(frontmatter[1])
        if match:
            path = match.group(1)
            if path in permalinks:
                errors.append(f"Duplicate permalink {path}: {permalinks[path]} and {source.relative_to(ROOT)}")
            permalinks[path] = source.relative_to(ROOT)

    for match in ROOT_LINK.finditer(text):
        errors.append(f"{source.relative_to(ROOT)}: root-absolute link {match.group(1)}")
    for match in LINK.finditer(text):
        url = match.group(2)
        path = unquote(urlsplit(url).path)
        target = SITE / path.lstrip("/")
        if not (target.is_file() or (target / "index.html").is_file()):
            errors.append(f"{source.relative_to(ROOT)}: missing link target {url}")

if not SITE.is_dir():
    errors.append("The _site directory is missing; build the site first.")

if errors:
    print("\n".join(errors), file=sys.stderr)
    sys.exit(1)

print("Documentation link targets and permalinks are valid.")
