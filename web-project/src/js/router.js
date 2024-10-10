import { createRouter, createWebHistory } from 'vue-router';
import Home from '../components/Home.vue';
import Faq from '../components/Faq.vue';
import Admin from '../components/Admin.vue';
import Animation from '../components/Animation.vue';

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
  },
  {
    path: '/faq',
    name: 'FAQ',
    component: Faq,
  },
  {
    path: '/admin',
    name: 'Admin Panel',
    component: Admin,
  },
  {
    path: '/animation',
    name: 'Anim',
    component: Animation,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
