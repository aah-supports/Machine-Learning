const slides = Array.from(document.querySelectorAll(".slide"));
const previousButton = document.querySelector("#prevSlide");
const nextButton = document.querySelector("#nextSlide");
const currentSlide = document.querySelector("#currentSlide");
const totalSlides = document.querySelector("#totalSlides");
const progressBar = document.querySelector("#progressBar");

let activeIndex = 0;

function clampIndex(index) {
  return Math.max(0, Math.min(index, slides.length - 1));
}

function showSlide(index, updateHash = true) {
  activeIndex = clampIndex(index);

  slides.forEach((slide, slideIndex) => {
    slide.classList.toggle("active", slideIndex === activeIndex);
  });

  currentSlide.textContent = String(activeIndex + 1);
  totalSlides.textContent = String(slides.length);
  progressBar.style.width = `${((activeIndex + 1) / slides.length) * 100}%`;

  previousButton.disabled = activeIndex === 0;
  nextButton.disabled = activeIndex === slides.length - 1;

  if (updateHash) {
    history.replaceState(null, "", `#slide-${activeIndex + 1}`);
  }
}

function indexFromHash() {
  const match = window.location.hash.match(/^#slide-(\d+)$/);
  if (!match) return 0;
  return clampIndex(Number(match[1]) - 1);
}

previousButton.addEventListener("click", () => showSlide(activeIndex - 1));
nextButton.addEventListener("click", () => showSlide(activeIndex + 1));

document.addEventListener("keydown", (event) => {
  if (event.key === "ArrowRight" || event.key === "PageDown" || event.key === " ") {
    event.preventDefault();
    showSlide(activeIndex + 1);
  }

  if (event.key === "ArrowLeft" || event.key === "PageUp") {
    event.preventDefault();
    showSlide(activeIndex - 1);
  }

  if (event.key === "Home") {
    event.preventDefault();
    showSlide(0);
  }

  if (event.key === "End") {
    event.preventDefault();
    showSlide(slides.length - 1);
  }
});

window.addEventListener("hashchange", () => showSlide(indexFromHash(), false));

showSlide(indexFromHash(), false);
