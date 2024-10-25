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

              <Field name="email" type="email" v-slot="{ field, meta }">
                <input v-bind="field" class="form-control" placeholder="Електронна пошта" />
                <span v-if="meta.touched && meta.error" class="text-danger">{{ meta.error }}</span>
              </Field>

              <Field name="password" v-slot="{ field, meta }">
                <input v-bind="field" type="password" class="form-control mt-2" placeholder="Пароль" />
                <span v-if="meta.touched && meta.error" class="text-danger">{{ meta.error }}</span>
              </Field>

              <Field name="name" v-slot="{ field, meta }">
                <input v-bind="field" class="form-control mt-2" placeholder="Ім'я" />
                <span v-if="meta.touched && meta.error" class="text-danger">{{ meta.error }}</span>
              </Field>

              <Field name="surname" v-slot="{ field, meta }">
                <input v-bind="field" class="form-control mt-2" placeholder="Прізвище" />
                <span v-if="meta.touched && meta.error" class="text-danger">{{ meta.error }}</span>
              </Field>

              <Field name="middlename" v-slot="{ field, meta }">
                <input v-bind="field" class="form-control mt-2" placeholder="По-батькові" />
                <span v-if="meta.touched && meta.error" class="text-danger">{{ meta.error }}</span>
              </Field>

              <Field name="birthdate" v-slot="{ field, meta }">
                <input v-bind="field" type="date" class="form-control mt-2" />
                <span v-if="meta.touched && meta.error" class="text-danger">{{ meta.error }}</span>
              </Field>

              <Field name="number" v-slot="{ field, meta }">
                <MaskInput v-bind="field" class="form-control mt-2" mask="38(###)-###-##-##"
                  placeholder="38(___)-___-__-__" />
                <span v-if="meta.touched && meta.error" class="text-danger">{{ meta.error }}</span>
              </Field>

              <div class="mt-2">
                <label>Стать:</label>
                <Field name="gender" v-slot="{ field }">
                  <input class="m-1" type="radio" id="male" value="Male" v-bind="field" />
                  <label for="male">Чоловіча</label>
                  <input class="m-1" type="radio" id="female" value="Female" v-bind="field" />
                  <label for="female">Жіноча</label>
                </Field>
              </div>

              <Field name="group" v-slot="{ field, meta }">
                <select v-bind="field" class="form-control mt-2">
                  <option value="">Оберіть вашу групу</option>
                  <option value="Ia31">ІА-31</option>
                  <option value="Ia32">ІА-32</option>
                  <option value="Ia33">ІА-33</option>
                  <option value="Ia34">ІА-34</option>
                </select>
                <span v-if="meta.touched && meta.error" class="text-danger">{{ meta.error }}</span>
              </Field>

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
import BASE_URL from "../js/api.js";
import { Field, useForm } from 'vee-validate';
import * as Yup from 'yup';

export default {
  components: {
    MaskInput,
    Field,
  },
  setup() {
    const { handleSubmit } = useForm({
      validationSchema: Yup.object({
        email: Yup.string().email('Будь ласка, введіть коректну електронну пошту.').required('Електронна пошта є обов\'язковою.'),
        password: Yup.string().required('Пароль є обов\'язковим.'),
        name: Yup.string().required('Ім\'я є обов\'язковим.'),
        surname: Yup.string().required('Прізвище є обов\'язковим.'),
        middlename: Yup.string().required('По-батькові є обов\'язковим.'),
        birthdate: Yup.date().required('Дата народження є обов\'язковою.'),
        number: Yup.string().required('Номер телефону є обов\'язковим.'),
        gender: Yup.string().required('Виберіть стать.'),
        group: Yup.string().required('Оберіть вашу групу.'),
      }),
    });

    const handleRegister = handleSubmit(async (values) => {
      console.log('Registering with values:', values);

      const userData = {
        email: values.email,
        name: values.name,
        password: values.password,
        surname: values.surname,
        middlename: values.middlename,
        birthdate: values.birthdate,
        gender: values.gender,
        number: values.number,
        group: values.group,
      };

      try {
        const response = await fetch(`${BASE_URL}/newuser`, {
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
        alert(`Вітаю ${values.name}. Ви успішно зареєстровані!`);
      } catch (error) {
        console.error('Error registering user:', error);
        alert('Підніми базу... Розробник...');
      }
    });

    return {
      handleRegister,
    };
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
      selectedUsers: [],
      errors: {}
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
      this.phone = '38()';
      this.group = '';
    },
  },
}
</script>