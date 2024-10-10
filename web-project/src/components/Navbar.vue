<template>
  <nav class="navbar fixed-top bg-dark navbar-expand-md" data-bs-theme="dark">
    <div class="container-fluid d-flex">
      <a class="navbar-brand justify-content-start" href="#">
        <img src="../../src/assets/img/logo.svg" alt="Logo" width="54" />
      </a>
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
      <div
        class="collapse navbar-collapse justify-content-center"
        id="navbarSupportedContent"
      >
        <ul class="navbar-nav mb-2 mb-md-0">
          <li class="nav-item">
            <a class="nav-link active" aria-current="page" href="#">Головна</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">FAQ</a>
          </li>
          <li class="nav-item d-block d-md-none">
            <a
              class="nav-link"
              href="#"
              data-bs-toggle="modal"
              data-bs-target="#ModalCenter"
              >Авторизація</a
            >
          </li>
          <li class="nav-item dropdown">
            <a
              class="nav-link dropdown-toggle"
              href="#"
              role="button"
              data-bs-toggle="dropdown"
              aria-expanded="false"
            >
              Випадаючий список
            </a>
            <ul class="dropdown-menu">
              <li><a class="dropdown-item" href="#">Дія</a></li>
              <li><a class="dropdown-item" href="#">Інша дія</a></li>
              <li><hr class="dropdown-divider" /></li>
              <li><a class="dropdown-item" href="#">Щось інше</a></li>
            </ul>
          </li>
        </ul>
      </div>

      <div class="ms-auto me-5 d-none d-md-block">
        <a
          href="#"
          class="text-light"
          data-bs-toggle="modal"
          data-bs-target="#ModalCenter"
          title="Авторизація"
        >
          <font-awesome-icon :icon="['fas', 'user-circle']" class="fa-2x" />
        </a>
      </div>
    </div>
  </nav>
</template>

<script>
import { library } from "@fortawesome/fontawesome-svg-core";
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";
import { faUserCircle } from "@fortawesome/free-solid-svg-icons";

library.add(faUserCircle);

export default {
  components: {
    FontAwesomeIcon,
  },
};
</script>
