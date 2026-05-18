---
title: "Generalist Robot Manipulation beyond Action Labeled Data"
year: 2025
venue: "Conference on Robot Learning (CoRL 2025)"
venue_display: "Conference on Robot Learning (CoRL 2025)"
venue_chronicle: "Conference on Robot Learning"
venue_abbr: "CoRL"
publication_date: "2025-11-06"
author_line_full: "Alexander Spiridonov, Jan-Nico Zaech, Nikolay Nikolov, Luc Van Gool, Danda Pani Paudel"
authors:
  - nikolay-nikolov
  - luc-van-gool
  - danda-paudel
paper_url: "https://arxiv.org/pdf/2509.19958"
---
## Abstract

Recent advances in generalist robot manipulation leverage pre-trained Vision-Language Models (VLMs) and large-scale robot demonstrations to tackle diverse tasks in a zero-shot manner. A key challenge remains: scaling high-quality, action-labeled robot demonstration data, which existing methods rely on for robustness and generalization. To address this, we propose a method that benefits from videos without action labels - featuring humans and/or robots in action - enhancing open-vocabulary performance and enabling data-efficient learning of new tasks. Our method extracts dense, dynamic 3D point clouds at the hand or gripper location and uses a proposed 3D dynamics predictor for self-supervision. This predictor is then tuned to an action predictor using a smaller labeled dataset for action alignment. We show that our method not only learns from unlabeled human and robot demonstrations - improving downstream generalist robot policies - but also enables robots to learn new tasks without action labels (i.e., out-of-action generalization) in both real-world and simulated settings.

