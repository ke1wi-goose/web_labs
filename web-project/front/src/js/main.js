import { createApp } from "vue";
import App from "../App.vue";
import "../scss/style.scss";
import * as bootstrap from "bootstrap";
import router from "./router";
import { MaskInput } from "vue-3-mask";

const app = createApp(App);
app.use(router);
app.component("MaskInput", MaskInput);
app.mount("#app");
