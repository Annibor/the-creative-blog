"""
Registering models with the Django admin interface.

"""
from django.contrib import admin
from .models import Category

# Register your models here.
admin.site.register(Category)

