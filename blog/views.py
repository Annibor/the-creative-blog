from django.shortcuts import render

# Create your views here.
def blog_page(request):
    """
    The blogpage views
    """
    return render(request, 'blog/blog.html')
