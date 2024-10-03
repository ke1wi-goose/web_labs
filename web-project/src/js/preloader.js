window.addEventListener("load", function () {
    const preloader = document.getElementById("preloader");

    // Додаємо невелику затримку перед видаленням preloader
    setTimeout(function () {
      preloader.style.display = "none";
    }, 350);
});
