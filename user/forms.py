from django import forms
from django.db import models
from django.forms import fields
from .models import User


class SignupForm(forms.Form):
    ID = forms.CharField(label="ID", max_length=15)
    PW = forms.CharField(label="PW", widget=forms.PasswordInput)
    PW_C = forms.CharField(label="PW 확인", widget=forms.PasswordInput)
    first_name = forms.CharField(label="닉네임", max_length=10)


class LoginForm(forms.Form):
    ID = forms.CharField(label="ID", max_length=15)
    PW = forms.CharField(label="PW", widget=forms.PasswordInput)
