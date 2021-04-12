from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from accounts.forms import UserAdminCreationForm


class RegisterView(CreateView):

    template_name = 'accounts/register.html'
    form_class = UserAdminCreationForm
    model = get_user_model()
    success_url = reverse_lazy('login')


register = RegisterView.as_view()
