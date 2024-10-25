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
              <input type="email" v-model="email" class="form-control" placeholder="Електронна пошта" required />
              <input type="password" v-model="password" class="form-control mt-2" placeholder="Пароль" required />
              <button type="submit" class="btn btn-primary mt-3">Авторизуватись</button>
            </form>

            <form v-else @submit.prevent="handleRegister" key="register">
              <h6>Створіть новий акаунт:</h6>
              <input type="email" v-model="email" class="form-control" placeholder="Електронна пошта" required />
              <input type="password" v-model="password" class="form-control mt-2" placeholder="Пароль" required />
              <input type="text" v-model="name" class="form-control mt-2" placeholder="Ім'я" required />
              <input type="text" v-model="surname" class="form-control mt-2" placeholder="Прізвище" required />
              <input type="text" v-model="middlename" class="form-control mt-2" placeholder="По-батькові" required />
              <input type="date" v-model="birthdate" class="form-control mt-2" placeholder="Дата народження" required />
              <MaskInput v-model="number" class="form-control mt-2" mask="38(###)-###-##-##"
                placeholder="38(___)-___-__-__" required />
              <div class="mt-2">
                <label>Стать:</label>
                <input class="m-1" type="radio" id="male" value="Male" v-model="gender" required />
                <label for="male">Чоловіча</label>
                <input class="m-1" type="radio" id="female" value="Female" v-model="gender" required />
                <label for="female">Жіноча</label>
              </div>
              <select v-model="group" class="form-control mt-2" required>
                <option value="">Оберіть вашу групу</option>
                <option value="Ia31">ІА-31</option>
                <option value="Ia32">ІА-32</option>
                <option value="Ia33">ІА-33</option>
                <option value="Ia34">ІА-34</option>
              </select>
              <button type="submit" class="btn btn-primary mt-3">Зареєструватись</button>
            </form>
          </transition>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" @click="toggleForm">
              {{ isLogin ? "Перейти до реєстрації" : "Перейти до авторизації" }}
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { MaskInput } from 'vue-3-mask';
import API_URL from "../js/api.js";
export default {
  components: {
    MaskInput,
  },
  data() {
    return {
      isLogin: true,
      email: '',
      password: '',
      name: '',
      surname: '',
      middlename: '',
      birthdate: '',
      number: '',
      gender: '',
      phone: '',
      group: '',
      registeredUsers: [],
      selectedUsers: []
    };
  },
  methods: {
    toggleForm() {
      this.isLogin = !this.isLogin;
    },
    resetForm() {
      this.email = '';
      this.password = '';
      this.name = '';
      this.surname = '';
      this.middlename = '';
      this.birthdate = '';
      this.number = '';
      this.gender = '';
      this.phone = '';
      this.group = '';
    },
    async handleRegister() {
      console.log({
        email: this.email,
        password: this.password,
        name: this.name,
        surname: this.surname,
        middlename: this.middlename,
        birthdate: this.birthdate,
        gender: this.gender,
        number: this.number,
        group: this.group,
      });

      const userData = {
        email: this.email,
        name: this.name,
        password: this.password,
        surname: this.surname,
        middlename: this.middlename,
        birthdate: this.birthdate,
        gender: this.gender,
        number: this.number,
        group: this.group
      };

      try {
        const response = await fetch(`${API_URL}/newuser`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(userData)
        });

        if (!response.ok) {
          alert('Упсі... Щось не так');
          throw new Error('Failed to register user');
        }

        const result = await response.json();
        console.log('User registered successfully:', result);
        alert(`Вітаю ${this.name}. Ви успішно зареєстровані!`);
      } catch (error) {
        console.error('Error registering user:', error);
        alert('Підніми базу... Розробник...');
      }

      this.resetForm();
    },
  }
}
</script>