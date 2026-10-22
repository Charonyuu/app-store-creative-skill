#!/usr/bin/env python3
"""Validate ordered PNG store assets without third-party dependencies."""

from __future__ import annotations

import argparse
import re
import struct
import sys
from pathlib import Path


PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"


def read_png(path: Path) -> tuple[int, int, bool]:
    data = path.read_bytes()
    if not data.startswith(PNG_SIGNATURE) or len(data) < 33:
        raise ValueError("not a valid PNG")
    length = struct.unpack(">I", data[8:12])[0]
    if data[12:16] != b"IHDR" or length != 13:
        raise ValueError("missing PNG IHDR")
    width, height, _depth, color_type = struct.unpack(">IIBB", data[16:26])
    has_alpha = color_type in (4, 6)
    offset = 8
    while offset + 12 <= len(data):
        chunk_length = struct.unpack(">I", data[offset : offset + 4])[0]
        chunk_type = data[offset + 4 : offset + 8]
        if chunk_type == b"tRNS":
            has_alpha = True
        offset += 12 + chunk_length
        if chunk_type == b"IEND":
            break
    return width, height, has_alpha


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("folder", type=Path)
    parser.add_argument("--width", type=int)
    parser.add_argument("--height", type=int)
    parser.add_argument("--min-count", type=int, default=1)
    parser.add_argument("--max-count", type=int, default=10)
    parser.add_argument("--forbid-alpha", action="store_true")
    parser.add_argument("--require-numbered", action="store_true")
    args = parser.parse_args()

    if not args.folder.is_dir():
        print(f"ERROR: folder not found: {args.folder}", file=sys.stderr)
        return 2

    files = sorted(
        (p for p in args.folder.iterdir() if p.is_file() and p.suffix.lower() == ".png"),
        key=lambda p: p.name.lower(),
    )
    errors: list[str] = []
    if not args.min_count <= len(files) <= args.max_count:
        errors.append(
            f"expected {args.min_count}-{args.max_count} PNG files, found {len(files)}"
        )

    if args.require_numbered:
        prefixes = []
        for path in files:
            match = re.match(r"^(\d+)[-_]", path.name)
            if not match:
                errors.append(f"{path.name}: missing numeric ordering prefix")
                continue
            prefixes.append(int(match.group(1)))
        if prefixes and prefixes != list(range(prefixes[0], prefixes[0] + len(prefixes))):
            errors.append(f"numeric prefixes are not contiguous: {prefixes}")

    for path in files:
        try:
            width, height, has_alpha = read_png(path)
        except ValueError as exc:
            errors.append(f"{path.name}: {exc}")
            continue
        status = "alpha" if has_alpha else "opaque"
        print(f"{path.name}: {width}x{height}, {status}")
        if args.width is not None and width != args.width:
            errors.append(f"{path.name}: width {width}, expected {args.width}")
        if args.height is not None and height != args.height:
            errors.append(f"{path.name}: height {height}, expected {args.height}")
        if args.forbid_alpha and has_alpha:
            errors.append(f"{path.name}: alpha channel/transparency is not allowed")

    if errors:
        print("\nValidation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(f"\nOK: validated {len(files)} asset(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
