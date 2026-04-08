#!/usr/bin/env python3
"""Convert PNG, JPG, JPEG, and static GIF images under static/ to WebP.

Animated GIFs are skipped (WebP animation is often larger).
Originals are deleted after successful conversion.
Already-converted files (where .webp exists) are skipped.

Usage:
    python3 convert-images.py          # convert all
    python3 convert-images.py --dry-run # preview what would be converted
"""

import argparse
import os
import glob
from PIL import Image

STATIC_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "static")
EXTENSIONS = ("*.png", "*.jpg", "*.jpeg", "*.gif")
QUALITY = 80


def is_animated_gif(path):
    try:
        img = Image.open(path)
        return getattr(img, "n_frames", 1) > 1
    except Exception:
        return False


def convert_image(path, dry_run=False):
    name, _ = os.path.splitext(path)
    out = name + ".webp"

    if os.path.exists(out):
        return None  # already converted

    if path.lower().endswith(".gif") and is_animated_gif(path):
        return "skip-animated"

    if dry_run:
        return "would-convert"

    img = Image.open(path)
    img.save(out, "webp", quality=QUALITY)

    old_size = os.path.getsize(path)
    new_size = os.path.getsize(out)
    os.remove(path)
    return (old_size, new_size)


def main():
    parser = argparse.ArgumentParser(description="Convert images in static/ to WebP")
    parser.add_argument("--dry-run", action="store_true", help="Preview without converting")
    args = parser.parse_args()

    total_old = 0
    total_new = 0
    converted = 0
    skipped_animated = 0
    skipped_existing = 0

    for ext in EXTENSIONS:
        for path in sorted(glob.glob(os.path.join(STATIC_DIR, "**", ext), recursive=True)):
            result = convert_image(path, dry_run=args.dry_run)

            if result is None:
                skipped_existing += 1
            elif result == "skip-animated":
                print(f"  SKIP (animated): {os.path.relpath(path, STATIC_DIR)}")
                skipped_animated += 1
            elif result == "would-convert":
                print(f"  WOULD CONVERT:   {os.path.relpath(path, STATIC_DIR)}")
            else:
                old_size, new_size = result
                reduction = 100 * (1 - new_size / old_size) if old_size else 0
                print(f"  {os.path.relpath(path, STATIC_DIR)} -> .webp  "
                      f"({old_size:,} -> {new_size:,}, {reduction:.0f}% reduction)")
                total_old += old_size
                total_new += new_size
                converted += 1

    print()
    if args.dry_run:
        print("Dry run complete. No files were modified.")
    elif converted:
        reduction = 100 * (1 - total_new / total_old) if total_old else 0
        print(f"Converted {converted} images: {total_old:,} -> {total_new:,} bytes "
              f"({reduction:.0f}% total reduction)")
    else:
        print("No images to convert.")

    if skipped_animated:
        print(f"Skipped {skipped_animated} animated GIF(s).")
    if skipped_existing:
        print(f"Skipped {skipped_existing} already-converted file(s).")


if __name__ == "__main__":
    main()
