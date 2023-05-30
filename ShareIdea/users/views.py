from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.models import User

from .models import Profile
from .forms import CustomUserCreationForm, ProfileForm


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


def register_user(request):
    page = 'register'
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, 'User account was created!')

            login(request, user)
            return redirect('edit-account')
        
        else:
            messages.error(request, 'Ann error has occurred during registration')

    context = {
        'page': page,
        'form': form
    }

    return render(request, 'users/login_register.html', context)


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


def user_account(request):
    profile = request.user.profile

    context = {
        'profile': profile,
    }

    return render(request, 'users/account.html', context)


def edit_account(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)

        if form.is_valid():
            form.save()
            return redirect('account')


    context = {
        'form': form,
    }

    return render(request, 'users/profile_form.html', context)