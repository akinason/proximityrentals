<template>
  <div class="signup">
    <h3>welcome to
      <br>
      {{ this.title }}
    </h3>
    <p>confirm email address</p>
    <p class="phone">{{ this.phone }}</p>
    <form action method="post">
      <input
        type="text"
        name="conf_phone"
        id="conf_phone"
        v-model="confirm_phone"
        placeholder="Enter Code"
      >
      <input type="submit" value="verify">
      <p id="login">
        Already have an account?
        <strong>
          <a href>login</a>
        </strong>
      </p>
    </form>
  </div>
</template>

<script>
export default {
  name: "confirm_phone",
  data() {
    return {
      confirm_phone: null
    };
  },
  computed: {
    phone() {
      return this.$store.getters.user.phone;
    },
    title() {
      return this.$store.getters.title;
    }
  }
};
</script>

<style scoped>
.signup {
  background: var(--white);
  width: 23rem;
  padding: 1rem 0;
  margin: 7% auto;
  text-align: center;
  text-transform: uppercase;
  box-sizing: border-box;
  box-shadow: 0.5px 1px 6px rgba(0, 0, 0, 0.5);
  border-radius: 7px;
}
.signup h3 {
  font-size: 1.45rem;
  font-weight: 300;
  letter-spacing: 1.1px;
  line-height: 2rem;
  margin: 1rem 0rem;
}
.signup:nth-child(2) {
  font-size: 13px;
  font-weight: 500;
  color: var(--gray);
  text-transform: capitalize;
}
form {
  width: 80%;
  margin: 1rem auto;
  position: relative;
}
form > input {
  width: 100%;
  border: none;
  background: transparent;
  border-bottom: 1px solid #ddd;
  padding: 0 5px;
  font-size: 15px;
  color: #555555;
  line-height: 1.2;
  display: block;
  height: 45px;
  outline: none;
}
form span {
  position: absolute;
  right: 0;
  top: 198px;
  color: var(--gray);
}
form span:hover {
  color: #474646;
  cursor: pointer;
  border: 1px unset transparent;
}
form input[type="submit"] {
  all: unset;
  display: block;
  background: var(--primary);
  height: 40px;
  width: 40%;
  font-size: 15px;
  margin: 40px auto 3rem;
  color: var(--white);
  border-radius: 50px;
}
form input[type="submit"]:hover {
  background: #6d466d;
  cursor: pointer;
}
form p#login {
  all: unset;
  text-transform: initial;
  font-size: 13px;
  color: #666666;
  line-height: 1.5;
}
form p a {
  text-decoration: none;
  text-transform: capitalize;
  color: #3339;
}

.phone {
  text-transform: lowercase;
  position: relative;
  margin-top: 0.6rem;
}

/* media query */
@media only screen and (max-width: 500px) {
  .signup {
    width: 100%;
  }
}
</style>
