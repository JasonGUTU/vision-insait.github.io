---
title: "Token-Consistent Dropout For Calibrated Vision Transformers"
year: 2023
venue: "International Conference on Image Processing (ICIP 2023)"
venue_display: "International Conference on Image Processing (ICIP 2023)"
venue_chronicle: "International Conference on Image Processing"
venue_abbr: "ICIP"
publication_date: "2023-10-13"
author_line_full: "Nikola Popovic, Danda Pani Paudel, Thomas Probst, Luc Van Gool"
authors:
  - nikola-popovic
  - danda-paudel
  - luc-van-gool
paper_url: "https://ieeexplore.ieee.org/abstract/document/10222084/"
---
## Abstract

We introduce token-consistent dropout in vision transformers, which improves network calibration without causing any severe drop in performance. We use linear layers with token-consistent stochastic parameters inside the multilayer perceptron blocks, without altering the architecture of the transformer. The stochastic parameters are sampled from the uniform distribution, both during training and inference. The applied linear operations preserve the topological structure, formed by the set of tokens passing through the shared multilayer perceptron. This operation encourages the learning of the recognition task to rely on the topological structures of the tokens, instead of their values, which in turn offers the desired behavior. We compare our method to established baselines and applicable state-of-the-art alternatives, to demonstrate its impact on the calibration of vision transformers.

