<template>
  <header>
    <nav class="navbar fixed-top bg-dark navbar-expand-md" data-bs-theme="dark">
      <div class="container-fluid d-flex">
        <a class="navbar-brand justify-content-start" href="#">
          <img
            src="../src/assets/img/logo.svg"
            alt="Logo"
            width="54"
            class=""
          />
        </a>
        <div class="justify-content-end">
          <button
            class="navbar-toggler"
            type="button"
            data-bs-toggle="collapse"
            data-bs-target="#navbarSupportedContent"
            aria-controls="navbarSupportedContent"
            aria-expanded="false"
            aria-label="Toggle navigation"
          >
            <span class="navbar-toggler-icon"></span>
          </button>
        </div>

        <div
          class="collapse navbar-collapse justify-content-center"
          id="navbarSupportedContent"
        >
          <ul class="navbar-nav mb-2 mb-md-0">
            <li class="nav-item">
              <a class="nav-link active" aria-current="page" href="#"
                >Головна</a
              >
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#">Посилання</a>
            </li>
            <li class="nav-item dropdown">
              <a
                class="nav-link dropdown-toggle"
                href="#"
                role="button"
                data-bs-toggle="dropdown"
                aria-expanded="false"
                >Випадаючий список</a
              >
              <ul class="dropdown-menu">
                <li><a class="dropdown-item" href="#">Дія</a></li>
                <li><a class="dropdown-item" href="#">Інша дія</a></li>
                <li><hr class="dropdown-divider" /></li>
                <li><a class="dropdown-item" href="#">Щось інше</a></li>
              </ul>
            </li>
          </ul>
        </div>

        <div class="d-flex ms-auto me-5">
          <a
            href="#"
            class="text-light"
            data-bs-toggle="modal"
            data-bs-target="#exampleModalCenter"
          >
            <font-awesome-icon :icon="['fas', 'user-circle']" class="fa-2x" />
          </a>
        </div>
      </div>
    </nav>
  </header>
  <main class="mt-5 pt-4">
    <div
      id="carouselExampleIndicators"
      class="carousel slide carousel-dark"
      data-bs-touch="true"
    >
      <div class="carousel-indicators">
        <button
          type="button"
          data-bs-target="#carouselExampleIndicators"
          data-bs-slide-to="0"
          class="active"
          aria-current="true"
          aria-label="Slide 1"
        ></button>
        <button
          type="button"
          data-bs-target="#carouselExampleIndicators"
          data-bs-slide-to="1"
          aria-label="Slide 2"
        ></button>
        <button
          type="button"
          data-bs-target="#carouselExampleIndicators"
          data-bs-slide-to="2"
          aria-label="Slide 3"
        ></button>
      </div>
      <div class="carousel-inner">
        <div class="carousel-item active">
          <img
            src="../src/assets/img/1.jpg"
            class="d-block w-100"
            alt="..."
            style="height: 500px; object-fit: cover"
            loading="lazy"
          />
        </div>
        <div class="carousel-item">
          <img
            src="../src/assets/img/2.jpg"
            class="d-block w-100"
            alt="..."
            style="height: 500px; object-fit: cover"
            loading="lazy"
          />
        </div>
        <div class="carousel-item">
          <img
            src="../src/assets/img/3.jpg"
            class="d-block w-100"
            alt="..."
            style="height: 500px; object-fit: cover"
            loading="lazy"
          />
        </div>
      </div>
      <button
        class="carousel-control-prev"
        type="button"
        data-bs-target="#carouselExampleIndicators"
        data-bs-slide="prev"
      >
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Previous</span>
      </button>
      <button
        class="carousel-control-next"
        type="button"
        data-bs-target="#carouselExampleIndicators"
        data-bs-slide="next"
      >
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Next</span>
      </button>
    </div>

    <div class="container mt-4">
      <div class="row row-cols-1 row-cols-md-3 g-4">
        <div class="col">
          <div class="card h-100">
            <img
              src="../src/assets/img/4.jpeg"
              class="card-img-top"
              alt="..."
              style="height: 200px; object-fit: cover"
              loading="lazy"
            />
            <div class="card-body">
              <h5 class="card-title">Lorem.</h5>
              <p class="card-text">
                Lorem, ipsum dolor sit amet consectetur adipisicing elit.
                Pariatur sint, quam eos consectetur dolore autem numquam at! Ex
                facilis laudantium, eius labore repellat ullam eaque accusamus
                aliquid sapiente distinctio quod!
              </p>
              <p class="card-text">
                <small class="text-body-secondary"
                  >Last updated 3 mins ago</small
                >
              </p>
            </div>
          </div>
        </div>
        <div class="col">
          <div class="card h-100">
            <img
              src="../src/assets/img/5.jpg"
              class="card-img-top"
              alt="..."
              style="height: 200px; object-fit: cover"
              loading="lazy"
            />
            <div class="card-body">
              <h5 class="card-title">Lorem, ipsum dolor.</h5>
              <p class="card-text">
                Lorem ipsum dolor sit amet consectetur adipisicing elit.
                Molestias adipisci sunt explicabo accusantium, alias tempora id
                natus! Optio, voluptas facilis qui nihil quos sint ducimus autem
                nisi tempore dolore provident.
              </p>
              <p class="card-text">
                <small class="text-body-secondary"
                  >Last updated 3 mins ago</small
                >
              </p>
            </div>
          </div>
        </div>
        <div class="col">
          <div class="card h-100">
            <img
              src="../src/assets/img/6.jpg"
              class="card-img-top"
              alt="..."
              style="height: 200px; object-fit: cover"
              loading="lazy"
            />
            <div class="card-body">
              <h5 class="card-title">Lorem, ipsum.</h5>
              <p class="card-text">
                Lorem ipsum, dolor sit amet consectetur adipisicing elit. Totam
                itaque recusandae facere? Adipisci corporis consequatur repellat
                dolores libero ducimus sed.
              </p>
              <p class="card-text">
                <small class="text-body-secondary"
                  >Last updated 3 mins ago</small
                >
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div
      class="modal fade"
      id="exampleModalCenter"
      tabindex="-1"
      role="dialog"
      aria-labelledby="exampleModalCenterTitle"
      aria-hidden="true"
    >
      <div class="modal-dialog modal-dialog-centered" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="exampleModalCenterTitle">
              {{ isLogin ? "Авторизація" : "Реєстрація" }}
            </h5>
            <button
              type="button"
              class="btn-close"
              data-bs-dismiss="modal"
              aria-label="Close"
            ></button>
          </div>
          <div class="modal-body">
            <transition name="fade" mode="out-in">
              <form v-if="isLogin" @submit.prevent="handleLogin" key="login">
                <h6>Будь ласка, авторизуйтесь:</h6>
                <input
                  type="email"
                  class="form-control"
                  placeholder="Електронна пошта"
                  required
                />
                <input
                  type="password"
                  class="form-control mt-2"
                  placeholder="Пароль"
                  required
                />
                <button type="submit" class="btn btn-primary mt-3">
                  Авторизуватись
                </button>
              </form>

              <form v-else @submit.prevent="handleRegister" key="register">
                <h6>Створіть новий акаунт:</h6>
                <input
                  type="email"
                  class="form-control"
                  placeholder="Електронна пошта"
                  required
                />
                <input
                  type="password"
                  class="form-control mt-2"
                  placeholder="Пароль"
                  required
                />
                <input
                  type="text"
                  class="form-control mt-2"
                  placeholder="Ім'я"
                  required
                />
                <input
                  type="text"
                  class="form-control mt-2"
                  placeholder="Прізвище"
                  required
                />
                <input
                  type="text"
                  class="form-control mt-2"
                  placeholder="По-батькові"
                  required
                />
                <input
                  type="date"
                  class="form-control mt-2"
                  placeholder="Дата народження"
                  max="2006-10-11"
                  required
                />
                <select class="form-control mt-2" required>
                  <option value="">Оберіть вашу групу</option>
                  <option value="1">Якась група 1</option>
                  <option value="2">Якась група 2</option>
                  <option value="2">Якась група 3</option>
                  <option value="2">Якась група 4</option>
                </select>
                <label for="picture-download" class="mt-2"
                  >Завантажте свій аватар</label
                >
                <input
                  type="file"
                  id="picture-download"
                  class="form-control"
                  accept="image/png, image/jpeg"
                  required
                />
                <button type="submit" class="btn btn-primary mt-3">
                  Зареєструватись
                </button>
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
  </main>

  <footer class="bg-dark text-light py-3 mt-auto">
    <div class="container">
      <div class="row justify-content-center">
        <div class="col-auto">
          <a href="tel:+1234567890" class="text-light">
            <font-awesome-icon :icon="['fas', 'phone']" />
          </a>
        </div>
        <div class="col-auto">
          <a href="mailto:example@email.com" class="text-light">
            <font-awesome-icon :icon="['fas', 'envelope']" />
          </a>
        </div>
        <div class="col-auto">
          <a href="https://t.me/username" class="text-light" target="_blank">
            <font-awesome-icon :icon="['fab', 'telegram-plane']" />
          </a>
        </div>
        <div class="col-auto">
          <a href="https://wa.me/1234567890" class="text-light" target="_blank">
            <font-awesome-icon :icon="['fab', 'whatsapp']" />
          </a>
        </div>
        <div class="col-auto">
          <a
            href="viber://chat?number=%2B1234567890"
            class="text-light"
            target="_blank"
          >
            <font-awesome-icon :icon="['fab', 'viber']" />
          </a>
        </div>
      </div>
    </div>
  </footer>
</template>

<script>
import { library } from "@fortawesome/fontawesome-svg-core";
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";
import {
  faPhone,
  faEnvelope,
  faUserCircle,
} from "@fortawesome/free-solid-svg-icons";
import {
  faTelegramPlane,
  faWhatsapp,
  faViber,
} from "@fortawesome/free-brands-svg-icons";

library.add(
  faPhone,
  faEnvelope,
  faTelegramPlane,
  faWhatsapp,
  faViber,
  faUserCircle
);

export default {
  components: {
    FontAwesomeIcon,
  },
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

<style scoped>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s;
}
.fade-enter,
.fade-leave-to {
  opacity: 0;
}
</style>
