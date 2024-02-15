from django.shortcuts import render
from django.views import generic
from .models import Post, Comment

# Create your views here.
def blog_page(request):
    """
    The blog page view
    """
    return render(request, 'blog/blog.html')

def blog_post_index(request):
    posts = Post.objects.all().order_by('-created_on')
    context = {
        "posts": posts,
    }
    return render(request, "blog/post_index.html", context)

def categories_posts(request, category):
    """
    
    """
    posts = Post.objects.filter(catagories__name__contains=category
    ).order_by("-created_on")
    context = {
        "catagory": category,
        "posts": posts,
    }
    return render(request, "blog/catagory.html", context)

