<template>
  <Navbar />
  <Carousel />
  <Cards />
  <Auth />
  <Footerbar />
</template>

<script>
import Auth from "./Auth.vue";
import Cards from "./Cards.vue";
import Carousel from "./Carousel.vue";
import Footerbar from "./Footerbar.vue";
import Navbar from "./Navbar.vue";

export default {
  name: "Home",
  components: {
    Navbar,
    Carousel,
    Cards,
    Auth,
    Footerbar,
  },
};
</script>
