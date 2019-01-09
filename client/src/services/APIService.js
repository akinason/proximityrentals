import Api from './Api';

const APiheaders = {
    headers: {
        'Content-Type': 'application/json',
        // 'Access-Control-Allow-Origin': '*',
        'API-KEY': 'rx6JjqWHcWXt5xLqsUYLJ2nvwbyaGKFyfYTUPn3xq36U7GqALz',
    }
}

export default {
    login(credentials) {
        return Api().post('v1/main/login/', credentials, APiheaders)
    },
    register(data) {
        return Api().post('v1/main/users/', data, APiheaders)
    },
    verifyEmailOrPhone(data) {
        return Api().post('v1/main/verification/', data, APiheaders)
    },
    confirmEmailOrPhoneVerification(data) {
        return Api().post("v1/main/verification/confirm/", data, APiheaders)
    },

    // applications
    createApp(data) {
        return Api().post('developer/apps/', data, APiheaders)
    },
    getApps() {
        return Api().get(`developer/apps/`, APiheaders)
    },
    getSingleApp(id) {
        return Api().get(`developer/app/?id=${id}`, APiheaders)
    }
}