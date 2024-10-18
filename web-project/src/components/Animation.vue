<template>
  <div class="container">
    <div class="logo">
      <span class="n">N</span>
      <span class="k">K</span>
      <span class="g">G</span>
      <span class="ball" :class="{ hit: isHit }"></span>
      <span class="club" :class="{ swing: isSwing }"></span>
      <span class="flag" :class="{ appear: isFlagVisible }"></span>
    </div>
    <div class="full-name" :class="{ fadeIn: isFullNameVisible }">NKGolf</div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      isHit: false,
      isSwing: false,
      isFlagVisible: false,
      isFullNameVisible: false,
    };
  },
  mounted() {
    setTimeout(() => {
      this.isSwing = true;
      this.isHit = true;
      this.isFlagVisible = true;
      setTimeout(() => {
        this.isFullNameVisible = true;
      }, 2000);
    }, 100);
  },
};
</script>

<style scoped>
.container {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  height: 100vh;
  background-color: #d9f7f0;
  /* Колір фону */
}

.logo {
  font-size: 5rem;
  font-family: 'Arial', sans-serif;
  position: relative;
}

.n,
.k,
.g {
  display: inline-block;
  transition: transform 1s;
}

.ball {
  position: absolute;
  width: 20px;
  height: 20px;
  background-color: white;
  border-radius: 50%;
  bottom: 20px;
  left: 150px;
  transition: transform 0.5s ease-in-out;
}

.club {
  position: absolute;
  width: 10px;
  height: 100px;
  background-color: #8B4513;
  /* Колір клюшки */
  left: 120px;
  bottom: 20px;
  transform-origin: bottom;
  transition: transform 0.5s ease-in-out;
}

.flag {
  position: absolute;
  width: 10px;
  height: 50px;
  background-color: red;
  /* Колір флагу */
  left: 180px;
  bottom: 40px;
  opacity: 0;
  transition: opacity 1s;
}

.full-name {
  font-size: 3rem;
  opacity: 0;
  transition: opacity 2s;
}

/* Анімаційні класи */
.hit {
  transform: translateY(-30px);
}

.swing {
  transform: rotate(-30deg);
}

.appear {
  opacity: 1;
}

.fadeIn {
  opacity: 1;
}
</style>