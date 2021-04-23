from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from django.views.generic import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.urls import reverse_lazy
from core.form import ContactForm

class IndexView(TemplateView):

    template_name = 'index.html'

class ContactView(FormView):

    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact')

    def form_valid(self, form):
        form.send_mail()
        messages.success(self.request, 'Mensagem enviada com sucesso')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, 'Formulario inválido')
        return super().form_invalid(form)


index = IndexView.as_view()
contact = ContactView.as_view()
