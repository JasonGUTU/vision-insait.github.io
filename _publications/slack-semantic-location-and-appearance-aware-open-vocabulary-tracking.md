---
title: "SLAck: Semantic, Location, and Appearance Aware Open-Vocabulary Tracking"
year: 2024
venue: "European Conference on Computer Vision (ECCV 2024)"
venue_display: "European Conference on Computer Vision (ECCV 2024)"
venue_chronicle: "European Conference on Computer Vision"
venue_abbr: "ECCV"
publication_date: "2024-09-29"
author_line_full: "Siyuan Li, Lei Ke, Yung-Hsu Yang, Luigi Piccinelli, Mattia Segù, Martin Danelljan, Luc Van Gool"
authors:
  - luc-van-gool
paper_url: "https://arxiv.org/pdf/2409.11235"
---
## Abstract

Open-vocabulary Multiple Object Tracking (MOT) aims to generalize trackers to novel categories not in the training set. Currently, the best-performing methods are mainly based on pure appearance matching. Due to the complexity of motion patterns in the large-vocabulary scenarios and unstable classification of the novel objects, the motion and semantics cues are either ignored or applied based on heuristics in the final matching steps by existing methods. In this paper, we present a unified framework SLAck that jointly considers semantics, location, and appearance priors in the early steps of association and learns how to integrate all valuable information through a lightweight spatial and temporal object graph. Our method eliminates complex post-processing heuristics for fusing different cues and boosts the association performance significantly for large-scale open-vocabulary tracking. Without bells and whistles, we outperform previous state-of-the-art methods for novel classes tracking on the open-vocabulary MOT and TAO TETA benchmarks. Our code is available at \href{https://github.com/siyuanliii/SLAck}{github.com/siyuanliii/SLAck}.

