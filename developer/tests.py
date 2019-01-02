from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from developer.models import App 
from main.models import User, UserManager

user_manager = UserManager()


class CreateApplicationTest(APITestCase):

    def setUp(self):
            # Let's create an admin API_KEY which we use when sending request to create or list applications.
            app = App.objects.create(name='Test App')
            app.set_keys()
            app.is_admin=True
            app.save()
            self.API_KEY = app.key 
            self.client.credentials(HTTP_API_KEY='%s' % self.API_KEY)

            #  Create the user account to use.
            data =  {'first_name': 'awa', 'last_name': 'kinason', 'phone': '237675397307', 'password': '123456789A'}
            res = self.client.post(reverse('main:users'), data=data)
            
            # Login with the user and obtain an authentication token 
            res = self.client.post(reverse('main:login'), data={'username': '237675397307', 'password': '123456789A'})
            self.token = res.data['token']

            return super(CreateApplicationTest, self).setUp()

    def test_can_create_an_application_with_valid_login_token_and_valid_API_KEY(self):
        # Ensure we can create an application given that the user is already logged in. 

        self.client.credentials(HTTP_AUTHORIZATION='Token %s' % self.token, HTTP_API_KEY='%s' % self.API_KEY)
        res = self.client.post(reverse('developer:apps'), data={'name': 'Proximity Rentals'})

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(App.objects.count(), 2)
    
    def test_cannot_create_an_application_with_valid_login_token_and_invalid_API_KEY(self):
        # Ensure we cannot create an application with valid login but invalid API supper access key. 
        app = App.objects.create(name='Test App')
        app.set_keys()
        app.is_admin=False  # Here we deny super access. It's False by default though.
        app.save()

        self.client.credentials(HTTP_AUTHORIZATION='Token %s' % self.token, HTTP_API_KEY='%s' % app.key)
        res = self.client.post(reverse('developer:apps'), data={'name': 'Proximity Rentals'})

        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(App.objects.count(), 2)

    def test_cannot_create_an_application_with_invalid_login_and_valid_API_KEY(self):
        # Ensure we cannot create an application when the user is not logged in.
        self.client.credentials(HTTP_AUTHORIZATION='Token %s' % 'akjJLKJ;KJFAfkjdjJFDSJsj25fa', HTTP_API_KEY='%s' % self.API_KEY)
        res = self.client.post(reverse('developer:apps'), data={'name': 'Proximity Rentals'})

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class ReadApplicationTest(APITestCase):

    def setUp(self):
        # Let's create an admin API_KEY which we use when sending request to create or list applications.
        app = App.objects.create(name='Test App')
        app.set_keys()
        app.is_admin=True
        app.save()
        self.API_KEY = app.key 
        self.client.credentials(HTTP_API_KEY='%s' % self.API_KEY)

        #  Create the user account to use.
        data =  {'first_name': 'awa', 'last_name': 'kinason', 'phone': '237675397307', 'password': '123456789A'}
        res = self.client.post(reverse('main:users'), data=data)
        
        # Login with the user and obtain an authentication token 
        res = self.client.post(reverse('main:login'), data={'username': '237675397307', 'password': '123456789A'})
        self.token = res.data['token']

        # add some applications.
        apps = [{'name': 'TestApp1'}, {'name': 'TestApp2'}, {'name': 'TestApp3'}]
        for obj in apps:
            self.client.credentials(HTTP_AUTHORIZATION='Token %s' % self.token, HTTP_API_KEY='%s' % app.key)
            self.client.post(reverse('developer:apps'), data=obj)

        return super(ReadApplicationTest, self).setUp()

    def test_can_read_all_user_applications_with_valid_credentials(self):
        # Ensure we can get all user applications. Active and inactive.
        self.client.credentials(HTTP_AUTHORIZATION='Token %s' % self.token, HTTP_API_KEY='%s' % self.API_KEY)
        res = self.client.get(reverse('developer:apps'))

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 3)

    def test_can_get_a_single_app_information_with_valid_credentials(self):
        # Ensure we can read information partening to a particular app.
        user = User.objects.get(phone='237675397307')
        app = App.objects.filter(user=user)[:1].get()

        self.client.credentials(HTTP_AUTHORIZATION='Token %s' % self.token, HTTP_API_KEY='%s' % self.API_KEY)
        res = self.client.get(reverse('developer:app'), data={'id': app.id })

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['id'], app.id)


class UpdateApplicationTest(APITestCase):

    def setUp(self):
        # Let's create an admin API_KEY which we use when sending request to create or list applications.
        app = App.objects.create(name='Test App')
        app.set_keys()
        app.is_admin=True
        app.save()
        self.API_KEY = app.key 
        self.client.credentials(HTTP_API_KEY='%s' % self.API_KEY)

        #  Create the user account to use.
        data =  {'first_name': 'awa', 'last_name': 'kinason', 'phone': '237675397307', 'password': '123456789A'}
        res = self.client.post(reverse('main:users'), data=data)
        
        # Login with the user and obtain an authentication token 
        res = self.client.post(reverse('main:login'), data={'username': '237675397307', 'password': '123456789A'})
        self.token = res.data['token']

        # add some applications.
        apps = [{'name': 'TestApp1'}, {'name': 'TestApp2'}, {'name': 'TestApp3'}]
        for obj in apps:
            self.client.credentials(HTTP_AUTHORIZATION='Token %s' % self.token, HTTP_API_KEY='%s' % app.key)
            self.client.post(reverse('developer:apps'), data=obj)

        return super(UpdateApplicationTest, self).setUp()
    
    def test_can_update_only_app_name_given_valid_credentials(self):
        # Ensure we can only update the app name and nothing else.

        user = User.objects.get(phone='237675397307')
        app = App.objects.filter(user=user)[:1].get()

        self.client.credentials(HTTP_AUTHORIZATION='Token %s' % self.token, HTTP_API_KEY='%s' % self.API_KEY)
        res = self.client.put(reverse('developer:app'), data={'id': app.id, 'name': 'ProxiMate', 'key': '222555666'})

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(res.data['name'], 'ProxiMate')
        self.assertNotEqual(res.data['key'], '222555666')
    