---
title: "Autonomous Vehicle Controllers From End-to-End Differentiable Simulation"
year: 2025
venue: "IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS 2025)"
venue_display: "IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS 2025)"
venue_chronicle: "IEEE/RSJ International Conference on Intelligent Robots and Systems"
venue_abbr: "IROS"
publication_date: "2025-10-14"
author_line_full: "Asen Nachkov, Danda Pani Paudel, Luc Van Gool"
authors:
  - asen-nachkov
  - danda-paudel
  - luc-van-gool
paper_url: "https://arxiv.org/pdf/2409.07965"
---
## Abstract

Current methods to learn controllers for autonomous vehicles (AVs) focus on behavioural cloning. Being trained only on exact historic data, the resulting agents often generalize poorly to novel scenarios. Simulators provide the opportunity to go beyond offline datasets, but they are still treated as complicated black boxes, only used to update the global simulation state. As a result, these RL algorithms are slow, sample-inefficient, and prior-agnostic. In this work, we leverage a differentiable simulator and design an analytic policy gradients (APG) approach to training AV controllers on the large-scale Waymo Open Motion Dataset. Our proposed framework brings the differentiable simulator into an end-to-end training loop, where gradients of the environment dynamics serve as a useful prior to help the agent learn a more grounded policy. We combine this setup with a recurrent architecture that can efficiently propagate temporal information across long simulated trajectories. This APG method allows us to learn robust, accurate, and fast policies, while only requiring widely-available expert trajectories, instead of scarce expert actions. We compare to behavioural cloning and find significant improvements in performance and robustness to noise in the dynamics, as well as overall more intuitive human-like handling.

