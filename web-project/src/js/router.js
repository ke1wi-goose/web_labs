import { createRouter, createWebHistory } from 'vue-router';
import Home from '../components/Home.vue';
import Faq from '../components/Faq.vue';
import Admin from '../components/Admin.vue';

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
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
