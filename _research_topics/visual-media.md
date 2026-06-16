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
  /* Video variant: give the container a fixed aspect ratio so it has a real
     hit-area before the videos load. Both videos are absolutely positioned to
     cover the container (overrides the theme's bare `video` rule too). */
  .vm-compare-video { aspect-ratio: 16 / 9; }
  .vm-compare-video video {
    position: absolute !important;
    top: 0 !important; left: 0 !important;
    width: 100% !important; height: 100% !important;
    object-fit: cover;
    display: block; pointer-events: none;
  }
  .vm-compare-video video.vm-compare-after {
    clip-path: inset(0 calc(100% - var(--pos)) 0 0);
  }
  /* Standalone (centered, narrower) variant for stand-alone compare blocks. */
  .vm-compare.vm-compare-standalone { max-width: 80%; }
  .vm-media-caption {
    text-align: center; font-size: 0.85rem; color: var(--bs-secondary-color, #666);
    margin: -1.25rem auto 2.5rem; max-width: 80%;
  }
  .vm-media-caption a { color: inherit; text-decoration: underline; }
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
    color: var(--bs-emphasis-color, #111); font-size: 1.1rem; pointer-events: none;
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
  /* Inside vm-row, force both sides to share the same aspect ratio (the base
     image's native 1024:542) and absolute-fill rendering, so that grid
     `stretch` does not leave base img (default height:auto) sitting at the
     top of a taller container while the after img (inset:0, height:100%)
     fills it, which would offset the same pixel across the two layers and
     break the slider alignment. */
  .vm-row > .vm-compare { aspect-ratio: 1024 / 542; }
  .vm-row > .vm-compare > img {
    position: absolute; inset: 0;
    width: 100%; height: 100%;
    object-fit: cover; display: block;
  }
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
    .vm-compare.vm-compare-standalone { max-width: 100%; }
    .vm-media-caption { max-width: 100%; }
  }
</style>

Images and videos are no longer only records of the physical world. They are becoming the primary interface through which people communicate, create, simulate, learn, and interact with intelligent systems. At the same time, visual content is entering a new stage: it must be captured under imperfect real-world conditions, restored with high fidelity, edited with precise human control, generated with semantic and physical consistency, and eventually used as a medium for modeling dynamic worlds. This makes Visual Media a foundational research area that connects low-level vision, generative modeling, multimodal intelligence, creative tools, and real-world AI applications.

Our vision is to build the next generation of visual media technologies along three tightly connected pillars: Media Processing, Media Editing, and Media Generation. These are not separate topics, but different levels of the same problem. Media Processing asks how to recover, enhance, and understand imperfect visual signals. Media Editing asks how to modify existing visual content while preserving identity, structure, style, and user intent. Media Generation asks how to synthesize new visual worlds from language, reference images, layouts, videos, and multimodal conditions. Together, they form a complete pipeline from visual signal to controllable creation.


#### Media Processing

Media Processing remains a fundamental layer of Visual Media research. Real-world images and videos are often degraded by noise, blur, compression, low resolution, poor lighting, motion, weather, sensor limitations, and temporal instability. These degradations are not merely cosmetic problems. They affect downstream perception, creative reuse, scientific analysis, cultural preservation, autonomous systems, and human communication. High-quality restoration and enhancement therefore serve as the entry point for trustworthy visual intelligence. Our work in this direction studies how to combine classical signal fidelity, learned generative priors, temporal coherence, perceptual quality, and real-world robustness. The goal is to move beyond benchmark-specific restoration toward systems that are fast, faithful, controllable, and useful in real deployment scenarios, from mobile imaging and video streaming to archival restoration and professional production.

<div class="vm-row">
  <div class="vm-compare" role="slider" tabindex="0" aria-label="Drag to compare degraded input with restored output" aria-valuemin="0" aria-valuemax="100" aria-valuenow="50">
    <img src="{{ '/assets/images/topics/visual-media-restoration-clear.jpg' | relative_url }}" alt="Restored output" loading="lazy" decoding="async" />
    <img class="vm-compare-after" src="{{ '/assets/images/topics/visual-media-restoration-blur.jpg' | relative_url }}" alt="Degraded input" loading="lazy" decoding="async" />
    <span class="vm-compare-label left">INPUT</span>
    <span class="vm-compare-label right">RESTORED</span>
    <div class="vm-compare-handle"></div>
    <div class="vm-compare-knob" aria-hidden="true"></div>
  </div>
  <div class="vm-compare vm-compare-video" role="slider" tabindex="0" aria-label="Drag to compare low-quality input video with restored output" aria-valuemin="0" aria-valuemax="100" aria-valuenow="50">
    <video src="{{ '/assets/images/topics/visual-media-hypir-output.mp4' | relative_url }}" autoplay muted loop playsinline preload="auto"></video>
    <video class="vm-compare-after" src="{{ '/assets/images/topics/visual-media-hypir-input.mp4' | relative_url }}" autoplay muted loop playsinline preload="auto"></video>
    <span class="vm-compare-label left">INPUT</span>
    <span class="vm-compare-label right">RESTORED</span>
    <div class="vm-compare-handle"></div>
    <div class="vm-compare-knob" aria-hidden="true"></div>
  </div>
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
    // If this compare block contains two videos, keep them in time sync so the
    // left/right halves always show the same moment in the clip.
    var videos = el.querySelectorAll('video');
    if (videos.length >= 2) {
      var primary = videos[0], secondary = videos[1];
      primary.addEventListener('timeupdate', function(){
        if (Math.abs(primary.currentTime - secondary.currentTime) > 0.15) {
          secondary.currentTime = primary.currentTime;
        }
      });
    }
  }
  // Defer until DOMContentLoaded so .vm-compare blocks rendered below this
  // <script> (e.g. the editing video demo) are also picked up.
  function initAll(){ document.querySelectorAll('.vm-compare').forEach(init); }
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initAll);
  } else {
    initAll();
  }
})();
</script>

#### Media Editing

Media Editing is the bridge between understanding and creation. Editing is generation under strong constraints: the system must understand what the user wants to change, what must remain untouched, and how the edit should respect the original image or video. This requires precise control over geometry, identity, lighting, motion, texture, style, and temporal consistency. It also requires interfaces that allow humans to specify intent through language, examples, sketches, masks, timelines, or multimodal instructions. We view editing as a key step toward practical visual intelligence because most real creative workflows are not purely generative. They are iterative, conditional, and human-in-the-loop. A powerful visual media system should not only produce beautiful content from scratch, but also revise, repair, extend, localize, and refine existing content with professional-level control.

<!-- Editing demo: physically-plausible video object & interaction removal
     (VOID, Motamed et al. 2026, Netflix x INSAIT). Drag the slider to reveal. -->
<div class="vm-compare vm-compare-video vm-compare-standalone" role="slider" tabindex="0" aria-label="Drag to compare input video with edited output" aria-valuemin="0" aria-valuemax="100" aria-valuenow="50">
  <video src="{{ '/assets/images/topics/visual-media-jumppool-void.mp4' | relative_url }}" autoplay muted loop playsinline preload="auto"></video>
  <video class="vm-compare-after" src="{{ '/assets/images/topics/visual-media-jumppool-input.mp4' | relative_url }}" autoplay muted loop playsinline preload="auto"></video>
  <span class="vm-compare-label left">INPUT + MASK</span>
  <span class="vm-compare-label right">EDITED</span>
  <div class="vm-compare-handle"></div>
  <div class="vm-compare-knob" aria-hidden="true"></div>
</div>
<!-- <p class="vm-media-caption">
  Drag to compare. Physically-plausible video object &amp; interaction removal, adapted from
  <a href="https://void-model.github.io/" target="_blank" rel="noopener">VOID</a>
  (Motamed et al., 2026).
</p> -->


#### Media Generation

Media Generation represents a deeper transformation. Image and video generation are becoming a new form of media, not just a tool for producing assets. Video generation, in particular, is moving toward the ability to synthesize temporally coherent scenes, persistent characters, realistic motion, physical interactions, camera movements, and eventually interactive environments. This changes the role of video from a passive recording medium to an active generative medium. Future video models may support filmmaking, advertising, education, simulation, gaming, robotics, virtual production, digital twins, and scientific visualization. More importantly, they may serve as a basis for learning world models: systems that do not merely generate pixels, but learn how objects move, how agents act, how scenes evolve, and how physical and social dynamics unfold over time.

<div class="vm-media-grid cols-2 ratio-16x9">
  <figure>
    <img src="{{ '/assets/images/topics/visual-media-image-generation.webp' | relative_url }}" alt="Image generation example" width="1440" height="810" loading="lazy" decoding="async" />
  </figure>
  <figure>
    <video src="{{ '/assets/images/topics/visual-media-video-generation.mp4' | relative_url }}" width="1928" height="1072" autoplay muted loop playsinline preload="metadata"></video>
  </figure>
</div>

More concretely, our Visual Media agenda includes the following technical directions:

- **Image and video processing** — Restoration, super-resolution, deblurring, denoising, low-light enhancement, and video quality improvement, with emphasis on input fidelity, perceptual quality, temporal stability, and real-world robustness.
- **Image and video generation** — Diffusion, flow-based, transformer, and latent generative models for realistic, diverse, temporally coherent, and efficient visual synthesis.
- **Controllable generation** — Synthesis conditioned on masks, sketches, depth, pose, layouts, camera paths, motion trajectories, reference images, identity, and style, toward precise and composable creative workflows.
- **Multimodal generation and editing** — Joint reasoning over language, images, video, audio, and user feedback, including language-guided editing, reference-based generation, and interactive refinement.
- **Quality assessment and perceptual evaluation** - Image, video, and multimodal quality assessment for restoration, enhancement, generation, and editing, covering fidelity, realism, aesthetics, temporal consistency, semantic correctness, instruction alignment, and human preference modeling.
- **Agentic media creation** — AI systems that decompose visual tasks, select tools, plan editing steps, verify results, and iteratively improve outputs as creative assistants.
- **World models and generative simulation** — Models that capture object permanence, spatial structure, physical interaction, causal dynamics, camera motion, and long-horizon scene evolution.
- **Diffusion theory and generative modeling foundations** — Theory and empirics of sampling, controllability, stability, failure modes, and the interplay between generative priors and input fidelity.
- **Real-world deployment and creative applications** — Mobile imaging, content creation, virtual production, education, cultural heritage, robotics simulation, and interactive AI tools, with attention to speed, latency, evaluation, and pipeline integration.


Our long-term ambition is to develop visual media systems that are faithful to real-world signals, controllable by humans, coherent over time, grounded in physical and semantic structure, and creative enough to expand the boundary of visual communication. By connecting media processing, editing, generation, multimodal intelligence, diffusion theory, agentic creation, and world modeling, we aim to build a unified research program for the next generation of visual intelligence.



### In Cooperation With

<div class="topic-cooperation-logos">
  <img src="{{ '/site-covers/sponsors/Adobe_Inc.png' | relative_url }}" alt="" loading="lazy" decoding="async" />
  <img src="{{ '/site-covers/sponsors/Snap_Inc.png' | relative_url }}" alt="" loading="lazy" decoding="async" />
  <img src="{{ '/site-covers/sponsors/Netflix.png' | relative_url }}" alt="" loading="lazy" decoding="async" />
  <!-- <img src="{{ '/site-covers/sponsors/tencent.png' | relative_url }}" alt="" loading="lazy" decoding="async" /> -->
  <!-- <img src="{{ '/site-covers/sponsors/Vivo.svg' | relative_url }}" alt="" loading="lazy" decoding="async" /> -->
</div>
