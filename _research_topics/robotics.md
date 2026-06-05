---
topic_id: robotics
title: Robotics
order: 1
summary: Robotics foundation models for physical AI—VLAs, dexterous manipulation, and learning from human and robot experience.
hero_image: /assets/images/blog/robotics.png
intro_video: /assets/images/topics/robotics-hero.mp4
---

<style>
  /* Float hero video beside the opening sections (magazine layout). */
  .ro-float-right {
    float: right;
    width: 55%;
    margin: 0.25rem 0 1.25rem 1.5rem;
    border-radius: 0.75rem;
    overflow: hidden;
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.1);
  }
  .ro-float-right .ratio {
    width: 100%;
    --bs-aspect-ratio: 56.25%;
  }
  /* Match site topic video embeds: video fills the ratio box (_hero.scss safe). */
  .ro-float-right .ratio > video {
    position: absolute !important;
    top: 0 !important;
    left: 0 !important;
    width: 100% !important;
    height: 100% !important;
    object-fit: cover;
    object-position: center;
  }
  .ro-float-right ~ h4 {
    clear: right;
  }
  @media (max-width: 700px) {
    .ro-float-right {
      float: none;
      width: 100%;
      margin: 0 0 1.5rem 0;
    }
  }
</style>

<figure class="ro-float-right">
  <div class="ratio ratio-16x9">
    <video class="object-fit-cover"
           src="{{ '/assets/images/topics/robotics-hero.mp4' | relative_url }}"
           autoplay muted loop playsinline preload="auto"
           aria-label="Robotics research highlight video"></video>
  </div>
</figure>

The world is facing unprecedented physical challenges, from critical labor shortages in manufacturing and logistics to the growing need for intuitive, versatile assistive robots in our homes. To meet these real-world demands, robotics must move beyond rigid, single-purpose machines confined to structured environments. Our group is building **Robotics Foundation Models**—such as Vision-Language-Action models (VLAs) and World-Action-Models (WAMs)—to serve as a universal brain for physical AI. By developing end-to-end methods that generalize across multiple similar robot embodiments, we are creating highly adaptable agents capable of instantly understanding and executing complex, real-time tasks specified by humans through natural language or video.

For these foundation models to truly master the physical world, they must replicate human-like adaptability and physical precision. Besides 2-finger grippers, we focus heavily on dexterous manipulation, advancing end-to-end models that govern complex, bi-manual 5-finger hands. To scale these physical capabilities rapidly, we translate vast amounts of various sources of data into robotics intelligence: e.g. teleoperation data, UMI (Universal Manipulation Interface) data, non-robotics 3D data, egocentric human videos. Powered by a robust pipeline of Imitation and Reinforcement Learning (IL and RL) for pre- and post-training, our research bridges the gap between digital reasoning and physical action, paving the way for general-purpose robotic assistants that can autonomously operate in both industry and everyday life.


#### Research topics

Representative research problems and themes in our Robotics agenda include:

- **Robotics foundation models** — End-to-end robotics models such as Vision-Language-Action models (VLAs) and World-Action-Models (WAMs) that work on multiple robot embodiments.
- **Dexterous manipulation** — End-to-end robotics models for bi-manual 5-finger hands.
- **Learning manipulation from egocentric human videos** — Effectively utilizing human video data to boost robotics foundation model performance.
- **Imitation and reinforcement learning for robotics manipulation** — Pre-training and post-training robotics policies via IL and/or RL.
