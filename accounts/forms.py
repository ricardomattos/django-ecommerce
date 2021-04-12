from django.contrib.auth.forms import UserCreationForm
from django import forms
from accounts.models import User


# form to register users
class UserAdminCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ["username", "email"]


# form to edit all info. about registered users
class UserAdminForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'name', 'is_active', 'is_staff']
