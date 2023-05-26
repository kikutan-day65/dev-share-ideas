from django.shortcuts import render, redirect


def projects(request):

    context = {

    }

    return render(request, 'projects/projects.html', context)