import { http } from './http';


export default {
    login(credentials) {
        return http.post('v1/main/login/', credentials )
    },
    register(params) {
        return http.post('v1/main/users/', params )
    },
    verifyEmailOrPhone(params) {
        return http.post('v1/main/verification/', params )
    },
    confirmEmailOrPhoneVerification(params) {
        return http.post("v1/main/verification/confirm/", params )
    },

    // applications
    createApp(params) {
        return http.post('developer/apps/', params )
    },
    getApps() {
        return http.get(`developer/apps/` )
    },
    getSingleApp(id) {
        return http.get(`developer/app/?id=${id}`)
    }
}