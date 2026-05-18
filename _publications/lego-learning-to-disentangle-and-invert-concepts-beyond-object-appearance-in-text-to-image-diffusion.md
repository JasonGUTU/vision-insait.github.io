---
title: "Lego: Learning to Disentangle and Invert Concepts Beyond Object Appearance in Text-to-Image Diffusion Models"
year: 2024
venue: "European Conference on Computer Vision (ECCV 2024)"
venue_display: "European Conference on Computer Vision (ECCV 2024)"
venue_chronicle: "European Conference on Computer Vision"
venue_abbr: "ECCV"
publication_date: "2024-09-29"
author_line_full: "Saman Motamed, Danda Pani Paudel, Luc Van Gool"
authors:
  - sam-motamed
  - danda-paudel
  - luc-van-gool
paper_url: "https://arxiv.org/pdf/2311.13833"
---
## Abstract

Text-to-Image (T2I) models excel at synthesizing concepts such as nouns, appearances, and styles. To enable customized content creation based on a few example images of a concept, methods such as Textual Inversion and DreamBooth invert the desired concept and enable synthesizing it in new scenes. However, inverting personalized concepts that go beyond object appearance and style (adjectives and verbs) through natural language remains a challenge. Two key characteristics of these concepts contribute to the limitations of current inversion methods. 1) Adjectives and verbs are entangled with nouns (subject) and can hinder appearance-based inversion methods, where the subject appearance leaks into the concept embedding, and 2) describing such concepts often extends beyond single word embeddings. In this study, we introduce Lego, a textual inversion method designed to invert subject-entangled concepts from a few example images. Lego disentangles concepts from their associated subjects using a simple yet effective Subject Separation step and employs a Context Loss that guides the inversion of single/multi-embedding concepts. In a thorough user study, Lego-generated concepts were preferred over 70% of the time when compared to the baseline in terms of authentically generating concepts according to a reference. Additionally, visual question answering using an LLM suggested Lego-generated concepts are better aligned with the text description of the concept.

