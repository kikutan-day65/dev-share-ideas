from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.ideas, name='ideas'),
    path('idea-detail/<str:pk>/', views.idea_detail, name='idea-detail'),

    path('add-idea/', views.add_idea, name='add-idea'),
    path('edit-idea/<str:pk>/', views.edit_idea, name='edit-idea'),
]