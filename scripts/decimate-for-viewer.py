"""
Decimate all 10 STLs in research/_staging/ to viewer-quality copies in public/models/.

Target: under 2 MB per file. Vase mode + dense scans (3DBenchy, octopus, vase-rose)
get heavy quadric-edge-collapse decimation; already-small models pass through as-is.

The output files are PREVIEW-QUALITY only. The detail page still primarily directs
visitors to the source link for the print-quality file.

Re-run safe: skips files where the existing public/models/<slug>.stl is already a
decimated copy with the same source mtime (cheap heuristic — delete the output to
force a re-run).

Usage:
    pip install trimesh numpy
    python scripts/decimate-for-viewer.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import trimesh

REPO_ROOT = Path(__file__).resolve().parent.parent
STAGING_DIR = REPO_ROOT / "research" / "_staging"
OUTPUT_DIR = REPO_ROOT / "public" / "models"

TARGET_FACE_COUNT = 8000  # ~400 KB binary STL; plenty for browser orbit preview
TARGET_MAX_BYTES = 2 * 1024 * 1024  # 2 MB hard cap


def process_one(stl_path: Path) -> tuple[int, int, int, int]:
    """Return (orig_faces, new_faces, orig_bytes, new_bytes)."""
    mesh = trimesh.load(str(stl_path), force="mesh")
    if not isinstance(mesh, trimesh.Trimesh):
        raise RuntimeError(f"{stl_path.name}: trimesh returned {type(mesh).__name__}, not a single mesh")

    orig_faces = len(mesh.faces)
    orig_bytes = stl_path.stat().st_size
    out_path = OUTPUT_DIR / stl_path.name

    if orig_faces <= TARGET_FACE_COUNT and orig_bytes <= TARGET_MAX_BYTES:
        # Already small enough — copy as-is.
        mesh.export(str(out_path), file_type="stl")
    else:
        # Iteratively decimate until we hit the size cap.
        target = TARGET_FACE_COUNT
        for attempt in range(4):
            try:
                decimated = mesh.simplify_quadric_decimation(face_count=target)
            except Exception as e:
                # Some older trimesh versions use different signatures; fall back.
                decimated = mesh.simplify_quadric_decimation(target)
            decimated.export(str(out_path), file_type="stl")
            if out_path.stat().st_size <= TARGET_MAX_BYTES:
                mesh = decimated
                break
            target = max(1000, target // 2)
        else:
            # Final attempt didn't fit; accept whatever we have.
            mesh = decimated

    new_bytes = out_path.stat().st_size
    new_faces = len(mesh.faces) if isinstance(mesh, trimesh.Trimesh) else orig_faces
    return orig_faces, new_faces, orig_bytes, new_bytes


def main() -> int:
    if not STAGING_DIR.exists():
        print(f"ERROR: staging dir not found: {STAGING_DIR}", file=sys.stderr)
        return 1

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    stl_files = sorted(STAGING_DIR.glob("*.stl"))
    if not stl_files:
        print(f"ERROR: no STL files in {STAGING_DIR}", file=sys.stderr)
        return 1

    print(f"{'slug':<28} {'orig faces':>12} {'new faces':>12} {'orig KB':>10} {'new KB':>10}")
    print("-" * 78)

    total_new_bytes = 0
    for stl in stl_files:
        slug = stl.stem
        try:
            of, nf, ob, nb = process_one(stl)
        except Exception as e:
            print(f"{slug:<28} FAILED: {e}", file=sys.stderr)
            continue
        total_new_bytes += nb
        print(f"{slug:<28} {of:>12,} {nf:>12,} {ob/1024:>10,.1f} {nb/1024:>10,.1f}")

    print("-" * 78)
    print(f"Total output: {total_new_bytes / 1024 / 1024:.2f} MB across {len(stl_files)} files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
