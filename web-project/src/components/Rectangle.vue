<template>
  <Navbar />
  <div class="container mt-5 mb-5">
    <h1 class="mb-4 text-center">Розрахунок прямокутника</h1>

    <div class="form-group">
      <label for="length">Довжина:</label>
      <input type="number" v-model="length" min="0" step="any" class="form-control" placeholder="Введіть довжину" />
    </div>

    <div class="form-group mt-3">
      <label for="width">Ширина:</label>
      <input type="number" v-model="width" min="0" step="any" class="form-control" placeholder="Введіть ширину" />
    </div>

    <div class="mt-4">
      <p class="result">Периметр: <span class="fw-bold">{{ perimeter.toFixed(2) }}</span></p>
      <p class="result">Площа: <span class="fw-bold">{{ area.toFixed(2) }}</span></p>
      <p class="result">Довжина діагоналі: <span class="fw-bold">{{ diagonal.toFixed(2) }}</span></p>
    </div>

    <p class="alert alert-danger mt-3" v-if="error">{{ error }}</p>
  </div>
  <Footerbar />
  <Auth />
</template>

<script>
import Footerbar from "./Footerbar.vue";
import Navbar from "./Navbar.vue";
import Auth from "./Auth.vue";

export default {
  name: "Rectangle",
  data() {
    return {
      length: 2,
      width: 2,
      error: "",
    };
  },
  computed: {
    perimeter() {
      if (this.isValid()) {
        return 2 * (parseFloat(this.length) + parseFloat(this.width));
      }
      return 0;
    },
    area() {
      if (this.isValid()) {
        return parseFloat(this.length) * parseFloat(this.width);
      }
      return 0;
    },
    diagonal() {
      if (this.isValid()) {
        return Math.sqrt(
          parseFloat(this.length) ** 2 + parseFloat(this.width) ** 2
        );
      }
      return 0;
    },
  },
  methods: {
    isValid() {
      if (this.length <= 0 || this.width <= 0 || isNaN(this.length) || isNaN(this.width)) {
        this.error = "Будь ласка, введіть дійсні позитивні числа для довжини та ширини.";
        return false;
      }
      this.error = "";
      return true;
    },
  },
  components: {
    Navbar,
    Footerbar,
    Auth,
  },
};
</script>

<style scoped>
.result {
  margin-top: 15px;
}
</style>