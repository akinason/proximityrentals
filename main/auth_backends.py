from django.contrib.auth import get_user_model as UserModel, backends
from sms.lib import format_number


class EmailAuthenticationBackend(backends.ModelBackend):
    """
    Authenticate users with 'Email'. Default implementation by django is 'username' and 'password'
    """
    def authenticate(self, request, username=None, password=None, **kwargs):
            try:
                user = UserModel().objects.filter(email=username)
                user = user.filter(is_deleted=False).filter(is_active=True).get()
                if user.check_password(password):
                    return user
                else:
                    return None
            except UserModel().DoesNotExist:
                return None
            except UserModel().MultipleObjectsReturned:
                return None


class PhoneAuthenticationBackend(backends.ModelBackend):
    """
    Authenticate users with 'phone number'. Default implementation by django is 'username' and 'password'
    """
    def authenticate(self, request, username=None, password=None, **kwargs):
            phone = format_number(username)
            if phone:
                try:
                    user = UserModel().objects.filter(phone=phone)
                    user = user.filter(is_deleted=False).filter(is_active=True).get()
                    if user.check_password(password):
                        return user
                    else:
                        return None
                except UserModel().DoesNotExist:
                    return None
                except UserModel().MultipleObjectsReturned:
                    return None
            else:
                return None

