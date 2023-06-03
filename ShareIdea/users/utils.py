from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from .models import Profile, Skill


def search_profiles(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    skills = Skill.objects.filter(name__icontains=search_query)

    profiles = Profile.objects.distinct().filter(
        Q(name__icontains=search_query) |
        Q(headline__icontains=search_query) |
        Q(location__icontains=search_query) |
        Q(skill__in=skills)
    )

    return profiles, search_query


def paginate_users(request, users, results):

    page = request.GET.get('page')
    paginator = Paginator(users, results)

    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        users = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        users = paginator.page(page)

    left_index = (int(page) - 4)

    if left_index < 1:
        left_index = 1
    
    right_index = (int(page) + 5)

    if right_index > paginator.num_pages:
        right_index = paginator.num_pages + 1

    custom_range = range(left_index, right_index)


    return custom_range, users