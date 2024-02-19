"""This will add the urls for the site"""
from django.urls import path
from . import views

app_name = "home"

urlpatterns = [
    path("", views.starting_page, name="starting_page"),
]
