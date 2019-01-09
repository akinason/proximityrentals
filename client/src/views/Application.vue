 <template>
  <div class="dashboard">
    <panel/>
    <div class="dash_layout">
      <section class="wrapper">
        <header>
          <h3>Dashboard</h3>
          <button @click="navigateTo({ name: 'dashboard' })">back</button>
        </header>
        <form action method="get">
          <fieldset disabled>
            <label for="app_id">
              <span>Id:</span>
              <input type="text" name="app_id" id="app_id" v-model="this.app.id">
            </label>
            <label for="app_name">
              <span>Name:</span>
              <input type="text" name="app_name" id="app_name" v-model="this.app.name">
            </label>
            <label for="app_key" value="key">
              <span>Key:</span>
              <input type="text" name="app_key" id="app_key" v-model="this.app.key">
            </label>
            <label for="app_secret">
              <span>Secret:</span>
              <input type="text" name="app_secret" id="app_secret" v-model="this.app.secret">
            </label>
            <label for="is_active">
              <span>Is_active:</span>
              <input type="text" name="is_active" id="is_active" v-model="this.app.is_active">
            </label>
            <label for="createdon">
              <span>Created On:</span>
              <input type="text" name="createdon" id="createdon" v-model="this.app.created_on">
            </label>
          </fieldset>
        </form>
      </section>
    </div>
  </div>
</template>

<script>
import Panel from "@/components/dashboard/Panel.vue";
export default {
  name: "app",
  components: {
    Panel
  },
  data() {
    return {};
  },
  methods: {
    navigateTo(route) {
      this.$router.push(route);
    }
  },
  computed: {
    app() {
      return this.$store.getters.app;
    }
  }
};
</script>

<style scoped>
.dash_layout {
  width: 100%;
  background: var(--white);
}
.dashboard {
  display: flex;
}
.wrapper {
  padding: 2rem 3rem 0 3rem;
}
.wrapper header {
  all: unset;
}
.wrapper header h3 {
  font-size: 20px;
  margin-bottom: 1rem;
}
.wrapper button {
  all: unset;
  background: var(--primary);
  color: var(--white);
  height: 30px;
  padding: 0 1rem;
  text-transform: uppercase;
  border-radius: 7px;
}
.wrapper button:hover {
  cursor: pointer;
}
.wrapper form {
  margin-top: 1.5rem;
  width: 100%;
}
.wrapper form label {
  width: 100%;
  display: grid;
  grid-template-columns: repeat(1, 1fr 10fr);
  margin-top: 1rem;
  align-items: end;
}
.wrapper form label span {
  font-size: 15px;
  font-weight: 100;
  color: var(--gray);
  margin-right: 0.6rem;
}
.wrapper form input {
  outline: none;
  width: 100%;
  height: 30px;
  font-size: 15px;
  color: var(--gray);
  padding-left: 25px;
  border: none;
  border-bottom: 1px solid var(--bg);
}
.wrapper form fieldset {
  border: none;
  background: transparent;
}
</style>
