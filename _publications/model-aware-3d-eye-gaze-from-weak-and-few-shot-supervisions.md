---
title: "Model-aware 3D Eye Gaze from Weak and Few-shot Supervisions"
year: 2023
venue: "International Symposium on Mixed and Augmented Reality (ISMAR 2023)"
venue_display: "International Symposium on Mixed and Augmented Reality (ISMAR 2023)"
venue_chronicle: "International Symposium on Mixed and Augmented Reality"
venue_abbr: "ISMAR"
publication_date: "2023-10-16"
author_line_full: "Nikola Popovic, Dimitrios Christodoulou, Danda Pani Paudel, Xi Wang, Luc Van Gool"
authors:
  - nikola-popovic
  - danda-paudel
  - luc-van-gool
paper_url: "https://arxiv.org/pdf/2311.12157"
---
## Abstract

The task of predicting 3D eye gaze from eye images can be performed either by (a) end-to-end learning for image-to-gaze mapping or by (b) fitting a 3D eye model onto images. The former case requires 3D gaze labels, while the latter requires eye semantics or landmarks to facilitate the model fitting. Although obtaining eye semantics and landmarks is relatively easy, fitting an accurate 3D eye model on them remains to be very challenging due to its ill-posed nature in general. On the other hand, obtaining large-scale 3D gaze data is cumbersome due to the required hardware setups and computational demands.In this work, we propose to predict 3D eye gaze from weak supervision of eye semantic segmentation masks and direct supervision of a few 3D gaze vectors. The proposed method combines the best of both worlds by leveraging large amounts of weak annotations–which are easy to obtain, and only a few 3D gaze vectors–which alleviate the difficulty of fitting 3D eye models on the semantic segmentation of eye images. Thus, the eye gaze vectors, used in the model fitting, are directly supervised using the few-shot gaze labels. Additionally, we propose a transformer-based network architecture, that serves as a solid baseline for our improvements. Our experiments in diverse settings illustrate the significant benefits of the proposed method, achieving about 5◦ lower angular gaze error over the baseline, when only 0.05% 3D annotations of the training images are used.

