import Api from './Api';
import store from '@/store/store'

const token = store.state.token

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
        return Api().post('/developer/apps/', data, {
            headers: {
                'Content-Type': 'application/json',
                // 'Access-Control-Allow-Origin': '*',
                'API-KEY': 'PhW8GMqZtapbk2yBB4apLVAXtWK6EALJE5q3d6e4uNY52wpmm9',
                "Token": token
            }
        })
    }
}