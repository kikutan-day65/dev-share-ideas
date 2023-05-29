from django.shortcuts import render, redirect

from .forms import IdeaForm
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


def add_idea(request):
    profile = request.user.profile
    form = IdeaForm()

    if request.method == 'POST':
        form = IdeaForm(request.POST, request.FILES)

        if form.is_valid():
            idea = form.save(commit=False)
            idea.owner = profile
            idea.save()
            return redirect('ideas')

    context = {
        'form': form,
    }

    return render(request, 'projects/idea_form.html', context)