from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.views import generic
from .models import Post
from .forms import CommentForm

#from .models import Post, Comment
#from .forms import CommentForm

# Create your views here.
#def blog_page(request):
   # """
   # The blog page view
   # """
  #  return render(request, 'blog/blog.html')

def blog_post_index(request):
    """
    Display a lis tof all blog posts.
    
    Retrives all blog posts from database & orders them by date they were written.
    Renders the 'blog/blog.html' tempalte with the list of posts in the context.
    
    Parameters:
    request (HttpRequest): The HTTP request object.
    
    Returns: 
    HttpResponse: Rendered HTML page displaying the list of blog posts.
    """
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
    post = get_object_or_404(Post, pk=pk)
    form = CommentForm()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.approved = False
            comment.save()
            messages.success(request, 'Comment submitted and awaiting approval')
            return HttpResponseRedirect(request.path_info)

    comments = post.comments.all().order_by("-created_on")
    context = {
        "post": post,
        "comments": comments,
        "comment_form": form,
    }
    return render(request, "blog/post_detail.html", context)
