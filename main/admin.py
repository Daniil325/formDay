from django.contrib import admin
from .models import *


@admin.register(Message)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['fio', 'group', 'comment']
