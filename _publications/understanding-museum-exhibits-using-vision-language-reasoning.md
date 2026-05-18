---
title: "Understanding Museum Exhibits using Vision-Language Reasoning"
year: 2025
venue: "International Conference on Computer Vision (ICCV 2025)"
venue_display: "International Conference on Computer Vision (ICCV 2025)"
venue_chronicle: "International Conference on Computer Vision"
venue_abbr: "ICCV"
publication_date: "2025-10-13"
author_line_full: "Ada-Astrid Balauca, Sanjana Garai, Stefan Balauca, Rasesh Udayakumar Shetty, Naitik Agrawal, Dhwanil Subhashbhai Shah, Yuqian Fu, Xi Wang, Kristina Toutanova, Danda Pani Paudel, Luc Van Gool"
authors:
  - danda-paudel
  - luc-van-gool
paper_url: "https://arxiv.org/pdf/2412.01370"
---
## Abstract

Museums serve as repositories of cultural heritage and historical artifacts from diverse epochs, civilizations, and regions, preserving well-documented collections that encapsulate vast knowledge, which, when systematically structured into large-scale datasets, can train specialized models. Visitors engage with exhibits through curiosity and questions, making expert domain-specific models essential for interactive query resolution and gaining historical insights. Understanding exhibits from images requires analyzing visual features and linking them to historical knowledge to derive meaningful correlations. We facilitate such reasoning by (a) collecting and curating a large-scale dataset of 65 M images and 200 M question-answer pairs for exhibits from all around the world; (b) training large vision-language models (VLMs) on the collected dataset; (c) benchmarking their ability on five visual question answering tasks, specifically designed to reflect real-world inquiries and challenges observed in museum settings. The complete dataset is labeled by museum experts, ensuring the quality and the practical significance of the labels. We train two VLMs from different categories: BLIP [41] with visionlanguage aligned embeddings, but lacking the expressive power of large language models, and the LLaVA [46] model, a powerful instruction-tuned LLM enriched with vision-language reasoning capabilities. Through extensive experiments, we find that while both model types effectively answer visually grounded questions, large vision-language models excel in queries requiring deeper historical context and reasoning. We further demonstrate the necessity of finetuning models on large-scale domain-specific datasets by showing that our fine-tuned models significantly outperform current SOTA VLMs in answering questions related to specific attributes, highlighting their limitations in handling complex, nuanced queries. Our dataset, benchmarks, and source code are available at: insait-institute/Museum-65.

