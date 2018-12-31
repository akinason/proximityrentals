<template>
  <div id="app">
    <signup></signup>
    <router-view/>
  </div>
</template>

<script>
import signup from "./views/signup";
export default {
  components: {
    signup
  }
};
</script>

<style>
@import url("https://fonts.googleapis.com/css?family=Titillium+Web");
#app {
  font-family: "Titillium Web", sans-serif;
}
</style>
