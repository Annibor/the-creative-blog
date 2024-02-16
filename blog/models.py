"""
This module defines the models for the blog application.
"""
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    """
      A model representing a category for organizing blog posts.

    Attributes:
        name: The name of the category.
    """
    name = models.CharField(max_length=40)

    class Meta:
        verbose_name_plural = "categories"
