import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    user: null,
    isLoggedIn: true,
    token: null,
    shop_title: "proximity rentals",
    app: null
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
    },
    setUserId(state, id) {
      state.user.id = id
    },
    setApp(state, app) {
      if (state.token && state.isLoggedIn) {
        state.app = app
      } else {
        state.app = null
      }
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
    },
    setApp({
      commit
    }, app) {
      commit('setApp', app)
    },
    setUserId({
      commit
    }, id) {
      commit('setUserId', id)
    }
  }
})