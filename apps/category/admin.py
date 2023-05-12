from django.contrib import admin
from unicodedata import category
from .models import Category

# Register your models here.
admin.site.register(Category)
