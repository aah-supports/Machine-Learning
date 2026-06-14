const slides = Array.from(document.querySelectorAll(".slide"));
const previousButton = document.querySelector("#prevSlide");
const nextButton = document.querySelector("#nextSlide");
const currentSlide = document.querySelector("#currentSlide");
const totalSlides = document.querySelector("#totalSlides");
const progressBar = document.querySelector("#progressBar");
const menuToggle = document.querySelector("#menuToggle");
const menuClose = document.querySelector("#menuClose");
const slideMenu = document.querySelector("#slideMenu");
const menuBackdrop = document.querySelector("#menuBackdrop");
const menuSections = document.querySelector("#menuSections");

let activeIndex = 0;
let menuButtons = [];

const courseSections = [
  { title: "Introduction", start: 0, end: 6 },
  { title: "Préparer les données", start: 7, end: 10 },
  { title: "Régression linéaire", start: 11, end: 21 },
  { title: "KNN", start: 22, end: 35 },
  { title: "Exercices", start: 36, end: 36 },
];

function clampIndex(index) {
  return Math.max(0, Math.min(index, slides.length - 1));
}

function showSlide(index, updateHash = true) {
  activeIndex = clampIndex(index);

  slides.forEach((slide, slideIndex) => {
    slide.classList.toggle("active", slideIndex === activeIndex);
  });

  menuButtons.forEach((button, buttonIndex) => {
    const isActive = buttonIndex === activeIndex;
    button.classList.toggle("active", isActive);
    button.setAttribute("aria-current", isActive ? "true" : "false");
  });

  currentSlide.textContent = String(activeIndex + 1);
  totalSlides.textContent = String(slides.length);
  progressBar.style.width = `${((activeIndex + 1) / slides.length) * 100}%`;

  previousButton.disabled = activeIndex === 0;
  nextButton.disabled = activeIndex === slides.length - 1;

  if (updateHash) {
    history.replaceState(null, "", `#${slides[activeIndex].id}`);
  }
}

function openMenu() {
  slideMenu.classList.add("open");
  menuBackdrop.classList.add("open");
  slideMenu.setAttribute("aria-hidden", "false");
  menuToggle.setAttribute("aria-expanded", "true");
}

function closeMenu() {
  slideMenu.classList.remove("open");
  menuBackdrop.classList.remove("open");
  slideMenu.setAttribute("aria-hidden", "true");
  menuToggle.setAttribute("aria-expanded", "false");
}

function toggleMenu() {
  if (slideMenu.classList.contains("open")) {
    closeMenu();
    return;
  }

  openMenu();
}

function buildMenu() {
  menuSections.innerHTML = "";
  menuButtons = [];

  courseSections.forEach((section) => {
    const group = document.createElement("section");
    group.className = "menu-group";

    const heading = document.createElement("h3");
    heading.textContent = section.title;
    group.append(heading);

    const list = document.createElement("ol");

    slides.slice(section.start, section.end + 1).forEach((slide, offset) => {
      const slideIndex = section.start + offset;
      const item = document.createElement("li");
      const button = document.createElement("button");
      const number = document.createElement("span");
      const label = document.createElement("strong");

      number.textContent = String(slideIndex + 1).padStart(2, "0");
      label.textContent = slide.dataset.title || `Slide ${slideIndex + 1}`;

      button.type = "button";
      button.append(number, label);
      button.addEventListener("click", () => {
        showSlide(slideIndex);
        closeMenu();
      });

      item.append(button);
      list.append(item);
      menuButtons[slideIndex] = button;
    });

    group.append(list);
    menuSections.append(group);
  });
}

function indexFromHash() {
  const hash = window.location.hash.slice(1);
  if (!hash) return 0;

  const idIndex = slides.findIndex((slide) => slide.id === hash);
  if (idIndex >= 0) return idIndex;

  const match = hash.match(/^slide-(\d+)$/);
  if (!match) return 0;
  return clampIndex(Number(match[1]) - 1);
}

previousButton.addEventListener("click", () => showSlide(activeIndex - 1));
nextButton.addEventListener("click", () => showSlide(activeIndex + 1));
menuToggle.addEventListener("click", toggleMenu);
menuClose.addEventListener("click", closeMenu);
menuBackdrop.addEventListener("click", closeMenu);

document.addEventListener("keydown", (event) => {
  if (event.key === "Escape") {
    closeMenu();
  }

  if (event.key.toLowerCase() === "m") {
    event.preventDefault();
    toggleMenu();
  }

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

buildMenu();
showSlide(indexFromHash(), false);
