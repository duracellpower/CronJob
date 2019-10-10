from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#Source: https://stackoverflow.com/questions/32860296/how-do-i-extend-usercreationform-to-include-email-field


class UserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email')

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
