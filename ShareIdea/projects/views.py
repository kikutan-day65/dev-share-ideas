from django.shortcuts import render, redirect

from .models import Idea

def ideas(request):
    ideas = Idea.objects.all()    

    context = {
        'ideas': ideas,
    }

    return render(request, 'projects/ideas.html', context)


def idea_detail(request, pk):
    detail = Idea.objects.get(id=pk)
    
    context = {
        'detail': detail,
    }

    return render(request, 'projects/idea_detail.html', context)