#-*- coding:utf-8 -*-
from django import forms

class CommentForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput())
   # content = forms.CharField(widget=forms.Textarea(attrs={'cols':50, 'rows': 5 , 'class':'form-control'}))
    content = forms.CharField(widget=forms.Textarea())

class UserForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput())

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=30)
    email = forms.EmailField()
    password = forms.CharField(max_length=128)
    password2 = forms.CharField(max_length=128)
