from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import IdeaForm, ReviewForm, TagForm
from .models import Idea, Tag
from .utils import search_ideas, paginate_ideas


def ideas(request):
    ideas, search_query = search_ideas(request)
    custom_range, ideas = paginate_ideas(request, ideas, 8)

    context = {
        'ideas': ideas,
        'search_query': search_query,
        'custom_range': custom_range,
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
    
    detail.view_count

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
        new_tags = request.POST.get('new_tags').replace(',', ' ').split()

        if form.is_valid():
            idea = form.save(commit=False)
            idea.owner = profile
            idea.save()

            for tag in new_tags:
                tag, created = Tag.objects.get_or_create(name=tag)
                idea.tags.add(tag)

            return redirect('ideas')

    context = {
        'form': form,
    }

    return render(request, 'projects/idea_form.html', context)


@login_required(login_url='login')
def edit_idea(request, pk):
    profile = request.user.profile
    idea = Idea.objects.get(id=pk)
    form = IdeaForm(instance=idea)

    if request.method == 'POST':
        form = IdeaForm(request.POST, request.FILES, instance=idea)
        new_tags = request.POST.get('new_tags').replace(',', ' ').split()

        if form.is_valid():
            form.save()

            for tag in new_tags:
                tag, created = Tag.objects.get_or_create(name=tag)
                idea.tags.add(tag)

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
        return redirect('account')

    context = {
        'deleteObj': idea
    }    
    
    return render(request, 'delete_form.html', context)\


@login_required(login_url='login')
def create_tag(request):
    form = TagForm()
    
    if request.method == 'POST':
        form = TagForm(request.POST)
        form.save()

        return redirect('ideas')
    
    context = {
        'form': form
    }

    return render(request, 'projects/tag_form.html', context)