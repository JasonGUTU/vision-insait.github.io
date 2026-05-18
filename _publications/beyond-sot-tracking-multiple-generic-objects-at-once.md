---
title: "Beyond SOT: Tracking Multiple Generic Objects at Once"
year: 2024
venue: "Winter Conference on Applications of Computer Vision Workshop (WACVW 2024)"
venue_display: "Winter Conference on Applications of Computer Vision Workshop (WACVW 2024)"
venue_chronicle: "Winter Conference on Applications of Computer Vision"
venue_abbr: "WACVW"
publication_date: "2024-03-03"
author_line_full: "Christoph Mayer, Martin Danelljan, Ming-Hsuan Yang, Vittorio Ferrari, Luc Van Gool, Alina Kuznetsova"
authors:
  - luc-van-gool
paper_url: "https://ieeexplore.ieee.org/document/10483760"
---
## Abstract

Generic Object Tracking (GOT) is the problem of tracking target objects, specified by bounding boxes in the first frame of a video. While the task has received much attention in the last decades, researchers have almost exclusively focused on the single object setting. However multiobject GOT poses its own challenges and is more attractive in real-world applications. We attribute the lack of research interest into this problem to the absence of suitable benchmarks. In this work, we introduce a new largescale GOT benchmark, LaGOT, containing multiple annotated target objects per sequence. Our benchmark allows users to tackle key remaining challenges in GOT, aiming to increase robustness and reduce computation through joint tracking of multiple objects simultaneously. In addition, we propose a transformer-based GOT tracker baseline capable of joint processing of multiple objects through shared computation. Our approach achieves a 4× faster run-time in case of 10 concurrent objects compared to tracking each object independently and outperforms existing single object trackers on our new benchmark. In addition, our approach achieves highly competitive results on single-object GOT datasets, setting a new state of the art on TrackingNet with a success rate AUC of 84.4%. Our benchmark, code, results and trained models are available at https://github.com/visionml/pytracking.

