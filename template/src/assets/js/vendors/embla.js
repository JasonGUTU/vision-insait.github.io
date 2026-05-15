document.addEventListener("DOMContentLoaded", () => {
   const viewportNodes = document.querySelectorAll(".embla__viewport");

   viewportNodes.forEach((viewportNode) => {
      const emblaApi = EmblaCarousel(
         viewportNode,
         { loop: true },
         [EmblaCarouselAutoScroll({ delay: 1000, speed: 0.5 })], // Add autoplay
      );

      // Find the closest `.embla` container for controls
      const emblaContainer = viewportNode.closest(".embla");
      const prevBtnNode = emblaContainer.querySelector(".embla__button--prev");
      const nextBtnNode = emblaContainer.querySelector(".embla__button--next");
      const dotsNode = emblaContainer.querySelector(".embla__dots");

      // Function to update dots
      const updateDots = () => {
         if (!dotsNode) return;
         const allDots = dotsNode.querySelectorAll(".embla__dot");
         const selectedIndex = emblaApi.selectedScrollSnap();
         allDots.forEach((dot, index) => {
            dot.classList.toggle("is-selected", index === selectedIndex);
         });
      };

      // Function to create dots dynamically
      const createDots = () => {
         if (!dotsNode) return;
         dotsNode.innerHTML = "";
         const slideCount = emblaApi.slideNodes().length;

         for (let i = 0; i < slideCount; i++) {
            const dot = document.createElement("button");
            dot.classList.add("embla__dot");
            dot.addEventListener("click", () => emblaApi.scrollTo(i));
            dotsNode.appendChild(dot);
         }
         updateDots();
      };

      // Add event listeners for buttons
      if (prevBtnNode) prevBtnNode.addEventListener("click", () => emblaApi.scrollPrev());
      if (nextBtnNode) nextBtnNode.addEventListener("click", () => emblaApi.scrollNext());
      emblaApi.on("select", updateDots);
      emblaApi.on("init", createDots);

      createDots();
   });
});
