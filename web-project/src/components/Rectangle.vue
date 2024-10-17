<template>
  <div>
    <Navbar />
    <h1>Розрахунок прямокутника</h1>

    <label for="length">Довжина:</label>
    <input type="number" v-model="length" min="0" step="any" />

    <label for="width">Ширина:</label>
    <input type="number" v-model="width" min="0" step="any" />

    <p class="result">Периметр: <span>{{ perimeter.toFixed(2) }}</span></p>
    <p class="result">Площа: <span>{{ area.toFixed(2) }}</span></p>
    <p class="result">Довжина діагоналі: <span>{{ diagonal.toFixed(2) }}</span></p>

    <p class="error" v-if="error">{{ error }}</p>
    <Footerbar />
    <Auth />
  </div>
</template>

<script>
import Footerbar from "./Footerbar.vue";
import Navbar from "./Navbar.vue";
import Auth from "./Auth.vue";

export default {
  name: "Rectangle",
  data() {
    return {
      length: 0,
      width: 0,
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
label {
  display: block;
  margin-top: 10px;
}
input[type="number"] {
  width: 100px;
}
.result {
  margin-top: 15px;
}
.error {
  color: red;
}
</style>
