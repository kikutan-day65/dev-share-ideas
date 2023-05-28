from django.shortcuts import render, redirect

from .models import Profile


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