from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import IdeaForm, ReviewForm
from .models import Idea
from .utils import search_ideas


def ideas(request):
    ideas, search_query = search_ideas(request) 

    context = {
        'ideas': ideas,
        'search_query': search_query,
    }

    return render(request, 'projects/ideas.html', context)


def idea_detail(request, pk):
    detail = Idea.objects.get(id=pk)
    form = ReviewForm()

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        review = form.save(commit=False)
        review.idea = detail
        review.owner = request.user.profile
        review.save()

        detail.get_vote_count

        messages.success(request, 'Your review was successfully submitted!')

        return redirect('idea-detail', pk=detail.id)
        
    context = {
        'detail': detail,
        'form': form
    }

    return render(request, 'projects/idea_detail.html', context)


@login_required(login_url='login')
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


@login_required(login_url='login')
def edit_idea(request, pk):
    idea = Idea.objects.get(id=pk)
    form = IdeaForm(instance=idea)

    if request.method == 'POST':
        form = IdeaForm(request.POST, request.FILES, instance=idea)

        if form.is_valid():
            form.save()
            return redirect('ideas')
    
    context = {
        'form': form
    }

    return render(request, 'projects/idea_form.html', context)


@login_required(login_url='login')
def delete_idea(request, pk):
    idea = Idea.objects.get(id=pk)

    if request.method == 'POST':
        idea.delete()
        return redirect('ideas')

    context = {
        'deleteObj': idea
    }    
    
    return render(request, 'delete_form.html', context)