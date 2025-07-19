
window.addEventListener("DOMContentLoaded", () => {
  const links = document.querySelectorAll(".nav-links a");
  const current = window.location.pathname.split("/").pop();

  links.forEach(link => {
    if (link.getAttribute("href").endsWith(current)) {
      link.classList.add("active");
    } else {
      link.classList.remove("active");
    }
  });
});
