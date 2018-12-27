from .base import *

DEBUG = True

INSTALLED_APPS += [

]


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


# SMS configuration
ONE_S_2_U_SEND_URL = "https://1s2u.com/sms/sendsms/sendsms.asp"
ONE_S_2_U_PASSWORD = "web54126"
ONE_S_2_U_USERNAME = "kinason42"


# DigitalOcean Spaces Configuration
# ==================================


AWS_ACCESS_KEY_ID = 'QTLO5ZTTURNR2DP7PJD7'
AWS_SECRET_ACCESS_KEY = 'dpcREnKiEgPEIe04fiPoNO4UDu2MS1xDIYT/YMP3Cso'

AWS_STORAGE_BUCKET_NAME = 'proximityrentals'

AWS_S3_REGION_NAME = 'sfo2'
AWS_S3_ENDPOINT_URL = 'https://sfo2.digitaloceanspaces.com'
AWS_S3_CUSTOM_DOMAIN = 'assets.njanginetwork.com'


AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}

AWS_S3_SECURE_URLS = False
AWS_STATIC_LOCATION = 'pr/static'
STATICFILES_STORAGE = 'storage_backends.StaticStorage'
STATIC_URL = "%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, AWS_STATIC_LOCATION)


AWS_PUBLIC_MEDIA_LOCATION = 'pr/media/public'
DEFAULT_FILE_STORAGE = 'storage_backends.PublicMediaStorage'

AWS_PRIVATE_MEDIA_LOCATION = 'pr/media/private'
PRIVATE_FILE_STORAGE = 'storage_backends.PrivateMediaStorage'
AWS_DEFAULT_ACL = 'public-read'

# EMAIL CONFIGURATION
DEFAULT_FROM_EMAIL = 'proximityrentals@gmail.com'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'proximityrentals@gmail.com'
EMAIL_HOST_PASSWORD = 'scoolings245'
EMAIL_PORT = 587