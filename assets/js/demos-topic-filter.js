(function () {
  function initDemosTopicFilter() {
    var filters = document.querySelector(".demos-topic-filters");
    var gallery = document.getElementById("demos-gallery");
    if (!filters || !gallery) return;

    var items = gallery.querySelectorAll("[data-topics]");
    var buttons = filters.querySelectorAll("[data-topic-filter]");
    var emptyEl = document.getElementById("demos-gallery-empty");

    function setActive(button) {
      buttons.forEach(function (btn) {
        var isActive = btn === button;
        btn.classList.toggle("active", isActive);
        btn.setAttribute("aria-pressed", isActive ? "true" : "false");
      });
    }

    function applyFilter(topicId) {
      var visible = 0;
      items.forEach(function (item) {
        var topics = (item.getAttribute("data-topics") || "").split(/\s+/).filter(Boolean);
        var show = topicId === "all" || topics.indexOf(topicId) !== -1;
        item.classList.toggle("demos-gallery-item--hidden", !show);
        if (show) visible += 1;
      });
      if (emptyEl) {
        emptyEl.classList.toggle("d-none", visible > 0);
      }
    }

    buttons.forEach(function (button) {
      button.addEventListener("click", function () {
        setActive(button);
        applyFilter(button.getAttribute("data-topic-filter"));
      });
    });

    applyFilter("all");
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initDemosTopicFilter);
  } else {
    initDemosTopicFilter();
  }
})();
