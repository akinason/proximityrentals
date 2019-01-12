import axios from 'axios'


let instance = axios.create({
    baseURL: `http://api.proximityrentals.com/`,
    headers: {
      'Content-Type': 'application/json',
      'API-KEY': 'rx6JjqWHcWXt5xLqsUYLJ2nvwbyaGKFyfYTUPn3xq36U7GqALz',
    }
  })

// request header
instance.interceptors.request.use((config) => {
    // Do something before request is sent

    // Get token from auth.js store
    const token = localStorage.getItem('user-token')

    // Update token axios header
    if (token) {
        const headers = config.headers
        headers['Authorization'] = `Token ${token}`
        config.headers = headers
    }

    return config
  }, error => {
    return Promise.reject(error)
  })


export const http = instance
