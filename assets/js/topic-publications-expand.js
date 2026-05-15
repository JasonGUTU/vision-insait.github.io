document.addEventListener("DOMContentLoaded", function () {
   document.querySelectorAll("[data-topic-pubs-toggle]").forEach(function (btn) {
      var panel = btn.closest("#topic-publications");
      if (!panel) return;
      var extras = panel.querySelectorAll(".topic-pub-item--extra");
      if (!extras.length) return;

      btn.addEventListener("click", function () {
         var expanded = btn.getAttribute("aria-expanded") === "true";
         expanded = !expanded;
         btn.setAttribute("aria-expanded", expanded ? "true" : "false");
         btn.textContent = expanded ? "Show less" : "Expand";
         extras.forEach(function (el) {
            el.classList.toggle("d-none", !expanded);
         });
      });
   });
});
