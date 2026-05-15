#!/usr/bin/env python3
"""
Format venue, venue_display, venue_abbr, venue_raw; strip Findings markers from titles.

Uses original venue from insait_publications.json for workshop/findings detection only;
display names use the concise canonical title only (no edition/ordinal prefix).
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FILTERED_PATH = ROOT / "data" / "insait_publications_cv_and_people.json"
FULL_PATH = ROOT / "data" / "insait_publications.json"
PUB_DIR = ROOT / "_publications"

sys.path.insert(0, str(Path(__file__).resolve().parent))

from canonicalize_venues import (  # noqa: E402
    canonicalize,
    is_acl_findings,
    is_workshop_venue,
)

FINDINGS_IN_TITLE = re.compile(r"\s*\(\s*findings\s*\)\s*$", re.IGNORECASE)

# venue_canonical (after canonicalize) -> string inside ( ... YEAR )
ABBREV_PARENS: dict[str, str] = {
    "AAAI Conference on Artificial Intelligence": "AAAI",
    "AAAI Conference on Artificial Intelligence (Technical Track on Computer Vision III)": "AAAI-CV",
    "ACM SIGGRAPH Conference and Exhibition on Computer Graphics and Interactive Techniques in Asia": "SIGGRAPH Asia",
    "Annual Meeting of the Association for Computational Linguistics": "ACL",
    "Asian Conference on Computer Vision": "ACCV",
    "British Machine Vision Conference": "BMVC",
    "Computer Vision and Image Understanding": "CVIU",
    "Conference on Neural Information Processing Systems": "NeurIPS",
    "Conference on Neural Information Processing Systems (Datasets and Benchmarks Track)": "NeurIPS",
    "Conference on Robot Learning": "CoRL",
    "European Conference on Computer Vision": "ECCV",
    "IEEE Robotics and Automation Letters": "RA-L",
    "IEEE Transactions on Multimedia": "TMM",
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


def concise_for_canonical(canno: str) -> str:
    """Same as venue_canonical (already concise, no The)."""
    return canno


def base_abbrev(canno: str) -> str:
    return ABBREV_PARENS.get(canno, "UNK")


def abbrev_for_parens(canno: str, is_ws: bool) -> str:
    """Workshop papers use a trailing W (e.g. CVPRW, CAPRW)."""
    a = base_abbrev(canno)
    if a == "UNK":
        return "UNK" + ("W" if is_ws else "")
    return a + ("W" if is_ws else "")


def display_suffix_after_year(is_ws: bool, is_findings: bool) -> str:
    parts: list[str] = []
    if is_ws:
        parts.append("Workshop")
    if is_findings:
        parts.append("Findings")
    return ("" if not parts else " " + " ".join(parts))


def build_venue_pair(
    canno: str,
    year: int,
    is_ws: bool,
    is_findings: bool,
) -> tuple[str, str, str]:
    """
    Returns (venue, venue_display, venue_abbr).

    venue vs venue_display differ for Findings (short name vs full line) and
    Workshops (trailing \" Workshop\" only on display).
    """
    concise = concise_for_canonical(canno)
    ab = base_abbrev(canno)
    abp = abbrev_for_parens(canno, is_ws)
    parens = f"({abp} {year})"
    venue_abbr = abbrev_for_parens(canno, is_ws)

    if is_findings:
        short_name = ab if ab != "UNK" else concise
        venue = short_name
        venue_display = f"{short_name} {parens}" + display_suffix_after_year(is_ws, True)
        return venue, venue_display, venue_abbr

    if is_ws:
        venue = f"{concise} Workshop {parens}"
        venue_display = venue + display_suffix_after_year(True, False)
        return venue, venue_display, venue_abbr

    venue = f"{concise} {parens}"
    return venue, venue, ab


def publication_date_for(year: int, canonical: str) -> str:
    month, day = VENUE_TYPICAL_MD.get(canonical, DEFAULT_MD)
    return f"{year:04d}-{month:02d}-{day:02d}"


def update_md_frontmatter(path: Path, new_title: str | None, new_venue: str) -> None:
    lines = path.read_text(encoding="utf-8").splitlines()
    out: list[str] = []
    dash = 0
    title_done = False
    venue_done = False
    for line in lines:
        if line.strip() == "---":
            dash += 1
            out.append(line)
            continue
        if dash == 1 and new_title is not None and line.startswith("title:") and not title_done:
            out.append(f"title: {json.dumps(new_title, ensure_ascii=False)}")
            title_done = True
            continue
        if dash == 1 and line.startswith("venue:") and not venue_done:
            out.append(f"venue: {json.dumps(new_venue, ensure_ascii=False)}")
            venue_done = True
            continue
        out.append(line)
    text = "\n".join(out)
    if not text.endswith("\n"):
        text += "\n"
    path.write_text(text, encoding="utf-8")


def main() -> None:
    full_data = json.loads(FULL_PATH.read_text(encoding="utf-8"))
    venue_source: dict[tuple[str, int], str] = {}
    for row in full_data:
        venue_source[(row["title"], int(row["year"]))] = row.get("venue") or ""

    data = json.loads(FILTERED_PATH.read_text(encoding="utf-8"))
    md_index: dict[tuple[str, int], dict] = {}

    for row in data:
        key = (row["title"], int(row["year"]))
        otitle = row["title"]
        raw = venue_source.get(key) or row.get("venue_raw") or row.get("venue") or ""

        if FINDINGS_IN_TITLE.search(row["title"]):
            row["title"] = FINDINGS_IN_TITLE.sub("", row["title"]).strip()

        row["venue_raw"] = raw
        is_findings = is_acl_findings(raw) or bool(FINDINGS_IN_TITLE.search(otitle))
        is_ws = is_workshop_venue(raw)
        canno, _ws_from_canon = canonicalize(raw)
        row["venue_canonical"] = canno
        row.pop("venue_is_workshop", None)

        y = int(row["year"])
        venue, venue_display, v_abbr = build_venue_pair(
            canno, y, is_ws, is_findings
        )
        row["venue"] = venue
        row["venue_display"] = venue_display
        row["venue_abbr"] = v_abbr
        row["publication_date"] = publication_date_for(y, canno)

        rec = {"venue": venue_display, "title": row["title"]}
        md_index[(row["title"], y)] = rec
        if otitle != row["title"]:
            md_index[(otitle, y)] = rec

    FILTERED_PATH.write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    updated = 0
    for path in sorted(PUB_DIR.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        parts = text.split("---", 2)
        if len(parts) < 3:
            continue
        header = parts[1]
        tm = re.search(r"^title:\s*(.+)$", header, re.M)
        ym = re.search(r"^year:\s*(\d+)\s*$", header, re.M)
        if not tm or not ym:
            continue
        tr = tm.group(1).strip()
        if tr.startswith('"') and tr.endswith('"'):
            try:
                t = json.loads(tr)
            except json.JSONDecodeError:
                t = tr[1:-1]
        elif tr.startswith("'") and tr.endswith("'"):
            t = tr[1:-1]
        else:
            t = tr
        y = int(ym.group(1))

        rec = md_index.get((t, y))
        if not rec:
            t2 = FINDINGS_IN_TITLE.sub("", t).strip()
            rec = md_index.get((t2, y))
        if not rec:
            continue
        update_md_frontmatter(
            path,
            rec["title"] if rec["title"] != t else None,
            rec["venue"],
        )
        updated += 1

    print(f"Updated {len(data)} JSON rows and {updated} markdown files.")


if __name__ == "__main__":
    main()
