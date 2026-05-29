# Block template sources (maintainer reference)

This directory is the **upstream Block theme source tree** (HTML + SCSS + Gulp). It is **not** part of the published Jekyll site.

| Directory | Role |
|-----------|------|
| `src/` | Page prototypes (`landing-it-company.html` → home), partials, SCSS |
| `src/assets/` | Source assets before Gulp build |
| `package.json` | `npm install` + `gulp` to compile |

**Runtime assets for vision.insait.ai** live in the repo root: [`../assets/`](../assets/).

See [docs/MAINTENANCE.md](../docs/MAINTENANCE.md) for the full repo map.
