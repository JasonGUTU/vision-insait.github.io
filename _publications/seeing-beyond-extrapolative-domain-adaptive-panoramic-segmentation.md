---
title: "Seeing Beyond: Extrapolative Domain Adaptive Panoramic Segmentation"
year: 2026
venue: "IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR 2026)"
venue_display: "IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR 2026)"
venue_chronicle: "IEEE/CVF Conference on Computer Vision and Pattern Recognition"
venue_abbr: "CVPR"
publication_date: "2026-06-15"
author_line_full: "Yuanfan Zheng, Kunyu Peng, Xu Zheng, Kailun Yang"
authors:
  - kunyu-peng
paper_url: "https://arxiv.org/pdf/2603.15475"
---
## Abstract

Cross-domain panoramic semantic segmentation has attracted growing interest as it enables comprehensive 360° scene understanding for real-world applications. However, it remains particularly challenging due to severe geometric Field of View (FoV) distortions and inconsistent open-set semantics across domains. In this work, we formulate an open-set domain adaptation setting, and propose Extrapolative Domain Adaptive Panoramic Segmentation (EDA-PSeg) framework that trains on local perspective views and tests on full 360° panoramic images, explicitly tackling both geometric FoV shifts across domains and semantic uncertainty arising from previously unseen classes. To this end, we propose the Euler-Margin Attention (EMA), which introduces an angular margin to enhance viewpoint-invariant semantic representation, while performing amplitude and phase modulation to improve generalization toward unseen classes. Additionally, we design the Graph Matching Adapter (GMA), which builds high-order graph relations to align shared semantics across FoV shifts while effectively separating novel categories through structural adaptation. Extensive experiments on four benchmark datasets under camera-shift, weather-condition, and open-set scenarios demonstrate that EDA-PSeg achieves state-of-the-art performance, robust generalization to diverse viewing geometries, and resilience under varying environmental conditions. The code is available at https://github.com/zyfone/EDA-PSeg.

