<template>
    <div id="carouselIndicators" class="carousel slide carousel-dark" data-bs-touch="true">
      <div class="carousel-indicators">
        <button type="button" data-bs-target="#carouselIndicators" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
        <button type="button" data-bs-target="#carouselIndicators" data-bs-slide-to="1" aria-label="Slide 2"></button>
        <button type="button" data-bs-target="#carouselIndicators" data-bs-slide-to="2" aria-label="Slide 3"></button>
      </div>
      <div class="carousel-inner">
        <div class="carousel-item active">
          <img src="../../src/assets/img/1.jpg" class="d-block w-100" alt="..." style="height: 500px; object-fit: cover" loading="lazy" />
        </div>
        <div class="carousel-item">
          <img src="../../src/assets/img/2.jpg" class="d-block w-100" alt="..." style="height: 500px; object-fit: cover" loading="lazy" />
        </div>
        <div class="carousel-item">
          <img src="../../src/assets/img/3.jpg" class="d-block w-100" alt="..." style="height: 500px; object-fit: cover" loading="lazy" />
        </div>
      </div>
      <button class="carousel-control-prev" type="button" data-bs-target="#carouselIndicators" data-bs-slide="prev">
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Previous</span>
      </button>
      <button class="carousel-control-next" type="button" data-bs-target="#carouselIndicators" data-bs-slide="next">
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Next</span>
      </button>
    </div>
  </template>
  
  <script>
  export default {};
  </script>
  