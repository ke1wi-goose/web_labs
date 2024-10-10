<template>
    <div class="container mt-4">
      <div class="row row-cols-1 row-cols-md-3 g-4">
        <div class="col" v-for="(card, index) in cards" :key="index">
          <div class="card h-100">
            <img :src="card.img" class="card-img-top" alt="..." style="height: 200px; object-fit: cover" loading="lazy" />
            <div class="card-body">
              <h5 class="card-title">{{ card.title }}</h5>
              <p class="card-text">{{ card.text }}</p>
              <p class="card-text">
                <small class="text-body-secondary">Last updated 3 mins ago</small>
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        cards: [
          { img: "../src/assets/img/4.jpeg", title: "Lorem.", text: "Description 1" },
          { img: "../src/assets/img/5.jpg", title: "Lorem, ipsum dolor.", text: "Description 2" },
          { img: "../src/assets/img/6.jpg", title: "Lorem, ipsum.", text: "Description 3" },
        ],
      };
    },
  };
  </script>
  