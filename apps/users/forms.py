# _*_ coding: utf-8 _*_
__author__ = 'lihao'
__date__ = '2017/11/24 17:58'
from django import forms
from captcha.fields import CaptchaField


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True,min_length=5)


class RegisterForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, min_length=5,max_length=20)
    captcha = CaptchaField(error_messages={'invalid':u'验证码错误'})


class ForgetForm(forms.Form):
    email = forms.EmailField(required=True)
    captcha = CaptchaField(error_messages={'invalid':u'验证码错误'})


class ModifyPwdForm(forms.Form):
    password1 = forms.CharField(required=True, min_length=5,max_length=20)
    password2 = forms.CharField(required=True, min_length=5,max_length=20)
