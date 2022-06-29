from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        # it is going to save it in this model
        model = User
        # for what fields wants and thier order
        fields = ['username', 'email', 'password1', 'password2']
#
