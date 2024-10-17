<template>
    <div>
      <Navbar />
      <div>
        <label for="inputText">Український текст:</label>
        <textarea id="inputText" v-model="inputText" rows="4" cols="50"></textarea>
  
        <label for="outputText">Транслітерований текст:</label>
        <textarea
          id="outputText"
          v-model="outputText"
          readonly
          rows="4"
          cols="50"
        ></textarea>
      </div>
      <Footerbar />
      <Auth />
    </div>
  </template>
  
  <script>
  import Footerbar from "./Footerbar.vue";
  import Navbar from "./Navbar.vue";
  import Auth from "./Auth.vue";
  
  export default {
    name: "Transliteration",
    data() {
      return {
        inputText: "", // Додаємо реактивну змінну для введеного тексту
      };
    },
    computed: {
      outputText() {
        if (this.inputText) {
          return this.transliterate(this.inputText); // Викликаємо метод для транслітерації введеного тексту
        }
        return "";
      },
    },
    methods: {
      transliterate(text) {
        const substitution = {
          а: "a",
          б: "b",
          в: "v",
          г: "h",
          ґ: "g",
          д: "d",
          е: "e",
          є: "ye",
          ж: "zh",
          з: "z",
          и: "y",
          і: "i",
          ї: "yi",
          й: "y",
          к: "k",
          л: "l",
          м: "m",
          н: "n",
          о: "o",
          п: "p",
          р: "r",
          с: "s",
          т: "t",
          у: "u",
          ф: "f",
          х: "kh",
          ц: "ts",
          ч: "ch",
          ш: "sh",
          щ: "shch",
          ю: "yu",
          я: "ya",
          ь: "",
          А: "A",
          Б: "B",
          В: "V",
          Г: "H",
          Ґ: "G",
          Д: "D",
          Е: "E",
          Є: "Ye",
          Ж: "Zh",
          З: "Z",
          И: "Y",
          І: "I",
          Ї: "Yi",
          Й: "Y",
          К: "K",
          Л: "L",
          М: "M",
          Н: "N",
          О: "O",
          П: "P",
          Р: "R",
          С: "S",
          Т: "T",
          У: "U",
          Ф: "F",
          Х: "Kh",
          Ц: "Ts",
          Ч: "Ch",
          Ш: "Sh",
          Щ: "Shch",
          Ю: "Yu",
          Я: "Ya",
          ь: "",
        };
  
        return text
          .split("")
          .map((char) => substitution[char] || char)
          .join("");
      },
    },
    components: {
      Navbar,
      Footerbar,
      Auth,
    },
  };
  </script>
  
  <style scoped>
  textarea {
    width: 100%;
    margin-bottom: 10px;
  }
  </style>
  