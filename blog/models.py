from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=40)


class Post(models.Model):
    title = models.CharField(max_length=250, unique=True)
    post_content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField("Category", related_name="posts")

class Comment(models.Model):
    author = models.CharField(max_length=70)
    comment_content = models.TextField(max_length=600)
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey("Post", on_delete=CASCADE)
