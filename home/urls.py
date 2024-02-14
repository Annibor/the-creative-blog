"""This will add the urls for the site"""
from django.urls import path
from . import views

urlpatterns = [
    path("", views.starting_page, name="starting_page"),
]
