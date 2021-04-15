from django.shortcuts import render
from django.views.generic import CreateView, TemplateView, UpdateView, FormView
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import PasswordChangeForm
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


class UpdateUserPasswordView(LoginRequiredMixin, FormView):

    template_name = 'accounts/update_password.html'
    form_class = PasswordChangeForm
    success_url = reverse_lazy('accounts:index')

    def get_form_kwargs(self):
        """ PasswordChangeForm requires an User at __init__, so we get the args and include the user """
        kwargs = super(UpdateUserPasswordView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        """ method called when form is valid """
        form.save()
        return super().form_valid(form)


index = IndexView.as_view()
register = RegisterView.as_view()
update = UpdateUserView.as_view()
update_password = UpdateUserPasswordView.as_view()