---
title: "Think Small, Act Big: Primitive Prompt Learning for Lifelong Robot Manipulation"
year: 2025
venue: "IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR 2025)"
venue_display: "IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR 2025)"
venue_chronicle: "IEEE/CVF Conference on Computer Vision and Pattern Recognition"
venue_abbr: "CVPR"
publication_date: "2025-06-15"
author_line_full: "Yuanqi Yao, Siao Liu, Haoming Song, Delin Qu, Qizhi Chen, Yan Ding, Bin Zhao, Zhigang Wang, Xuelong Li, Dong Wang"
authors:
  - yuanqi-yao
paper_url: "https://arxiv.org/pdf/2504.00420"
---
## Abstract

Building a lifelong robot that can effectively leverage prior knowledge for continuous skill acquisition remains significantly challenging. Despite the success of experience replay and parameter-efficient methods in alleviating catastrophic forgetting problem, naively applying these methods causes a failure to leverage the shared primitives between skills. To tackle these issues, we propose Primitive Prompt Learning (PPL), to achieve lifelong robot manipulation via reusable and extensible primitives. Within our two stage learning scheme, we first learn a set of primitive prompts to represent shared primitives through multi-skills pre-training stage, where motion-aware prompts are learned to capture semantic and motion shared primitives across different skills. Secondly, when acquiring new skills in lifelong span, new prompts are appended and optimized with frozen pretrained prompts, boosting the learning via knowledge transfer from old skills to new ones. For evaluation, we construct a large-scale skill dataset and conduct extensive experiments in both simulation and real-world tasks, demonstrating PPL's superior performance over state-of-the-art methods.

