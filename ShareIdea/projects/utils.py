from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from .models import Idea, Tag


def search_ideas(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
    
    tags = Tag.objects.filter(name__icontains=search_query)

    ideas = Idea.objects.distinct().filter(
        Q(title__icontains=search_query) |
        Q(description__icontains=search_query) |
        Q(owner__name__icontains=search_query) |
        Q(tags__in=tags)
    )

    return ideas, search_query


def paginate_ideas(request, ideas, results):

    page = request.GET.get('page')
    paginator = Paginator(ideas, results)

    try:
        ideas = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        ideas = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        ideas = paginator.page(page)

    left_index = (int(page) - 4)

    if left_index < 1:
        left_index = 1
    
    right_index = (int(page) + 5)

    if right_index > paginator.num_pages:
        right_index = paginator.num_pages + 1

    custom_range = range(left_index, right_index)


    return custom_range, ideas