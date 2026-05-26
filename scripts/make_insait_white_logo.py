"""Generate a white-on-transparent variant of the INSAIT logo.

Reads the colored, transparent-background INSAIT logo and rewrites every
non-fully-transparent pixel as white while preserving its alpha channel.
The resulting PNG is suitable for use on dark backgrounds.

Usage:
    python scripts/make_insait_white_logo.py
"""

from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image

REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SRC = REPO_ROOT / "assets/images/logo/insait-trans.png"
DEFAULT_DST = REPO_ROOT / "assets/images/logo/insait-trans-white.png"


def make_white_variant(src: Path, dst: Path) -> None:
    img = Image.open(src).convert("RGBA")
    pixels = img.load()
    width, height = img.size
    # Rewrite RGB to white; keep the per-pixel alpha so anti-aliased
    # edges remain smooth on dark backgrounds.
    for y in range(height):
        for x in range(width):
            r, g, b, a = pixels[x, y]
            pixels[x, y] = (255, 255, 255, a)
    dst.parent.mkdir(parents=True, exist_ok=True)
    img.save(dst, format="PNG", optimize=True)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--src", type=Path, default=DEFAULT_SRC)
    parser.add_argument("--dst", type=Path, default=DEFAULT_DST)
    args = parser.parse_args()
    make_white_variant(args.src, args.dst)
    print(f"Wrote {args.dst.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    main()
