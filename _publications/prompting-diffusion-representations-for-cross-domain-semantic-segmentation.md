---
title: "Prompting Diffusion Representations for Cross-Domain Semantic Segmentation"
year: 2024
venue: "British Machine Vision Conference (BMVC 2024)"
venue_display: "British Machine Vision Conference (BMVC 2024)"
venue_chronicle: "British Machine Vision Conference"
venue_abbr: "BMVC"
publication_date: "2024-11-20"
author_line_full: "Rui Gong, Martin Danelljan, Han Sun, Julio Delgado Mangas, Nikolay Marin, Luc Van Gool"
authors:
  - luc-van-gool
paper_url: "https://arxiv.org/abs/2307.02138"
---
## Abstract

While originally designed for image generation, diffusion models have recently shown to provide excellent pretrained feature representations for semantic segmentation. Intrigued by this result, we set out to explore how well diffusion-pretrained representations generalize to new domains, a crucial ability for any representation. We find that diffusion-pretraining achieves extraordinary domain generalization results for semantic segmentation, outperforming both supervised and self-supervised backbone networks. Motivated by this, we investigate how to utilize the model's unique ability of taking an input prompt, in order to further enhance its cross-domain performance. We introduce a scene prompt and a prompt randomization strategy to help further disentangle the domain-invariant information when training the segmentation head. Moreover, we propose a simple but highly effective approach for test-time domain adaptation, based on learning a scene prompt on the target domain in an unsupervised manner. Extensive experiments conducted on four synthetic-to-real and clear-to-adverse weather benchmarks demonstrate the effectiveness of our approaches. Without resorting to any complex techniques, such as image translation, augmentation, or rare-class sampling, we set a new state-of-the-art on all benchmarks. Our implementation will be publicly available at \url{https://github.com/ETHRuiGong/PTDiffSeg}.

