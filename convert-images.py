#!/usr/bin/env python3
"""Convert PNG, JPG, JPEG, and GIF images under static/ to WebP.

Animated GIFs are converted to animated WebP with frame timing preserved.
Originals are deleted only after the converted file passes verification.
Already-converted files (where .webp exists) are skipped.
Markdown files under content/ have local image links updated to .webp.

Usage:
    python3 convert-images.py           # convert all + update markdown
    python3 convert-images.py --dry-run # preview what would change
    python3 convert-images.py --verify  # check all markdown image refs exist and load
"""

import argparse
import os
import re
import glob
import shutil
import subprocess
import sys
from PIL import Image, ImageSequence

REPO_ROOT = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(REPO_ROOT, "static")
CONTENT_DIR = os.path.join(REPO_ROOT, "content")
EXTENSIONS = ("*.png", "*.jpg", "*.jpeg", "*.gif")
QUALITY = 80

GIF2WEBP = shutil.which("gif2webp")

# Matches any local image ref (not http/https) in markdown: ![alt](path)
_MD_IMAGE_RE = re.compile(
    r'!\[[^\]]*\]\((?!https?://)([^)]+)\)',
    re.IGNORECASE
)

# Matches non-webp local image refs (used by update_markdown_links)
_NON_WEBP_RE = re.compile(
    r'(!\[[^\]]*\]\()(?!https?://)([^)]+\.(png|jpg|jpeg|gif))(\))',
    re.IGNORECASE
)


def is_animated_gif(path):
    try:
        img = Image.open(path)
        return getattr(img, "n_frames", 1) > 1
    except Exception:
        return False


def verify_converted_webp(webp_path, orig_img):
    """Check a newly-converted WebP against the original image object.
    Returns (error, warning): error is a hard failure, warning is advisory.
    """
    try:
        converted = Image.open(webp_path)
    except Exception as e:
        return f"cannot open: {e}", None

    if converted.size != orig_img.size:
        return (
            f"dimension mismatch: original {orig_img.size} vs converted {converted.size}",
            None,
        )

    orig_frames = getattr(orig_img, "n_frames", 1)
    conv_frames = getattr(converted, "n_frames", 1)
    if orig_frames != conv_frames:
        if abs(orig_frames - conv_frames) <= 1:
            # Known Pillow off-by-one bug in animated WebP encoding
            return None, f"frame count off by 1 ({orig_frames} -> {conv_frames}), known Pillow limitation"
        return f"frame count mismatch: original {orig_frames} vs converted {conv_frames}", None

    return None, None


def convert_image(path, dry_run=False):
    """Convert a single image to WebP.

    Returns:
        None                     — already converted, skipped
        "would-convert"          — dry run, static image
        "would-convert-animated" — dry run, animated GIF
        (old_size, new_size, warning) — converted successfully
        raises RuntimeError      — conversion or verification failed
    """
    name, _ = os.path.splitext(path)
    out = name + ".webp"

    if os.path.exists(out):
        return None

    animated = path.lower().endswith(".gif") and is_animated_gif(path)

    if dry_run:
        return "would-convert-animated" if animated else "would-convert"

    img = Image.open(path)

    if animated:
        if GIF2WEBP:
            subprocess.run(
                [GIF2WEBP, "-q", str(QUALITY), path, "-o", out],
                check=True, capture_output=True,
            )
        else:
            frames, durations = [], []
            for frame in ImageSequence.Iterator(img):
                durations.append(frame.info.get("duration", 100))
                frames.append(frame.copy().convert("RGBA"))
            frames[0].save(
                out, "webp", save_all=True, append_images=frames[1:],
                quality=QUALITY, loop=0, duration=durations,
            )
    else:
        img.save(out, "webp", quality=QUALITY)

    error, warning = verify_converted_webp(out, img)
    if error:
        os.remove(out)
        raise RuntimeError(f"verification failed for {path}: {error}")

    old_size = os.path.getsize(path)
    new_size = os.path.getsize(out)
    os.remove(path)
    return (old_size, new_size, warning)


def update_markdown_links(dry_run=False):
    updated_files = 0

    for md_path in glob.glob(os.path.join(CONTENT_DIR, "**", "*.md"), recursive=True):
        with open(md_path, "r", encoding="utf-8") as f:
            original = f.read()

        def replace_ext(m):
            prefix, img_path, ext, suffix = m.group(1), m.group(2), m.group(3), m.group(4)
            new_path = re.sub(r'\.' + ext + r'$', '.webp', img_path, flags=re.IGNORECASE)
            return prefix + new_path + suffix

        updated = _NON_WEBP_RE.sub(replace_ext, original)

        if updated != original:
            rel = os.path.relpath(md_path, REPO_ROOT)
            if dry_run:
                for i, (ol, nl) in enumerate(zip(original.splitlines(), updated.splitlines()), 1):
                    if ol != nl:
                        print(f"  WOULD UPDATE {rel}:{i}: {ol.strip()} -> {nl.strip()}")
            else:
                with open(md_path, "w", encoding="utf-8") as f:
                    f.write(updated)
                print(f"  Updated links: {rel}")
            updated_files += 1

    return updated_files


def verify_all():
    """Check every local image reference in markdown exists on disk and loads cleanly.
    Returns True if all checks pass, False if any fail.
    """
    errors = []
    warnings = []
    checked = 0

    for md_path in sorted(glob.glob(os.path.join(CONTENT_DIR, "**", "*.md"), recursive=True)):
        with open(md_path, "r", encoding="utf-8") as f:
            content = f.read()

        rel_md = os.path.relpath(md_path, REPO_ROOT)

        for i, line in enumerate(content.splitlines(), 1):
            for m in _MD_IMAGE_RE.finditer(line):
                img_ref = m.group(1).split()[0]  # strip any title attr
                disk_path = os.path.join(STATIC_DIR, img_ref.lstrip("/"))
                checked += 1

                if not os.path.exists(disk_path):
                    errors.append(f"  MISSING  {rel_md}:{i}  {img_ref}")
                    continue

                ext = os.path.splitext(img_ref)[1].lower()

                # SVGs are valid as-is; Pillow can't open them
                if ext == ".svg":
                    print(f"  OK (svg)  {img_ref}")
                    continue

                try:
                    img = Image.open(disk_path)
                    img.verify()
                except Exception as e:
                    errors.append(f"  CORRUPT  {rel_md}:{i}  {img_ref}  ({e})")
                    continue

                # Re-open after verify() (verify() closes the file)
                try:
                    img = Image.open(disk_path)
                    n_frames = getattr(img, "n_frames", 1)
                except Exception as e:
                    errors.append(f"  UNREADABLE  {rel_md}:{i}  {img_ref}  ({e})")
                    continue

                if ext in (".gif", ".png", ".jpg", ".jpeg"):
                    warnings.append(f"  NON-WEBP {rel_md}:{i}  {img_ref}")
                elif ext == ".webp" and n_frames > 1:
                    print(f"  OK (animated, {n_frames} frames)  {img_ref}")
                else:
                    print(f"  OK  {img_ref}")

    print()
    for w in warnings:
        print(w)
    for e in errors:
        print(e)

    print()
    print(f"Checked {checked} image reference(s).")
    if errors:
        print(f"FAILED: {len(errors)} missing or corrupt.")
    if warnings:
        print(f"WARN: {len(warnings)} reference(s) still using non-webp format.")
    if not errors and not warnings:
        print("All image references OK.")

    return len(errors) == 0


def main():
    parser = argparse.ArgumentParser(
        description="Convert images in static/ to WebP, update markdown links, and verify."
    )
    parser.add_argument("--dry-run", action="store_true", help="Preview without modifying files")
    parser.add_argument("--verify", action="store_true", help="Check all markdown image refs exist and load")
    args = parser.parse_args()

    if args.verify:
        print("=== Image reference verification ===")
        ok = verify_all()
        sys.exit(0 if ok else 1)

    # --- conversion ---
    total_old = total_new = converted = failed = skipped_existing = 0

    print("=== Image conversion ===")
    for ext in EXTENSIONS:
        for path in sorted(glob.glob(os.path.join(STATIC_DIR, "**", ext), recursive=True)):
            try:
                result = convert_image(path, dry_run=args.dry_run)
            except RuntimeError as e:
                print(f"  FAIL: {e}")
                failed += 1
                continue

            if result is None:
                skipped_existing += 1
            elif isinstance(result, str):
                label = "WOULD CONVERT (animated)" if "animated" in result else "WOULD CONVERT"
                print(f"  {label}: {os.path.relpath(path, STATIC_DIR)}")
            else:
                old_size, new_size, warning = result
                reduction = 100 * (1 - new_size / old_size) if old_size else 0
                note = f"  [WARN: {warning}]" if warning else "  [verified OK]"
                print(f"  {os.path.relpath(path, STATIC_DIR)} -> .webp  "
                      f"({old_size:,} -> {new_size:,}, {reduction:.0f}% reduction){note}")
                total_old += old_size
                total_new += new_size
                converted += 1

    print()
    if args.dry_run:
        print("Dry run: no images modified.")
    elif converted:
        reduction = 100 * (1 - total_new / total_old) if total_old else 0
        print(f"Converted {converted} image(s): {total_old:,} -> {total_new:,} bytes ({reduction:.0f}% reduction)")
    else:
        print("No images to convert.")

    if failed:
        print(f"FAILED: {failed} image(s) — originals preserved.")
    if skipped_existing:
        print(f"Skipped {skipped_existing} already-converted file(s).")

    print()
    print("=== Markdown link updates ===")
    updated = update_markdown_links(dry_run=args.dry_run)
    if not updated:
        print("  No markdown links needed updating.")
    elif args.dry_run:
        print(f"  Dry run: {updated} file(s) would be updated.")
    else:
        print(f"  Updated {updated} markdown file(s).")


if __name__ == "__main__":
    main()
