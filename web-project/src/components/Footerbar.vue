<template>
  <footer class="bg-dark text-light py-3 mt-auto ">
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
import { faPhone, faEnvelope } from "@fortawesome/free-solid-svg-icons";
import {
  faTelegramPlane,
  faWhatsapp,
  faViber,
} from "@fortawesome/free-brands-svg-icons";

library.add(faPhone, faEnvelope, faTelegramPlane, faWhatsapp, faViber);

export default {
  components: {
    FontAwesomeIcon,
  },
};
</script>

<style scoped>
footer {
  background-color: #343a40;
  padding-top: 1rem;
  padding-bottom: 1rem;
  color: #fff;
}
</style>
