import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    user: {
      f_name: null,
      l_name: null,
      email: "vegascedric28@gmail.com",
      phone: '680752220',
      password: null
    },
    shop_title: "proximity rentals",
  },
  mutations: {

  },
  getters: {
    user(state) {
      return state.user
    },
    title(state) {
      return state.shop_title
    }
  },
  actions: {

  }
})