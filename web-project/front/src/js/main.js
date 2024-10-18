import { createApp } from "vue";
import "../scss/styles.scss";
import App from "../App.vue";
import "../scss/styles.scss";
import * as bootstrap from "bootstrap";
import router from "./router";

createApp(App).use(router).mount("#app");
