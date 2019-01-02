 <template>
  <div class="dashboard">
    <panel/>
    <div class="dash_layout">
      <section class="wrapper">
        <header>
          <h3>Dashboard</h3>
          <p>Add a new application</p>
        </header>
        <form action>
          <input
            type="text"
            name="app_name"
            id="app_name"
            v-model="app_name"
            placeholder="Enter app name"
          >
          <input type="submit" value="Register">
        </form>
        <section id="list_apps">
          <h3>List of applications</h3>
          <form action>
            <input type="search" name="seacrh" id="search" placeholder="Enter application name">
            <label for="search">
              <button name="search">Search</button>
            </label>
          </form>
          <div class="display">
            <table>
              <thead>
                <th>Application Name</th>
                <th>Created on</th>
              </thead>
              <tbody>
                <tr>
                  <td>wheelbarow</td>
                  <td>1/jan/19</td>
                </tr>
                <tr>
                  <td>wheelbarow</td>
                  <td>1/jan/19</td>
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
export default {
  name: "dashboard",
  components: {
    Panel
  },
  data() {
    return {
      app_name: null
    };
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
#list_apps {
  margin-top: 4rem;
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

/* table style */
.display table {
  width: 100%;
}
.display table thead {
  text-align: start;
  border-collapse: collapse;
  width: 100%;
  display: flex;
}
.display table thead > * {
  flex-grow: 1;
  width: 50%;
}
.display table th {
  text-align: start;
  border-bottom: 1px solid #ddd;
  padding: 10px;
  box-sizing: border-box;
}
.display table tbody tr {
  text-align: start;
  border-collapse: collapse;
  width: 100%;
  display: flex;
}
.display table tbody tr > * {
  flex-grow: 1;
  width: 50%;
}
.display table td {
  text-align: start;
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
