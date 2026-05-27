---
title: COM4D
tagline: Compositional 4D scene reconstruction from monocular video — CVPR 2026.
cover_image: /assets/images/portfolio/com4d.png
release_date: 2026-06-15
project_year: "2026"
sidebar_tags: 4D, Compositional, Video-to-3D
external_url: https://com4d.insait.ai/
contributors:
  - berke-gokmen
  - ajad-chhatkuli
  - danda-paudel
  - luc-van-gool
topics:
  - 3d-vision
---

**COM4D** (Compositional 4D) jointly infers **static and dynamic object** structure and spatio-temporal layout in real-world scenes from **monocular video**, without category-specific parametric shape models or any 4D compositional training data.

Training disentangles **multi-object spatial composition** and **single-object temporal dynamics** via separate spatial and temporal attentions on 2D video; at inference, an attention-mixing step combines them to reconstruct persistent **compositional 4D scenes** with explicit meshes and interacting objects.

**Resources:** [Project page](https://com4d.insait.ai/) · [Paper](https://arxiv.org/pdf/2512.05272) · [Code](https://github.com/insait-institute/COM4D)
