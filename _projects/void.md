---
title: VOID
tagline: Video object and interaction deletion — INSAIT × Netflix.
cover_image: /assets/images/portfolio/void.png
release_date: 2026-04-08
project_year: "2026"
sidebar_tags: Video, Inpainting, Diffusion
external_url: https://void-model.github.io/
contributors:
  - sam-motamed
  - luc-van-gool
topics:
  - visual-media
---

**VOID** (Video Object and Interaction Deletion) removes objects from video while reconstructing **physically plausible** downstream motion — not only inpainting what was behind the object, but also correcting collisions, falls, and other interaction effects.

The model builds on CogVideoX with a **quadmask** that separates objects, interaction zones, and background. Training uses Blender-simulated counterfactual scenes from Kubric and HUMOTO. The project is **open source**.

**Resources:** [Project page](https://void-model.github.io/) · [Paper](https://arxiv.org/abs/2604.02296) · [Code](https://github.com/Netflix/void-model) · [Demo](https://huggingface.co/spaces/sam-motamed/VOID) · [INSAIT news](https://insait.ai/insait-and-netflix-develop-ai-model-that-realistically-removes-objects-from-video/)
