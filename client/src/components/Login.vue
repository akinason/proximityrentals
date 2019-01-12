<template>
  <div class="signup">
    <h3>welcome to
      <br>
      {{ this.title }}
    </h3>
    <p>Login to get started</p>
    <form autocomplete="off" @submit.prevent="Login">
      <input
        type="text"
        name="username"
        id="username"
        v-model="username"
        placeholder="Enter Email or Phone"
      >
      <div class="password">
        <input
          type="password"
          name="password"
          id="password"
          v-model="password"
          placeholder="Password"
        >
        <span class="btn-show-pass">
          <i class="fas fa-eye" @click="showpassword"></i>
        </span>
      </div>
      <p v-if="feedback" class="red-text">{{ feedback }}</p>
      <input type="submit" value="submit">
      <p>
        Already have an account?
        <strong @click.prevent="Signup({ name: 'signup' })">
          <a href="./signup">signup</a>
        </strong>
      </p>
    </form>
  </div>
</template>

<script>
import APIService from "@/services/APIService";
export default {
  name: "register",
  data() {
    return {
      feedback: null,
      username: "kinason42@gmail.com",
      password: "123456"
    };
  },
  methods: {
    Signup(route) {
      this.$router.push(route);
    },
    showpassword() {
      const password = document.querySelector("input[name=password]");
      if (password.type == "password") {
        password.setAttribute("type", "text");
      } else {
        password.setAttribute("type", "password");
      }
    },
    async Login() {
      try {
        await APIService.login({
          username: this.username,
          password: this.password
        }).then(res => {
          const token = res.data.token;
          const user = res.data.user;
          localStorage.setItem("user-token", token);
          this.$store.dispatch("setToken", localStorage.getItem("user-token"));
          this.$store.dispatch("setUser", user);
          if (this.$store.state.isLoggedIn) {
            this.$router.push({ name: "dashboard" });
          } else {
            this.$router.push({ name: "login" });
          }
        });
      } catch (error) {
       
        // this.feedback = error.response.data.non_field_errors[0];
        const elements = document.querySelector("form").elements;
        Array.from(elements).forEach(() => {
          if (
            error.response.data.password ||
            error.response.data.username ||
            error.response.data.non_field_errors
          )
            this.feedback = "Invalid Username or Password";
        });
      }
    }
  },
  computed: {
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
.signup p {
  font-size: 13px;
  font-weight: 500;
  color: var(--gray);
}
form {
  width: 80%;
  margin: 1rem auto;
  position: relative;
}
form input {
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
.password {
  position: relative;
}
form span {
  position: absolute;
  right: 0;
  top: 40%;
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
  height: 45px;
  width: 90%;
  margin: 40px auto 3rem;
  color: var(--white);
  border-radius: 50px;
}
form input[type="submit"]:hover {
  background: #6d466d;
  cursor: pointer;
  transition: all linear 0.5s;
}
form input[type="submit"]:active {
  background: #d69a71;
  transition: all linear 0.5s;
}
form p {
  all: unset;
  text-transform: initial;
  font-size: 15px;
  color: #666666;
  line-height: 1.5;
}
form p a {
  text-decoration: none;
  text-transform: capitalize;
  color: #3339;
}
form .red-text {
  display: block;
  margin: 1rem 0 0;
  color: #dc0047;
  font-size: 11px;
}

/* media query */
@media only screen and (max-width: 500px) {
  .signup {
    width: 100%;
  }
}
</style>
