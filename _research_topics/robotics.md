---
topic_id: robotics
title: Robotics
order: 1
summary: Reference page for editing Research Topics — use this file as the template for your own topic.
hero_image: /assets/images/blog/blog-img-2.jpg
intro_video: /site-covers/home/hero-video.mp4
---

This page is the **reference template** for all Research Topic pages. Edit your own file in `_research_topics/` (for example `3d-vision.md`), preview at `/research/topics/<topic-id>/`, and do **not** change `_layouts/topic.html` or other templates.

We build representations that fuse **vision**, proprioception, and language so robots can follow sparse instructions, recover from contact-rich failures, and reuse skills across cells and grippers. Our work builds on *sim-to-real transfer* and related ideas in manipulation and navigation.

### Which file to edit

Each direction has one Markdown file; the filename must match `topic_id`:

| Direction | File | Preview path |
|-----------|------|----------------|
| Robotics | `robotics.md` | `/research/topics/robotics/` |
| Space AI | `space-ai.md` | `/research/topics/space-ai/` |
| 3D Vision | `3d-vision.md` | `/research/topics/3d-vision/` |
| Egocentric Vision | `egocentric-vision.md` | `/research/topics/egocentric-vision/` |
| Visual Media | `visual-media.md` | `/research/topics/visual-media/` |
| Vision Agent | `vision-agent.md` | `/research/topics/vision-agent/` |

The YAML block at the top of each file sets the page title, summary, and hero image. The sections **Projects and demos**, **Related news**, **Publications**, and **People** are filled automatically from other folders when items are tagged with your `topic_id` — you do not write those in this file.

#### YAML fields (top of the file)

| Field | Purpose |
|-------|---------|
| `topic_id` | Must match the filename; do not change |
| `title` | Main page heading (H1) |
| `order` | Sort order on the Research list |
| `summary` | Short lead line under the title |
| `hero_image` | Banner image path, e.g. `/assets/images/blog/blog-img-2.jpg` or `/site-covers/topics/robotics/hero.jpg` |

Do not use `topic_sponsors` or `collaborators` in YAML. Partner logos go in the **In Cooperation With** section below.

### Headings and text

The page title is already H1 from `title` in YAML. In the body, use **only** `###` (section) and `####` (subsection). Do not use `##`, `#####`, or HTML heading tags.

#### Example subsection

Domain randomization, system identification, and tactile feedback for closing the reality gap. Use **bold** for key terms and *italic* for paper or dataset names.

### Manipulation and contact-rich control

Policies that reason over force, slip, and partial observability during assembly and tool use.

#### Sim-to-real transfer

How we close the gap between simulation and deployment on real hardware.

#### Data-efficient learning

Few-shot adaptation from teleoperation or sparse human corrections.

### Perception and language

#### Vision–proprioception fusion

Representations that align egocentric video, depth, and joint states for closed-loop control.

#### Instruction following

Grounding free-form language in scene graphs and affordances for multi-step rearrangement.

### Images

**Hero image:** set `hero_image` in YAML (see above).

**Inline image** in the body:

```markdown
![Short description of the image](/assets/images/blog/blog-img-7.jpg)
```

Live example:

<figure class="my-4 mb-0">
  <img src="{ '/assets/images/blog/blog-img-7.jpg' | relative_url }" alt="Representative robotics scene" class="img-fluid rounded-3 w-100" loading="lazy" decoding="async" />
</figure>

Upload your own files under `site-covers/topics/<topic-id>/` and use paths starting with `/`.

### Video

Do not use a bare `<video>` tag (it will not size correctly). Wrap the player in a 16:9 container:

```html
<div class="ratio ratio-16x9 rounded-3 overflow-hidden shadow-sm bg-dark my-4">
  <video class="object-fit-cover" controls playsinline muted loop poster="/assets/images/blog/blog-img-7.jpg">
    <source src="{ '/site-covers/home/hero-video.mp4' | relative_url }" type="video/mp4" />
  </video>
</div>
```

Example embed (paths already in the repo):

<div class="ratio ratio-16x9 rounded-3 overflow-hidden shadow-sm bg-dark my-4">
  <video class="object-fit-cover" controls playsinline muted loop poster="/assets/images/blog/blog-img-7.jpg">
    <source src="{ '/site-covers/home/hero-video.mp4' | relative_url }" type="video/mp4" />
  </video>
</div>

### In Cooperation With

Add this section at the end of your file. Write a short line about partners, then list logos in HTML:

Joint workshops with ETH Robotics and industry partners on sim-to-real transfer, tactile sensing, and safe deployment in shared workspaces.

<div class="topic-cooperation-logos">
  <a href="https://example.org/agile-lab" target="_blank" rel="noopener" title="Agile Systems Lab">
    <img src="{ '/site-covers/sponsors/brand-logo-1.svg' | relative_url }" alt="Agile Systems Lab" loading="lazy" decoding="async" />
  </a>
  <img src="{ '/site-covers/sponsors/brand-logo-3.svg' | relative_url }" alt="Eurobotics Initiative" loading="lazy" decoding="async" />
</div>

- With a website: wrap `<img>` in `<a href="..." target="_blank" rel="noopener">`
- Without a link: use `<img src="..." alt="..." />` only
- Prefer SVG or PNG under `site-covers/sponsors/` or `site-covers/topics/<topic-id>/`

#### Before you submit

- Edit only your assigned `_research_topics/<topic-id>.md`
- Use only `###` and `####` for headings
- Keep `topic_id` aligned with the filename
- Update `summary` and `hero_image`; upload image and video files to the repo
- Wrap inline videos in `<div class="ratio ratio-16x9 ...">`
- Run `bundle exec jekyll serve` and check the page locally
