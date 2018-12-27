
from django.utils.translation import ugettext_lazy as _

from rest_framework import serializers

from main.models import User
from main.defaults import get_default_username
from sms.lib import format_number


class UserSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    username = serializers.CharField(allow_blank=True, required=False)
    password = serializers.CharField(
        allow_blank=True, write_only=True, style={'input_type': 'password', 'placeholder': 'Password'}, required=False
    )
    email = serializers.EmailField(allow_blank=True, required=False)
    phone = serializers.CharField(allow_blank=True, required=False)
    photo = serializers.FileField(read_only=True, allow_null=True)
    verified_email = serializers.EmailField(read_only=True)
    verified_phone = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = (
            'id', 'first_name', 'last_name', 'email', 'phone', 'language', 'password', 'username', 'title', 'photo',
            'verified_email', 'verified_phone',
        )

    def validate(self, attrs):
        if not self.instance:  # if we are updating, the fields are not required.
            if 'email' not in attrs and 'phone' not in attrs:
                raise serializers.ValidationError(_('email or phone number is required.'))
        return attrs

    def validate_password(self, value):
        if self.instance:  # If we are updating, only return the new password if it was provided else the existing one.
            if value:
                return value
            else:
                return self.instance.password
        else:  # If we are creating a new object, ensure value is provided else raise validation error.
            if value:
                return value
            else:
                raise serializers.ValidationError(_('password is required.'))

    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(user.password)
        user.save()
        return user

    def update(self, instance, validated_data):
        user = super(UserSerializer, self).update(instance, validated_data)
        if 'password' in validated_data:  # if a new password was set, encrypt it.
            user.set_password(user.password)
            user.save()
        return user

    def validate_email(self, value):
        # Checks to ensure the email provided does not exist already.

        if not self.instance:  # If we are creating a new user, validate the email
            if value and User.objects.filter(email=value).exists():
                raise serializers.ValidationError(_('an account with this email already exist.'))
            else:
                return value
        else:
            # Else if we are updating, only validate email if the email is different.

            if self.instance.email == value:  # then do not validate.
                return value
            else:  # The user has updated the email field, validate the new email.
                if User.objects.filter(email=value).exists():
                    raise serializers.ValidationError(_('an account with this email already exist.'))
                else:
                    return value

    def validate_phone(self, value):
        # Checks to ensure the phone number provided does not exist already and that is well formatted.

        formatted = format_number(value)
        if formatted:
            value = formatted
        else:
            raise serializers.ValidationError(_('phone number is invalid.'))

        if not self.instance:  # If we are creating a new user, validate the email
            if value and User.objects.filter(phone=value).exists():
                raise serializers.ValidationError(_('an account with this phone number already exist.'))
            else:
                return value
        else:
            # Else if we are updating, only validate phone number if the phone number is different.
            if self.instance.phone == value:  # then do not validate.
                return value
            else:  # The user has updated the email field, validate the new email.
                if User.objects.filter(phone=value).exists():
                    raise serializers.ValidationError(_('an account with this phone number already exist.'))
                else:
                    return value

    def validate_username(self, value):
        # Checks to ensure the phone number provided does not exist already and that is well formatted

        if not self.instance:  # If we are creating a new user, validate the username
            if value:
                if User.objects.filter(username=value).exists():
                    raise serializers.ValidationError(_('an account with this username already exist.'))
                else:
                    return value
            else:
                return get_default_username()
        else:
            # Else if we are updating, only validate if it's different.
            if self.instance.username == value:  # then do not validate.
                return value
            else:  # The user has updated the username field, validate the new username.
                if User.objects.filter(username=value).exists():
                    raise serializers.ValidationError(_('an account with this username already exist.'))
                else:
                    return value


class ProfilePictureSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('photo',)


class PasswordResetSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    # code = serializers.CharField(r)

    class Meta:
        model = User
        fields = ('password', 'id', 'code')

    def update(self, instance, validated_data):
        user = super(PasswordResetSerializer, self).update(instance, validated_data)
        if 'password' in validated_data:  # if a new password was set, encrypt it.
            user.set_password(user.password)
            user.save()
        return user
