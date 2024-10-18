import { createRouter, createWebHistory } from "vue-router";
import Home from "../components/Home.vue";
import Faq from "../components/Faq.vue";
import Admin from "../components/Admin.vue";
import Animation from "../components/Animation.vue";
import Chat from "../components/Chat.vue";
import Transliteration from "../components/Transliteration.vue";
import Rectangle from "../components/Rectangle.vue";

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/faq",
    name: "FAQ",
    component: Faq,
  },
  {
    path: "/admin",
    name: "Admin Panel",
    component: Admin,
  },
  {
    path: "/animation",
    name: "Anim",
    component: Animation,
  },
  {
    path: "/chat",
    name: "Chat",
    component: Chat,
  },
  {
    path: "/rectangle",
    name: "Rectangle",
    component: Rectangle,
  },
  {
    path: "/transliteration",
    name: "Transliteration",
    component: Transliteration,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
