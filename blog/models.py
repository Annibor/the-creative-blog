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

class Comment(models.Model):
    """
    A model representing a comment.

    Attributes:
    author: The author of the comment.
    comment_content: The actual comment.
    created_on: The time when the comment was written.
    approved: Inidicates whether the comment was approved or not.
    post: The post to witch the comment belongs.
    """
    author = models.CharField(max_length=70)
    comment_content = models.TextField(max_length=600)
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    post = models.ForeignKey("Post", on_delete=models.CASCADE)
