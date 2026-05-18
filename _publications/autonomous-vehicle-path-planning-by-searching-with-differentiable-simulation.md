---
title: "Autonomous Vehicle Path Planning by Searching With Differentiable Simulation"
year: 2026
venue: "AAAI Conference on Artificial Intelligence (AAAI 2026)"
venue_display: "AAAI Conference on Artificial Intelligence (AAAI 2026)"
venue_chronicle: "AAAI Conference on Artificial Intelligence"
venue_abbr: "AAAI"
publication_date: "2026-02-15"
author_line_full: "Asen Nachkov, Jan-Nico Zaech, Danda Pani Paudel, Xi Wang, Luc Van Gool"
authors:
  - asen-nachkov
  - danda-paudel
  - luc-van-gool
paper_url: "https://arxiv.org/pdf/2511.11043"
---
## Abstract

Planning allows an agent to safely refine its actions before executing them in the real world. In autonomous driving, this is crucial to avoid collisions and navigate in complex, dense traffic scenarios. One way to plan is to search for the best action sequence. However, this is challenging when all necessary components – policy, next-state predictor, and critic – have to be learned. Here we propose Differentiable Simulation for Search (DSS), a framework that leverages the differentiable simulator Waymax as both a next state predictor and a critic. It relies on the simulator’s hardcoded dynamics, making state predictions highly accurate, while utilizing the simulator’s differentiability to effectively search across action sequences. Our DSS agent optimizes its actions using gradient descent over imagined future trajectories. We show experimentally that DSS – the combination of planning gradients and stochastic search – significantly improves tracking and path planning accuracy compared to sequence prediction, imitation learning, model-free RL, and other planning methods.

