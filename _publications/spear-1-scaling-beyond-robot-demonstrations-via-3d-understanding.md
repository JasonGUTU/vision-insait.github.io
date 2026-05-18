---
title: "SPEAR-1: Scaling Beyond Robot Demonstrations via 3D Understanding"
year: 2026
venue: "IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR 2026)"
venue_display: "IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR 2026)"
venue_chronicle: "IEEE/CVF Conference on Computer Vision and Pattern Recognition"
venue_abbr: "CVPR"
publication_date: "2026-06-15"
author_line_full: "Nikolay Nikolov, Giuliano Albanese, Sombit Dey, Aleksandar Yanev, Luc Van Gool, Jan-Nico Zaech, Danda Pani Paudel"
authors:
  - nikolay-nikolov
  - giuliano-albanese
  - sombit-dey
  - luc-van-gool
  - danda-paudel
paper_url: "https://arxiv.org/pdf/2511.17411"
---
## Links

- [Project](https://spear.insait.ai/)

## Abstract

Robotic Foundation Models (RFMs) hold great promise as generalist, end-to-end systems for robot control. Yet their ability to generalize across new environments, tasks, and embodiments remains limited. We argue that a major bottleneck lies in their foundations: most RFMs are built by fine-tuning internet-pretrained Vision-Language Models (VLMs). However, these VLMs are trained on 2D image-language tasks and lack the 3D spatial reasoning inherently required for embodied control in the 3D world. Bridging this gap directly with large-scale robotic data is costly and difficult to scale. Instead, we propose to enrich easy-to-collect non-robotic image data with 3D annotations and enhance a pretrained VLM with 3D understanding capabilities. Following this strategy, we train SPEAR-VLM, a 3D-aware VLM that infers object coordinates in 3D space from a single 2D image. Building on SPEAR-VLM, we introduce our main contribution, $~\textbf{SPEAR-1}$: a robotic foundation model that integrates grounded 3D perception with language-instructed embodied control. Trained on $\sim$45M frames from 24 Open X-Embodiment datasets, SPEAR-1 outperforms or matches state-of-the-art models such as $π_0$-FAST and $π_{0.5}$, while it uses 20$\times$ fewer robot demonstrations. This carefully-engineered training strategy unlocks new VLM capabilities and as a consequence boosts the reliability of embodied control beyond what is achievable with only robotic data. We make our model weights and 3D-annotated datasets publicly available at https://spear.insait.ai.
