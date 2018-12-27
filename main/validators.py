from django.contrib.auth import get_user_model as UserModel
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


def validate_email_exist(value):
    # Checks to ensure the email provided does not exist already.
    if UserModel().objects.filter(email=value).exists():
        raise ValidationError(_('an account with this email already exist.'))
    else:
        return value


def validate_phone_exist(value):
    # Checks to ensure the phone number provided does not exist already.
    if UserModel().objects.filter(phone=value).exists():
        raise ValidationError(_('an account with this phone number already exist.'))
    else:
        return value
