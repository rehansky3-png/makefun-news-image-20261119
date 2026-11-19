#!/usr/bin/env python3
"""news-image-20261119: copy the pre-drawn front page to the output dir.

The image (1024x1024 PNG, "THE WORLD — Thursday 19 November 2026") was
drawn with Pillow during development and is stored next to this file as
entry.png. This program is stdlib-only: it just copies that file to
$MAKEFUN_OUTPUT_DIR/entry.png, so both runs write identical bytes.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


MAX_BYTES = 1048576  # competition limit: at most 1 MiB


def main():
    src = os.path.join(HERE, "entry.png")
    if not os.path.isfile(src):
        raise SystemExit("entry.png missing next to main.py")
    if os.path.getsize(src) > MAX_BYTES:
        raise SystemExit("entry.png exceeds the 1 MiB limit")
    os.makedirs(OUT, exist_ok=True)
    shutil.copyfile(src, os.path.join(OUT, "entry.png"))


if __name__ == "__main__":
    main()
