import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [{
      path: '/signup',
      name: 'signup',
      // route level code-splitting
      // this generates a separate chunk (signup.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import( /* webpackChunkName: "signup" */ './views/Signup.vue')
    },
    {
      path: '/signup/confirmation_email',
      name: 'confirm_email',
      props: true,
      component: () => import('./views/Confirm_email.vue')
    },
    {
      path: '/signup/confirmation_phone',
      name: 'confirm_phone',
      props: true,
      component: () => import('./views/Confirm_phone.vue')
    },
    {
      path: '/dashboard',
      name: 'dashboard',
      component: () => import('./views/Dashboard')
    },
    {
      path: '/dashboard/app_details',
      name: 'apps',
      component: () => import('./views/Application')
    }
  ]
})