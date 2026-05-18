---
title: "Unlocking Efficient Vehicle Dynamics Modeling via Analytic World Models"
year: 2026
venue: "AAAI Conference on Artificial Intelligence (AAAI 2026)"
venue_display: "AAAI Conference on Artificial Intelligence (AAAI 2026)"
venue_chronicle: "AAAI Conference on Artificial Intelligence"
venue_abbr: "AAAI"
publication_date: "2026-02-15"
author_line_full: "Asen Nachkov, Danda Pani Paudel, Jan-Nico Zaech, Davide Scaramuzza, Luc Van Gool"
authors:
  - asen-nachkov
  - danda-paudel
  - luc-van-gool
paper_url: "https://arxiv.org/pdf/2502.10012"
---
## Abstract

Differentiable simulators represent an environment’s dynamics as a differentiable function. Within robotics and autonomous driving, this property is used in Analytic Policy Gradients (APG), which relies on backpropagating through the dynamics to train accurate policies for diverse tasks. Here we show that differentiable simulation also has an important role in world modeling, where it can impart predictive, prescriptive, and counterfactual capabilities to an agent. Specifically, we design three novel task setups in which the differentiable dynamics are combined within an end-to-end computation graph not with a policy, but a state predictor. This allows us to learn relative odometry, optimal planners, and optimal inverse states. We collectively call these predictors Analytic World Models (AWMs) and demonstrate how differentiable simulation enables their efficient, end-to-end learning. In autonomous driving scenarios, they have broad applicability and can augment an agent’s decision-making beyond reactive control.

