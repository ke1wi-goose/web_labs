<template>
  <div class="modal fade" id="ModalCenter" tabindex="-1" role="dialog" aria-labelledby="ModalCenterTitle"
    aria-hidden="true">
    <div class="modal-dialog modal-dialog-centered" role="document">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="ModalCenterTitle">{{ isLogin ? "Авторизація" : "Реєстрація" }}</h5>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <transition name="fade" mode="out-in">
            <form v-if="isLogin" @submit.prevent="handleLogin" key="login">
              <h6>Будь ласка, авторизуйтесь:</h6>
              <input type="email" class="form-control" placeholder="Електронна пошта" required />
              <input type="password" class="form-control mt-2" placeholder="Пароль" required />
              <button type="submit" class="btn btn-primary mt-3">Авторизуватись</button>
            </form>

            <form v-else @submit.prevent="handleRegister" key="register">
              <h6>Створіть новий акаунт:</h6>
              <input type="email" class="form-control" placeholder="Електронна пошта" required />
              <input type="password" class="form-control mt-2" placeholder="Пароль" required />
              <input type="text" class="form-control mt-2" placeholder="Ім'я" required />
              <input type="text" class="form-control mt-2" placeholder="Прізвище" required />
              <input type="text" class="form-control mt-2" placeholder="По-батькові" required />
              <input type="date" class="form-control mt-2" placeholder="Дата народження" max="2006-10-11" required />
              <select class="form-control mt-2" required>
                <option value="">Оберіть вашу групу</option>
                <option value="1">Якась група 1</option>
                <option value="2">Якась група 2</option>
                <option value="3">Якась група 3</option>
                <option value="4">Якась група 4</option>
              </select>
              <label for="picture-download" class="mt-2">Завантажте свій аватар</label>
              <input type="file" id="picture-download" class="form-control" accept="image/png, image/jpeg" required />
              <button type="submit" class="btn btn-primary mt-3">Зареєструватись</button>
            </form>
          </transition>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-secondary" @click="toggleForm">
            {{ isLogin ? "Перейти до реєстрації" : "Перейти до авторизації" }}
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      isLogin: true,
    };
  },
  methods: {
    toggleForm() {
      this.isLogin = !this.isLogin;
    },
  },
};
</script>