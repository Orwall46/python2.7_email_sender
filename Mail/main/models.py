# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class ListEmail(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length = 254)
    birthday = models.DateField()


class ReadMail(models.Model):
    user = models.ForeignKey(ListEmail, on_delete=models.CASCADE)
    is_read = models.BooleanField(default=False)
    url = models.URLField(max_length=250)
    code = models.CharField(max_length=8, blank=True)
