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

class Post(models.Model):
    """
    This model represents a post.

    Attributes:
    title: The title of the post.
    post_content: The content of the post.
    created_on: The date and time when the post was created.
    last_modifed: The last time the post was updated or changed.
    categoris: The categoris associated with the post.
    """
    title = models.CharField(max_length=250, unique=True)
    post_content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField("Category", related_name="posts")

    class Meta:
        verbose_name_plural = "Posts"

    def __str__(self):
        return f"{self.title}"
