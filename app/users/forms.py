from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from app.catalog.forms import StyleFormMixin
from app.users.models import Users
from django import forms



class UserForm(StyleFormMixin, UserCreationForm):
    class Meta:
        model = Users
        fields = ['email', 'password1', 'password2']


class LoginForm(StyleFormMixin, AuthenticationForm):
    pass