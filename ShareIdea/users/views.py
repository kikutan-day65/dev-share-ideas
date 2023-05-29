from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.models import User

from .models import Profile


def login_user(request):
    page = 'login'

    context = {
        'page': page
    }

    if request.user.is_authenticated:
        return redirect('profiles')
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Username does not exist')
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Logged in successfully!')
            return redirect('profiles')
        else:
            messages.error(request, 'Username OR password is incorrect')

    return render(request, 'users/login_register.html', context)


def logout_user(request):
    logout(request)
    messages.info(request, 'You are logged out!')
    return redirect('login')


def profiles(request):
    profiles = Profile.objects.all()

    context = {
        'profiles': profiles,
    }

    return render(request, 'users/profiles.html', context)


def profile_detail(request, pk):
    detail = Profile.objects.get(id=pk)

    context = {
        'detail': detail,
    }

    return render(request, 'users/profile_detail.html', context)