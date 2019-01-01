<template>
  <div id="app">
    <Header></Header>
    <router-view/>
  </div>
</template>

<script>
import Header from "@/views/Header.vue";
export default {
  components: {
    Header
  },
  name: "app",
  data() {
    return {};
  }
};
</script>

<style>
@import url("https://fonts.googleapis.com/css?family=Titillium+Web");
:root {
  --text_color: #2c3e50;
  --primary: #744e64;
  --white: #ffffff;
  --bg: #f2f2f2;
}

body {
  background: var(--bg);
}
#app {
  font-family: "Titillium Web";
  color: #2c3e50;
}
</style>
