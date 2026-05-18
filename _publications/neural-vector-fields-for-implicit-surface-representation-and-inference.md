---
title: "Neural Vector Fields for Implicit Surface Representation and Inference"
year: 2024
venue: "International Journal of Computer Vision (IJCV 2024)"
venue_display: "International Journal of Computer Vision (IJCV 2024)"
venue_chronicle: "International Journal of Computer Vision"
venue_abbr: "IJCV"
publication_date: "2024-12-01"
author_line_full: "Edoardo Mello Rella, Ajad Chhatkuli, Ender Konukoglu & Luc Van Gool"
authors:
  - ajad-chhatkuli
  - luc-van-gool
paper_url: "https://link.springer.com/article/10.1007/s11263-024-02251-z"
---
## Abstract

Abstract Neural implicit fields have recently shown increasing success in representing, learning and analysis of 3D shapes. Signed distance fields and occupancy fields are still the preferred choice of implicit representations with well-studied properties, despite their restriction to closed surfaces. With neural networks, unsigned distance fields as well as several other variations and training principles have been proposed with the goal to represent all classes of shapes. In this paper, we develop a novel and yet a fundamental representation considering unit vectors in 3D space and call it Vector Field (VF). At each point in $$\mathbb {R}^3$$ R 3 , VF is directed to the closest point on the surface. We theoretically demonstrate that VF can be easily transformed to surface density by computing the flux density. Unlike other standard representations, VF directly encodes an important physical property of the surface, its normal. We further show the advantages of VF representation, in learning open, closed, or multi-layered surfaces. We show that, thanks to the continuity property of the neural optimization with VF, a separate distance field becomes unnecessary for extracting surfaces from the implicit field via Marching Cubes. We compare our method on several datasets including ShapeNet where the proposed new neural implicit field shows superior accuracy in representing any type of shape, outperforming other standard methods. Codes are available at https://github.com/edomel/ImplicitVF.

