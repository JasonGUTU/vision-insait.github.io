(function () {
  function initTopicProjectsSwipers() {
    if (typeof Swiper === "undefined") return;
    document.querySelectorAll(".topic-projects-swiper").forEach(function (el) {
      if (el.dataset.initialized === "true") return;
      el.dataset.initialized = "true";
      var wrap = el.closest(".topic-projects-swiper-wrap");
      if (!wrap) return;
      new Swiper(el, {
        speed: 500,
        spaceBetween: 24,
        slidesPerView: 1.15,
        slidesPerGroup: 1,
        loop: false,
        watchOverflow: true,
        autoplay: { delay: 2000, disableOnInteraction: true },
        pagination: {
          el: wrap.querySelector(".topic-projects-swiper__pagination"),
          clickable: true,
        },
        navigation: {
          prevEl: wrap.querySelector(".topic-projects-swiper__nav--prev"),
          nextEl: wrap.querySelector(".topic-projects-swiper__nav--next"),
        },
        breakpoints: {
          576: { slidesPerView: 2, slidesPerGroup: 1 },
          992: { slidesPerView: 3, slidesPerGroup: 1 },
        },
      });
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initTopicProjectsSwipers);
  } else {
    initTopicProjectsSwipers();
  }
})();
