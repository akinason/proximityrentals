from django.contrib.auth.models import UserManager
from django.contrib.auth import get_user_model as UserModel
from django.db.utils import ProgrammingError

user_manager = UserManager()


def get_default_username():
    # Generates a random unique username for the user.

    while True:
        username = user_manager.make_random_password(
            length=10, allowed_chars='abcdefghjkmnpqrstuvwxyz'
                                     '23456789'
        )
        try:
            if not UserModel().objects.filter(username=username).exists():
                return username
        except Exception:
            return username


def get_default_password():
    return UserModel().objects.make_random_password(length=10)
