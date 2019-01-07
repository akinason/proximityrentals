<template>
  <div id="panel">
    <div class="profile">
      <div class="logout">
        <p @click="logout">Logout</p>
      </div>
      <div class="profile_img">
        <img src="../../../public/profile-icon-png-898.png" alt="profile_image">
      </div>
      <p class="name">{{ this.user.first_name }} {{ this.user.last_name }}</p>
    </div>
    <div class="panel">
      <nav>
        <ul>
          <li>
            <a href>
              <span>
                <i class="fas fa-igloo"></i>
              </span> Dashboard
            </a>
          </li>
        </ul>
      </nav>
    </div>
  </div>
</template>

<script>
export default {
  name: "panel",
  data() {
    return {};
  },
  methods: {
    logout() {
      this.$store.dispatch("setToken", null);
      this.$store.dispatch("setUser", null);
      this.$router.push({
        name: "login"
      });
    }
  },
  computed: {
    user() {
      return this.$store.getters.user;
    }
  }
};
</script>

<style scoped>
.profile {
  position: absolute;
  top: 1.2%;
  right: 2.5rem;
  display: flex;
  color: var(--white);
  width: 270px;
  align-items: center;
  cursor: pointer;
}
.profile .profile_img {
  width: 35px;
  height: 35px;
}
.profile .profile_img img {
  width: 100%;
  height: 100%;
  object-fit: contain;
}
.profile > p {
  position: absolute;
  right: 0;
  text-transform: capitalize;
}
.profile .logout {
  margin-right: 45px;
  text-transform: uppercase;
  padding: 10px;
}
.profile .logout:hover {
  background: #775036;
  transition: all linear 0.5s;
}
.profile .logout:active {
  background: #d69a71;
  transition: all linear 0.5s;
}

.panel a {
  text-decoration: none;
  color: var(--text_color);
  padding: 7px 0 7px 13px;
  display: block;
  letter-spacing: 0.8px;
}
.panel a span {
  margin-right: 5px;
}
.panel a:hover {
  background: #fff;
}
.panel {
  width: 200px;
  height: calc(100vh - 65px);
  background: #d8d5d5;
}
.panel > * {
  width: 100%;
  display: block;
}
.panel ul:nth-child(1) {
  background: #e5e5e5;
}
.panel nav {
  padding-top: 1rem;
}

/* media query */
@media only screen and (max-width: 548px) {
  .profile p {
    display: none;
  }
  .profile {
    right: 10px;
    width: auto;
  }
  .panel {
    width: 140px;
  }
}
</style>
