from django.contrib import admin
from django.urls import path

from . import views


urlpatterns = [
    path('', views.profiles, name='profiles'),
    path('user/<str:pk>/', views.profile_detail, name='profile-detail'),
]