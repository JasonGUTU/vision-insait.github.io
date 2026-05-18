---
title: "EngiBench: A Benchmark for Evaluating Large Language Models on Engineering Problem Solving"
year: 2026
venue: "Annual Meeting of the Association for Computational Linguistics (ACL 2026) Findings"
venue_display: "Annual Meeting of the Association for Computational Linguistics (ACL 2026) Findings"
venue_chronicle: "Annual Meeting of the Association for Computational Linguistics"
venue_abbr: "ACL"
publication_date: "2026-07-15"
author_line_full: "Xiyuan Zhou, Xinlei Wang, Yirui He, Ruixi Zou, Yang Wu, Yuheng Cheng, Yulu Xie, Wenxuan Liu, Huan Zhao, Yan Xu, Jinjin Gu, Junhua Zhao"
authors:
  - jinjin-gu
paper_url: "https://arxiv.org/pdf/2509.17677"
---
## Abstract

Large language models (LLMs) have shown strong performance on mathematical reasoning under well-defined conditions. However, real-world engineering problems involve uncertainty, context, and open-ended settings that extend beyond symbolic computation. Existing benchmarks largely focus on well-defined or abstract reasoning and therefore fail to capture these complexities. We introduce EngiBench, a hierarchical benchmark designed to evaluate LLMs on solving engineering problems. It spans three levels of increasing difficulty (foundational knowledge retrieval, contextual reasoning, and open-ended modeling) and covers diverse engineering subfields. To facilitate a deeper understanding of model performance, we systematically rewrite each problem into three controlled variants (perturbed, knowledge-enhanced, and math abstraction), enabling us to separately evaluate the model's robustness, domain-specific knowledge, and mathematical reasoning abilities. Experimental results show clear performance stratification across difficulty levels: model accuracy declines with task complexity, degrades under minor perturbations, and remains substantially below human performance on high-level engineering tasks. These findings reveal that current LLMs still lack the high-level reasoning needed for real-world engineering, highlighting the need for future models with deeper and more reliable problem-solving capabilities. Our source code and data are available at https://github.com/AI4Engi/EngiBench.

