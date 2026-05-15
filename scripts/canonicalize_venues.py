#!/usr/bin/env python3
"""
Normalize venue strings: strip years / ordinals, merge aliases.

Updates venue_canonical in data/insait_publications_cv_and_people.json and writes
data/venues_canonical.json. Full venue lines are produced by format_venue_full_display.py.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
JSON_PATH = ROOT / "data" / "insait_publications_cv_and_people.json"
PUB_DIR = ROOT / "_publications"
OUTPUT_LIST = ROOT / "data" / "venues_canonical.json"

# Acronym (from parenthetical like "CVPR 2024") -> canonical venue name (no year, no ordinal)
ACRONYM_CANONICAL = {
    "CVPR": "IEEE/CVF Conference on Computer Vision and Pattern Recognition",
    "ICCV": "International Conference on Computer Vision",
    "ECCV": "European Conference on Computer Vision",
    "WACV": "Winter Conference on Applications of Computer Vision",
    "ICML": "International Conference on Machine Learning",
    "ICLR": "International Conference on Learning Representations",
    "NeurIPS": "Conference on Neural Information Processing Systems",
    "AAAI": "AAAI Conference on Artificial Intelligence",
    "BMVC": "British Machine Vision Conference",
    "CoRL": "Conference on Robot Learning",
    "IROS": "IEEE/RSJ International Conference on Intelligent Robots and Systems",
    "ICRA": "International Conference on Robotics and Automation",
    "3DV": "International Conference on 3D Vision",
    "3DIMPVT": "International Conference on 3D Imaging, Modeling, Processing, Visualization and Transmission",
    "MICCAI": "International Conference on Medical Image Computing and Computer Assisted Intervention",
    "ICIP": "International Conference on Image Processing",
    "ACCV": "Asian Conference on Computer Vision",
    "SIGGRAPH": "ACM SIGGRAPH Conference and Exhibition on Computer Graphics and Interactive Techniques in Asia",
    "ISMAR": "International Symposium on Mixed and Augmented Reality",
    "ICPR": "International Conference on Pattern Recognition",
    "ACL": "Annual Meeting of the Association for Computational Linguistics",
    "TMM": "IEEE Transactions on Multimedia",
}

ORDINAL_START = re.compile(
    r"^(the\s+)?("
    r"\d+(?:st|nd|rd|th)|"
    r"twenty-seventh|twenty-second|twenty-fifth|twenty-sixth|"
    r"forty-third|forty-second|fortieth|"
    r"eighteenth|fourteenth|thirty-ninth|"
    r"sixty-fourth|fifty-eighth|nineteenth"
    r")\s+",
    re.IGNORECASE,
)

PAREN_YEAR = re.compile(
    r"\(\s*([A-Za-z0-9][A-Za-z0-9/\s-]*?)\s+(20\d{2})\s*\)"
)


def is_workshop_venue(raw: str) -> bool:
    return bool(re.search(r"\bworkshop\b", raw, re.IGNORECASE))


def is_acl_findings(raw: str) -> bool:
    return bool(re.search(r"\bfindings\b", raw, re.IGNORECASE))


def is_neurips_dataset_track(raw: str) -> bool:
    low = raw.lower()
    return "dataset" in low and "benchmark" in low


def extract_acronym(raw: str) -> str | None:
    for m in PAREN_YEAR.finditer(raw):
        token = re.sub(r"\s+", "", m.group(1))
        if token in ACRONYM_CANONICAL:
            return token
    return None


def strip_years_and_acronym_parens(text: str) -> str:
    text = PAREN_YEAR.sub("", text)
    text = re.sub(r"\b20\d{2}\b", "", text)
    return text


def strip_ordinals(text: str) -> str:
    t = text
    while True:
        n = ORDINAL_START.sub("", t)
        if n == t:
            break
        t = n
    return t


def collapse_space(text: str) -> str:
    text = re.sub(r"\s+", " ", text).strip(" ,;")
    return text


def canonicalize(raw: str) -> tuple[str, bool]:
    """Return (canonical_venue_name, is_workshop)."""
    ws = is_workshop_venue(raw)
    findings = is_acl_findings(raw)
    neurips_ds = is_neurips_dataset_track(raw)

    # Journals and fixed names (check raw before stripping)
    u = raw.upper()
    if "IEEE TRANSACTIONS ON PATTERN ANALYSIS" in u or "PATTERN ANALYSIS AND MACHINE INTELLIGENCE" in u:
        return "IEEE Transactions on Pattern Analysis and Machine Intelligence", ws
    if "INTERNATIONAL JOURNAL OF COMPUTER VISION" in u:
        return "International Journal of Computer Vision", ws
    if "COMPUTER VISION AND IMAGE UNDERSTANDING" in u:
        return "Computer Vision and Image Understanding", ws
    if "IEEE ROBOTICS AND AUTOMATION LETTERS" in u or re.search(
        r"\bRA-L\b", raw
    ):
        return "IEEE Robotics and Automation Letters", ws
    if "IEEE TRANSACTIONS ON MULTIMEDIA" in u or re.search(r"\bTMM\b", raw):
        return "IEEE Transactions on Multimedia", ws

    if neurips_ds:
        return (
            "Conference on Neural Information Processing Systems "
            "(Datasets and Benchmarks Track)",
            ws,
        )

    if re.search(r"\bNeurIPS\b", raw, re.I) and not neurips_ds:
        return "Conference on Neural Information Processing Systems", ws

    ac = extract_acronym(raw)
    if ac and ac in ACRONYM_CANONICAL:
        base = ACRONYM_CANONICAL[ac]
        return base, ws

    # AAAI without year in parens (e.g. Technical Track)
    if re.search(r"AAAI\s+Conference\s+on\s+Artificial\s+Intelligence", raw, re.I):
        if re.search(r"Technical\s+Track", raw, re.I):
            return (
                "AAAI Conference on Artificial Intelligence "
                "(Technical Track on Computer Vision III)",
                ws,
            )
        return "AAAI Conference on Artificial Intelligence", ws

    # Fallback: strip noise and use cleaned remainder
    t = raw
    t = re.sub(r"\s*\([^)]*[Ww]orkshop[^)]*\)", "", t)
    t = strip_years_and_acronym_parens(t)
    t = strip_ordinals(t)
    t = re.sub(r"^in\s+", "", t, flags=re.IGNORECASE)
    t = re.sub(r"^the\s+", "", t, flags=re.IGNORECASE)
    t = collapse_space(t)
    t = re.sub(r",?\s*(datasets?\s+and\s+benchmarks?\s+track)\s*,?\s*$", "", t, flags=re.I)
    t = collapse_space(t)

    # Merge duplicate phrasing
    if re.search(r"Computer Vision and Pattern Recognition Conference", t, re.I):
        t = "IEEE/CVF Conference on Computer Vision and Pattern Recognition"
    elif re.search(r"^Conference on Computer Vision and Pattern Recognition", t, re.I):
        t = "IEEE/CVF Conference on Computer Vision and Pattern Recognition"

    if "computational linguistics" in t.lower() and findings:
        t = "Annual Meeting of the Association for Computational Linguistics"

    return collapse_space(t), ws


def venue_for_front_matter(canonical: str, is_ws: bool) -> str:
    if is_ws:
        return f"{canonical} (Workshop)"
    return canonical


def update_markdown_venue(path: Path, new_venue: str) -> bool:
    lines = path.read_text(encoding="utf-8").splitlines()
    out: list[str] = []
    dash_count = 0
    replaced = False
    for line in lines:
        if line.strip() == "---":
            dash_count += 1
            out.append(line)
            continue
        if dash_count == 1 and line.startswith("venue:"):
            out.append(f"venue: {json.dumps(new_venue, ensure_ascii=False)}")
            replaced = True
            continue
        out.append(line)
    if replaced:
        text = "\n".join(out)
        if not text.endswith("\n"):
            text += "\n"
        path.write_text(text, encoding="utf-8")
    return replaced


def main() -> None:
    data = json.loads(JSON_PATH.read_text(encoding="utf-8"))

    seen_main: set[str] = set()
    seen_ws: set[str] = set()

    for row in data:
        raw = row.get("venue_raw") or row.get("venue") or ""
        c, ws = canonicalize(raw)
        row["venue_canonical"] = c
        row.pop("venue_is_workshop", None)

        if ws:
            seen_ws.add(c)
        else:
            seen_main.add(c)

    JSON_PATH.write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    payload = {
        "main_venues": sorted(seen_main),
        "workshop_venues": sorted(seen_ws),
        "counts": {
            "main_distinct": len(seen_main),
            "workshop_distinct": len(seen_ws),
            "papers": len(data),
        },
    }
    OUTPUT_LIST.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    print(
        f"JSON updated (venue_canonical only): {JSON_PATH}\n"
        f"Canonical list: {OUTPUT_LIST}\n"
        f"Distinct main venues: {len(seen_main)}\n"
        f"Distinct workshop (base) venues: {len(seen_ws)}\n"
        f"Re-run scripts/format_venue_full_display.py to refresh venue strings and markdown."
    )


if __name__ == "__main__":
    main()
