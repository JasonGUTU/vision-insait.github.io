#!/usr/bin/env python3
"""Import people from INSAIT staff listing into _people/*.md with photos."""

from __future__ import annotations

import json
import re
import subprocess
import html as htmlmod
from datetime import date, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PEOPLE_DIR = ROOT / "_people"
PHOTO_DIR = ROOT / "assets" / "images" / "people"
HTML_PATH = Path("/tmp/insait-people.html")

SLUG_TO_ID = {
    "saman-motamed": "sam-motamed",
    "nikolay-nikolov-2": "nikolay-nikolov",
    "mohammadmahdi-ghahramani-2": "mohammadmahdi-ghahramani",
    "stefan-maria-ailuro": "stefan-ailuro",
    "german-ortiz": "jesus-german-ortiz-barajas",
    "dr-mengshun-hu": "mengshun-hu",
    "dr-danda-paudel": "danda-paudel",
    "prof-luc-van-gool": "luc-van-gool",
    "dr-jinjin-gu": "jinjin-gu",
    "xu-zheng": "xu-zheng",
    "dr-nikola-popovic": "nikola-popovic",
    "dr-lei-sun": "lei-sun",
    "lei-sun": "lei-sun",
    "dr-ajad-chhatkuli": "ajad-chhatkuli",
    "dr-yuqian-fu": "yuqian-fu",
    "dr-nico-zaech": "nico-zaech",
}

SKIP_IDS = {"luc-van-gool", "danda-paudel", "jinjin-gu"}

SECTION_ROLE = {
    "PhD Students": "phd",
    "Postdocs & Research Scientists": "postdoc",
    "Visiting Doctoral Students": "visitor",
    "Long-Term Research Visitors": "visitor",
    "Past Members": None,  # resolved per person
}


def decode(s: str) -> str:
    return htmlmod.unescape(s.strip())


def parse_title_html(title_html: str) -> dict[str, str]:
    text = re.sub(r"<br\s*/?>", "\n", title_html)
    text = re.sub(r"<[^>]+>", "", text)
    text = htmlmod.unescape(text)
    info = {"area": "", "education": "", "advisers": ""}
    for line in text.split("\n"):
        line = line.strip()
        if not line:
            continue
        low = line.lower()
        if low.startswith("area:"):
            info["area"] = line[5:].strip()
        elif low.startswith("education:"):
            info["education"] = line[10:].strip()
        elif low.startswith("adviser") or low.startswith("advisor"):
            info["advisers"] = re.sub(r"^advisers?:?\s*", "", line, flags=re.I).strip()
    return info


def best_image(src: str, srcset: str = "") -> str:
    if srcset:
        urls = re.findall(
            r"(https://[^\s]+\.(?:jpg|jpeg|png|webp))(?:\s+\d+w)?", srcset
        )
        for u in reversed(urls):
            if not re.search(r"-\d+x\d+\.", u):
                return u
        if urls:
            return urls[-1]
    return src


def slug_to_person_id(slug: str) -> str:
    if slug in SLUG_TO_ID:
        return SLUG_TO_ID[slug]
    s = slug
    for prefix in ("dr-ing-", "dr-", "prof-"):
        if s.startswith(prefix):
            s = s[len(prefix) :]
    return s


def clean_name(name: str) -> tuple[str, str]:
    """Return (display_name, page_title)."""
    name = re.sub(r"\s+", " ", name.strip())
    page_title = name
    display = name
    if name.lower().startswith("dr. "):
        display = name[4:].strip()
    if name.endswith(" (Visiting)"):
        display = name[: -len(" (Visiting)")].strip()
        if display.lower().startswith("dr. "):
            display = display[4:].strip()
    return display, page_title


def map_topics(area: str, advisers: str) -> list[str]:
    blob = f"{area} {advisers}".lower()
    topics: list[str] = []
    if any(
        k in blob
        for k in (
            "computer vision",
            "generative ai",
            "3d scene",
            "visual",
            "egocentric",
        )
    ):
        topics.append("visual-media")
    if "3d" in blob:
        topics.append("3d-vision")
    if "robot" in blob or "foundation model" in blob:
        topics.append("robotics")
    if "egocentric" in blob:
        topics.append("egocentric-vision")
    if "space" in blob:
        topics.append("space-ai")
    if "agent" in blob or "vla" in blob:
        topics.append("vision-agent")
    # CV group default when advised by Luc / Danda / Jinjin
    if not topics and any(
        x in blob
        for x in ("luc van gool", "danda paudel", "jinjin gu", "danda pani")
    ):
        topics.append("visual-media")
    return list(dict.fromkeys(topics))


def role_for(section: str, name: str, page_title: str) -> str:
    if section != "Past Members":
        return SECTION_ROLE[section] or "phd"
    if page_title.lower().startswith("dr.") or "dr " in page_title.lower()[:4]:
        return "postdoc"
    return "phd"


def title_en_for(role: str, area: str, section: str) -> str:
    area = area.strip()
    if role == "faculty":
        return area or "Faculty"
    if role == "postdoc":
        if area:
            return f"Postdoctoral Researcher, {area}"
        return "Postdoctoral Researcher"
    if role == "visitor":
        if section == "Long-Term Research Visitors":
            base = "Long-Term Research Visitor"
        else:
            base = "Visiting PhD Student"
        return f"{base}, {area}" if area else base
    if area:
        return f"PhD Student, {area}"
    return "PhD Student"


def bio_for(role: str, area: str, education: str, advisers: str, section: str) -> str:
    parts: list[str] = []
    if section == "Past Members":
        parts.append("Former member of INSAIT.")
    elif role == "postdoc":
        parts.append("Postdoctoral researcher at INSAIT.")
    elif role == "visitor":
        if section == "Long-Term Research Visitors":
            parts.append("Long-term research visitor at INSAIT.")
        else:
            parts.append("Visiting doctoral student at INSAIT.")
    else:
        parts.append("PhD student at INSAIT.")
    if area:
        parts.append(f"Research area: {area}.")
    if education:
        parts.append(f"Education: {education}.")
    if advisers:
        parts.append(f"Advised by {advisers}.")
    return " ".join(parts)


def parse_people(html: str) -> list[dict]:
    parts = re.split(r"<h2[^>]*>([^<]+)</h2>", html)
    people: list[dict] = []
    for i in range(1, len(parts), 2):
        section = decode(parts[i].replace("&#038;", "&"))
        block = parts[i + 1]
        cards = re.findall(
            r'<a\s+href="([^"]+)"\s+class="person"[^>]*>(.*?)</a>',
            block,
            re.DOTALL,
        )
        for href, inner in cards:
            name_m = re.search(r'<span class="name">([^<]+)</span>', inner)
            title_m = re.search(r"<span class=\"title\">(.*?)</span>", inner, re.DOTALL)
            img_m = re.search(
                r'<img[^>]+src="([^"]+)"[^>]*(?:srcset="([^"]*)")?', inner, re.DOTALL
            )
            if not name_m:
                continue
            name = decode(name_m.group(1))
            meta = parse_title_html(title_m.group(1) if title_m else "")
            src = img_m.group(1) if img_m else ""
            srcset = (img_m.group(2) or "") if img_m else ""
            slug = href.rstrip("/").split("/")[-1]
            # Allow external homepages (e.g. alumni); still require INSAIT-hosted photo
            people.append(
                {
                    "section": section,
                    "name": name,
                    "href": href,
                    "image": best_image(src, srcset),
                    "slug": slug,
                    **meta,
                }
            )
    return people


def download_photo(url: str, dest: Path) -> bool:
    if dest.exists() and dest.stat().st_size > 1000:
        return True
    dest.parent.mkdir(parents=True, exist_ok=True)
    r = subprocess.run(
        [
            "curl",
            "-fsSL",
            "-A",
            "Mozilla/5.0",
            "-o",
            str(dest),
            url,
        ],
        capture_output=True,
    )
    return r.returncode == 0 and dest.exists() and dest.stat().st_size > 500


def ext_from_url(url: str) -> str:
    m = re.search(r"\.(jpe?g|png|webp)", url, re.I)
    return "." + m.group(1).lower().replace("jpeg", "jpg") if m else ".jpg"


def existing_body(path: Path) -> str:
    if not path.exists():
        return ""
    text = path.read_text(encoding="utf-8")
    if "---" not in text:
        return text.strip()
    _, _, body = text.partition("---")
    _, _, body = body.partition("---")
    return body.strip()


def write_person(
    person_id: str,
    page_title: str,
    display: str,
    title_en: str,
    role: str,
    start_date: str,
    topics: list[str],
    homepage: str,
    photo: str,
    body: str,
) -> None:
    path = PEOPLE_DIR / f"{person_id}.md"
    old_body = existing_body(path)
    if old_body and len(old_body) > len(body) + 40:
        body = old_body

    lines = [
        "---",
        f"person_id: {person_id}",
        f"title: {page_title}",
        f"name_display: {display}",
        f"title_en: {title_en}",
        f"role: {role}",
        f'start_date: "{start_date}"',
        "order: 0",
    ]
    if topics:
        lines.append("topics:")
        for t in topics:
            lines.append(f"  - {t}")
    if homepage:
        lines.append(f"homepage: {homepage}")
    if photo:
        lines.append(f"photo: {photo}")
    lines.extend(["---", "", body, ""])
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    if not HTML_PATH.exists():
        subprocess.run(
            [
                "curl",
                "-fsSL",
                "-A",
                "Mozilla/5.0",
                "https://insait.ai/phd-post-docs-research-scientists/",
                "-o",
                str(HTML_PATH),
            ],
            check=True,
        )
    html = HTML_PATH.read_text(encoding="utf-8", errors="replace")
    people = parse_people(html)
    print(f"Parsed {len(people)} people")

    role_counters: dict[str, int] = {}
    created = updated = skipped = 0

    for p in people:
        person_id = slug_to_person_id(p["slug"])
        if person_id in SKIP_IDS:
            skipped += 1
            continue

        display, page_title = clean_name(p["name"])
        role = role_for(p["section"], p["name"], page_title)
        role_counters.setdefault(role, 0)
        base = {
            "phd": date(2022, 9, 1),
            "postdoc": date(2023, 1, 1),
            "visitor": date(2024, 6, 1),
        }.get(role, date(2022, 1, 1))
        start = base + timedelta(days=role_counters[role])
        role_counters[role] += 1
        start_date = start.isoformat()

        topics = map_topics(p["area"], p["advisers"])
        title_en = title_en_for(role, p["area"], p["section"])
        body = bio_for(role, p["area"], p["education"], p["advisers"], p["section"])
        homepage = p["href"]

        ext = ext_from_url(p["image"])
        photo_path = PHOTO_DIR / f"{person_id}{ext}"
        photo_rel = f"/assets/images/people/{person_id}{ext}"
        if p["image"] and download_photo(p["image"], photo_path):
            photo = photo_rel
        else:
            photo = ""
            print(f"  warn: no photo for {person_id}")

        path = PEOPLE_DIR / f"{person_id}.md"
        existed = path.exists()
        write_person(
            person_id,
            page_title,
            display,
            title_en,
            role,
            start_date,
            topics,
            homepage,
            photo,
            body,
        )
        if existed:
            updated += 1
        else:
            created += 1

    print(f"Done: {created} created, {updated} updated, {skipped} skipped (faculty)")


if __name__ == "__main__":
    main()
