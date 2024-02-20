"""This will keep the views"""
from django.shortcuts import render
from blog.models import Post

# Create your views here.
def starting_page(request):
    """
    The startpage views
    """
    return render(request, 'home/index.html')


def homepost(request):
    latest_post = (Post.objects.filter(published=True).order_by
                   ('-created_on').first())
    
    context = {'latest_post': latest_post}

    return render(request, 'index.html', context)