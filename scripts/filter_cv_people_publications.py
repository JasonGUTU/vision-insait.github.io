#!/usr/bin/env python3
"""
Filter insait_publications.json:
  - Keep if venue matches core CV conferences/journals, OR
  - Keep if any author matches _people/*.md name_display.

Writes JSON with added field "filter_reasons": list of "cv_venue" / "people_author".
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PEOPLE_DIR = ROOT / "_people"
DEFAULT_IN = ROOT / "data" / "insait_publications.json"
DEFAULT_OUT = ROOT / "data" / "insait_publications_cv_and_people.json"

# Case-insensitive substring match on venue (uppercased for acronyms, original for phrases)
CV_VENUE_SUBSTRINGS = (
    "CVPR",
    "ICCV",
    "ECCV",
    "WACV",
    "BMVC",
    "NTIRE",
    "ICIP",
    "ACCV",
    "3DV",
    "IEEE TRANSACTIONS ON PATTERN ANALYSIS AND MACHINE INTELLIGENCE",
    "PATTERN ANALYSIS AND MACHINE INTELLIGENCE",
    "COMPUTER VISION AND IMAGE UNDERSTANDING",
    "IEEE TRANSACTIONS ON MULTIMEDIA",
    "INTERNATIONAL CONFERENCE ON 3D VISION",
    "INTERNATIONAL CONFERENCE ON 3D IMPVT",
    "3DIMPVT",
    # Full / long names that are specific enough
    "COMPUTER VISION AND PATTERN RECOGNITION",
    "INTERNATIONAL CONFERENCE ON COMPUTER VISION",
    "EUROPEAN CONFERENCE ON COMPUTER VISION",
    "WINTER CONFERENCE ON APPLICATIONS OF COMPUTER VISION",
    "IEEE/CVF CONFERENCE ON COMPUTER VISION",
    "BRITISH MACHINE VISION CONFERENCE",
)


def load_people_names(people_dir: Path) -> list[str]:
    names: list[str] = []
    for path in sorted(people_dir.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        if not text.startswith("---"):
            continue
        end = text.find("\n---", 3)
        if end == -1:
            continue
        front = text[3:end]
        for line in front.splitlines():
            line = line.strip()
            if line.startswith("name_display:"):
                raw = line.split(":", 1)[1].strip()
                if raw.startswith('"') and raw.endswith('"'):
                    raw = raw[1:-1]
                elif raw.startswith("'") and raw.endswith("'"):
                    raw = raw[1:-1]
                if raw:
                    names.append(raw)
                break
        else:
            raise ValueError(f"No name_display in {path}")
    return names


def norm_tokens(s: str) -> list[str]:
    s = s.lower()
    s = re.sub(r"[^a-z0-9\s]", " ", s)
    return [t for t in s.split() if t]


def person_matches_author(person: str, author: str) -> bool:
    """True if person name tokens appear in order as a subsequence of author tokens."""
    pa, aa = norm_tokens(person), norm_tokens(author)
    if not pa or not aa:
        return False
    i = 0
    for t in pa:
        while i < len(aa) and aa[i] != t:
            i += 1
        if i >= len(aa):
            return False
        i += 1
    return True


def author_in_people(author: str, people: list[str]) -> bool:
    for p in people:
        if person_matches_author(p, author):
            return True
        # Allow reversed coverage: scraped person longer than site author list
        if person_matches_author(author, p):
            return True
    return False


def venue_is_cv(venue: str | None) -> bool:
    if not venue:
        return False
    u = venue.upper()
    for marker in CV_VENUE_SUBSTRINGS:
        if marker in u:
            return True
    return False


def filter_publications(rows: list[dict], people: list[str]) -> list[dict]:
    out: list[dict] = []
    for row in rows:
        venue = row.get("venue")
        reasons: list[str] = []
        matched: list[str] = []

        if venue_is_cv(venue):
            reasons.append("cv_venue")

        authors = row.get("authors") or []
        for a in authors:
            if author_in_people(str(a), people):
                matched.append(str(a))
        if matched:
            reasons.append("people_author")

        if not reasons:
            continue

        item = dict(row)
        item["filter_reasons"] = sorted(set(reasons))
        item["matched_people_authors"] = sorted(set(matched))
        out.append(item)
    return out


def main() -> None:
    in_path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_IN
    out_path = Path(sys.argv[2]) if len(sys.argv) > 2 else DEFAULT_OUT

    people = load_people_names(PEOPLE_DIR)
    with in_path.open(encoding="utf-8") as f:
        data = json.load(f)

    filtered = filter_publications(data, people)
    with out_path.open("w", encoding="utf-8") as f:
        json.dump(filtered, f, ensure_ascii=False, indent=2)
        f.write("\n")

    print(f"People entries: {len(people)}")
    print(f"Input: {len(data)} → kept: {len(filtered)} → {out_path}")


if __name__ == "__main__":
    main()
