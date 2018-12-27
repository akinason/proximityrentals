from .base import *

DEBUG = False

ALLOWED_HOSTS += ['api.proximityrentals.com']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'proximityrentals',
        'USER': 'mihma',
        'PASSWORD': 'mihmaworld',
        'HOST': '127.0.0.1',
        'PORT': '5432',
        'CONN_MAX_AGE': 5,
    }
}
