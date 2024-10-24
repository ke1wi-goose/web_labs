function hidePreloader() {
  const preloader = document.getElementById("preloader");
  preloader.classList.add("hidden");

  setTimeout(() => {
    preloader.remove();
  }, 500);
}

window.onload = () => {
  hidePreloader();
};
