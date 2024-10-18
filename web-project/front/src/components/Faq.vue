<template>
  <Navbar />
  <div class="container my-5">
    <h2 class="text-center mb-4">Часті запитання</h2>
    <div class="accordion" id="faqAccordion">
      <div v-for="(item, index) in faqs" :key="index" class="accordion-item">
        <h2 class="accordion-header" :id="'heading' + index">
          <button class="accordion-button" type="button" @click="toggle(index)" :aria-expanded="isOpen(index)"
            :aria-controls="'collapse' + index">
            {{ item.question }}
          </button>
        </h2>
        <div :id="'collapse' + index" class="accordion-collapse collapse" :class="{ show: isOpen(index) }"
          aria-labelledby="'heading' + index" data-bs-parent="#faqAccordion">
          <div class="accordion-body">
            {{ item.answer }}
          </div>
        </div>
      </div>
    </div>
  </div>
  <Footerbar />
  <Auth />
</template>

<script>
import Footerbar from './Footerbar.vue';
import Navbar from './Navbar.vue';
import Auth from './Auth.vue';
export default {
  data() {
    return {
      faqs: [
        {
          question: "Які види гольф атрибутів ви пропонуєте?",
          answer: "Ми пропонуємо широкий асортимент гольфклубів, гольфкарів, м'ячів та аксесуарів."
        },
        {
          question: "Чи можна взяти атрибути в оренду?",
          answer: "Так, ви можете взяти гольф атрибути в оренду на короткий або довгий термін."
        },
        {
          question: "Які способи оплати ви приймаєте?",
          answer: "Ми приймаємо оплату готівкою, банківськими картками, а також онлайн-платежі."
        },
        {
          question: "Як я можу забронювати гольфкарт?",
          answer: "Ви можете забронювати гольфкарт через наш сайт або зателефонувавши нам."
        },
        {
          question: "Чи можу я повернути атрибути раніше терміну?",
          answer: "Так, ви можете повернути орендовані атрибути раніше терміну. Зверніться до нас для деталей."
        },
        {
          question: "Чи є знижки для постійних клієнтів?",
          answer: "Так, ми пропонуємо знижки для постійних клієнтів. Зателефонуйте нам для отримання більше інформації."
        },
        {
          question: "Яка політика повернення товарів?",
          answer: "Повернення товарів можливе протягом 14 днів з моменту покупки за умови, що товар не був використаний."
        },
        {
          question: "Чи можу я замовити атрибути онлайн?",
          answer: "Так, ви можете замовити атрибути через наш сайт, і ми доставимо їх до вас."
        },
        {
          question: "Чи є у вас атрибути для початківців?",
          answer: "Так, ми маємо спеціальні набори для початківців, які включають всі необхідні атрибути."
        },
        {
          question: "Які години роботи вашої компанії?",
          answer: "Наші години роботи: понеділок - неділя з 9:00 до 18:00."
        },
        {
          question: "Чи пропонуєте ви доставку гольфкартів та екіпірування?",
          answer: "Так, ми пропонуємо доставку гольфкартів та екіпірування в межах міста та області. Вартість доставки залежить від відстані."
        },
        {
          question: "Як часто оновлюється асортимент гольф обладнання?",
          answer: "Наш асортимент оновлюється щомісяця, щоб забезпечити вам доступ до нових моделей гольфкартів та екіпірування."
        },
        {
          question: "Чи можу я орендувати обладнання на один день?",
          answer: "Так, ви можете орендувати обладнання на один день. Мінімальний термін оренди — 24 години."
        },
        {
          question: "Чи потрібно вносити заставу за оренду?",
          answer: "Так, за деякі товари необхідно внести заставу. Це залежить від типу обладнання."
        },
        {
          question: "Чи проводите ви технічне обслуговування орендованих гольфкартів?",
          answer: "Так, ми пропонуємо технічне обслуговування орендованих гольфкартів. Обслуговування входить у вартість довгострокової оренди."
        },
        {
          question: "Чи є можливість випробувати гольф обладнання перед покупкою?",
          answer: "Так, ви можете випробувати гольф обладнання в нашому шоурумі перед покупкою."
        },
        {
          question: "Якщо гольфкар вийде з ладу під час оренди, що робити?",
          answer: "У випадку несправності ми оперативно замінимо гольфкар або надамо технічну допомогу."
        }
      ],
      openIndex: null,
    };
  },
  methods: {
    toggle(index) {
      this.openIndex = this.openIndex === index ? null : index;
    },
    isOpen(index) {
      return this.openIndex === index;
    },
  },
  components: {
    Navbar, Footerbar, Auth
  }
};
</script>

<style scoped>
.accordion-button {
  background-color: #f8f9fa;
}

.accordion-button:not(.collapsed) {
  color: #0d6efd;
}

.accordion-body {
  background-color: #ffffff;
}

* {
  transition: 0.4s;
}
</style>