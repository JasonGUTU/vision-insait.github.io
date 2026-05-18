---
title: "Autodecoding Latent 3D Diffusion Models"
year: 2023
venue: "Conference on Neural Information Processing Systems (NeurIPS 2023)"
venue_display: "Conference on Neural Information Processing Systems (NeurIPS 2023)"
venue_chronicle: "Conference on Neural Information Processing Systems"
venue_abbr: "NeurIPS"
publication_date: "2023-12-10"
author_line_full: "Evangelos Ntavelis, Aliaksandr Siarohin, Kyle Olszewski, Chaoyang Wang, Luc Van Gool, Sergey Tulyakov"
authors:
  - luc-van-gool
paper_url: "https://openreview.net/pdf?id=YhAZqWhOnS"
---
## Abstract

We present a novel approach to the generation of static and articulated 3D assets that has a 3D autodecoder at its core. The 3D autodecoder framework embeds properties learned from the target dataset in the latent space, which can then be decoded into a volumetric representation for rendering view-consistent appearance and geometry. We then identify the appropriate intermediate volumetric latent space, and introduce robust normalization and de-normalization operations to learn a 3D diffusion from 2D images or monocular videos of rigid or articulated objects. Our approach is flexible enough to use either existing camera supervision or no camera information at all -- instead efficiently learning it during training. Our evaluations demonstrate that our generation results outperform state-of-the-art alternatives on various benchmark datasets and metrics, including multi-view image datasets of synthetic objects, real in-the-wild videos of moving people, and a large-scale, real video dataset of static objects.

