document.addEventListener("DOMContentLoaded", function (event) {
   // Get the current page URL
   var url = window.location.href;

   // Select all navigation links, including those inside dropdowns
   var navLinks = document.querySelectorAll(".navbar .nav-link, .navbar .dropdown-menu .dropdown-item");

   // Loop through the links
   for (var i = 0; i < navLinks.length; i++) {
      // Check if the link's URL matches the current page URL
      if (navLinks[i].href === url) {
         // Add the "active" class to the nav-link
         navLinks[i].classList.add("active");

         // If the active link is a dropdown item, activate its parent dropdown-toggle
         if (navLinks[i].classList.contains("dropdown-item")) {
            const parentDropdown = navLinks[i].closest(".dropdown");
            if (parentDropdown) {
               const parentToggle = parentDropdown.querySelector(".nav-link.dropdown-toggle");
               if (parentToggle) {
                  parentToggle.classList.add("active");
               }
            }
         }

         // Store the active link in local storage
         localStorage.setItem("activeLink", navLinks[i].href);
      }
   }

   // Retrieve the active link from local storage
   var activeLink = localStorage.getItem("activeLink");

   // If an active link is found, reapply the "active" class
   if (activeLink) {
      for (var i = 0; i < navLinks.length; i++) {
         if (navLinks[i].href === activeLink) {
            // Add the "active" class to the nav-link
            navLinks[i].classList.add("active");

            // If the active link is a dropdown item, activate its parent dropdown-toggle
            if (navLinks[i].classList.contains("dropdown-item")) {
               const parentDropdown = navLinks[i].closest(".dropdown");
               if (parentDropdown) {
                  const parentToggle = parentDropdown.querySelector(".nav-link.dropdown-toggle");
                  if (parentToggle) {
                     parentToggle.classList.add("active");
                  }
               }
            }
         }
      }
   }
});
