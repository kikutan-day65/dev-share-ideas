from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .models import Profile
from .forms import CustomUserCreationForm, ProfileForm, SkillForm
from .utils import search_profiles, paginate_users


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
            return redirect('account')
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
    profiles, search_query = search_profiles(request)
    custom_range, profiles = paginate_users(request, profiles, 6)

    context = {
        'profiles': profiles,
        'search_query': search_query,
        'custom_range': custom_range,
    }

    return render(request, 'users/profiles.html', context)


def profile_detail(request, pk):
    detail = Profile.objects.get(id=pk)
    skills = detail.skill_set.all()

    context = {
        'detail': detail,
        'skills': skills,
    }

    return render(request, 'users/profile_detail.html', context)


@login_required(login_url='login')
def user_account(request):
    profile = request.user.profile
    skills = profile.skill_set.all()

    context = {
        'profile': profile,
        'skills': skills,
    }

    return render(request, 'users/account.html', context)


@login_required(login_url='login')
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


@login_required(login_url='login')
def add_skill(request):
    profile = request.user.profile
    form = SkillForm()

    if request.method == 'POST':
        form = SkillForm(request.POST)

        if form.is_valid():
            skill = form.save(commit=False)
            skill.owner = profile
            skill.save()

            messages.success(request, 'Skill was added successfully!')
            return redirect('account')

    context = {
        'form': form,
    }

    return render(request, 'users/skill_form.html', context)