
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = '5$+hqvk%k^*id42fi62g%@)(24%tr3c!4i@x@edbz2a-#f$jeg'

ALLOWED_HOSTS = ['localhost', '127.0.0.1']


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'main.apps.MainConfig',
    'sms.apps.SmsConfig',
    'rest_framework',
    'storages',
    'rest_framework.authtoken',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'proximityrentals.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'proximityrentals.wsgi.application'

# Authentication user model
AUTH_USER_MODEL = 'main.User'

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


AUTHENTICATION_BACKENDS = (
    'main.auth_backends.EmailAuthenticationBackend', 'main.auth_backends.PhoneAuthenticationBackend',
    'rest_framework.authentication.TokenAuthentication', 'django.contrib.auth.backends.ModelBackend',
)

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


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

