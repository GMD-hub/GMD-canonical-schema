document$.subscribe(() => {
  let progress = document.querySelector(".gmd-reading-progress");

  if (!progress) {
    progress = document.createElement("div");
    progress.className = "gmd-reading-progress";
    progress.setAttribute("aria-hidden", "true");
    document.body.appendChild(progress);
  }

  if (window.gmdReadingProgressHandler) {
    window.removeEventListener("scroll", window.gmdReadingProgressHandler);
  }

  window.gmdReadingProgressHandler = () => {
    const scrollable = document.documentElement.scrollHeight - window.innerHeight;
    const percent = scrollable > 0 ? (window.scrollY / scrollable) * 100 : 0;
    progress.style.width = `${Math.min(100, Math.max(0, percent))}%`;
  };

  window.addEventListener("scroll", window.gmdReadingProgressHandler, { passive: true });
  window.gmdReadingProgressHandler();
});