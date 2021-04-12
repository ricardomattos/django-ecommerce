from django.urls import path
from accounts.views import register


urlpatterns = [
    path('registro', register, name='register')
]
