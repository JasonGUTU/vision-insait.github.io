# Repository maintenance map

This document maps **what ships on the live site** vs **maintainer-only** folders, and lists legacy or unused pieces. Routine content editors can ignore this file; use [README.md](../README.md) instead.

---

## What actually builds (Jekyll)

| Path | Role |
|------|------|
| `_config.yml` | Production config (`url`, collections, `exclude`) |
| `_config.dev.yml` | Local preview: only overrides `url` (merged by `rake serve` / `rake build:local`) |
| `_layouts/`, `_includes/` | HTML shells and fragments |
| `_data/` | YAML consumed by Liquid (`news.yml`, `alumni.yml`, `footer.yml`) |
| `_people/`, `_research_topics/`, `_publications/`, `_projects/`, `_jobs/` | Collections |
| `index.md`, `people/`, `research/`, `publications/`, `demos/`, `news/`, `openings/`, `sponsorship/`, `blog/`, `404.html` | Top-level pages |
| `assets/` | Block theme **compiled** CSS/JS/images (site runtime) |
| `assets/css/site-additions.css` | Vision Lab overrides |
| `site-covers/` | Group-owned media |

**Not built** (listed in `_config.yml` → `exclude`): `template/`, `vendor/`, `Gemfile*`, `README.md`, plus maintainer paths documented below.

---

## `template/` — Block theme **source** (Codescandy Block 1.3.x)

- **~240 MB** of upstream HTML/SCSS/Gulp sources (`template/src/…`).
- **Never deployed**; kept for reference when adjusting markup or recompiling theme assets.
- The live site uses **`assets/`** (compiled `dist`), not `template/src` directly.
- Home page was derived from `template/src/landing-it-company.html`.
- Upstream docs: `template/README.md` and [Block documentation](https://block.codescandy.com/docs/index.html).

To change global styles: edit SCSS under `template/src`, run `npm install && gulp` inside `template/`, then copy output into `assets/` (or symlink `assets` → `../block-1.3.2/dist/assets` as described in README).

---

## Maintainer-only (must stay out of `_site/`)

| Path | Purpose |
|------|---------|
| `scripts/` | Python helpers (import publications, crop portraits, scrape INSAIT, …) |
| `data/` | JSON caches for import pipelines (`insait_publications*.json`, `venues_canonical.json`) |
| `.venv-face/` | Local Python venv for `crop_portraits_nose_center.py` — **must not be committed** |

These are added to Jekyll `exclude` so they are not copied to `_site/`.

---

## Legacy / removed blog stack

News is **`_data/news.yml`** + layout `news-list` at `/news/`.

| Item | Status |
|------|--------|
| `/blog/` | **Keep** — `blog/index.md` redirects to `/news/` |
| `_posts/` | Removed (was a single demo post) |
| `post.html`, `blog-list.html` layouts | Removed (unused) |
| `post-row-compact.html` | Removed (only used by blog list) |

---

## Unused layouts (removed)

| Layout | Was intended for |
|--------|------------------|
| `people-category.html` | Per-role people subpages (`people_role` in front matter) — never wired; `/people/` uses `people.html` only |

---

## Active layout ↔ page map

| Layout | Used by |
|--------|---------|
| `default.html` | Wrapper for most inner pages |
| `home.html` | `/` |
| `research-list.html` | `/research/` |
| `topic.html` | `_research_topics/*` |
| `people.html` | `/people/` |
| `person.html` | `_people/*` |
| `publications-list.html` | `/publications/` |
| `publication.html` | `_publications/*` |
| `demos-grid.html` | `/demos/` |
| `project.html` | `_projects/*` |
| `news-list.html` | `/news/` |
| `job-list.html` | `/openings/` |
| `job.html` | `_jobs/*` |
| `page.html` | `404.html`, `sponsorship/` |
| `redirect.html` | `/blog/` → `/news/` |

---

## `_includes/` reference

| Include | Used by |
|---------|---------|
| `head.html`, `scripts.html`, `scripts-landing.html` | `default`, `home` |
| `navbar.html`, `navbar-landing.html` | Inner / home nav |
| `site-logo.html`, `insait-lockup.html` | Nav, footer |
| `nav-research-dropdown.html` | Navbars |
| `footer.html` | All pages |
| `pub-*`, `project-link.html` | Publications & topics |
| `news-row.html` | News list |
| `job-row-compact.html` | Openings list |
| `topic-projects-carousel.html` | Topic pages |

---

## Config files

| File | Use |
|------|-----|
| `_config.yml` | Production + shared settings |
| `_config.dev.yml` | Local `url` override (`rake serve`, `rake build:local`) |
| ~~`_config_local.yml`~~ | Removed — duplicate of `_config.dev.yml` |

---

## Accidental / broken paths (watch list)

| Path | Notes |
|------|--------|
| `assets 2` | macOS duplicate folder; listed in `.gitignore` — delete locally if present |
| `.venv-face/` | Should not be in git; use `.venv/` or project venv for scripts |
| Committed `assets/` vs README symlink | Repo currently **commits** full `assets/` (~140 MB). Symlink to external Block `dist` is optional for developers |

---

## Suggested git hygiene (one-time)

```bash
# Stop tracking the face-crop venv (after .gitignore is updated)
git rm -r --cached .venv-face/
```

Do **not** delete `template/` from git unless the team stores Block elsewhere; document the external path in README instead.
