<template>
  <div class="container mt-4">
    <div class="row row-cols-1 row-cols-md-3 g-4">
      <div class="col" v-for="(card, index) in cards" :key="index">
        <div class="card h-100">
          <img
            :src="card.img"
            class="card-img-top"
            alt="..."
            style="height: 200px; object-fit: cover"
            loading="lazy"
          />
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
        {
          img: "../src/assets/img/4.jpeg",
          title: "Lorem.",
          text: "Aute nostrud adipisicing magna ut aliquip sint qui enim eiusmod laborum. Laboris sunt reprehenderit sunt magna culpa pariatur labore ullamco exercitation ipsum nisi dolor deserunt elit. Do aliqua et duis officia id nulla esse ut. Exercitation non in do mollit. Anim culpa deserunt dolore labore consectetur anim consequat reprehenderit. Occaecat adipisicing enim consequat anim irure dolor velit anim.Est exercitation ad ex occaecat nostrud ullamco nostrud labore sit proident. Consectetur ut nulla duis fugiat magna sint aute fugiat magna non laborum minim cupidatat officia. Esse sit aute non ea anim tempor laboris. Deserunt ad voluptate dolore velit quis esse velit aute sit eiusmod ex irure. Ullamco sunt dolor laborum duis anim eiusmod aute officia nostrud aute qui quis. Nisi ipsum elit aute eu do sunt duis amet qui consequat. Incididunt elit ea consectetur ipsum.",
        },
        {
          img: "../src/assets/img/5.jpg",
          title: "Lorem, ipsum dolor.",
          text: "Proident officia tempor irure amet dolore velit excepteur sint laboris. Pariatur sit qui do ut officia. Incididunt qui cillum irure pariatur nostrud aliqua Lorem. Reprehenderit ipsum incididunt cillum dolore. Qui proident sint id reprehenderit labore sint ad veniam culpa ullamco qui elit. Incididunt nostrud labore sint labore.",
        },
        {
          img: "../src/assets/img/6.jpg",
          title: "Lorem, ipsum.",
          text: "Cupidatat est aliquip aliquip ipsum. Aliqua elit labore ut qui sit laborum. Amet voluptate consectetur exercitation excepteur minim magna quis nisi ullamco proident sunt do est labore.",
        },
      ],
    };
  },
};
</script>
