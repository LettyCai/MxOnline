# -*- coding: utf-8 -*-
__author__ = 'clj'
__date__ = '2019/1/31 15:04'

from django import forms
from .models import UserProfile

class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True,min_length=5)