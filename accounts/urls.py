from django.urls import path
from accounts.views import register, index, update, update_password


urlpatterns = [
    path('', index, name='index'),
    path('registro', register, name='register'),
    path('atualizar-dados', update, name='update_user'),
    path('atualizar-senha', update_password, name='update_password')
]
