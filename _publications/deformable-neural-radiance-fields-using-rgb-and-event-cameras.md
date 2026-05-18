---
title: "Deformable Neural Radiance Fields using RGB and Event Cameras"
year: 2023
venue: "International Conference on Computer Vision (ICCV 2023)"
venue_display: "International Conference on Computer Vision (ICCV 2023)"
venue_chronicle: "International Conference on Computer Vision"
venue_abbr: "ICCV"
publication_date: "2023-10-13"
author_line_full: "Qi Ma, Danda Pani Paudel, Ajad Chhatkuli, Luc Van Gool"
authors:
  - qi-ma
  - danda-paudel
  - ajad-chhatkuli
  - luc-van-gool
paper_url: "https://openaccess.thecvf.com/content/ICCV2023/papers/Ma_Deformable_Neural_Radiance_Fields_using_RGB_and_Event_Cameras_ICCV_2023_paper.pdf"
---
## Abstract

Modeling Neural Radiance Fields for fast-moving deformable objects from visual data alone is a challenging problem. A major issue arises due to the high deformation and low acquisition rates. To address this problem, we propose to use event cameras that offer very fast acquisition of visual change in an asynchronous manner. In this work, we develop a novel method to model the deformable neural radiance fields using RGB and event cameras. The proposed method uses the asynchronous stream of events and calibrated sparse RGB frames. In our setup, the camera pose at the individual events –required to integrate them into the radiance fields– remains unknown. Our method jointly optimizes these poses and the radiance field. This happens efficiently by leveraging the collection of events at once and actively sampling the events during learning. Experiments conducted on both realistically rendered graphics and real-world datasets demonstrate a significant benefit of the proposed method over the state-of-the-art and the compared baseline. This shows a promising direction for modeling deformable neural radiance fields in real-world dynamic scenes. We release our code at: https://qimaqi.github.io/DE-NeRF.github.io/

