---
title: StateSpaceDiffuser
tagline: Long-context diffusion world models — NeurIPS 2025.
cover_image: /assets/images/portfolio/StateSpaceDiffuser.png
release_date: 2025-11-21
project_year: "2025"
sidebar_tags: World model, Video, Diffusion
demo_url: https://insait-institute.github.io/StateSpaceDiffuser/
contributors:
  - nedko-savov
  - deheng-zhang
  - danda-paudel
  - luc-van-gool
topics:
  - robotics
---

**StateSpaceDiffuser** combines **diffusion-based world models** with a **state-space backbone** so rollouts keep coherent context over long horizons. Standard video diffusion models often forget scene structure after a few steps; this design retains an environment state across frames while preserving high-fidelity synthesis.

The work introduces evaluation protocols for **temporal consistency** in extended rollouts and shows strong gains on 2D (MiniGrid) and 3D (CSGO) benchmarks — maintaining context for an order of magnitude more steps than diffusion-only baselines with modest extra compute.

**Resources:** [Project page](https://insait-institute.github.io/StateSpaceDiffuser/) · [Paper](https://arxiv.org/pdf/2505.22246) · [Code](https://github.com/insait-institute/StateSpaceDiffuser) · [INSAIT news](https://insait.ai/insait-researchers-advance-video-ai-with-statespacediffuser/)
