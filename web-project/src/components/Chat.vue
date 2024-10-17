<template>
  <Navbar />
  <Footerbar />
  <Auth />
</template>

<script>
import Footerbar from "./Footerbar.vue";
import Navbar from "./Navbar.vue";
import Auth from "./Auth.vue";
export default {
  methods: {
    toggle(index) {
      this.openIndex = this.openIndex === index ? null : index;
    },
    isOpen(index) {
      return this.openIndex === index;
    },
  },
  components: {
    Navbar,
    Footerbar,
    Auth,
  },
};
</script>

<style scoped></style>
