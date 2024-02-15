"""This will add the urls for the site"""
from django.urls import path
from . import views

urlpatterns = [
    path("", views.blog_post_index, name="blog_post_index"),
    path("post/<int:pk>/", views.blog_post_detail, name="blog_post_detail"),
    path("category/<category>/", views.categories_posts, name="categories_posts"),
]
