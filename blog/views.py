from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import generic
from .models import Post, Comment
from .forms import CommentForm

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
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post,
            )
            comment.save()
            return HttpResponseRedirect(request.path_info)
        
    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
        "form": CommentForm(),
    }

    return render(request, "blog/post_detail.html", context)