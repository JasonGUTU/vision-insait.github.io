---
title: "ProOOD: Prototype-Guided Out-of-Distribution 3D Occupancy Prediction"
year: 2026
venue: "IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR 2026)"
venue_display: "IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR 2026)"
venue_chronicle: "IEEE/CVF Conference on Computer Vision and Pattern Recognition"
venue_abbr: "CVPR"
publication_date: "2026-06-15"
author_line_full: "Yuheng Zhang, Mengfei Duan, Kunyu Peng, Yuhang Wang, Ruiping Liu, Fei Teng, Kai Luo, Zhiyong Li, Kailun Yang"
authors:
  - kunyu-peng
paper_url: "https://arxiv.org/pdf/2506.21185"
---
## Abstract

3D semantic occupancy prediction is crucial for autonomous driving, providing a dense, semantically rich environmental representation. However, existing methods focus on in-distribution scenes, making them susceptible to Out-of-Distribution (OoD) objects and long-tail distributions, which increases the risk of undetected anomalies and misinterpretations, posing safety hazards. To address these challenges, we introduce Out-of-Distribution Semantic Occupancy Prediction, targeting OoD detection in 3D voxel space. To fill dataset gaps, we propose a Realistic Anomaly Augmentation that injects synthetic anomalies while preserving realistic spatial and occlusion patterns, enabling the creation of two datasets: VAA-KITTI and VAA-KITTI-360. Then, a novel framework that integrates OoD detection into 3D semantic occupancy prediction, OccOoD, is proposed, which uses Cross-Space Semantic Refinement (CSSR) to refine semantic predictions from complementary voxel and BEV representations, improving OoD detection. Experimental results demonstrate that OccOoD achieves state-of-the-art OoD detection with an AuROC of 65.50% and an AuPRCr of 31.83 within a 1.2m region, while maintaining competitive semantic occupancy prediction performance and generalization in real-world urban driving scenes. The established datasets and source code will be made publicly available at https://github.com/7uHeng/OccOoD.

