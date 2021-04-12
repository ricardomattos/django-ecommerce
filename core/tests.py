from django.test import TestCase, Client
from django.urls import reverse
from django.core import mail
from django.conf import settings
from django.contrib.auth import get_user_model
from model_mommy import mommy

User = get_user_model()

class IndexViewTestCase(TestCase):

    def setUp(self) -> Client:
        self.client = Client()
        self.url = reverse('index')

    def tearDown(self):
        pass

    def test_index_status_code(self):
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 200)

    def test_index_template_used(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, "index.html")


class ContactViewTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse('contact')

    def test_index_status_code(self):
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 200)

    def test_index_template_used(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, "contact.html")

    def test_form_error(self):
        data = {'name': '', 'email': '', 'message': ''}
        response = self.client.post(self.url, data)
        self.assertFormError(response, 'form', 'name', 'Por favor, preencha o campo com um nome valido')
        self.assertFormError(response, 'form', 'email', 'Esse campo é obrigatório')
        self.assertFormError(response, 'form', 'message', 'Esse campo é obrigatório')

    def test_form_success(self):
        data = {'name': 'ricardo', 'email': 'user@gmail.com', 'message': 'blablabla'}
        response = self.client.post(self.url, data)
        self.assertTrue(response.context['success'])
        self.assertEquals(len(mail.outbox), 1)
        self.assertEquals(mail.outbox[0].subject, 'Contato do Django E-Commerce')


class LoginViewTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.login_url = reverse('login')
        self.user = mommy.prepare(User)  # prepare -> don't save on database yet
        # set_password -> method that cryptography the password
        # we can't do self.user.password = xx because the password will not be encrypted
        self.user.set_password('123')
        self.user.save()

    def tearDown(self):
        self.user.delete()

    def test_login_template_used(self):
        response = self.client.get(self.login_url)
        self.assertTemplateUsed(response, 'login.html')

    def test_login_status_code(self):
        response = self.client.get(self.login_url)
        self.assertEquals(response.status_code, 200)

    def test_login_error(self):
        data = {'username': self.user.username, 'password': '1234'}
        error_msg = 'Please enter a correct Apelido / Usuário and password. ' \
                    'Note that both fields may be case-sensitive.'

        response = self.client.post(self.login_url, data)
        self.assertFormError(response, 'form', None, error_msg)

    def test_login_success(self):
        data = {'username': self.user.username, 'password': '123'}
        redirect_url = reverse(settings.LOGIN_REDIRECT_URL)
        response = self.client.post(self.login_url, data)
        self.assertRedirects(response, redirect_url)

        # verify if user is really logged in
        self.assertTrue(response.wsgi_request.user.is_authenticated)
