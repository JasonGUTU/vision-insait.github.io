---
title: "Reducing Unimodal Bias in Multi-Modal Semantic Segmentation with Multi-Scale Functional Entropy Regularization"
year: 2025
venue: "International Conference on Computer Vision (ICCV 2025)"
venue_display: "International Conference on Computer Vision (ICCV 2025)"
venue_chronicle: "International Conference on Computer Vision"
venue_abbr: "ICCV"
publication_date: "2025-10-13"
author_line_full: "Xu Zheng, Yuanhuiyi Lyu, Lutao Jiang, Danda Pani Paudel, Luc Van Gool, Xuming Hu"
authors:
  - danda-paudel
  - luc-van-gool
paper_url: "https://arxiv.org/pdf/2505.06635"
---
## Abstract

Fusing and balancing multi-modal inputs from novel sensors for dense prediction tasks, particularly semantic segmentation, is critically important yet remains a significant challenge. One major limitation is the tendency of multimodal frameworks to over-rely on easily learnable modalities, a phenomenon referred to as unimodal dominance or bias. This issue becomes especially problematic in realworld scenarios where the dominant modality may be unavailable, resulting in severe performance degradation. To this end, we apply a simple but effective plug-and-play regularization term based on functional entropy, which introduces no additional parameters or modules. This term is designed to intuitively balance the contribution of each visual modality to the segmentation results. Specifically, we leverage the log-Sobolev inequality to bound functional entropy using functional-Fisher-information. By maximizing the information contributed by each visual modality, our approach mitigates unimodal dominance and establishes a more balanced and robust segmentation framework. A multi-scale regularization module is proposed to apply our proposed plug-and-paly term on high-level features and also segmentation predictions for more balanced multimodal learning. Extensive experiments on three datasets demonstrate that our proposed method achieves superior performance, i.e., $\mathbf{+ 1 3. 9 4 \%} \boldsymbol{,} \mathbf{+ 3. 2 5 \%}$ and $\mathbf{+ 3. 6 4 \%}$, without introducing any additional parameters.

