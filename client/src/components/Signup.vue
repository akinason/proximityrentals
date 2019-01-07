<template>
  <div class="signup">
    <h3>welcome to
      <br>
      {{ this.title }}
    </h3>
    <p>signup to get started</p>
    <form method="post" autocomplete="off">
      <input
        type="text"
        name="firstName"
        id="idFirstName"
        placeholder="First Name"
        v-model="user.first_name"
      >
      <input
        type="text"
        name="lastName"
        id="idLastName"
        v-model="user.last_name"
        placeholder="Last Name"
      >
      <!-- <input
        type="text"
        name="username"
        id="idUsername"
        v-model="user.username"
        placeholder="User Name"
      >-->
      <input type="email" name="email" id="eamil" v-model="user.email" placeholder="Email Address">
      <p v-if="error.email" class="red-text">
        <ul v-for="err in error.email" :key="err">
          <li>{{ err }}</li>
        </ul>
      </p>
      <input type="text" name="phone" id="phone" v-model="user.phone" placeholder="Phone Number">
      <p v-if="error.phone" class="red-text">
        <ul v-for="err in error.phone" :key="err">
          <li>{{ err }}</li>
        </ul>
      </p>
      <div class="password">
        <input
          type="password"
          name="password"
          id="password"
          v-model="user.password"
          placeholder="Password"
          autocomplete="nope"
        >
        <span class="btn-show-pass">
          <i class="fas fa-eye" @click="showpassword"></i>
        </span>
        <p v-if="error.password" class="red-text">
          <ul v-for="err in error.password" :key="err">
            <li>{{ err }}</li>
          </ul>
        </p>
      </div>
      <input type="submit" value="submit" @click.prevent="Register">
      <p>
        Already have an account?
        <strong @click.prevent="Login({ name: 'login' })">
          <a href="">login</a>
        </strong>
      </p>
    </form>
  </div>
</template>

<script>
// import { mapGetters } from "vuex";
import APIService from "@/services/APIService";
export default {
  name: "register",
  data() {
    return {
      user: {
        first_name: null,
        last_name: null,
        email: null,
        phone: null,
        password: null
      },
      error: {}
    };
  },
  methods: {
    Login(route) {
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
    async Register() {
      try {
        /*const response = */await APIService.register(this.user).then(res => {
          APIService.verifyEmailOrPhone({
          username: res.data.email
          })
        this.$store.dispatch("setUser", this.user);
        this.$router.push({ name: 'confirm_email' });
        }).catch(err => {
          if(err) {
            this.error = err.response.data
          }
        });
        
      } catch (error) {
        if (error.response) {
          this.error = error.response.data;
        }
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
  margin: 0.21rem 0 0.11rem;
  color: #dc0047;
  font-size: 11px;
}
ul {
  list-style: none;
}
/* media query */
@media only screen and (max-width: 500px) {
  .signup {
    width: 100%;
  }
}
</style>
