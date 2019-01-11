import Vue from 'vue'
import Router from 'vue-router'
import store from './store/store'

Vue.use(Router)

const router = new Router({
    mode: 'history',
    base: process.env.BASE_URL,
    routes: [{
            path: '/signup',
            name: 'signup',
            // route level code-splitting
            // this generates a separate chunk (signup.[hash].js) for this route
            // which is lazy-loaded when the route is visited.
            component: () => import( /* webpackChunkName: "signup" */ '@/views/Signup.vue')
        },
        {
            path: '/signup/confirmation_email',
            name: 'confirm_email',
            component: () => import('@/views/Confirm_email.vue'),
            meta: {
                guest: true
            }
        },
        {
            path: '/signup/confirmation_phone',
            name: 'confirm_phone',
            component: () => import('@/views/Confirm_phone.vue'),
            meta: {
                guest: true
            }
        },
        {
            path: '/dashboard',
            name: 'dashboard',
            component: () => import('@/views/Dashboard'),
            meta: {
                requiresAuth: true
            }
        },
        {
            path: '/dashboard/app',
            name: 'apps',
            component: () => import('@/views/Application'),
            meta: {
                requiresAuth: true
            }
        },
        {
            path: '/login',
            name: 'login',
            component: () => import('@/views/Login')
        },
        {
            path: '*',
            redirect: 'login'
        }
    ]
})

// route guard
router.beforeEach((to, from, next) => {
    if (to.matched.some(record => record.meta.requiresAuth)) {
        if (localStorage.getItem('user-token') == null && !store.state.isLoggedIn) {
            next({
                path: '/login',
                params: {
                    nextUrl: to.fullPath
                }
            })
        } else {
            next()
        }
    } else if (to.matched.some(record => record.meta.guest)) {
        console.log(router.options.routes[0].path)
        next()
    } else {
        next()
    }
})
router.beforeResolve((to, from, next) => {
    if (to.name) {
        NProgress.start()
    }
    next()
})
router.afterEach((to, from) => {
    NProgress.done()
})

export default router;