---
title: "Learning Generative Interactive Environments By Trained Agent Exploration"
year: 2024
venue: "Conference on Neural Information Processing Systems Workshop (NeurIPSW 2024)"
venue_display: "Conference on Neural Information Processing Systems Workshop (NeurIPSW 2024)"
venue_chronicle: "Conference on Neural Information Processing Systems"
venue_abbr: "NeurIPSW"
publication_date: "2024-12-10"
author_line_full: "Naser Kazemi, Nedko Savov, Danda Paudel, Luc Van Gool"
authors:
  - nedko-savov
  - danda-paudel
  - luc-van-gool
paper_url: "https://arxiv.org/pdf/2409.06445"
---
## Abstract

World models are increasingly pivotal in interpreting and simulating the rules and actions of complex environments. Genie, a recent model, excels at learning from visually diverse environments but relies on costly human-collected data. We observe that their alternative method of using random agents is too limited to explore the environment. We propose to improve the model by employing reinforcement learning based agents for data generation. This approach produces diverse datasets that enhance the model's ability to adapt and perform well across various scenarios and realistic actions within the environment. In this paper, we first release the model GenieRedux - an implementation based on Genie. Additionally, we introduce GenieRedux-G, a variant that uses the agent's readily available actions to factor out action prediction uncertainty during validation. Our evaluation, including a replication of the Coinrun case study, shows that GenieRedux-G achieves superior visual fidelity and controllability using the trained agent exploration. The proposed approach is reproducable, scalable and adaptable to new types of environments. Our codebase is available at https://github.com/insait-institute/GenieRedux .

