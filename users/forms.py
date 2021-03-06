from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())


class ProfileForm(forms.Form):
    age = forms.IntegerField()
    phone_number = forms.IntegerField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField(required=False)
    bio = forms.CharField(required=False)
    avatar = forms.ImageField(required=False)


class ConfigurationCodeForm(forms.Form):
    code = forms.IntegerField()
