from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.ideas, name='ideas'),
    path('idea-detail/<str:pk>/', views.idea_detail, name='idea-detail'),
]