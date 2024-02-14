"""This will keep the views"""
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def starting_page(request):
    return HttpResponse("Hello, World!")
