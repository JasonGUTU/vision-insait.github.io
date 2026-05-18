---
title: "Ternary-type Opacity and Hybrid Odometry for RGB-only NeRF-SLAM"
year: 2024
venue: "IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS 2024)"
venue_display: "IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS 2024)"
venue_chronicle: "IEEE/RSJ International Conference on Intelligent Robots and Systems"
venue_abbr: "IROS"
publication_date: "2024-10-14"
author_line_full: "Junru Lin, Asen Nachkov, Songyou Peng, Luc Van Gool, Danda Pani Paudel"
authors:
  - asen-nachkov
  - luc-van-gool
  - danda-paudel
paper_url: "https://arxiv.org/pdf/2312.13332"
---
## Abstract

In this work, we address the challenge of deploying Neural Radiance Field (NeRFs) in Simultaneous Localization and Mapping (SLAM) under the condition of lacking depth information, relying solely on RGB inputs. The key to unlocking the full potential of NeRF in such a challenging context lies in the integration of real-world priors. A crucial prior we explore is the binary opacity prior of 3D space with opaque objects. To effectively incorporate this prior into the NeRF framework, we introduce a ternary-type opacity (TT) model instead, which categorizes points on a ray intersecting a surface into three regions: before, on, and behind the surface. This enables a more accurate rendering of depth, subsequently improving the performance of image warping techniques. Therefore, we further propose a novel hybrid odometry (HO) scheme that merges bundle adjustment and warping-based localization. Our integrated approach of TT and HO achieves state-of-the-art performance on synthetic and real-world datasets, in terms of both speed and accuracy. This breakthrough underscores the potential of NeRF-SLAM in navigating complex environments with high fidelity.

