<template>
  <Navbar />
  <Carousel />
  <Cards />
  <Auth />
  <Footerbar />
</template>

<script>
import Auth from "./components/Auth.vue";
import Cards from "./components/Cards.vue";
import Carousel from "./components/Carousel.vue";
import Footerbar from "./components/Footerbar.vue";

import Navbar from "./components/Navbar.vue";

export default {
  components: {
    Navbar,
    Carousel,
    Cards,
    Auth,
    Footerbar,
  },
};
</script>
