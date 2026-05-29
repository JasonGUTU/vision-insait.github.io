---
topic_id: space-ai
title: Space AI
order: 2
summary: Reliable Understanding and Reasoning for Earth Observation
hero_image: /assets/images/blog/space-ai.png
intro_video: /site-covers/home/hero-video.mp4
---

<style>
  .sa-float-right {
    float: right;
    width: 55%;
    margin: 0.25rem 0 1rem 1.5rem;
    border-radius: 0.75rem;
    overflow: hidden;
    box-shadow: 0 4px 16px rgba(0,0,0,0.08);
  }
  .sa-float-right img { width: 100%; height: auto; display: block; }
  .sa-float-right ~ h4 { clear: right; }
  .sa-topic-figure { margin: 1.5rem 0 2.5rem; }
  .sa-topic-figure img {
    width: 100%; height: auto; display: block;
    border-radius: 0.75rem;
    box-shadow: 0 4px 16px rgba(0,0,0,0.08);
  }
  @media (max-width: 700px) {
    .sa-float-right {
      float: none;
      width: 100%;
      margin: 0 0 1.5rem 0;
    }
  }
</style>

<figure class="sa-float-right">
  <img src="{{ '/assets/images/topics/space-ai-unified-understanding.png' | relative_url }}"
       alt="Unified understanding of Earth: fusing diverse signals, viewpoints, times, and scales"
       loading="lazy" decoding="async" />
</figure>

Earth is the largest and most information-dense scene available to any vision system. Remote sensing captures it across spatial structure, spectral signatures, temporal change, and physical signals simultaneously — encoding patterns and dynamics invisible to conventional imagery. SpaceAI develops large multimodal models that combine satellite imagery, text, spatiotemporal signals, and geospatial context to advance planning, prediction, prevention, and high-resolution monitoring across diverse Earth systems.

We do not treat a satellite image in isolation, but reason about it in the context of its temporal history, spectral properties, geographic grounding, and the broader chain of events it belongs to. This demands architectures that coordinate across sensor types, adapt to missing or imperfect data, apply physical and geometric priors, and produce outputs beyond text — including dense prediction maps, segmentation masks, risk rasters, and vector geospatial layers. By uniting multimodal models, spatiotemporal reasoning, and agentic perception, SpaceAI aims to build a unified research program for intelligent Earth understanding.


#### Multi-Modal Earth Understanding

Earth observation requires reading the planet across all the signals it offers — multispectral and hyperspectral imagery, synthetic aperture radar, LiDAR, and modelled geophysical fields — each encoding different physical phenomena. Equally important is reasoning across viewpoints (ground, aerial, satellite), across time (single acquisitions to long time series), and across scales (sub-metre detail to continental coverage). We develop large multimodal models that fuse these heterogeneous sources into unified understanding, addressing the practical realities of operational Earth observation: missing data, domain shifts across regions and seasons, and the need for physical and geometric priors that anchor learned representations in the structure of the real world.


<figure class="sa-topic-figure">
  <img src="{{ '/assets/images/topics/space-ai-generative-earth-intelligence.png' | relative_url }}"
       alt="Future wildfire risk prediction: dense risk rasters with multimodal reasoning over vegetation, climate, and topography"
       loading="lazy" decoding="async" />
</figure>

#### Generative Earth Intelligence

Many consequential Earth observation tasks require producing spatially precise, semantically grounded outputs that can be acted upon: risk rasters for disaster modelling, dense segmentation maps for damage assessment, vector geospatial layers for infrastructure mapping, and dense field predictions for geoscience. We treat these as reasoning problems where the model must integrate multi-modal context, respect spatial and physical constraints, and produce outputs directly usable in planning and decision-support systems — faithful to the underlying data, consistent across time, and robust under real-world distributional complexity.

#### Agentic Earth Observation

<figure class="sa-float-right">
  <img src="{{ '/assets/images/topics/space-ai-agentic-earth-observation.png' | relative_url }}"
       alt="Unified understanding of Earth: fusing diverse signals, viewpoints, times, and scales"
       loading="lazy" decoding="async" />
</figure>


The most complex Earth observation tasks cannot be solved in a single forward pass. Monitoring deforestation, assessing post-disaster damage, or modelling urban flood risk may require selecting the right modalities and temporal windows, chaining analytical steps, calling specialised tools, and verifying intermediate results. We aim to develop agentic systems that autonomously construct analytical pipelines, access and select relevant data, and produce high-quality outputs with minimal human supervision — laying the foundation for systems that operate continuously over live data streams and respond to events as they unfold.

#### Technical directions

More concretely, our SpaceAI agenda includes the following technical directions:

- **Multi-view reasoning** — Combining ground-level, aerial, drone, and satellite perspectives to build complementary scene understanding that no single viewpoint can provide.
- **Temporal reasoning** — Learning from bi-temporal pairs, long time series, and video-rate acquisitions to detect change, model dynamics, and predict future states.
- **Multi-scale reasoning** — Connecting very high-resolution local detail with long-range spatial dependencies and continental-scale context within unified model architectures.
- **Multi-modal fusion and representation** — Joint reasoning over RGB, multispectral, hyperspectral, SAR, LiDAR, and modelled geophysical data, with emphasis on native spectral encoding, sensor-physics priors, and robustness to missing or imperfect inputs.
- **Dense prediction and generative outputs** — Producing segmentation masks, risk rasters, dense fields, and vector geospatial layers as spatially precise, physically grounded model outputs.
- **Reasoning-intensive generation** — Combining multi-modal context, spatial constraints, and physical priors to generate outputs that go beyond pattern matching toward structured inference.
- **Agentic perception and data selection** — Models that autonomously query the most relevant context (modalities, views, scales, time windows) for solving a given task.
- **Automatic analytical pipelines** — End-to-end systems that chain data access, preprocessing, inference, and verification steps with minimal human supervision.
- **Domains and applications** — Land use analysis, man-made object and infrastructure monitoring, disaster assessment, ecology, geoscience, and socioeconomic modelling, with extensibility to new input and output modalities as the platform matures.


Our long-term ambition is to build AI systems that understand Earth reliably — fusing heterogeneous sensors and scales, reasoning over time and physical structure, and producing decision-ready geospatial outputs through both unified models and autonomous analytical agents. In this framing, SpaceAI connects multimodal Earth understanding, generative spatial intelligence, and agentic observation into one program for intelligent, operational Earth observation.


