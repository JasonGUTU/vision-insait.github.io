#!/usr/bin/env python3
"""Sync _people markdown bios from scraped INSAIT HTML pages."""

from __future__ import annotations

import html as html_lib
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRAPE = ROOT / "_tmp" / "insait-scrape"
PEOPLE = ROOT / "_people"
FACULTY_KEEP = {"luc-van-gool", "jinjin-gu", "danda-paudel"}

SLUG_ALIASES = {
    "dr-ajad-chhatkuli": "ajad-chhatkuli",
    "dr-ing-kunyu-peng": "kunyu-peng",
    "dr-nikola-popovic": "nikola-popovic",
    "dr-mengshun-hu": "mengshun-hu",
    "dr-taewoo-kim": "taewoo-kim",
    "saman-motamed": "sam-motamed",
    "mohammadmahdi-ghahramani-2": "mohammadmahdi-ghahramani",
    "nikolay-nikolov-2": "nikolay-nikolov",
    "stefan-maria-ailuro": "stefan-ailuro",
}

ROLE_BY_DIR = {"phd": "phd", "postdoc": "postdoc", "visitor": "visitor"}
VISITING_PHD_IDS = {"yutong-hu", "yuedong-tan", "qi-ma"}
LONG_TERM_VISITOR_IDS = {"berke-gokmen", "xiaoye-wang"}
ALLOWED_FM_KEYS = {
    "person_id",
    "title",
    "name_display",
    "title_en",
    "role",
    "start_date",
    "order",
    "topics",
    "working_with",
    "homepage",
    "photo",
}


def normalize_slug(html_stem: str) -> str:
    return SLUG_ALIASES.get(html_stem, html_stem)


def parse_front_matter(text: str) -> tuple[dict[str, str | list], str]:
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 3)
    if end == -1:
        return {}, text
    block = text[3:end]
    body = text[end + 4 :].lstrip("\n")
    fm: dict[str, str | list] = {}
    key = None
    for line in block.splitlines():
        if line.strip().startswith("- ") and key in ("topics", "working_with"):
            items = fm.get(key)
            if not isinstance(items, list):
                items = []
                fm[key] = items
            items.append(line.strip()[2:].strip())
            continue
        m = re.match(r"^(\w+):\s*(.*)$", line)
        if m:
            key = m.group(1)
            val = m.group(2).strip()
            if val.startswith('"') and val.endswith('"'):
                val = val[1:-1]
            if key in ("topics", "working_with") and not val:
                fm[key] = []
            else:
                fm[key] = val
    return fm, body


def dump_front_matter(fm: dict[str, str | list]) -> str:
    order = [
        "person_id",
        "title",
        "name_display",
        "title_en",
        "role",
        "start_date",
        "order",
        "topics",
        "working_with",
        "homepage",
        "photo",
    ]
    lines = ["---"]
    for key in order:
        if key not in fm:
            continue
        val = fm[key]
        if key in ("topics", "working_with") and isinstance(val, list):
            lines.append(f"{key}:")
            for t in val:
                lines.append(f"  - {t}")
        elif key in ("start_date", "title_en") or (
            isinstance(val, str) and "," in val and key == "title_en"
        ):
            lines.append(f'{key}: "{val}"')
        elif isinstance(val, str) and (
            key not in ("homepage", "photo")
            and (":" in val or '"' in val or "\n" in val)
        ):
            lines.append(f'{key}: "{val}"')
        else:
            lines.append(f"{key}: {val}")
    for key, val in fm.items():
        if key in order:
            continue
        lines.append(f"{key}: {val}")
    lines.append("---")
    return "\n".join(lines)


def extract_canonical(html: str) -> str | None:
    m = re.search(r'<link rel="canonical" href="([^"]+)"', html)
    return m.group(1).rstrip("/") + "/" if m else None


def extract_h1(html: str) -> str:
    m = re.search(
        r'<div class="person-head">.*?<h1[^>]*>(.*?)</h1>',
        html,
        re.S | re.I,
    )
    return html_lib.unescape(re.sub(r"<[^>]+>", "", m.group(1))).strip() if m else ""


def extract_subtitle(html: str) -> str:
    # INSAIT pages often close subtitle with </h1> instead of </h2>; scope to person-head.
    m = re.search(
        r'<div class="person-head">.*?<h2 class="subtitle[^"]*"[^>]*>(.*?)</(?:h2|h1)>',
        html,
        re.S | re.I,
    )
    if not m:
        return ""
    text = html_lib.unescape(re.sub(r"<[^>]+>", "", m.group(1))).strip()
    return text if len(text) <= 200 else ""


def extract_entry_blocks(html: str) -> list[str]:
    return re.findall(
        r'<div class="entry-content rtf wide">\s*(.*?)\s*</div>',
        html,
        re.S | re.I,
    )


def is_spacer_only(fragment: str) -> bool:
    stripped = re.sub(r"<[^>]+>", "", fragment)
    return not html_lib.unescape(stripped).strip()


def inline_to_md(fragment: str) -> str:
    s = fragment.strip()
    s = re.sub(r"<br\s*/?>", "\n", s, flags=re.I)
    s = re.sub(r"</p>\s*<p>", "\n\n", s, flags=re.I)
    s = re.sub(r"<p[^>]*>", "", s, flags=re.I)
    s = re.sub(r"</p>", "\n\n", s, flags=re.I)
    s = re.sub(r"<strong>(.*?)</strong>", r"**\1**", s, flags=re.I | re.S)
    s = re.sub(r"<b>(.*?)</b>", r"**\1**", s, flags=re.I | re.S)
    s = re.sub(r"<em>(.*?)</em>", r"*\1*", s, flags=re.I | re.S)

    def link_repl(m: re.Match[str]) -> str:
        href = html_lib.unescape(m.group(1))
        text = html_lib.unescape(re.sub(r"<[^>]+>", "", m.group(2))).strip()
        if "email-protection" in href or href.startswith("/cdn-cgi/"):
            return text or ""
        return f"[{text}]({href})"

    s = re.sub(
        r'<a[^>]+href="([^"]*)"[^>]*>(.*?)</a>',
        link_repl,
        s,
        flags=re.I | re.S,
    )
    s = re.sub(r"<li[^>]*>", "- ", s, flags=re.I)
    s = re.sub(r"</li>", "\n", s, flags=re.I)
    s = re.sub(r"</?ul[^>]*>", "\n", s, flags=re.I)
    s = re.sub(r"<div[^>]*wp-block-spacer[^>]*>.*?</div>", "", s, flags=re.I | re.S)
    s = re.sub(r"<[^>]+>", "", s)
    s = html_lib.unescape(s)
    return re.sub(r"\n{3,}", "\n\n", s).strip()


def blocks_to_markdown(blocks: list[str]) -> str:
    parts: list[str] = []
    for block in blocks:
        if is_spacer_only(block):
            continue
        md = inline_to_md(block)
        if md:
            parts.append(md)
    return "\n\n".join(parts).strip()


def display_name_from_title(title: str) -> str:
    for prefix in ("Prof. ", "Dr. "):
        if title.startswith(prefix):
            return title[len(prefix) :]
    return title


def load_listing_cards() -> dict[str, str]:
    listing = SCRAPE / "listing" / "phd-post-docs-research-scientists.html"
    if not listing.exists():
        return {}
    html = listing.read_text(encoding="utf-8", errors="replace")
    cards: dict[str, str] = {}
    for m in re.finditer(
        r'<a href="(https://insait\.ai/[^"]+)" class="person">.*?'
        r'<span class="name">(.*?)</span>.*?'
        r'<span class="title">(.*?)</span>',
        html,
        re.S | re.I,
    ):
        url = m.group(1).rstrip("/") + "/"
        title_html = m.group(3)
        title_text = html_lib.unescape(
            re.sub(r"<br\s*/?>", "; ", title_html, flags=re.I)
        )
        title_text = re.sub(r"<[^>]+>", "", title_text)
        cards[url] = re.sub(r"\s+", " ", title_text).strip()
    return cards


def find_people_md(canonical: str | None, person_id: str) -> Path | None:
    direct = PEOPLE / f"{person_id}.md"
    if direct.exists():
        return direct
    if not canonical:
        return None
    for md in PEOPLE.glob("*.md"):
        if canonical in md.read_text(encoding="utf-8", errors="replace"):
            return md
    return None


def build_title_en(
    role: str, subtitle: str, listing_line: str, h1: str, person_id: str = ""
) -> str:
    if subtitle:
        return subtitle
    if listing_line:
        area = ""
        if listing_line.lower().startswith("area:"):
            area = listing_line.split(":", 1)[1].split(";", 1)[0].strip()
        else:
            area = listing_line.split(";", 1)[0].strip()
        role_label = {
            "phd": "PhD Student",
            "postdoc": "Postdoctoral Researcher",
            "visitor": "Research Visitor",
        }.get(role, "")
        if role == "visitor":
            if person_id in VISITING_PHD_IDS:
                role_label = "Visiting PhD Student"
            elif person_id in LONG_TERM_VISITOR_IDS:
                role_label = "Long-Term Research Visitor"
        if area and role_label:
            return f"{role_label}, {area}"
        cleaned = listing_line.replace("Area:", "").strip()
        return cleaned or role_label
    role_label = {
        "phd": "PhD Student",
        "postdoc": "Postdoctoral Researcher",
        "visitor": "Research Visitor",
    }.get(role, "")
    if h1.startswith("Dr. "):
        return "Postdoctoral Researcher"
    return role_label


def process_html(html_path: Path, role: str, listing_cards: dict[str, str]) -> dict:
    html = html_path.read_text(encoding="utf-8", errors="replace")
    person_id = normalize_slug(html_path.stem)
    canonical = extract_canonical(html)
    h1 = extract_h1(html)
    subtitle = extract_subtitle(html)
    bio = blocks_to_markdown(extract_entry_blocks(html))
    listing_line = listing_cards.get(canonical or "", "")

    md_path = find_people_md(canonical, person_id)
    existing_fm: dict[str, str | list] = {}
    if md_path:
        existing_fm, _ = parse_front_matter(md_path.read_text(encoding="utf-8"))
        person_id = str(existing_fm.get("person_id", person_id))

    fm = {k: v for k, v in existing_fm.items() if k in ALLOWED_FM_KEYS}
    fm["person_id"] = person_id
    if h1:
        fm["title"] = h1
    fm["name_display"] = display_name_from_title(str(fm.get("title", h1)))
    fm["role"] = role
    title_en = build_title_en(role, subtitle, listing_line, h1, person_id)
    fm["title_en"] = " ".join(title_en.split())
    if canonical:
        fm["homepage"] = canonical
    fm.setdefault("start_date", "2024-01-01")
    fm.setdefault("order", "0")

    return {
        "person_id": person_id,
        "md_path": md_path or (PEOPLE / f"{person_id}.md"),
        "fm": fm,
        "bio": bio,
    }


def main() -> int:
    listing_cards = load_listing_cards()
    keep_ids: set[str] = set(FACULTY_KEEP)
    updated: list[str] = []
    created: list[str] = []

    for subdir, role in ROLE_BY_DIR.items():
        folder = SCRAPE / subdir
        if not folder.is_dir():
            print(f"Missing folder: {folder}", file=sys.stderr)
            continue
        for html_path in sorted(folder.glob("*.html")):
            data = process_html(html_path, role, listing_cards)
            keep_ids.add(data["person_id"])
            path = data["md_path"]
            existed = path.exists()
            path.write_text(
                dump_front_matter(data["fm"]) + "\n\n" + data["bio"] + "\n",
                encoding="utf-8",
            )
            (updated if existed else created).append(path.name)

    deleted: list[str] = []
    for md in sorted(PEOPLE.glob("*.md")):
        fm, _ = parse_front_matter(md.read_text(encoding="utf-8"))
        pid = str(fm.get("person_id", md.stem))
        if pid not in keep_ids:
            md.unlink()
            deleted.append(md.name)

    print(f"Updated: {len(updated)}")
    print(f"Created: {len(created)}")
    print(f"Deleted: {len(deleted)}")
    if deleted:
        print("Removed files:")
        for name in deleted:
            print(f"  - {name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
