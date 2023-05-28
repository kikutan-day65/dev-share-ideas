from django.shortcuts import render, redirect

from .models import Profile

def profiles(request):
    profiles = Profile.objects.all()

    context = {
        'profiles': profiles,
    }

    return render(request, 'users/profiles.html', context)