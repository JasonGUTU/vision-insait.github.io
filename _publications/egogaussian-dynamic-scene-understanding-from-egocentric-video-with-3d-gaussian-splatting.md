---
title: "EgoGaussian: Dynamic Scene Understanding from Egocentric Video with 3D Gaussian Splatting"
year: 2025
venue: "International Conference on 3D Imaging, Modeling, Processing, Visualization and Transmission (3DIMPVT 2025)"
venue_display: "International Conference on 3D Imaging, Modeling, Processing, Visualization and Transmission (3DIMPVT 2025)"
venue_chronicle: "International Conference on 3D Imaging, Modeling, Processing, Visualization and Transmission"
venue_abbr: "3DIMPVT"
publication_date: "2025-06-01"
author_line_full: "Daiwei Zhang, Gengyan Li, Jiajie Li, Mickaël Bressieux, Otmar Hilliges, Marc Pollefeys, Luc Van Gool, Xi Wang"
authors:
  - luc-van-gool
paper_url: "https://ieeexplore.ieee.org/document/11125625/authors#authors"
---
## Abstract

Human activities are inherently complex, and even simple household tasks involve numerous object interactions. To better understand these activities, it is crucial to model their interactions with the environment captured through dynamic changes. The recent availability of affordable head-mounted cameras and egocentric data offers a more accessible and efficient means to understand dynamic human-object interactions in 3D environments. However, most existing methods for human activity modeling either focus on reconstructing 3D models of hand-object or human-scene interactions or on mapping 3D scenes, neglecting dynamic interactions with objects. The few existing solutions often require inputs from multiple sources, including multi-camera setups, depth-sensing cameras, or kinesthetic sensors. To this end, we introduce EgoGaussian, the first method capable of simultaneously reconstructing 3D scenes and dynamically tracking 3D object motion from RGB egocentric input alone. We leverage the uniquely discrete nature of Gaussian Splatting and segment dynamic interactions from the background. Our approach employs a clip-level online learning pipeline that leverages the dynamic nature of human activities, allowing us to reconstruct the temporal evolution of the scene in chronological order and track rigid object motion. Additionally, our method automatically segments object and background Gaussians, providing explicit 3D representations for both static scenes and dynamic objects. EgoGaussian shows significant improvements in terms of both dynamic object and background reconstruction quality compared to the state-of-the-art. We also qualitatively demonstrate the high quality of the reconstructed models.

