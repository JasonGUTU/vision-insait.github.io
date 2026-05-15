#!/usr/bin/env python3
"""
Convert filtered publication JSON into _publications/*.md files for Jekyll.

Reads: data/insait_publications_cv_and_people.json
Writes: _publications/<slug>.md

Front matter includes: title, year, venue, venue_display, venue_chronicle
(JSON venue_canonical), venue_abbr, publication_date, author_line_full,
authors (person_id[]), paper_url when available.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PEOPLE_DIR = ROOT / "_people"
PUB_DIR = ROOT / "_publications"
DEFAULT_JSON = ROOT / "data" / "insait_publications_cv_and_people.json"


def norm_tokens(s: str) -> list[str]:
    s = s.lower()
    s = re.sub(r"[^a-z0-9\s]", " ", s)
    return [t for t in s.split() if t]


def person_matches_author(person: str, author: str) -> bool:
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


def load_people(people_dir: Path) -> list[tuple[str, str]]:
    rows: list[tuple[str, str]] = []
    for path in sorted(people_dir.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        if not text.startswith("---"):
            continue
        end = text.find("\n---", 3)
        if end == -1:
            continue
        front = text[3:end]
        person_id: str | None = None
        name_display: str | None = None
        for line in front.splitlines():
            line = line.strip()
            if line.startswith("person_id:"):
                person_id = line.split(":", 1)[1].strip()
            elif line.startswith("name_display:"):
                raw = line.split(":", 1)[1].strip()
                if raw.startswith('"') and raw.endswith('"'):
                    raw = raw[1:-1]
                elif raw.startswith("'") and raw.endswith("'"):
                    raw = raw[1:-1]
                name_display = raw
        if person_id and name_display:
            rows.append((person_id, name_display))
        else:
            raise ValueError(f"Missing person_id or name_display in {path}")
    return rows


def match_author_person_ids(author_strings: list[str], people: list[tuple[str, str]]) -> list[str]:
    ids: list[str] = []
    seen: set[str] = set()
    for a in author_strings:
        for pid, pname in people:
            if person_matches_author(pname, a) or person_matches_author(a, pname):
                if pid not in seen:
                    ids.append(pid)
                    seen.add(pid)
                break
    return ids


def slugify(title: str, year: int, used: set[str]) -> str:
    base = title.lower().strip()
    base = re.sub(r"[^a-z0-9]+", "-", base).strip("-")
    base = re.sub(r"-+", "-", base)
    if not base:
        base = f"publication-{year}"
    if len(base) > 100:
        base = base[:100].rstrip("-")
    cand = base
    counter = 0
    while cand in used:
        counter += 1
        cand = f"{base}-{year}-{counter}"
    used.add(cand)
    return cand


def yaml_escape(s: str) -> str:
    return json.dumps(s, ensure_ascii=False)


LINK_LABELS = [
    ("paper", "Paper"),
    ("project", "Project"),
    ("code", "Code"),
    ("slides", "Slides"),
    ("dataset", "Dataset"),
]


def primary_paper_url(links: dict) -> str | None:
    for key in ("paper", "project", "slides"):
        v = links.get(key)
        if v and isinstance(v, str):
            return v
    for k, v in sorted(links.items()):
        if k.startswith("other") and v:
            return v
    return None


def venue_abbr(venue: str | None) -> str | None:
    if not venue:
        return None
    u = venue.upper()
    compact = u.replace(" ", "")
    for abbr in (
        "CVPR",
        "ICCV",
        "ECCV",
        "WACV",
        "BMVC",
        "NTIRE",
        "ICIP",
        "ACCV",
        "3DV",
        "MICCAI",
        "ICLR",
        "ICML",
        "NEURIPS",
        "AAAI",
        "IJCV",
    ):
        if abbr in compact:
            return abbr
    if "IEEETRANSACTIONSONPATTERN" in compact.replace(".", ""):
        return "TPAMI"
    if "COMPUTERVISIONANDIMAGEUNDERSTANDING" in compact.replace(" ", ""):
        return "CVIU"
    if "IEEETRANSACTIONSONMULTIMEDIA" in compact.replace(" ", "") or "(TMM" in u:
        return "TMM"
    if "ROBOTICSANDAUTOMATIONLETTERS" in compact.replace(" ", ""):
        return "RA-L"
    if "INTELLIGENTROBOTSANDSYSTEMS" in compact.replace(" ", "") or "IROS" in compact:
        return "IROS"
    if "INTERNATIONALCONFERENCEONROBOTICSANDAUTOMATION" in compact.replace(" ", "") or "ICRA" in compact:
        return "ICRA"
    return None


def build_markdown(entry: dict, people: list[tuple[str, str]]) -> str:
    title = (entry.get("title") or "").strip()
    year = int(entry["year"])
    venue_display_val = (entry.get("venue_display") or "").strip()
    venue_storage = (entry.get("venue") or "").strip()
    authors = entry.get("authors") or []
    links = dict(entry.get("links") or {})
    note = entry.get("note")

    author_line_full = ", ".join(authors)
    author_ids = match_author_person_ids([str(x) for x in authors], people)

    display_line = venue_display_val or venue_storage
    primary_venue = venue_storage or venue_display_val

    fm: dict = {}
    fm["title"] = title
    fm["year"] = year
    if primary_venue:
        fm["venue"] = primary_venue
    if venue_display_val:
        fm["venue_display"] = venue_display_val
    elif display_line:
        fm["venue_display"] = display_line

    chronicle = (entry.get("venue_canonical") or "").strip()
    if chronicle:
        fm["venue_chronicle"] = chronicle

    ab = entry.get("venue_abbr")
    if ab is None or str(ab).strip() == "":
        ab = venue_abbr(display_line)
    if ab is not None and str(ab).strip():
        fm["venue_abbr"] = str(ab).strip()

    pub_date = entry.get("publication_date")
    if pub_date is not None and str(pub_date).strip():
        fm["publication_date"] = str(pub_date).strip()

    fm["author_line_full"] = author_line_full
    if author_ids:
        fm["authors"] = author_ids

    primary = primary_paper_url(links)
    if primary:
        fm["paper_url"] = primary

    lines = ["---"]
    for k, v in fm.items():
        if k == "authors" and isinstance(v, list):
            lines.append("authors:")
            for aid in v:
                lines.append(f"  - {aid}")
        elif isinstance(v, str):
            lines.append(f"{k}: {yaml_escape(v)}")
        elif isinstance(v, bool):
            lines.append(f"{k}: {str(v).lower()}")
        elif isinstance(v, int):
            lines.append(f"{k}: {v}")
        else:
            lines.append(f"{k}: {v}")
    lines.append("---")

    body_parts: list[str] = []
    link_lines: list[str] = []
    used_primary = primary
    for key, label in LINK_LABELS:
        url = links.get(key)
        if not url or not isinstance(url, str):
            continue
        if used_primary and url == used_primary:
            continue
        link_lines.append(f"- [{label}]({url})")
    for k, url in sorted(links.items()):
        if not k.startswith("other") or not url:
            continue
        if used_primary and url == used_primary:
            continue
        link_lines.append(f"- [Link]({url})")

    if link_lines:
        body_parts.append("## Links\n")
        body_parts.append("\n".join(link_lines))

    if note:
        if body_parts:
            body_parts.append("\n")
        ntxt = note if isinstance(note, str) else "; ".join(str(x) for x in note)
        body_parts.append(f"_Note:_ {ntxt}\n")

    body = "\n".join(body_parts).rstrip() + ("\n" if body_parts else "")
    return "\n".join(lines) + "\n" + body


def main() -> None:
    in_path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_JSON
    PUB_DIR.mkdir(parents=True, exist_ok=True)

    people = load_people(PEOPLE_DIR)
    with in_path.open(encoding="utf-8") as f:
        data = json.load(f)

    used_slugs: set[str] = set()
    written = 0
    for entry in data:
        slug = slugify(str(entry["title"]), int(entry["year"]), used_slugs)
        md = build_markdown(entry, people)
        (PUB_DIR / f"{slug}.md").write_text(md, encoding="utf-8")
        written += 1
        print(f"{written}/{len(data)} {slug}.md", flush=True)

    print(f"Done. Wrote {written} files under {PUB_DIR}")


if __name__ == "__main__":
    main()
