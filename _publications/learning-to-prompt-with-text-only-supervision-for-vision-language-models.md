---
title: "Learning to Prompt with Text Only Supervision for Vision-Language Models"
year: 2025
venue: "AAAI Conference on Artificial Intelligence (Technical Track on Computer Vision III) (AAAI-CV 2025)"
venue_display: "AAAI Conference on Artificial Intelligence (Technical Track on Computer Vision III) (AAAI-CV 2025)"
venue_chronicle: "AAAI Conference on Artificial Intelligence (Technical Track on Computer Vision III)"
venue_abbr: "AAAI-CV"
publication_date: "2025-02-15"
author_line_full: "Muhammad Uzair Khattak, Muhammad Ferjad Naeem, Muzammal Naseer, Luc Van Gool, Federico Tombari"
authors:
  - luc-van-gool
paper_url: "https://ojs.aaai.org/index.php/AAAI/article/view/32444"
---
## Abstract

Foundational vision-language models like CLIP are emerging as a promising paradigm in vision due to their excellent generalization. However, adapting these models for downstream tasks while maintaining their generalization remains challenging. In literature, one branch of methods adapts CLIP by learning prompts using images. While effective, these methods often rely on image-label data, which is not always practical, and struggle to generalize to new datasets due to overfitting on few-shot source data. Another approach explores training-free methods by generating class captions from large language models (LLMs) and performing prompt ensembling, but these methods often produce static, class-specific prompts that cannot be transferred to new classes and incur additional costs by generating LLM descriptions for each class separately. In this work, we aim to combine the strengths of both approaches by learning prompts using only text data derived from LLMs. As supervised training of prompts in the image-free setup is non-trivial, we develop a language-only efficient training approach that enables prompts to distill rich contextual knowledge from LLM data. Furthermore, by mapping the LLM contextual text data within the learned prompts, our approach enables zero-shot transfer of prompts to new classes and datasets, potentially reducing the LLM prompt engineering cost. To the best of our knowledge, this is the first work that learns generalized and transferable prompts for image tasks using only text data. We perform evaluations on 4 benchmarks, where ProText improves over ensembling methods while being competitive with those using labeled images.

