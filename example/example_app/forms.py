# -*- coding:utf-8 -*-
from django import forms
from django.contrib.auth.models import User as DjangoUser

if DjangoUser.objects.all().count() == 0:
    DjangoUser.objects.create_user(email="test@funshion.com", password="111111", username="test")
    DjangoUser.objects.create_user(email="test1@funshion.com", password="111111", username="test1")
    DjangoUser.objects.create_user(email="test2@funshion.com", password="111111", username="test2")


class ExampleForm(forms.Form):
    title = forms.CharField()
    selects = forms.ModelChoiceField(queryset=DjangoUser.objects.all())
    checkinput = forms.ChoiceField(choices=((0, 'Zero'), (1, 'One'), (2, 'Two')), widget=forms.CheckboxInput)
    radioselect = forms.ChoiceField(choices=((0, 'Zero'), (1, 'One'), (2, 'Two')), widget=forms.RadioSelect)
    password = forms.CharField(widget=forms.PasswordInput, help_text=u"测试")
    textarea = forms.CharField(widget=forms.Textarea)
    end_date = forms.DateTimeField()
    start_date = forms.DateTimeField()
    date = forms.DateField()
    time = forms.TimeField()
