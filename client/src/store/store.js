import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    user: null,
    isLoggedIn: false,
    token: null,
    shop_title: "proximity rentals",
  },
  mutations: {
    setToken(state, token) {
      state.token = token
      if (token) {
        state.isLoggedIn = true
      } else {
        state.isLoggedIn = false
      }
    },
    setUser(state, user) {
      state.user = user
    }
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
    setToken({
      commit
    }, token) {
      commit('setToken', token)
    },
    setUser({
      commit
    }, user) {
      commit('setUser', user)
    }
  }
})