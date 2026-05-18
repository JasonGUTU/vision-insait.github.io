---
title: "SceneSplat: Gaussian Splatting-based Scene Understanding with Vision-Language Pretraining"
year: 2025
venue: "International Conference on Computer Vision (ICCV 2025)"
venue_display: "International Conference on Computer Vision (ICCV 2025)"
venue_chronicle: "International Conference on Computer Vision"
venue_abbr: "ICCV"
publication_date: "2025-10-13"
author_line_full: "Yue Li, Qi Ma, Runyi Yang, Huapeng Li, Mengjiao Ma, Bin Ren, Nikola Popovic, Nicu Sebe, Ender Konukoglu, Theo Gevers, Luc Van Gool, Martin R. Oswald, Danda Pani Paudel"
authors:
  - qi-ma
  - runyi-yang
  - mengjiao-ma
  - nikola-popovic
  - luc-van-gool
  - danda-paudel
paper_url: "https://arxiv.org/pdf/2503.18052"
---
## Abstract

Recognizing arbitrary or previously unseen categories is essential for comprehensive real-world 3D scene understanding. Currently, all existing methods rely on 2D or textual modalities during training or together at inference. This highlights the clear absence of a model capable of processing 3D data alone for learning semantics end-to-end, along with the necessary data to train such a model. Meanwhile, 3D Gaussian Splatting (3DGS) has emerged as the de facto standard for 3D scene representation across various vision tasks. However, effectively integrating semantic reasoning into 3DGS in a generalizable manner remains an open challenge. To address these limitations, we introduce SceneSplat in Fig. 1, to our knowledge the first large-scale 3D indoor scene understanding approach that operates natively on 3DGS. Furthermore, we propose a self-supervised learning scheme that unlocks rich 3D feature learning from unlabeled scenes. To power the proposed methods, we introduce SceneSplat-7K, the first large-scale 3DGS dataset for indoor scenes, comprising 7916 scenes derived from seven established datasets, such as ScanNet and Matterport3D. Generating SceneSplat-7K required computational resources equivalent to 150 GPU days on an L4 GPU, enabling standardized benchmarking for 3DGS-based reasoning for indoor scenes. Our exhaustive experiments on SceneSplat-7K demonstrate the significant benefit of the proposed method over the established baselines. Our code, model, and datasets will be released at SceneSplat.

