from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class register_forms(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "username"})
    )
    email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder": "email"}))
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Your password"})
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Confirm your password"})
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
