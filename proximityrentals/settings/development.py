from .base import *

DEBUG = False

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'proximityrentals',
        'USER': 'viicha',
        'PASSWORD': 'viicha',
        'HOST': '127.0.0.1',
        'PORT': '5432',
        'CONN_MAX_AGE': 5,
    }
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

