---
title: MotoVLA
tagline: Generalist robot manipulation beyond action-labeled data — CoRL 2025.
cover_image: /assets/images/portfolio/motovla.png
release_date: 2025-11-06
project_year: "2025"
sidebar_tags: Robotics, VLA, 3D
external_url: https://motovla.insait.ai/
contributors:
  - nikolay-nikolov
  - danda-paudel
  - luc-van-gool
topics:
  - robotics
---

**MotoVLA** learns generalist robot manipulation from **videos without action labels** — including human demonstrations and cross-embodiment robot footage — then aligns to executable actions with a smaller labeled set.

The method builds dense **dynamic 3D point clouds** at the hand or gripper and trains a **3D dynamics predictor** for self-supervision, which is transferred to an action predictor for downstream control. This supports stronger open-vocabulary policies and **out-of-action generalization**: new tasks without action labels in both simulation (SIMPLER) and real-robot evaluations.

**Resources:** [Project page](https://motovla.insait.ai/) · [Paper](https://arxiv.org/pdf/2509.19958) · [OpenReview](https://openreview.net/forum?id=ZqBXnR6ppz)
