---
title: "A Unified Framework for Event-Based Frame Interpolation With Ad-Hoc Deblurring in the Wild"
year: 2024
venue: "IEEE Transactions on Pattern Analysis and Machine Intelligence (TPAMI 2024)"
venue_display: "IEEE Transactions on Pattern Analysis and Machine Intelligence (TPAMI 2024)"
venue_chronicle: "IEEE Transactions on Pattern Analysis and Machine Intelligence"
venue_abbr: "TPAMI"
publication_date: "2024-12-01"
author_line_full: "Lei Sun, Daniel Gehrig, Christos Sakaridis, Mathias Gehrig, Jingyun Liang, Peng Sun, Zhijie Xu, Kaiwei Wang, Luc Van Gool"
authors:
  - lei-sun
  - luc-van-gool
paper_url: "https://ieeexplore.ieee.org/document/10794600/authors#authors"
---
## Abstract

Effective video frame interpolation hinges on the adept handling of motion in the input scene. Prior work acknowledges asynchronous event information for this, but often overlooks whether motion induces blur in the video, limiting its scope to sharp frame interpolation. We instead propose a unified framework for event-based frame interpolation that performs deblurring ad-hoc and thus works both on sharp and blurry input videos. Our model consists in a bidirectional recurrent network that incorporates the temporal dimension of interpolation and fuses information from the input frames and the events adaptively based on their temporal proximity. To enhance the generalization from synthetic data to real event cameras, we integrate self-supervised framework with the proposed model to enhance the generalization on real-world datasets in the wild. At the dataset level, we introduce a novel real-world high-resolution dataset with events and color videos named HighREV, which provides a challenging evaluation setting for the examined task. Extensive experiments show that our network consistently outperforms previous state-of-the-art methods on frame interpolation, single image deblurring, and the joint task of both. Experiments on domain transfer reveal that self-supervised training effectively mitigates the performance degradation observed when transitioning from synthetic data to real-world data. Code and datasets are available at https://github.com/AHupuJR/REFID.

