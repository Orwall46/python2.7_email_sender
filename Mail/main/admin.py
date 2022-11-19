# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import ListEmail, ReadMail

# Register your models here.
admin.site.register(ListEmail)
admin.site.register(ReadMail)