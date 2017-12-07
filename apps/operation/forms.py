# _*_ coding: utf-8 _*_
__author__ = 'lihao'
__date__ = '2017/11/28 10:23'

from django import forms
from operation.models import UserAsk



class UserAskForm(forms.ModelForm):

    class Meta:
        model = UserAsk
        fields = ['name','course_name','mobile']



