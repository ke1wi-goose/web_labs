<template>
  <div class="container-fluid">
    <h2 class="my-4">Admin Panel</h2>
    <div class="table-responsive-md">
      <table class="table table-bordered table-hover">
        <thead class="table-light">
          <tr>
            <th scope="col">№</th>
            <th scope="col">Назва</th>
            <th scope="col">ГРН</th>
            <th scope="col">Photo</th>
            <th scope="col">Дії</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(item, index) in items" :key="item.id">
            <td>{{ index + 1 }}</td>
            <td>{{ item.name }}</td>
            <td>{{ item.price }}</td>
            <td>
              <img :src="item.photo" alt="Product Image" width="50" height="50" />
            </td>
            <td>
              <button class="btn btn-sm btn-primary me-2" @click="viewItem(item)">
                <i class="fas fa-eye"></i>
              </button>
              <button class="btn btn-sm btn-warning me-2" @click="editItem(item)">
                <i class="fas fa-edit"></i>
              </button>
              <button class="btn btn-sm btn-danger" @click="deleteItem(item.id)">
                <i class="fas fa-trash"></i>
              </button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import product1_photo from '@/assets/img/product1.jpg';
import product2_photo from '@/assets/img/product2.jpg';

export default {
  name: "Admin Panel",
  data() {
    return {
      items: [
        {
          id: 1,
          name: "Клюшка для гольфу (оренда)",
          price: "500.00",
          photo: product1_photo,
        },
        {
          id: 2,
          name: "Гольфкар (оренда)",
          price: "1000.00",
          photo: product2_photo,
        },
      ],
    };
  },
  methods: {
    viewItem(item) {
      alert(`Перегляд елемента: ${item.name}`);
    },
    editItem(item) {
      alert(`Редагування елемента: ${item.name}`);
    },
    deleteItem(id) {
      alert(`Елемент з id ${id} видалено`);
    },
  },
};
</script>

<style scoped>
.table-responsive-md {
  overflow-x: auto;
}

table {
  min-width: 600px;
}

td img {
  object-fit: cover;
}
</style>
