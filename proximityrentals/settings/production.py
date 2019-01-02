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

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'developer.permissions.HasAPIAccess',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),
}