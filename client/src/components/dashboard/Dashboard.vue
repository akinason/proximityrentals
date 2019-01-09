 <template>
  <div class="dashboard">
    <panel/>
    <div class="dash_layout">
      <section class="wrapper">
        <header>
          <h3>Dashboard</h3>
          <p>Add a new application</p>
        </header>
        <form action method="post">
          <input type="text" name="name" id="name" v-model="name" placeholder="Enter app name">
          <p v-if='feedback' class='red-text'>
            <ul v-for="err in feedback" :key="err">
              <li>{{ err }}</li>
            </ul>
          </p>
          <input type="submit" value="Register" @click.prevent="registerApp">
        </form>
        <section id="list_apps">
          <h3>List of applications</h3>
          <div class="display">
            <table>
              <thead>
                <th>Application Name</th>
                <th>Created on</th>
                <th>Is_Active</th>
              </thead>
              <tbody>
                <tr v-for="app in apps" :key="app.id" @click="navigateTo(app.id)">
                  <td>{{ app.name }}</td>
                  <td>{{ app.created_on }}</td>
                  <td>{{ app.is_active }}</td>
                </tr>
              </tbody>
            </table>
          </div>
        </section>
      </section>
    </div>
  </div>
</template>

<script>


import Panel from "./Panel.vue";
import APIService from "@/services/APIService";
export default {
  name: "dashboard",
  components: {
    Panel
  },
  data() {
    return {
      name: null,
      apps: {},
      feedback: {},
    };
  },
  methods: {
    navigateTo(id) {
      APIService.getSingleApp(id).then(res => {
        this.$store.dispatch('createApp', res.data)
        this.$router.push({ name: 'apps' })
      })
    },
    async registerApp() {
      try {
        await APIService.createApp({ name: this.name }).then(() => {
          this.$router.push({ name: 'login' })
        }).catch(err => {
          this.feedback = err.response.data
        });
      } catch (error) {
        if (error) {
          this.feedback = error.response.data
        }
      }
    }
  },
  async mounted() {
    try {
        await APIService.getApps().then(res => {
          this.apps = res.data
        })
      }catch (error) {
        if(error){
          error.response.data
        }
      }
  },
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
.wrapper form {
  position: relative;
  /* border: 1px solid white; */
  width: 100%;
  margin: 1rem 0;
}
.wrapper form input {
  position: relative;
  border: none;
  background: none;
  outline: none;
  height: 40px;
  padding: 0 0 0 5px;
  width: 100%;
  background: var(--white);
  border-bottom: 1px solid #ddd;
  font-size: 15px;
  color: #555555;
  border-radius: 2px;
}
.wrapper form input[type="submit"] {
  all: unset;
  background: var(--primary);
  color: var(--white);
  height: 40px;
  padding: 0 3rem;
  margin-top: 10px;
  text-transform: uppercase;
  position: absolute;
  right: 0;
}
.wrapper form input[type="submit"]:hover {
  background: #5f3f52;
  cursor: pointer;
}
.wrapper form input[type="submit"]:active {
  background: #d69a71;
  transition: all linear 0.5s;
}
#list_apps {
  margin-top: 8rem;
  position: relative;
}
#list_apps form {
  all: initial;
  display: flex;
  margin: 1.5rem 0;
  flex-basis: 300;
  justify-content: flex-end;
}
#list_apps input {
  all: unset;
  border: 1px solid #ddd;
  height: 40px;
  padding-left: 5px;
  width: 40%;
}
#list_apps button {
  border: none;
  background: var(--primary);
  color: var(--white);
  height: 40px;
  padding: 0 3rem;
  text-transform: uppercase;
}
#list_apps button:hover {
  background: #5f3f52;
  cursor: pointer;
}
#list_apps button:active {
  background: #d69a71;
  transition: all linear 0.5s;
}
/* table style */
.display table {
  width: 100%;
}
.display table thead {
  border-collapse: collapse;
  width: 100%;
  display: flex;
}
.display table thead > * {
  flex-grow: 1;
  width: 50%;
}
.display table th {
  text-align: center;
  border-bottom: 1px solid #ddd;
  padding: 10px;
  box-sizing: border-box;
}
.display table tbody tr {
  text-align: center;
  border-collapse: collapse;
  width: 100%;
  display: flex;
}
.display table tbody tr > * {
  flex-grow: 1;
  width: 50%;
}
.display table td {
  text-align: center;
  border-bottom: 1px solid #ddd;
  padding: 10px;
  box-sizing: border-box;
}
.display table tbody tr:nth-child(even) {
  background: rgb(243, 240, 243);
}
.display table tbody tr:hover {
  background: rgb(180, 180, 180);
  cursor: pointer;
}
form .red-text {
  display: block;
  margin: 0.41rem 0 0.31rem;
  color: #dc0047;
  font-size: 15px;
  text-align: center;
}
ul {
  list-style: none;
}

/* media query */
@media only screen and (max-width: 518px) {
  panel {
    background: #000;
  }
  .dash_layout {
    font-size: 13px;
  }
  input {
    width: 100%;
    font-size: 13px;
  }
  .wrapper form input[type="submit"] {
    padding: 0;
  }
  #list_apps button {
    padding: 0;
  }
}
</style>
