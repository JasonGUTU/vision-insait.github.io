---
title: "Image Fusion via Vision-Language Model"
year: 2024
venue: "International Conference on Machine Learning (ICML 2024)"
venue_display: "International Conference on Machine Learning (ICML 2024)"
venue_chronicle: "International Conference on Machine Learning"
venue_abbr: "ICML"
publication_date: "2024-07-21"
author_line_full: "Zixiang Zhao, Lilun Deng, Haowen Bai, Yukun Cui, Zhipeng Zhang, Yulun Zhang, Haotong Qin, Dongdong Chen, Jiangshe Zhang, Peng Wang, Luc Van Gool"
authors:
  - luc-van-gool
paper_url: "https://openreview.net/pdf/26f043e709cf17b73a2ecd60f42cb0638d19ad61.pdf?fbclid=IwY2xjawEYYM5leHRuA2FlbQIxMAABHT1laVrR5Jt165KocsOzY7p18MU9vnbJBEtm1ZmU1fZvy0jDBep1BBnWmg_aem_9N98VTknXEaKQTjFkao2aA"
---
## Abstract

Image fusion integrates essential information from multiple images into a single composite, enhancing structures, textures, and refining imperfections. Existing methods predominantly focus on pixel-level and semantic visual features for recognition, but often overlook the deeper text-level semantic information beyond vision. Therefore, we introduce a novel fusion paradigm named image Fusion via vIsion-Language Model (FILM), for the first time, utilizing explicit textual information from source images to guide the fusion process. Specifically, FILM generates semantic prompts from images and inputs them into ChatGPT for comprehensive textual descriptions. These descriptions are fused within the textual domain and guide the visual information fusion, enhancing feature extraction and contextual understanding, directed by textual semantic information via cross-attention. FILM has shown promising results in four image fusion tasks: infrared-visible, medical, multi-exposure, and multi-focus image fusion. We also propose a vision-language dataset containing ChatGPT-generated paragraph descriptions for the eight image fusion datasets across four fusion tasks, facilitating future research in vision-language model-based image fusion. Code and dataset are available at https://github.com/Zhaozixiang1228/IF-FILM.

