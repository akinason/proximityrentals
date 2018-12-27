from django.contrib.auth import get_user_model as UserModel


def get_default_username():
    # Generates a random unique username for the user.
    while True:
        username = UserModel().objects.make_random_password(
            length=10, allowed_chars='abcdefghjkmnpqrstuvwxyz'
                                     '23456789'
        )
        if not UserModel().objects.filter(username=username).exists():
            return username


def get_default_password():
    return UserModel().objects.make_random_password(length=10)
