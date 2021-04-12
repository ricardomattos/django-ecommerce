from django import forms
from django.core.mail import send_mail
from django.conf import settings


class ContactForm(forms.Form):

    name = forms.CharField(label='Nome', error_messages={'required': 'Por favor, preencha o campo com um nome valido'})
    email = forms.EmailField(label='E-Mail', error_messages={'required': 'Esse campo é obrigatório'})
    message = forms.CharField(label='Mensagem', widget=forms.Textarea, error_messages={'required': 'Esse campo é obrigatório'})

    # def __init__(self, *args, **kwargs):
    #     super(ContactForm, self).__init__(*args, **kwargs)
    #     self.fields['name'].widget.attrs['class'] = 'form-control'
    #     self.fields['email'].widget.attrs['class'] = 'form-control'
    #     self.fields['message'].widget.attrs['class'] = 'form-control'

    def send_mail(self):
        # cleaned_data -> retorna o dado ja serializado
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        message = self.cleaned_data['message']

        message = f'Nome: {name}\nE-mail: {email}\nMessage: {message}'
        send_mail(subject='Contato do Django E-Commerce',
                  message=message,
                  from_email=settings.DEFAULT_FROM_EMAIL,
                  recipient_list=[settings.DEFAULT_FROM_EMAIL])
