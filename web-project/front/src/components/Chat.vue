<template>
  <Navbar />
  <div class="container mt-4 mb-4">
    <div class="row">
      <div class="col-3">
        <div class="input-group mb-3">
          <textarea type="text" class="form-control" placeholder="Повідомлення від користувача 1" v-model="user1Input"
            @keyup.enter="sendMessage(1)" />
        </div>
        <button class="btn btn-primary" @click="sendMessage(1)">Відправити</button>
      </div>
      <div class="col-6">
        <div ref="chatBox" class="chat-box border rounded p-3 flex-grow-1">
          <div v-for="(msg, index) in messages" :key="index" class="d-flex mb-2"
            :class="msg.user === 1 ? 'justify-content-start' : 'justify-content-end'">
            <div :class="['p-2 rounded', msg.user === 1 ? 'bg-primary text-white' : 'bg-secondary text-white']"
              style="max-width: 60%; word-wrap: break-word;">
              <strong>{{ msg.user === 1 ? 'Користувач 1' : 'Користувач 2' }}:</strong>
              <br>
              <span>{{ msg.text }}</span>
            </div>
          </div>
        </div>
      </div>
      <div class="col-3">
        <div class="input-group mb-3">
          <textarea type="text" class="form-control" placeholder="Повідомлення від користувача 2" v-model="user2Input"
            @keyup.enter="sendMessage(2)" />
        </div>
        <button class="btn btn-primary" @click="sendMessage(2)">Відправити</button>
      </div>
    </div>
  </div>
  <Auth />
  <Footerbar />
</template>
<script>
import Footerbar from "./Footerbar.vue";
import Navbar from "./Navbar.vue";
import Auth from "./Auth.vue";
export default {
  data() {
    return {
      user1Input: "",
      user2Input: "",
      messages: [],
    };
  },
  methods: {
    name: "Chat",
    toggle(index) {
      this.openIndex = this.openIndex === index ? null : index;
    },
    isOpen(index) {
      return this.openIndex === index;
    },
    sendMessage(user) {
      const messageText = user === 1 ? this.user1Input : this.user2Input;
      if (messageText.trim() === "") return;

      this.messages.push({ user, text: messageText });
      if (user === 1) {
        this.user1Input = "";
      } else {
        this.user2Input = "";
      }

      this.$nextTick(() => {
        const chatBox = this.$refs.chatBox;
        chatBox.scrollTop = chatBox.scrollHeight;
      });
    }
  },
  components: {
    Navbar,
    Footerbar,
    Auth,
  },
};
</script>

<style scoped>
.chat-box {
  background-color: #f8f9fa;
  overflow-y: auto;
  height: calc(100vh - 120px);
}

.chat-box::-webkit-scrollbar {
  display: none;
}
</style>
