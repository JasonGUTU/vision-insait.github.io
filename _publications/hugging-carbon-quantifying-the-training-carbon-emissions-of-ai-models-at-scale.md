---
title: "Hugging Carbon: Quantifying the Training Carbon Emissions of AI Models at Scale"
year: 2026
venue: "International Conference on Machine Learning (ICML 2026)"
venue_display: "International Conference on Machine Learning (ICML 2026)"
venue_chronicle: "International Conference on Machine Learning"
venue_abbr: "ICML"
publication_date: "2026-07-21"
author_line_full: "Xinlei Wang, Ruibo Ming, Jing Qiu, Junhua Zhao, Jinjin Gu"
authors:
  - ruibo-ming
  - jinjin-gu
paper_url: "https://arxiv.org/pdf/2605.01549"
---
## Abstract

The scaling-law era has transformed artificial intelligence from research into a global industry, but its rapid growth raises concerns over energy usage, carbon emissions, and environmental sustainability. Unlike traditional sectors, the AI industry still lacks systematic carbon accounting methods that support large-scale estimates without reproducing the original model. This leaves open questions about how large the problem is today and how large it might be in the near future. Given that the Hugging Face (HF) platform well represents the broader open-source community, we treat it as a large-scale, publicly accessible, and audit-ready corpus for carbon accounting. We propose a FLOPs-based framework to estimate aggregate training emissions of HF open-source models. Considering their uneven disclosure quality, we introduce a tiered approach to handle incomplete metadata, supported by empirical regressions that verify the statistical significance. Compute is also converted to AI training carbon intensity (ATCI, emissions per compute), a metric to assess the sustainability efficiency of model training. Our results show that training the most popular open-source models (with over 5,000 downloads) has resulted in approximately $5.8\times10^4$ metric tons of carbon emissions. This paper provides a scalable framework for emission estimations and a practical methodology to guide future standards and sustainability strategies in the AI industry.

