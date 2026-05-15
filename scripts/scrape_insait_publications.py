#!/usr/bin/env python3
"""
Fetch https://insait.ai/publications/ and export structured JSON.

Dependencies: pip install beautifulsoup4
"""

from __future__ import annotations

import json
import re
import sys
import urllib.request
from html import unescape

try:
    from bs4 import BeautifulSoup
except ImportError:
    print("Install dependencies: pip install beautifulsoup4", file=sys.stderr)
    raise

URL = "https://insait.ai/publications/"
USER_AGENT = "vision-insait-scraper/1.0 (+research)"

LABEL_TO_KEY = {
    "paper": "paper",
    "website": "project",
    "code": "code",
    "slides": "slides",
    "dataset": "dataset",
}

ICON_TO_KEY = {
    "icon-paper": "paper",
    "icon-website": "project",
    "icon-github": "code",
    "icon-slides": "slides",
    "icon-dataset": "dataset",
}


def fetch_html(url: str) -> str:
    req = urllib.request.Request(
        url,
        headers={"User-Agent": USER_AGENT},
    )
    with urllib.request.urlopen(req, timeout=60) as resp:
        return resp.read().decode("utf-8", errors="replace")


def split_description_segments(html_inner: str) -> list[str]:
    parts = re.split(r"<br\s*/?>", html_inner, flags=re.IGNORECASE)
    out: list[str] = []
    for p in parts:
        t = p.strip()
        if not t or t in ("&nbsp;", "<p>&nbsp;</p>"):
            continue
        out.append(t)
    return out


def segment_plain(seg: str) -> str:
    frag = BeautifulSoup(seg, "html.parser")
    t = frag.get_text(separator=" ", strip=True)
    return re.sub(r"\s+", " ", unescape(t))


def parse_authors(author_html: str) -> list[str]:
    frag = BeautifulSoup(author_html, "html.parser")
    blob = frag.get_text(separator=" ", strip=True)
    blob = re.sub(r"\s+", " ", unescape(blob))

    pieces: list[str] = []
    if ";" in blob:
        for chunk in re.split(r"\s*;\s*", blob):
            if not chunk.strip():
                continue
            pieces.extend(a.strip() for a in re.split(r"\s*,\s*", chunk) if a.strip())
    else:
        pieces = [a.strip() for a in re.split(r"\s*,\s*", blob) if a.strip()]

    return [re.sub(r"\.\s*$", "", n).strip() for n in pieces if n.strip()]


def parse_venue(venue_html: str) -> str | None:
    frag = BeautifulSoup(venue_html, "html.parser")
    t = frag.get_text(separator=" ", strip=True)
    t = re.sub(r"^\s*In:\s*", "", t, flags=re.IGNORECASE).strip()
    return t or None


def extract_year_int(year_text: str) -> int:
    m = re.search(r"(20\d{2})", year_text)
    if not m:
        raise ValueError(f"Could not parse year from {year_text!r}")
    return int(m.group(1))


def link_key_for_anchor(a) -> str | None:
    span = a.find("span")
    if span:
        label = span.get_text(strip=True).lower()
        if label in LABEL_TO_KEY:
            return LABEL_TO_KEY[label]
    icon = a.find("i")
    if icon:
        for cls in icon.get("class", []):
            if cls in ICON_TO_KEY:
                return ICON_TO_KEY[cls]
    return None


def collect_links(links_el) -> dict[str, str]:
    links: dict[str, str] = {}
    other_n = 0
    for a in links_el.select("a.publication-link"):
        href = (a.get("href") or "").strip()
        if not href:
            continue
        key = link_key_for_anchor(a)
        if key is None:
            other_n += 1
            key = "other" if other_n == 1 else f"other_{other_n}"
        if key not in links:
            links[key] = href
    return links


def parse_publication_item(item, year: int) -> dict:
    desc = item.select_one(".publication-description")
    if not desc:
        raise ValueError("publication-item missing .publication-description")

    main_p = None
    for p in desc.find_all("p", recursive=False):
        text_probe = p.get_text(strip=True)
        if text_probe and text_probe.replace("\xa0", "").strip():
            main_p = p
            break
    if main_p is None:
        main_p = desc.find("p")

    if main_p is None:
        raise ValueError("No <p> in publication-description")

    segments = split_description_segments(main_p.decode_contents())
    if not segments:
        raise ValueError("Empty publication description")

    authors = parse_authors(segments[0])
    rest = segments[1:]

    venue_idx: int | None = None
    for i, seg in enumerate(rest):
        if segment_plain(seg).lower().lstrip().startswith("in:"):
            venue_idx = i
            break

    if venue_idx is not None:
        mid = rest[:venue_idx]
        venue = parse_venue(rest[venue_idx])
    else:
        mid = rest
        venue = None

    note_bits: list[str] = []
    title_segs: list[str] = []
    for seg in mid:
        pt = segment_plain(seg)
        if re.match(r"^\([^)]+\)\s*$", pt):
            note_bits.append(pt)
        else:
            title_segs.append(seg)

    title = " ".join(segment_plain(s) for s in title_segs).strip()

    links: dict[str, str] = {}
    links_el = item.select_one(".publication-links")
    if links_el:
        links = collect_links(links_el)

    entry: dict = {
        "title": title,
        "year": year,
        "venue": venue,
        "authors": authors,
        "links": links,
    }
    if note_bits:
        entry["note"] = note_bits if len(note_bits) > 1 else note_bits[0]
    return entry


def has_row_class(classes) -> bool:
    if not classes:
        return False
    if isinstance(classes, str):
        return "row" in classes.split()
    return "row" in classes


def scrape(html: str) -> list[dict]:
    soup = BeautifulSoup(html, "html.parser")
    sections = soup.select("section.block-publications")
    if not sections:
        raise RuntimeError("Could not find section.block-publications")

    publications: list[dict] = []

    for section in sections:
        container = section.select_one(".container")
        if not container:
            continue

        rows = container.find_all("div", class_=has_row_class)
        current_year: int | None = None

        for row in rows:
            h2 = row.find("h2", class_="h3")
            if h2:
                current_year = extract_year_int(h2.get_text(strip=True))
                continue

            plist = row.select_one(".publications-list")
            if plist and current_year is not None:
                for item in plist.select(".publication-item"):
                    publications.append(parse_publication_item(item, current_year))

    return publications


def main() -> None:
    out_path = sys.argv[1] if len(sys.argv) > 1 else "insait_publications.json"
    html = fetch_html(URL)
    data = scrape(html)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print(f"Wrote {len(data)} publications to {out_path}")


if __name__ == "__main__":
    main()
