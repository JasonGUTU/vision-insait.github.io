---
topic_id: robotics
title: Robotics
order: 1
summary: Foundation models for physical intelligence—perception, language, action, and real-world deployment.
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
  /* Let the float span the first two subsections; clear before the themes list. */
  .ro-float-right ~ h4:nth-of-type(3) {
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

Robotics is a core direction for building AI systems that can understand, reason, and act in the physical world. While recent advances in AI have transformed language, vision, and digital content creation, the next frontier is **physical intelligence**: systems that can operate safely and effectively in factories, logistics centers, hospitals, homes, and everyday human environments. The world is facing growing physical challenges, from labor shortages in manufacturing and service industries to the need for intuitive assistive robots that can support aging societies, healthcare, education, and domestic life. Meeting these demands requires robotics to move beyond rigid, single-purpose machines and toward general-purpose agents that can adapt to diverse tasks, embodiments, and environments.


#### Foundation Models for Physical Intelligence

Our vision is to develop **Robotics Foundation Models** as the universal intelligence layer for physical AI. These models should connect perception, language, action, memory, and world understanding into a single framework, allowing robots to interpret human instructions, understand visual and spatial context, and execute complex tasks in real time. Instead of designing a separate model for every robot, object, and environment, we aim to build end-to-end models that can generalize across related robot embodiments, learn from diverse sources of data, and transfer knowledge across tasks. This shift is essential for scaling robotics from controlled demonstrations to real-world deployment.


#### Reasoning, manipulation, and learning

A central challenge in robotics is that physical intelligence requires both high-level reasoning and low-level precision. A robot must understand what a human wants, plan a sequence of actions, adapt to uncertainty, and control its body with accuracy. This is especially important for manipulation, where robots must handle deformable objects, cluttered scenes, tool use, contact-rich interactions, and long-horizon tasks. Beyond simple grippers, we are particularly interested in dexterous manipulation, including bi-manual systems and five-finger hands that can approach human-like flexibility. To scale these capabilities, robotics models must learn from many forms of experience, including teleoperation data, human demonstration, egocentric video, 3D data, simulation, and real robot interaction. By combining imitation learning, reinforcement learning, and foundation-model pre-training and post-training, robotics can become a bridge between digital intelligence and physical action.


#### Strategic research themes

More concretely, our Robotics agenda includes the following strategic research themes:

- **Robotics foundation models** — End-to-end models that integrate vision, language, action, and world understanding, with the goal of supporting multiple robot embodiments and diverse real-world tasks.
- **Vision-Language-Action models** — Models that translate visual observations and human instructions into executable robot actions, enabling robots to follow natural language commands, interpret context, and adapt to changing environments.
- **World-Action models** — Models that learn how the physical world changes as a result of actions, supporting prediction, planning, simulation, and long-horizon decision making.
- **Generalization across robot embodiments** — Methods that allow policies and representations to transfer across related robots, sensors, grippers, hands, arms, and platforms, reducing the need to train isolated systems from scratch.
- **Dexterous manipulation** — Robot manipulation with high degrees of freedom, including bi-manual coordination, five-finger hands, contact-rich control, tool use, object reorientation, and fine-grained physical interaction.
- **Learning from human data** — Approaches that transform human demonstrations, egocentric videos, teleoperation trajectories, and 3D human-object interaction data into useful supervision for robotic intelligence.
- **Imitation and reinforcement learning for robotics** — Pre-training and post-training pipelines that combine imitation learning for scalable skill acquisition with reinforcement learning for robustness, adaptation, and task-specific improvement.
- **Embodied perception and action** — Systems that connect visual perception, spatial reasoning, object affordances, physical constraints, and action execution, allowing robots to act based on a grounded understanding of the environment.
- **Real-world deployment and reliable autonomy** — Robotics systems that are robust, safe, efficient, and deployable in realistic environments, with attention to latency, uncertainty, failure recovery, human oversight, and long-term reliability.
- **Human-centered robotic assistants** — Robots that can collaborate naturally with people through language, visual context, demonstration, and feedback, with applications in homes, workplaces, healthcare, logistics, and service environments.


Our long-term ambition is to build general-purpose physical agents that can understand human goals, learn from human and robot experience, and act reliably in the real world. By connecting foundation models, dexterous manipulation, multimodal learning, imitation and reinforcement learning, and embodied world modeling, we aim to move robotics from specialized automation toward adaptable, intelligent, and human-centered physical AI.
