---
title: AR-VLA
tagline: Autoregressive action expert for vision–language–action models — RSS 2026.
cover_image: /assets/images/portfolio/ar-vla.png
release_date: 2026-03-10
project_year: "2026"
sidebar_tags: Demo, Robotics, VLA
external_url: https://arvla.insait.ai/
contributors:
  - yutong-hu
  - nikolay-nikolov
  - yuanqi-yao
  - sombit-dey
  - giuliano-albanese
  - luc-van-gool
  - danda-paudel
topics:
  - robotics
---

**AR-VLA** replaces chunk-based action heads in vision–language–action policies with a standalone **autoregressive action expert** that streams actions continuously while conditioning on refreshable vision–language prefixes.

Unlike snapshot-to-chunk loops that reset temporal context each step, the action expert keeps long-lived memory for **history-aware** multi-stage control and **smoother** trajectories at chunk boundaries. Experiments on simulation and real-robot manipulation show it can match or exceed reactive VLA baselines on standard benchmarks.

**Resources:** [Project page](https://arvla.insait.ai/) · [Paper](https://arxiv.org/abs/2603.10126)
