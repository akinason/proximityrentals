import Api from './Api';

const APiheaders = {
    headers: {
        'Content-Type': 'application/json',
        // 'Access-Control-Allow-Origin': '*',
        'API-KEY': 'PhW8GMqZtapbk2yBB4apLVAXtWK6EALJE5q3d6e4uNY52wpmm9'
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
}