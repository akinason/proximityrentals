from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager as BaseUserManager
from django.utils.translation import ugettext_lazy as _

from main.defaults import get_default_username
from storage_backends import PublicMediaStorage

AUTH_TYPES = (('basic', _('basic')), ('facebook', _('facebook')), ('google', _('google')))


class User(AbstractUser):
    username = models.CharField(_('username'), max_length=128, blank=True, unique=True, default=get_default_username)
    password = models.CharField(_('password'), max_length=100, blank=True)
    language = models.CharField(_('default language'), max_length=10, default='en-us')
    title = models.CharField(_('title'), blank=True, max_length=20)
    photo = models.FileField(storage=PublicMediaStorage(), blank=True, null=True)
    email = models.EmailField(_('email'), blank=True)
    verified_email = models.EmailField(_('verified_email'), blank=True)
    phone = models.CharField(_('phone number'), max_length=20, blank=True)
    verified_phone = models.CharField(_('verified phone number'), blank=True, max_length=20)
    country = models.CharField(_('country'), max_length=50, blank=True)
    town = models.CharField(_('town'), max_length=50, blank=True)
    address = models.CharField(_('address'), max_length=255, blank=True)

    is_deleted = models.BooleanField(default=False)
    code = models.CharField(max_length=20, blank=True, verbose_name='password_reset_code')
    phone_verification_code = models.CharField(max_length=20, blank=True, verbose_name='phone_verification_code')
    email_verification_code = models.CharField(max_length=20, blank=True, verbose_name='email_verification_code')

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        if self.first_name or self.last_name:
            return self.get_full_name()
        elif self.email:
            return self.email
        elif self.phone:
            return self.phone
        else:
            return self.username


class SocialAuth(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='social_auth')
    auth_type = models.CharField(choices=AUTH_TYPES, default='basic', max_length=20)
    auth_id = models.CharField(_('External Auth ID'), max_length=100, blank=True)


class UserManager(BaseUserManager):
    model = User

    def get_user(self, username):
        """
        Get a user with email or username or phone number matching the given value 'username'
        :param username: could be email or phone number or username
        :return: user instance
        """
        if User.objects.filter(username=username).exists():
            return User.objects.get(username=username)

        if User.objects.filter(phone=username).exists():
            return User.objects.get(phone=username)

        if User.objects.filter(email=username).exists():
            return User.objects.get(email=username)

        return False


manager = UserManager()
