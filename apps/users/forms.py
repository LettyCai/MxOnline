# -*- coding: utf-8 -*-
__author__ = 'clj'
__date__ = '2019/1/31 15:04'

from django import forms
from captcha.fields import CaptchaField

class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True,min_length=5)

class RegisterForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True,min_length=5)
    captcha = CaptchaField(error_messages={"invaild":u"验证码错误"})

