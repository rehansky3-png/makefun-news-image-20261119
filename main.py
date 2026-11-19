#!/usr/bin/env python3
"""Publish the 19 November 2026 front page.

The front page itself is a finished 1024x1024 PNG stored next to this
script as entry.png. This program does nothing clever: it checks that the
image is present and inside the competition's one-mebibyte limit, then
places an exact copy of it in the output directory. The copy is byte for
byte the same file, so running the program twice always yields the same
result. Nothing in the image is generated at run time: the program ships
the finished picture exactly as drawn.

The destination comes from the MAKEFUN_OUTPUT_DIR environment variable;
when that variable is not set, /output is used.
"""

import os
import shutil
import sys

IMAGE_NAME = "entry.png"
SIZE_LIMIT = 1024 * 1024  # one mebibyte, the competition cap


def fail(message):
    """Print an error to stderr and stop with a non-zero status."""
    print("main.py: " + message, file=sys.stderr)
    raise SystemExit(1)


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(script_dir, IMAGE_NAME)

    if not os.path.exists(source):
        fail("cannot find " + IMAGE_NAME + " next to main.py")

    if os.path.getsize(source) > SIZE_LIMIT:
        fail(IMAGE_NAME + " is larger than the 1 MiB limit")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)

    shutil.copyfile(source, os.path.join(out_dir, IMAGE_NAME))


if __name__ == "__main__":
    main()
