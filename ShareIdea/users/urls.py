from django.contrib import admin
from django.urls import path

from . import views


urlpatterns = [
    path('', views.profiles, name='profiles'),
    path('user/<str:pk>/', views.profile_detail, name='profile-detail'),

    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),

    path('account/', views.user_account, name='account'),
    path('edit-account/', views.edit_account, name='edit-account'),

    path('add-skill/', views.add_skill, name='add-skill'),
    path('delete-skill/<str:pk>/', views.delete_skill, name='delete-skill'),
]