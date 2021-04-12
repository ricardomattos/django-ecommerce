from django.test import Client, TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

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
