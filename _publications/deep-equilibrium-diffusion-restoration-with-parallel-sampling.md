---
title: "Deep Equilibrium Diffusion Restoration with Parallel Sampling"
year: 2024
venue: "IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR 2024)"
venue_display: "IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR 2024)"
venue_chronicle: "IEEE/CVF Conference on Computer Vision and Pattern Recognition"
venue_abbr: "CVPR"
publication_date: "2024-06-15"
author_line_full: "Jiezhang Cao, Yue Shi, Kai Zhang, Yulun Zhang, Radu Timofte, Luc Van Gool"
authors:
  - luc-van-gool
---
## Links

- [Code](https://github.com/caojiezhang/DeqIR?tab=readme-ov-file)

## Abstract

Diffusion model-based image restoration (IR) aims to use diffusion models to recover high-quality (HQ) images from degraded images, achieving promising performance. Due to the inherent property of diffusion models, most existing methods need long serial sampling chains to restore HQ images step-by-step, resulting in expensive sampling time and high computation costs. Moreover, such long sampling chains hinder understanding the relationship between inputs and restoration results since it is hard to compute the gra-dients in the whole chains. In this work, we aim to rethink the diffusion model-based IR models through a different per-spective, i.e., a deep equilibrium (DEQ) fixed point system, called DeqIR. Specifically, we derive an analytical solution by modeling the entire sampling chain in these IR models as a joint multivariate fixed point system. Based on the analyti-cal solution, we can conduct parallel sampling and restore HQ images without training. Furthermore, we compute fast gradients via DEQ inversion and found that initialization optimization can boost image quality and control the gen-eration direction. Extensive experiments on benchmarks demonstrate the effectiveness of our method on typical IR tasks and real-world settings.
