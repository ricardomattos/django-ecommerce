from django.test import Client, TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from model_mommy import mommy

User = get_user_model()


class RegisterViewTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.register_url = reverse('accounts:register')

    def test_register_error(self):
        data = {'username': 'maya', 'password1': 'puguinha', 'password2': 'puguinha'}
        response = self.client.post(self.register_url, data)
        self.assertFormError(response, 'form', 'email', 'This field is required.')

    def test_register_success(self):
        data = {
            'username': 'maya', 
            'email': 'maya@email.com',
            'password1': 'puguinha', 
            'password2': 'puguinha'
        }
        login_url = reverse('login')
        response = self.client.post(self.register_url, data)
        self.assertRedirects(response, login_url)
        self.assertEquals(User.objects.count(), 1)


class UpdateUserViewTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.update_user_url = reverse('accounts:update_user')
        self.user = mommy.prepare(User)
        self.user.set_password('123')
        self.user.save()
    
    def tearDown(self):
        self.user.delete()

    def test_update_user_redirect(self):
        """ if user isn't logged in """
        response = self.client.get(self.update_user_url)

        self.assertEqual(response.status_code, 302)
    
    def test_update_user_success(self):
        new_name = 'test'
        new_email = 'test@test.com'
    
        self.client.login(username=self.user.username, password='123')

        data = {'name': new_name, 'email': new_email}
        response = self.client.post(self.update_user_url, data)

        accounts_index = reverse('accounts:index')
        self.assertRedirects(response, accounts_index)

        self.user.refresh_from_db()
        self.assertEqual(self.user.name, new_name)
        self.assertEqual(self.user.email, new_email)

    def test_update_user_error(self):
        self.client.login(username=self.user.username, password='123')        
        response = self.client.post(self.update_user_url, {})

        self.assertFormError(response, 'form', 'email', 'This field is required.')


class UpdatePasswordViewTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.update_password_url = reverse('accounts:update_password')
        self.user = mommy.prepare(User)
        self.user.set_password('123')
        self.user.save()
    
    def tearDown(self):
        self.user.delete()
    
    def test_update_password_success(self):
        data = {
            'old_password': 123,
            'new_password1': 'Test@123',
            'new_password2': 'Test@123'
        }

        self.client.login(username=self.user.username, password=123)
        response = self.client.post(self.update_password_url, data)

        self.user.refresh_from_db()
        self.assertTrue(self.user.check_password('Test@123'))
