from django.shortcuts import render
from django.views import generic
from .models import Post, Comment

# Create your views here.
#def blog_page(request):
   # """
   # The blog page view
   # """
  #  return render(request, 'blog/blog.html')

def blog_post_index(request):
    posts = Post.objects.all().order_by('-created_on')
    context = {
        "posts": posts,
    }
    return render(request, "blog/blog.html", context)

def categories_posts(request, category):
    """
    
    """
    posts = Post.objects.filter(categories__name__contains=category
    ).order_by("-created_on")
    context = {
        "category": category,
        "posts": posts,
    }
    return render(request, "blog/category.html", context)

def blog_post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
    }

    return render(request, "blog/post_detail.html", context)