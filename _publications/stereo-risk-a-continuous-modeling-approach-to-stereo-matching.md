---
title: "Stereo Risk: A Continuous Modeling Approach to Stereo Matching"
year: 2024
venue: "International Conference on Machine Learning (ICML 2024)"
venue_display: "International Conference on Machine Learning (ICML 2024)"
venue_chronicle: "International Conference on Machine Learning"
venue_abbr: "ICML"
publication_date: "2024-07-21"
author_line_full: "Ce Liu, Suryansh Kumar, Shuhang Gu, Radu Timofte, Yao Yao, Luc Van Gool"
authors:
  - luc-van-gool
paper_url: "https://openreview.net/pdf/564a60520f502e7842cb3d694a69d28d7f1c8414.pdf?fbclid=IwY2xjawEYYNZleHRuA2FlbQIxMAABHSUR-AtDZIOJsgv86YPMsv9ANV1xyRkiMsYuV58eWyjhmxJra07TvjePhw_aem_zHMExuV983r28hEf2aY_DA"
---
## Abstract

We introduce Stereo Risk, a new deep-learning approach to solve the classical stereo-matching problem in computer vision. As it is well-known that stereo matching boils down to a per-pixel disparity estimation problem, the popular state-of-the-art stereo-matching approaches widely rely on regressing the scene disparity values, yet via discretization of scene disparity values. Such discretization often fails to capture the nuanced, continuous nature of scene depth. Stereo Risk departs from the conventional discretization approach by formulating the scene disparity as an optimal solution to a continuous risk minimization problem, hence the name"stereo risk". We demonstrate that $L^1$ minimization of the proposed continuous risk function enhances stereo-matching performance for deep networks, particularly for disparities with multi-modal probability distributions. Furthermore, to enable the end-to-end network training of the non-differentiable $L^1$ risk optimization, we exploited the implicit function theorem, ensuring a fully differentiable network. A comprehensive analysis demonstrates our method's theoretical soundness and superior performance over the state-of-the-art methods across various benchmark datasets, including KITTI 2012, KITTI 2015, ETH3D, SceneFlow, and Middlebury 2014.

