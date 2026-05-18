---
title: "Vanishing-Point-Guided Video Semantic Segmentation of Driving Scenes ."
year: 2024
venue: "IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR 2024)"
venue_display: "IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR 2024)"
venue_chronicle: "IEEE/CVF Conference on Computer Vision and Pattern Recognition"
venue_abbr: "CVPR"
publication_date: "2024-06-15"
author_line_full: "Diandian Guo, Deng-Ping Fan, Tongyu Lu, Christos Sakaridis, Luc Van Gool"
authors:
  - luc-van-gool
paper_url: "https://arxiv.org/pdf/2401.15261.pdf"
---
## Abstract

The estimation of implicit cross-frame correspondences and the high computational cost have long been major chal-lenges in video semantic segmentation (VSS) for driving scenes. Prior works utilize keyframes, feature propagation, or cross-frame attention to address these issues. By contrast, we are the first to harness vanishing point (VP) priors for more effective segmentation. Intuitively, objects near VPs (i.e., away from the vehicle) are less discernible. Moreover, they tend to move radially away from the VP over time in the usual case of a forward-facing camera, a straight road, and linear forward motion of the vehicle. Our novel, efficient network for VSS, named VPSeg, incor-porates two modules that utilize exactly this pair of static and dynamic VP priors: sparse-to-dense feature mining (DenseVP) and VP-guided motion fusion (MotionVP). MotionVP employs VP-guided motion estimation to establish explicit correspondences across frames and help attend to the most relevant features from neighboring frames, while Dense Vp enhances weak dynamic features in distant re-gions around VPs. These modules operate within a context-detail framework, which separates contextual features from high-resolution local features at different input resolutions to reduce computational costs. Contextual and local fea-tures are integrated through contextualized motion attention (CMA) for the final prediction. Extensive experiments on two popular driving segmentation benchmarks, Cityscapes and ACDC, demonstrate that VPSeg outperforms previous SOTA methods, with only modest computational overhead. The resources are available at https://github.com/RascalGdd/VPSeg.

