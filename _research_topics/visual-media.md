---
topic_id: visual-media
title: Visual Media
order: 5
summary: Processing, Editing, and Generating the Visual World
hero_image: /assets/images/blog/visual-media.png
intro_video: /site-covers/home/hero-video.mp4
---

<style>
  /* Visual-media topic: shared media layouts (grid / single / before-after slider). */
  .vm-media-grid { display: grid; gap: 1rem; margin: 1.5rem 0 2.5rem; }
  .vm-media-grid.cols-2 { grid-template-columns: repeat(2, 1fr); }
  .vm-media-grid figure { margin: 0; }
  /* Override theme's bare `video { position:absolute; ... }` rule from _hero.scss. */
  .vm-media-grid video,
  .vm-media-single video {
    position: static !important;
    top: auto !important;
    left: auto !important;
    height: auto !important;
  }
  .vm-media-grid img,
  .vm-media-grid video {
    width: 100%; max-width: 100%; height: auto; display: block;
    border-radius: 0.75rem; box-shadow: 0 4px 16px rgba(0,0,0,0.08);
  }
  .vm-media-grid.ratio-16x9 img,
  .vm-media-grid.ratio-16x9 video { aspect-ratio: 16 / 9; object-fit: cover; }
  .vm-media-single { margin: 1.5rem auto 2.5rem; max-width: 80%; }
  .vm-media-single img,
  .vm-media-single video {
    width: 100%; height: auto; border-radius: 0.75rem;
    box-shadow: 0 4px 16px rgba(0,0,0,0.08);
  }
  @media (max-width: 700px) {
    .vm-media-grid.cols-2 { grid-template-columns: 1fr; }
    .vm-media-single { max-width: 100%; }
  }
  /* Before/after compare slider. */
  .vm-compare {
    position: relative; max-width: 100%; margin: 1.5rem auto 2.5rem;
    border-radius: 0.75rem; overflow: hidden;
    box-shadow: 0 4px 16px rgba(0,0,0,0.08);
    user-select: none; touch-action: none; --pos: 50%; cursor: ew-resize;
  }
  .vm-compare img { display: block; width: 100%; height: auto; pointer-events: none; }
  .vm-compare .vm-compare-after {
    position: absolute; inset: 0; width: 100%; height: 100%;
    object-fit: cover; clip-path: inset(0 calc(100% - var(--pos)) 0 0);
  }
  .vm-compare .vm-compare-handle {
    position: absolute; top: 0; bottom: 0; left: var(--pos);
    width: 3px; background: #fff;
    box-shadow: 0 0 0 1px rgba(0,0,0,0.25), 0 0 12px rgba(0,0,0,0.35);
    transform: translateX(-50%); pointer-events: none;
  }
  .vm-compare .vm-compare-knob {
    position: absolute; top: 50%; left: var(--pos);
    width: 44px; height: 44px; background: #fff; border-radius: 50%;
    box-shadow: 0 2px 12px rgba(0,0,0,0.3);
    transform: translate(-50%, -50%);
    display: flex; align-items: center; justify-content: center;
    color: #111; font-size: 1.1rem; pointer-events: none;
  }
  .vm-compare .vm-compare-knob::before { content: "‹"; margin-right: 2px; }
  .vm-compare .vm-compare-knob::after  { content: "›"; margin-left: 2px; }
  .vm-compare .vm-compare-label {
    position: absolute; top: 0.75rem; padding: 0.25rem 0.6rem;
    background: rgba(0,0,0,0.55); color: #fff; font-size: 0.75rem;
    border-radius: 999px; pointer-events: none; letter-spacing: 0.05em;
  }
  .vm-compare .vm-compare-label.left { left: 0.75rem; }
  .vm-compare .vm-compare-label.right { right: 0.75rem; }
  /* Two-column row that mixes the .vm-compare slider with a sibling figure. */
  .vm-row {
    display: grid; grid-template-columns: 1fr 1fr; gap: 1rem;
    align-items: stretch; margin: 1.5rem 0 2.5rem;
  }
  .vm-row > .vm-compare { margin: 0; max-width: none; }
  .vm-row > figure {
    margin: 0; border-radius: 0.75rem; overflow: hidden;
    box-shadow: 0 4px 16px rgba(0,0,0,0.08);
  }
  .vm-row > figure img {
    width: 100%; height: 100%; object-fit: cover; display: block;
  }
  @media (max-width: 700px) {
    .vm-row { grid-template-columns: 1fr; }
    .vm-row > figure img { height: auto; }
  }
</style>

<figure class="vm-media-single">
  <img src="{{ '/assets/image/topics/visual-media-framework.png' | relative_url }}" alt="Visual Media research framework" loading="lazy" decoding="async" />
</figure>

Images and videos are no longer only records of the physical world. They are becoming the primary interface through which people communicate, create, simulate, learn, and interact with intelligent systems. At the same time, visual content is entering a new stage: it must be captured under imperfect real-world conditions, restored with high fidelity, edited with precise human control, generated with semantic and physical consistency, and eventually used as a medium for modeling dynamic worlds. This makes Visual Media a foundational research area that connects low-level vision, generative modeling, multimodal intelligence, creative tools, and real-world AI applications.

Our vision is to build the next generation of visual media technologies along three tightly connected pillars: Media Processing, Media Editing, and Media Generation. These are not separate topics, but different levels of the same problem. Media Processing asks how to recover, enhance, and understand imperfect visual signals. Media Editing asks how to modify existing visual content while preserving identity, structure, style, and user intent. Media Generation asks how to synthesize new visual worlds from language, reference images, layouts, videos, and multimodal conditions. Together, they form a complete pipeline from visual signal to controllable creation.

Media Processing remains a fundamental layer of Visual Media research. Real-world images and videos are often degraded by noise, blur, compression, low resolution, poor lighting, motion, weather, sensor limitations, and temporal instability. These degradations are not merely cosmetic problems. They affect downstream perception, creative reuse, scientific analysis, cultural preservation, autonomous systems, and human communication. High-quality restoration and enhancement therefore serve as the entry point for trustworthy visual intelligence. Our work in this direction studies how to combine classical signal fidelity, learned generative priors, temporal coherence, perceptual quality, and real-world robustness. The goal is to move beyond benchmark-specific restoration toward systems that are fast, faithful, controllable, and useful in real deployment scenarios, from mobile imaging and video streaming to archival restoration and professional production.

<div class="vm-row">
  <div class="vm-compare" role="slider" tabindex="0" aria-label="Drag to compare degraded input with restored output" aria-valuemin="0" aria-valuemax="100" aria-valuenow="50">
    <img src="{{ '/assets/image/topics/visual-media-restoration-clear.jpg' | relative_url }}" alt="Restored output" loading="lazy" decoding="async" />
    <img class="vm-compare-after" src="{{ '/assets/image/topics/visual-media-restoration-blur.jpg' | relative_url }}" alt="Degraded input" loading="lazy" decoding="async" />
    <span class="vm-compare-label left">INPUT</span>
    <span class="vm-compare-label right">RESTORED</span>
    <div class="vm-compare-handle"></div>
    <div class="vm-compare-knob" aria-hidden="true"></div>
  </div>
  <figure>
    <img src="{{ '/assets/image/topics/visual-media-hypir-animation.gif' | relative_url }}" alt="HYPIR restoration animation" loading="lazy" decoding="async" />
  </figure>
</div>

<script>
(function(){
  // Lightweight drag-to-compare slider for the .vm-compare blocks above.
  function init(el){
    if (el.dataset.vmCompareInit) return;
    el.dataset.vmCompareInit = '1';
    var dragging = false;
    function setPos(clientX){
      var r = el.getBoundingClientRect();
      var p = Math.max(0, Math.min(1, (clientX - r.left) / r.width));
      var pct = (p * 100).toFixed(2);
      el.style.setProperty('--pos', pct + '%');
      el.setAttribute('aria-valuenow', Math.round(p * 100));
    }
    function onDown(e){ dragging = true; var x = (e.touches ? e.touches[0].clientX : e.clientX); setPos(x); e.preventDefault(); }
    function onMove(e){ if (!dragging) return; var x = (e.touches ? e.touches[0].clientX : e.clientX); setPos(x); }
    function onUp(){ dragging = false; }
    el.addEventListener('mousedown', onDown);
    el.addEventListener('touchstart', onDown, {passive:false});
    window.addEventListener('mousemove', onMove);
    window.addEventListener('touchmove', onMove, {passive:true});
    window.addEventListener('mouseup', onUp);
    window.addEventListener('touchend', onUp);
    el.addEventListener('keydown', function(e){
      var cur = parseFloat(getComputedStyle(el).getPropertyValue('--pos')) || 50;
      if (e.key === 'ArrowLeft')  { el.style.setProperty('--pos', Math.max(0, cur-5) + '%'); e.preventDefault(); }
      if (e.key === 'ArrowRight') { el.style.setProperty('--pos', Math.min(100, cur+5) + '%'); e.preventDefault(); }
    });
  }
  document.querySelectorAll('.vm-compare').forEach(init);
})();
</script>

Media Editing is the bridge between understanding and creation. Editing is generation under strong constraints: the system must understand what the user wants to change, what must remain untouched, and how the edit should respect the original image or video. This requires precise control over geometry, identity, lighting, motion, texture, style, and temporal consistency. It also requires interfaces that allow humans to specify intent through language, examples, sketches, masks, timelines, or multimodal instructions. We view editing as a key step toward practical visual intelligence because most real creative workflows are not purely generative. They are iterative, conditional, and human-in-the-loop. A powerful visual media system should not only produce beautiful content from scratch, but also revise, repair, extend, localize, and refine existing content with professional-level control.

Media Generation represents a deeper transformation. Image and video generation are becoming a new form of media, not just a tool for producing assets. Video generation, in particular, is moving toward the ability to synthesize temporally coherent scenes, persistent characters, realistic motion, physical interactions, camera movements, and eventually interactive environments. This changes the role of video from a passive recording medium to an active generative medium. Future video models may support filmmaking, advertising, education, simulation, gaming, robotics, virtual production, digital twins, and scientific visualization. More importantly, they may serve as a basis for learning world models: systems that do not merely generate pixels, but learn how objects move, how agents act, how scenes evolve, and how physical and social dynamics unfold over time.

<div class="vm-media-grid cols-2 ratio-16x9">
  <figure>
    <img src="{{ '/assets/image/topics/visual-media-image-generation.webp' | relative_url }}" alt="Image generation example" width="1440" height="810" loading="lazy" decoding="async" />
  </figure>
  <figure>
    <video src="{{ '/assets/image/topics/visual-media-video-generation.mp4' | relative_url }}" width="1928" height="1072" autoplay muted loop playsinline preload="metadata"></video>
  </figure>
</div>

A major focus of our Visual Media research is therefore controllable and multimodal generation. Text alone is often insufficient for professional visual creation. Real applications require generation conditioned on reference images, identity, layout, pose, depth, segmentation, camera trajectories, previous frames, audio, user feedback, and task-specific constraints. We are interested in models that can combine these signals in a unified architecture, allowing users to generate and edit content with both semantic flexibility and structural precision. This includes theoretical studies of image generation, practical system development, evaluation of controllability and fidelity, and deployment-oriented work that considers speed, memory, latency, user experience, and integration into real creative pipelines.

<div class="vm-media-grid cols-2">
  <figure>
    <img src="{{ '/assets/image/topics/visual-media-hypir-sample-1.png' | relative_url }}" alt="HYPIR result 1" loading="lazy" decoding="async" />
  </figure>
  <figure>
    <img src="{{ '/assets/image/topics/visual-media-hypir-sample-2.png' | relative_url }}" alt="HYPIR result 2" loading="lazy" decoding="async" />
  </figure>
</div>

Looking forward, Visual Media will become a key interface between AI and the physical, social, and creative world. It will support not only better images and videos, but new ways of imagining, simulating, communicating, and acting. For a research group, this direction is strategically important because it sits at the intersection of scientific depth and real-world impact. It involves fundamental questions about representation, generation, perception, causality, temporal consistency, and human control, while also enabling technologies that can be directly used in media production, mobile devices, cultural heritage, robotics, education, design, and interactive AI systems.

Our long-term ambition is to develop visual media systems that are faithful to the input, controllable by humans, coherent over time, grounded in the physical world, and creative enough to expand the boundary of visual communication. By connecting media processing, editing, and generation, we aim to build a research program that treats visual media not as isolated image-level tasks, but as a unified foundation for the next generation of visual intelligence.

<div class="vm-media-single">
  <figure>
    <video src="{{ '/assets/image/topics/visual-media-hypvr.mp4' | relative_url }}" width="1920" height="1080" autoplay muted loop playsinline preload="metadata"></video>
  </figure>
</div>

### In Cooperation With

Tooling collaborations with broadcast archives and mobile OEMs on perceptual metrics, on-device super-resolution, and dataset curation for under-represented sensors.

<div class="topic-cooperation-logos">
  <a href="https://example.org/sponsor-b" target="_blank" rel="noopener" title="Vision Industry Partner">
    <img src="{{ '/site-covers/sponsors/brand-logo-3.svg' | relative_url }}" alt="Vision Industry Partner" loading="lazy" decoding="async" />
  </a>
  <img src="{{ '/site-covers/sponsors/brand-logo-5.svg' | relative_url }}" alt="University Initiative" loading="lazy" decoding="async" />
</div>
