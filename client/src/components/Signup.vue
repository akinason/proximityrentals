<template>
  <div class="signup">
    <h3>welcome to
      <br>proximity rentals
    </h3>
    <p>signup to get started</p>
    <form action method="post">
      <input type="text" name="f_name" id="f_name" v-model="f_name" placeholder="First Name">
      <input type="text" name="l_name" id="l_name" v-model="l_name" placeholder="Last Name">
      <input type="email" name="email" id="eamil" v-model="email" placeholder="Email Address">
      <input type="text" name="number" id="number" v-model="p_number" placeholder="Phone Number">
      <input
        type="password"
        name="password"
        id="password"
        v-model="password"
        placeholder="Password"
      >
      <input type="submit" value="submit">
      <p>Already have an account?
        <strong>
          <a href>login</a>
        </strong>
      </p>
    </form>
  </div>
</template>

<script>
export default {
  name: "register",
  data() {
    return {};
  }
};
</script>

<style scoped>
.signup {
  width: 40rem;
  padding: 1rem 0;
  margin: 10% auto;
  border: 1px solid var(--text_color);
}
</style>
