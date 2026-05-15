#!/usr/bin/env python3
"""
Add venue_abbr and publication_date to each entry in insait_publications_cv_and_people.json.

publication_date: ISO YYYY-MM-DD. Source data has no exact day; we use typical conference
month/day per venue_canonical when known, else mid-year. Precision is indicative only.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
JSON_PATH = ROOT / "data" / "insait_publications_cv_and_people.json"

# Exact match on venue_canonical (as produced by canonicalize_venues.py)
CANONICAL_TO_ABBR: dict[str, str] = {
    "AAAI Conference on Artificial Intelligence": "AAAI",
    "AAAI Conference on Artificial Intelligence (Technical Track on Computer Vision III)": "AAAI-CV",
    "ACM SIGGRAPH Conference and Exhibition on Computer Graphics and Interactive Techniques in Asia": "SIGGRAPH Asia",
    "Annual Meeting of the Association for Computational Linguistics": "ACL",
    "Asian Conference on Computer Vision": "ACCV",
    "British Machine Vision Conference": "BMVC",
    "Computer Vision and Image Understanding": "CVIU",
    "Conference on Neural Information Processing Systems": "NeurIPS",
    "Conference on Neural Information Processing Systems (Datasets and Benchmarks Track)": "NeurIPS DB",
    "Conference on Robot Learning": "CoRL",
    "European Conference on Computer Vision": "ECCV",
    "IEEE Robotics and Automation Letters": "RA-L",
    "IEEE Transactions on Multimedia": "IEEE TMM",
    "IEEE Transactions on Pattern Analysis and Machine Intelligence": "TPAMI",
    "IEEE/CVF Conference on Computer Vision and Pattern Recognition": "CVPR",
    "IEEE/RSJ International Conference on Intelligent Robots and Systems": "IROS",
    "International Conference on 3D Imaging, Modeling, Processing, Visualization and Transmission": "3DIMPVT",
    "International Conference on 3D Vision": "3DV",
    "International Conference on Computer Vision": "ICCV",
    "International Conference on Image Processing": "ICIP",
    "International Conference on Learning Representations": "ICLR",
    "International Conference on Machine Learning": "ICML",
    "International Conference on Medical Image Computing and Computer Assisted Intervention": "MICCAI",
    "International Conference on Pattern Recognition": "ICPR",
    "International Conference on Robotics and Automation": "ICRA",
    "International Journal of Computer Vision": "IJCV",
    "International Symposium on Mixed and Augmented Reality": "ISMAR",
    "Winter Conference on Applications of Computer Vision": "WACV",
}

# Typical (month, day) for conference-style venues; journals use (12, 1).
VENUE_TYPICAL_MD: dict[str, tuple[int, int]] = {
    "AAAI Conference on Artificial Intelligence": (2, 15),
    "AAAI Conference on Artificial Intelligence (Technical Track on Computer Vision III)": (2, 15),
    "ACM SIGGRAPH Conference and Exhibition on Computer Graphics and Interactive Techniques in Asia": (12, 1),
    "Annual Meeting of the Association for Computational Linguistics": (7, 15),
    "Asian Conference on Computer Vision": (12, 1),
    "British Machine Vision Conference": (11, 20),
    "Computer Vision and Image Understanding": (12, 1),
    "Conference on Neural Information Processing Systems": (12, 10),
    "Conference on Neural Information Processing Systems (Datasets and Benchmarks Track)": (12, 10),
    "Conference on Robot Learning": (11, 6),
    "European Conference on Computer Vision": (9, 29),
    "IEEE Robotics and Automation Letters": (6, 1),
    "IEEE Transactions on Multimedia": (12, 1),
    "IEEE Transactions on Pattern Analysis and Machine Intelligence": (12, 1),
    "IEEE/CVF Conference on Computer Vision and Pattern Recognition": (6, 15),
    "IEEE/RSJ International Conference on Intelligent Robots and Systems": (10, 14),
    "International Conference on 3D Imaging, Modeling, Processing, Visualization and Transmission": (6, 1),
    "International Conference on 3D Vision": (3, 18),
    "International Conference on Computer Vision": (10, 13),
    "International Conference on Image Processing": (10, 13),
    "International Conference on Learning Representations": (5, 1),
    "International Conference on Machine Learning": (7, 21),
    "International Conference on Medical Image Computing and Computer Assisted Intervention": (10, 6),
    "International Conference on Pattern Recognition": (8, 15),
    "International Conference on Robotics and Automation": (5, 19),
    "International Journal of Computer Vision": (12, 1),
    "International Symposium on Mixed and Augmented Reality": (10, 16),
    "Winter Conference on Applications of Computer Vision": (3, 3),
}

DEFAULT_MD = (6, 15)


def venue_abbr_for(canonical: str) -> str:
    if canonical in CANONICAL_TO_ABBR:
        return CANONICAL_TO_ABBR[canonical]
    # Safe fallback: first acronym-like token
    return "UNK"


def publication_date_for(year: int, canonical: str) -> str:
    month, day = VENUE_TYPICAL_MD.get(canonical, DEFAULT_MD)
    return f"{year:04d}-{month:02d}-{day:02d}"


def main() -> None:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else JSON_PATH
    data = json.loads(path.read_text(encoding="utf-8"))
    missing_abbr: set[str] = set()

    for row in data:
        canonical = row.get("venue_canonical") or ""
        year = int(row.get("year", 0))
        if canonical in CANONICAL_TO_ABBR:
            abbr = CANONICAL_TO_ABBR[canonical]
        else:
            abbr = "UNK"
            if canonical:
                missing_abbr.add(canonical)
        row["venue_abbr"] = abbr
        row["publication_date"] = publication_date_for(year, canonical)

    if missing_abbr:
        print(
            "WARN: venue_canonical without abbr mapping (set to UNK):",
            file=sys.stderr,
        )
        for s in sorted(missing_abbr):
            print(f"  {s}", file=sys.stderr)

    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Updated {len(data)} entries in {path}")


if __name__ == "__main__":
    main()
