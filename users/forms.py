from django.contrib.auth.forms import UserCreationForm
from django.forms import EmailField, TextInput

from .models import User


class UserForm(UserCreationForm):
    email = EmailField(label="", widget=TextInput(attrs={"class": "form-control", "placeholder": "Enter Your Email"}))

    class Meta:
        model = User
        fields = ["email", "password1", "password2"]
