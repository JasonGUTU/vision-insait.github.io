---
title: "RealisMotion: Decomposed Human Motion Control and Video Generation in the World Space"
year: 2026
venue: "International Conference on Machine Learning (ICML 2026)"
venue_display: "International Conference on Machine Learning (ICML 2026)"
venue_chronicle: "International Conference on Machine Learning"
venue_abbr: "ICML"
publication_date: "2026-07-21"
author_line_full: "Jingyun Liang, Jingkai Zhou, Shikai Li, Chenjie Cao, Lei Sun, Yichen Qian, Weihua Chen, Fan Wang"
authors:
  - lei-sun
paper_url: "https://arxiv.org/pdf/2508.08588"
topics:
  - visual-media
---
## Abstract

Generating human videos with realistic and controllable motions is a challenging task. While existing methods can generate visually compelling videos, they lack separate control over four key video elements: foreground subject, background video, human trajectory and action patterns. In this paper, we propose a decomposed human motion control and video generation framework that explicitly decouples motion from appearance, subject from background, and action from trajectory, enabling flexible mix-and-match composition of these elements. Concretely, we first build a ground-aware 3D world coordinate system and perform motion editing directly in the 3D space. Trajectory control is implemented by unprojecting edited 2D trajectories into 3D with focal-length calibration and coordinate transformation, followed by speed alignment and orientation adjustment; actions are supplied by a motion bank or generated via text-to-motion methods. Then, based on modern text-to-video diffusion transformer models, we inject the subject as tokens for full attention, concatenate the background along the channel dimension, and add motion (trajectory and action) control signals by addition. Such a design opens up the possibility for us to generate realistic videos of anyone doing anything anywhere. Extensive experiments on benchmark datasets and real-world cases demonstrate that our method achieves state-of-the-art performance on both element-wise controllability and overall video quality.

## Links

- [Project page](https://jingyunliang.github.io/RealisMotion)
- [arXiv](https://arxiv.org/abs/2508.08588)
- [Code](https://github.com/JingyunLiang/RealisMotion)
