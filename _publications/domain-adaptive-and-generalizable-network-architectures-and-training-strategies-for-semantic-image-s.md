---
title: "Domain Adaptive and Generalizable Network Architectures and Training Strategies for Semantic Image Segmentation"
year: 2024
venue: "IEEE Transactions on Pattern Analysis and Machine Intelligence (TPAMI 2024)"
venue_display: "IEEE Transactions on Pattern Analysis and Machine Intelligence (TPAMI 2024)"
venue_chronicle: "IEEE Transactions on Pattern Analysis and Machine Intelligence"
venue_abbr: "TPAMI"
publication_date: "2024-12-01"
author_line_full: "Lukas Hoyer, Dengxin Dai, Luc Van Gool"
authors:
  - luc-van-gool
paper_url: "https://ieeexplore.ieee.org/document/10266755"
---
## Abstract

Unsupervised domain adaptation (UDA) and domain generalization (DG) enable machine learning models trained on a source domain to perform well on unlabeled or even unseen target domains. As previous UDA&DG semantic segmentation methods are mostly based on outdated networks, we benchmark more recent architectures, reveal the potential of Transformers, and design the DAFormer network tailored for UDA&DG. It is enabled by three training strategies to avoid overfitting to the source domain: While (1) Rare Class Sampling mitigates the bias toward common source domain classes, (2) a Thing-Class ImageNet Feature Distance and (3) a learning rate warmup promote feature transfer from ImageNet pretraining. As UDA&DG are usually GPU memory intensive, most previous methods downscale or crop images. However, low-resolution predictions often fail to preserve fine details while models trained with cropped images fall short in capturing long-range, domain-robust context information. Therefore, we propose HRDA, a multi-resolution framework for UDA&DG, that combines the strengths of small high-resolution crops to preserve fine segmentation details and large low-resolution crops to capture long-range context dependencies with a learned scale attention. DAFormer and HRDA significantly improve the state-of-the-art UDA&DG by more than 10 mIoU on 5 different benchmarks.

