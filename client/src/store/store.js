import Vue from 'vue'
import Vuex from 'vuex'
import Api from '@/services/Api'
import createPersistedState from 'vuex-persistedstate'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    user: null,
    isLoggedIn: false,
    token: null,
    shop_title: "proximity rentals",
    apps: null
  },
  mutations: {
    setToken(state, token) {
      state.token = token
      if (token) {
        Api().defaults.headers.common['Authorization'] = `Token ${token}`
        state.isLoggedIn = true
      } else {
        state.isLoggedIn = false
      }
    },
    setUser(state, user) {
      state.user = user
    },
    logout(state) {
      state.isLoggedIn = false
      state.token = null
      state.user = null
      delete Api().defaults.headers.common['Authorization']
    },
    createApp(state, apps) {
      state.apps = apps
    }
  },
  getters: {
    user(state) {
      return state.user
    },
    title(state) {
      return state.shop_title
    },
    token(state) {
      return state.token
    },
    app(state) {
      return state.apps
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
    logout({
      commit
    }) {
      commit('logout')
    },
    createApp({
      commit
    }, app) {
      commit('createApp', app)
    }
  },
  plugins: [createPersistedState()]
})