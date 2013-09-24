# -*- coding:utf-8 -*-
from django import forms
from django.contrib.auth.models import User as DjangoUser
import html5tags.bootstrap as floppy
import time
import datetime

if DjangoUser.objects.all().count() == 0:
    DjangoUser.objects.create_user(email="test@funshion.com", password="111111", username="test")
    DjangoUser.objects.create_user(email="test1@funshion.com", password="111111", username="test1")
    DjangoUser.objects.create_user(email="test2@funshion.com", password="111111", username="test2")


class ExampleForm(forms.Form):
    title = forms.CharField(max_length=3)
    selects = forms.ModelChoiceField(queryset=DjangoUser.objects.all())
    checkinput = forms.ChoiceField(choices=((0, 'Zero'), (1, 'One'), (2, 'Two')), widget=forms.CheckboxInput)
    radioselect = forms.ChoiceField(choices=((0, 'Zero'), (1, 'One'), (2, 'Two')), widget=forms.RadioSelect)
    password = forms.CharField(widget=forms.PasswordInput, help_text=u"测试")
    textarea = forms.CharField(widget=forms.Textarea)
    end_date = forms.DateTimeField()
    start_date = forms.DateTimeField()
    date = forms.DateField()
    time = forms.TimeField()
    file_ = forms.FileField(required=False)


class TestForm(floppy.Form):
    title = floppy.CharField(widget=floppy.TextInput, max_length=3)
    selects = floppy.ModelChoiceField(queryset=DjangoUser.objects.all())
    checkinput = floppy.ChoiceField(choices=((0, 'Zero'), (1, 'One'),), required=False, widget=floppy.CheckboxInput)
    radioselect = forms.ChoiceField(choices=((0, 'Zero'), (1, 'One'), (2, 'Two')), required=False, widget=floppy.RadioSelect)
    password = floppy.CharField(widget=floppy.PasswordInput, help_text=u"测试")
    textarea = floppy.CharField(widget=floppy.Textarea({'class': 'test'}))
    bootstrap_textarea = floppy.CharField(widget=floppy.MarkDownTextarea)
    end_date = floppy.DateTimeField(initial=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time() + 24 * 60 * 60)))
    start_date = floppy.DateTimeField()
    date = floppy.DateField()
    time = floppy.TimeField()
    url_floppy = floppy.URLField()
    null = floppy.NullBooleanField()
