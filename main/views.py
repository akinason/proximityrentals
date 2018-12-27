from django.core.mail import send_mail
from django.http import Http404
from django.views import generic as generic_views

from rest_framework.authtoken.views import ObtainAuthToken as BaseObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status, generics, permissions
from rest_framework.views import APIView

from main import serializers
from main.models import User, manager as user_manager
from main.permissions import IsUserOrReadOnly
from sms.models import SmsManager


sms_manager = SmsManager()


class UserList(generics.GenericAPIView):
    """
    List existing users or creates a new user. GET request to list with no params and POST request to create
    with params {optional phone, optional email, optional first_name, optional last_name, optional ...}
    """

    queryset = User.objects.filter(is_deleted=False)
    serializer_class = serializers.UserSerializer

    def get_queryset(self):
        querset = super(UserList, self).get_queryset()
        querset = querset.filter(is_deleted=False)
        return querset

    def get(self, request, format=None):
        data = self.get_queryset()
        serializer = self.serializer_class(data, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetail(APIView):
    """
    List detail information about a single user, then, delete, or update the user
    """
    model = User
    serializer_class = serializers.UserSerializer

    permission_classes = (IsUserOrReadOnly, permissions.IsAuthenticatedOrReadOnly)

    def get_object(self):
        id = self.request.query_params.get('id') or self.request.POST.get('id')

        try:
            obj = self.model.objects.filter(is_deleted=False).get(pk=id)
            self.check_object_permissions(self.request, obj)
            return obj
        except self.model.DoesNotExist:
            raise Http404
        except Exception:
            raise Http404

    def get(self, request, format=None):
        obj = self.get_object()
        serializer = self.serializer_class(obj)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, format=None):
        obj = self.get_object()
        serializer = self.serializer_class(obj, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, format=None):
        obj = self.get_object()
        if obj:
            obj.is_deleted = True
            obj.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_401_UNAUTHORIZED)


class ProfilePictureDetail(APIView):
    """
    Update user's profile picture.
    """

    model = User
    queryset = User.objects.filter(is_deleted=False)
    serializer_class = serializers.ProfilePictureSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsUserOrReadOnly)

    def get_object(self):
        id = self.request.query_params.get('id') or self.request.POST.get('id')

        try:
            return self.queryset.get(pk=id)
        except self.model.DoesNotExist:
            raise Http404
        except Exception:
            raise Http404

    def put(self, request, format=None):
        obj = self.get_object()
        serializer = self.serializer_class(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VerifyUserName(APIView):

    """
    Verify if a username already exists. Username can be phone number or email or username.
    Returns "true" if it exist and "false" if it does not exist.
    """
    def get(self, request, format=None):
        username = request.query_params.get('username')
        if username:
            exist = (
                User.objects.filter(username=username).exists() or User.objects.filter(email=username).exists() or
                User.objects.filter(phone=username).exists()
            )
        else:
            return Response(False, status=status.HTTP_400_BAD_REQUEST)
        return Response(exist, status=status.HTTP_200_OK)


class VerifyEmail(APIView):
    """
    Verify if email already exists.
    Returns "true" if it exist and "false" if it does not exist.
    """

    def get(self, request, format=None):
        email = request.query_params.get('email')
        if email:
            exist = User.objects.filter(email=email).exists()

        else:
            return Response(False, status=status.HTTP_400_BAD_REQUEST)
        return Response(exist, status=status.HTTP_200_OK)


class VerifyPhone(APIView):
    """
    Verify if a phone number already exists. Phone number should be in international format without + or 00
    Returns "true" if it exist and "false" if it does not exist.
    """

    def get(self, request, format=None):
        phone = request.query_params.get('phone')
        if phone:
            exist =User.objects.filter(phone=phone).exists()

        else:
            return Response(False, status=status.HTTP_400_BAD_REQUEST)
        return Response(exist, status=status.HTTP_200_OK)


class ObtainAuthToken(BaseObtainAuthToken):
    """
    Extend base ObtainAuthToken which creates a single token for a user to that which creates a token each time a
    user logs in.
    """
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        if Token.objects.filter(user=user).exists():
            token = Token.objects.get(user=user)
            token.delete()
        token, created = Token.objects.get_or_create(user=user)

        serializer = serializers.UserSerializer(user)
        return Response({'token': token.key, 'user': serializer.data}, status=status.HTTP_200_OK)


class PasswordReset(APIView):

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        # Generate a 5 digits code and send.
        user = user_manager.get_user(username)
        if not user:
            return Response(status=status.HTTP_404_NOT_FOUND)
        if not user.verified_email and not user.verified_phone:
            return Response(
                {'verified': 'phone number and email are not verified'}, status=status.HTTP_404_NOT_FOUND
            )

        code = user_manager.make_random_password(length=5, allowed_chars='23456789')
        user.code = code  # store the code to be used during the next api request for verification
        user.save()
        message = 'Your Password Reset Code \n%s' % code
        if user.verified_phone:
            sms_manager.send(user.verified_phone, message)

        if user.verified_email:
            send_mail(
                subject='Your Password Reset Code',
                message='This is your password reset code. <br> <h1>%s</h1> ' % code,
                from_email='proximityrentals@gmail.com',
                recipient_list=[user.verified_email],
                html_message='This is your password reset code. <br> <h1>%s</h1> ' % code,
            )

        return Response({'id': user.id}, status=status.HTTP_200_OK)


class PasswordResetVerifyCode(APIView):
    """
    Used to verify if a password reset code is correct. This endpoint can be called for each character keyed in by the
    user. Returns True or False. Status Code 200 ok, or 404 Not Found
    """
    def get(self, request, *args, **kwargs):
        id = request.query_params.get('id')
        code = request.query_params.get('code')

        if User.objects.filter(is_deleted=False, pk=id, code=code).exists():
            return Response(True, status=status.HTTP_200_OK)

        return Response(False, status=status.HTTP_404_NOT_FOUND)


class PasswordResetConfirm(APIView):
    """
    Takes the id and code plus password to create a new password and return a login token plus user instance.
    """
    def put(self, request, *args, **kwargs):
        id = request.POST.get('id')
        code = request.POST.get('code')
        if User.objects.filter(is_deleted=False, pk=id, code=code).exists():
            user = User.objects.filter(pk=id).get()
            serializer = serializers.PasswordResetSerializer(user, data=request.data)
            if serializer.is_valid():
                serializer.save()  # Save the password serializer and initialize a user serializer below.

                serializer = serializers.UserSerializer(user)
                if Token.objects.filter(user=user).exists():
                    token = Token.objects.get(user=user)
                    token.delete()
                token, created = Token.objects.get_or_create(user=user)
                return Response({'token': token.key, 'user': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(False, status=status.HTTP_400_BAD_REQUEST)

