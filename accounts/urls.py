from django.urls import path
from accounts.views import register, index, update


urlpatterns = [
    path('', index, name='index'),
    path('registro', register, name='register'),
    path('atualizar', update, name='update')
]
