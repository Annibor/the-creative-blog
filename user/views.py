from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import RegisterUserForm


# Create your views here.
def user_login(request):
    """
    User login view for logging in users.
    """
    if request.user.is_authenticated:
        return redirect('home:index')

    if request. method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f'You are logged in as {username}')
                return redirect('home:index')

    else:
        messages.error(request, "Invalid username or password.")
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})


def user_register(request):
    """
    Register view for registering new users.
    """
    if request.user.is_authenticated():
        return redirect('home:index')
    
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Your registration was successful!')
            return redirect('home:index')
    else:
        messages.error(
            request, "Your registration failed. Please put it valid information."
        )
        form = RegisterUserForm()

    return render(request, 'register.html', {'form': form})

def user_logout(request):
    """
    Logout view for users to log out from website.
    """
    if request.user.is_authenticated:
        logout(request)
        messages.info(request, 'You have been logged out!')
    return redirect('home:index')
