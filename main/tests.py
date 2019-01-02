from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from main.models import User, UserManager

user_manager = UserManager()


class CreateUserTest(APITestCase):
    def test_create_useraccount_with_phone_and_password(self):
        """
        Ensure we can create a new user account object with phone and password
        """
        url = reverse('main:users')
        data = {'phone': '237675397307', 'password': '123456789A'}
        res = self.client.post(url, data, format='json')
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().phone, '237675397307')

    def test_create_useraccount_with_email_and_password(self):
        """
        Ensure we can create a new user account object with email and password
        """

        url = reverse('main:users')
        data = {'email': 'kinason42@gmail.com', 'password': '123456789A'}
        res = self.client.post(url, data, format='json')
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().email, 'kinason42@gmail.com')

    def test_create_useraccount_with_phone_email_otherdata_and_password(self):
        """
        Ensure we can create a new user account object with phone, email, other data and password
        """

        url = reverse('main:users')
        data = {'phone': '237675397307', 'password': '123456789A', 'email': 'kinason42@gmail.com', 'first_name': 'awa',
                'last_name': 'kinason', 'username': 'kinason'
                }
        res = self.client.post(url, data, format='json')
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().phone, '237675397307')

    def test_cannot_create_user_without_email_or_phone(self):
        """
        Ensure we cannot create an account with no email and phone.
        """

        url = reverse('main:users')
        data = {'first_name': 'awa', 'password': '123456789A'}
        res = self.client.post(url, data, format='json')
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 0)


class ReadUserTest(APITestCase):

    def setUp(self):
        users = [
            {'first_name': 'awa', 'last_name': 'kinason', 'phone': '237675397307', 'password': '123456789A'},
            {'first_name': 'bih', 'email': 'bih@example.com', 'password': '123456789A'},
            {'first_name': 'ngwi', 'last_name': 'simon', 'email': 'simon@gmail.com', 'phone': '237655916762', 'password': '123456789A'}
        ]
        for data in users:
            res = self.client.post(reverse('main:users'), data=data)
        return super(ReadUserTest, self).setUp()

    def test_get_single_user(self):
        """
        Ensures we can get details of a single account.
        """
        user = User.objects.order_by('id')[:1].get()
        res = self.client.get(reverse('main:user'), {'id': user.pk})
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['first_name'], user.first_name)

    def test_can_get_user_accounts(self):
        """
        Ensures we can get the list of all user accounts.
        """
        res = self.client.get(reverse('main:users'))
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_username_is_not_yet_in_use(self):
        """
        Ensures we get a False when a username is not yet in use.
        """
        username = 'thisusernamedoesnotexist'
        res = self.client.get(reverse('main:verify_username'), {'username': username})
        self.assertEqual(res.data, False )
    
    def test_username_is_already_in_use(self):
        """
        Ensures we get a False when a username is not yet in use.
        """
        user = User.objects.order_by('-id')[:1].get()
        res = self.client.get(reverse('main:verify_username'), {'username': user.username})
        self.assertEqual(res.data, True )

    def test_phone_is_not_yet_in_use(self):
        """
        Ensures we get a False when a username is not yet in use.
        """
        phone = '6753973074'
        res = self.client.get(reverse('main:verify_phone'), {'phone': phone})
        self.assertEqual(res.data, False )
    
    def test_phone_is_already_in_use(self):
        """
        Ensures we get a False when a username is not yet in use.
        """
        user = User.objects.order_by('-id')[:1].get()
        res = self.client.get(reverse('main:verify_phone'), {'phone': user.phone})
        self.assertEqual(res.data, True )

    def test_email_is_not_yet_in_use(self):
        """
        Ensures we get a False when a username is not yet in use.
        """
        email = 'doesnotexist@example.com'
        res = self.client.get(reverse('main:verify_email'), {'email': email})
        self.assertEqual(res.data, False )
    
    def test_email_is_already_in_use(self):
        """
        Ensures we get a False when a username is not yet in use.
        """
        user = User.objects.order_by('-id')[:1].get()
        res = self.client.get(reverse('main:verify_email'), {'email': user.email})
        self.assertEqual(res.data, True )


class UpdateUserTest(APITestCase):

    def setUp(self):
        users = [
            {'first_name': 'awa', 'last_name': 'kinason', 'phone': '237675397307', 'password': '123456789A'},
            {'first_name': 'bih', 'email': 'bih@example.com', 'password': '123456789A'},
            {'first_name': 'ngwi', 'last_name': 'simon', 'email': 'simon@gmail.com', 'phone': '237655916762', 'password': '123456789A'}
        ]
        for data in users:
            res = self.client.post(reverse('main:users'), data=data)
        
        user = User.objects.order_by('id')[:1].get()
        res = self.client.post(reverse('main:login'), {'username': user.phone, 'password': '123456789A'})
        self.token = res.data['token']

        return super(UpdateUserTest, self).setUp()
    
    def test_cannot_change_account_details_without_auth(self):
        user = User.objects.order_by('id')[:1].get()
        res = self.client.put(reverse('main:user'), {'id': user.pk, 'first_name': 'kutaba'})
       
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(User.objects.order_by('id')[:1].get().first_name, user.first_name)

    def test_can_change_account_details_with_valid_authtoken(self):
        user = User.objects.order_by('id')[:1].get()

        self.client.credentials(HTTP_AUTHORIZATION='Token %s' % self.token)
        res = self.client.put(reverse('main:user'), {'id': user.pk, 'first_name': 'kutaba'})
   
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.order_by('id')[:1].get().first_name, 'kutaba')


class DeleteUserTest(APITestCase):

    def setUp(self):
            users = [
                {'first_name': 'awa', 'last_name': 'kinason', 'phone': '237675397307', 'password': '123456789A'},
                {'first_name': 'bih', 'email': 'bih@example.com', 'password': '123456789A'},
                {'first_name': 'ngwi', 'last_name': 'simon', 'email': 'simon@gmail.com', 'phone': '237655916762', 'password': '123456789A'}
            ]
            for data in users:
                res = self.client.post(reverse('main:users'), data=data)
            
            user = User.objects.order_by('id')[:1].get()
            res = self.client.post(reverse('main:login'), {'username': user.phone, 'password': '123456789A'})
            self.token = res.data['token']

            return super(DeleteUserTest, self).setUp()

    def test_cannot_delete_account_without_valid_authtoken(self):
        """
        Ensures we cannot delete a user account if there is no valid auth token provided. 
        """
        user = User.objects.order_by('id')[:1].get()
        res = self.client.delete(reverse('main:user'), {'id': user.pk})
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_delete_user_account_with_valid_authtoken(self):
        """
        Ensures we can delete a user account only if there is a valid auth token provided. 
        """
        user = User.objects.order_by('id')[:1].get()
        self.client.credentials(HTTP_AUTHORIZATION='Token %s' % self.token)
        res = self.client.delete(reverse('main:user'), {'id': user.pk})

        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)

    def test_cannot_delete_a_different_user_account_with_valid_authtoken(self):
        """
        Ensures we can delete a user account only if there is a valid auth token provided. 
        """
        user = User.objects.order_by('id')[:1].get()
        user2 = User.objects.order_by('-id')[:1].get()
        self.client.credentials(HTTP_AUTHORIZATION='Token %s' % self.token)
        res = self.client.delete(reverse('main:user'), {'id': user2.pk})

        self.assertEqual(res.status_code, status.HTTP_404_NOT_FOUND)


class UserLoginTest(APITestCase):

    def setUp(self):
        users = [
            {'first_name': 'awa', 'last_name': 'kinason', 'phone': '237675397307', 'password': '123456789A', 'email': 'kinason42@gmail.com'},
            {'first_name': 'bih', 'email': 'bih@example.com', 'password': '123456789A'},
            {'first_name': 'ngwi', 'last_name': 'simon', 'email': 'simon@gmail.com', 'phone': '237655916762', 'password': '123456789A'}
        ]
        for data in users:
            res = self.client.post(reverse('main:users'), data=data)
        return super(UserLoginTest, self).setUp()

    def test_can_login_with_username_and_password(self):
        """
        Ensures the user can login with provided 'username' and 'password'
        """
        user = User.objects.order_by('id')[:1].get()
        res = self.client.post(reverse('main:login'), {'username': user.username, 'password': '123456789A'})
        
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertIn('user', res.data)

    def test_can_login_with_phone_and_password(self):
        """
        Ensures the user can login with provided 'username' and 'password'
        """
        user = User.objects.order_by('id')[:1].get()
        res = self.client.post(reverse('main:login'), {'username': user.phone, 'password': '123456789A'})
        
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertIn('user', res.data)

    def test_can_login_with_email_and_password(self):
            """
            Ensures the user can login with provided 'username' and 'password'
            """
            user = User.objects.order_by('id')[:1].get()
            res = self.client.post(reverse('main:login'), {'username': user.email, 'password': '123456789A'})
            
            self.assertEqual(res.status_code, status.HTTP_200_OK)
            self.assertIn('user', res.data)


class PasswordResetTest(APITestCase):

    def setUp(self):
        
        users = [
            {'first_name': 'awa', 'last_name': 'kinason', 'phone': '237675397307', 'password': '123456789A', 'email': 'kinason42@gmail.com'},
            {'first_name': 'bih', 'email': 'bih@example.com', 'password': '123456789A'},
            {'first_name': 'ngwi', 'last_name': 'simon', 'email': 'simon@gmail.com', 'phone': '237655916762', 'password': '123456789A'}
        ]

        for data in users:
            res = self.client.post(reverse('main:users'), data=data)
        
        self.user = User.objects.order_by('id')[:1].get()
        self.code = user_manager.make_random_password(length=5, allowed_chars='123456789')
        self.user.code = self.code 
        self.user.save()
        return super(PasswordResetTest, self).setUp()

    def test_can_receive_password_reset_OTP(self):
        """
        Ensures we can send a password reset One Time Password (code) to the user.
        The code is sent by SMS and Email to the user if and only if user.verified_phone or user.verified_email exists.
        """
        if self.user.email:
            self.user.verified_email = self.user.email
        if self.user.phone:
            self.user.verified_phone = self.user.phone 
        self.user.save()

        res = self.client.post(reverse('main:password_reset'), {'username': self.user.phone})
        # username kwarg can be 'user.phone' or 'user.email' or 'user.username'

        # response is in the format {'id': user.pk}, since we do not have access to the code that was sent by SMS or Email to the user, 
        # we are going to read that value from the user instance. First we need to reload the user instance.

        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_code_sent_to_user_exists(self):
        """
        Ensures frontend applications can test if the code entered by the user is correct.
        """
        user = User.objects.get(pk=self.user.pk)

        res = self.client.get(reverse('main:verify_reset_code'), {'code': user.code, 'id': self.user.pk})
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, True)

    def test_password_reset_confirm_with_correct_params(self):
        """
        Ensures we get a token and user instance as response after submitting an id and code.

        Since we do not have access to the code sent to the user, we will read it from the user instance.
        """
        user = User.objects.get(pk=self.user.pk)  #  First we refresh the user from db. self.user.refresh_from_db() does not do the job.

        res = self.client.put(reverse('main:password_reset_confirm'), data={'id': user.id, 'code': user.code})
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertIn('token', res.data)
        self.assertIn('user', res.data)

class EmailAndPhoneVerificationTest(APITestCase):

    def setUp(self):
        users = [
            {'first_name': 'awa', 'last_name': 'kinason', 'phone': '237675397307', 'password': '123456789A', 'email': 'kinason42@gmail.com'},
            {'first_name': 'bih', 'email': 'bih@example.com', 'password': '123456789A'},
            {'first_name': 'ngwi', 'last_name': 'simon', 'email': 'simon@gmail.com', 'phone': '237655916762', 'password': '123456789A'}
        ]

        for data in users:
            res = self.client.post(reverse('main:users'), data=data)
        
        self.user = User.objects.order_by('id')[:1].get()
        self.user.email_verification_code = user_manager.make_random_password(length=5, allowed_chars='123456789')
        self.user.phone_verification_code = user_manager.make_random_password(length=5, allowed_chars='123456789')
        self.user.save()
        return super(EmailAndPhoneVerificationTest, self).setUp()
    
    def test_can_send_email_verification_code(self):
        """
        Ensures we can verify a user's email address.
        """
        params = {'username': self.user.email}
        res = self.client.post(reverse('main:verification'), data=params)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, {'id': self.user.id})

    def test_can_send_phone_verification_code(self):
        """
        Ensures we can verify a user's email address.
        """
        params = {'username': self.user.phone}
        res = self.client.post(reverse('main:verification'), data=params)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, {'id': self.user.id})
    
    def test_can_confirm_email_verification_code_already_sent(self):
        """
        Ensures that we can confirm phone or email verification codes. 
        """
        res = self.client.post(reverse('main:confirm_verification'), data={'id': self.user.id, 'code': self.user.email_verification_code})
        user = User.objects.get(pk=self.user.pk)

        self.assertEqual(res.data, True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(user.verified_email, self.user.email)

    def test_can_confirm_phone_verification_code_already_sent(self):
        """
        Ensures that we can confirm phone or email verification codes. 
        """
        res = self.client.post(reverse('main:confirm_verification'), data={'id': self.user.id, 'code': self.user.phone_verification_code})
        user = User.objects.get(pk=self.user.pk)
        
        self.assertEqual(res.data, True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(user.verified_phone, self.user.phone)
        