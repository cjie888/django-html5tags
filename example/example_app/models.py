# -*- coding:utf-8 -*-
from django.db import models

class SomeModel(models.Model):
    some_field = models.CharField(max_length=255)

    def __str__(self):
        return u'%s' % self.some_field