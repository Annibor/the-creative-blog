from django.urls import path
from . import views

urlspattern = [
    path("", views.starting_page, name="starting_page")
]
