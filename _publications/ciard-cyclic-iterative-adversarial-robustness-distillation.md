---
title: "CIARD: Cyclic Iterative Adversarial Robustness Distillation"
year: 2025
venue: "International Conference on Computer Vision (ICCV 2025)"
venue_display: "International Conference on Computer Vision (ICCV 2025)"
venue_chronicle: "International Conference on Computer Vision"
venue_abbr: "ICCV"
publication_date: "2025-10-13"
author_line_full: "Liming Lu, Shuchao Pang, Xu Zheng, Xiang GU, Anan Du, Yunhuai Liu, Yongbin Zhou"
---
## Abstract

Adversarial robustness distillation (ARD) aims to transfer both performance and robustness from teacher model to lightweight student model, enabling resilient performance on resource-constrained scenarios. Though existing ARD approaches enhance student model's robustness, the inevitable by-product leads to the degraded performance on clean examples. We summarize the causes of this problem inherent in existing methods with dual-teacher framework as: (1) The divergent optimization objectives of dualteacher models, i.e., the clean and robust teachers, impede effective knowledge transfer to the student model, and (2) The iteratively generated adversarial examples during training lead to performance deterioration of the robust teacher model. To address these challenges, we propose a novel Cyclic Iterative ARD (CIARD) method with two key innovations: (1) A multi-teacher framework with contrastive push-loss alignment to resolve conflicts in dualteacher optimization objectives, and (2) Continuous adversarial retraining to maintain dynamic teacher robustness against performance degradation from the varying adversarial examples. Extensive experiments on CIFAR-10, CIFAR-100, and Tiny-ImageNet demonstrate that CIARD achieves remarkable performance with an average 3.53% improvement in adversarial defense rates across various attack scenarios and a $\mathbf{5. 8 7 \%}$ increase in clean sample accuracy, establishing a new benchmark for balancing model robustness and generalization. Our code is available at https://github.com/eminentgu/CIARD.

