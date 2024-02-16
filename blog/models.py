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

    def __str__(self):
        return f"{self.title}"


class Comment(models.Model):
    """
    A model representing a comment.

    Attributes:
    author: The author of the comment.
    comment_content: The actual comment.
    created_on: The time when the comment was written.
    approved: Indicates whether the comment was approved or not.
    post: The post to which the comment belongs.
    """
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    comment_content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")

    class Meta:
        ordering = ["created_on"]
        
    def __str__(self):
        return f"Comment by {self.author} on post '{self.post}'"