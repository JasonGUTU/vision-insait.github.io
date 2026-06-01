---
title: "AR-VLA: Autoregressive Action Expert for Vision–Language–Action Models"
year: 2026
venue: "Robotics: Science and Systems (RSS 2026)"
venue_display: "Robotics: Science and Systems (RSS 2026)"
venue_chronicle: "Robotics: Science and Systems"
venue_abbr: "RSS"
publication_date: "2026-03-10"
author_line_full: "Yutong Hu, Jan-Nico Zaech, Nikolay Nikolov, Yuanqi Yao, Sombit Dey, Giuliano Albanese, Renaud Detry, Luc Van Gool, Danda Pani Paudel"
authors:
  - yutong-hu
  - nikolay-nikolov
  - yuanqi-yao
  - sombit-dey
  - giuliano-albanese
  - luc-van-gool
  - danda-paudel
paper_url: "https://arxiv.org/abs/2603.10126"
topics:
  - robotics
---
## Links

- [Project](https://arvla.insait.ai/)
- [Paper](https://arxiv.org/abs/2603.10126)

## Abstract

We propose a standalone autoregressive (AR) Action Expert that generates actions as a continuous causal sequence while conditioning on refreshable vision-language prefixes. In contrast to existing Vision-Language-Action (VLA) models and diffusion policies that reset temporal context with each new observation and predict actions reactively, our Action Expert maintains its own history through a long-lived memory and is inherently context-aware. Experiments on simulated and real-robot manipulation tasks demonstrate that AR-VLA can effectively replace traditional chunk-based action heads for both specialist and generalist policies, with superior history awareness and substantially smoother action trajectories while maintaining or exceeding the task success rates of state-of-the-art reactive VLAs.
