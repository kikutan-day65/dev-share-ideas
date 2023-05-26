from django.shortcuts import render, redirect

from .models import Idea

def projects(request):
    ideas = Idea.objects.all()    

    context = {
        'ideas': ideas,
    }

    return render(request, 'projects/projects.html', context)