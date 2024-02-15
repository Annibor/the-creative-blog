"""This will add the urls for the site"""
from django.urls import path
from . import views

urlpatterns = [
    path("", views.blog_page, name="blog_page"),
    
]
