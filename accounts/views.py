from django.shortcuts import render
from django.views.generic import CreateView, TemplateView, UpdateView
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from accounts.forms import UserAdminCreationForm


class IndexView(LoginRequiredMixin, TemplateView):

    template_name = 'accounts/index.html'


class RegisterView(CreateView):

    template_name = 'accounts/register.html'
    form_class = UserAdminCreationForm
    model = get_user_model()
    success_url = reverse_lazy('login')


class UpdateUserView(LoginRequiredMixin, UpdateView):

    model = get_user_model()
    template_name = 'accounts/update_user.html'
    fields = ['name', 'email']
    success_url = reverse_lazy('accounts:index')

    def get_object(self):
        """ overwrite method that get obj to update (usually get by query params.)"""
        return self.request.user


index = IndexView.as_view()
register = RegisterView.as_view()
update = UpdateUserView.as_view()
