---
title: ObjectRelator
tagline: Cross-view ego–exo object correspondence with MCFuse and XObjAlign — ICCV 2025 Highlight.
cover_image: /assets/images/portfolio/objectrelator.png
release_date: 2025-10-13
project_year: "2025"
sidebar_tags: Egocentric, Cross-view, Segmentation
external_url: https://yuqianfu.com/ObjectRelator/
contributors:
  - danda-paudel
  - luc-van-gool
topics:
  - egocentric-vision
---

**ObjectRelator** tackles **ego–exo object correspondence**: given object queries from one view (e.g. egocentric), predict matching object masks in another (e.g. exocentric). The task is grounded in **Ego-Exo4D** and supports VR and robotics settings where agents learn from cross-view demonstrations.

The method combines **Multimodal Condition Fusion (MCFuse)**, which brings text into cross-view segmentation for stronger localization, and **Cross-View Object Alignment (XObjAlign)** for consistency under large appearance and viewpoint shifts. ObjectRelator reaches **state-of-the-art** results on Ego-Exo4D and the additional **HANDAL-X** benchmark.

**Resources:** [Project page](https://yuqianfu.com/ObjectRelator/) · [Paper](https://arxiv.org/pdf/2411.19083) · [Data & code](https://yuqianfu.com/ObjectRelator/) · [Live demo](https://huggingface.co/spaces/YuqianFu/ObjectRelatorDemo)
