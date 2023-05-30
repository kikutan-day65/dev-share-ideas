from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Profile


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'username',
            'email',
            'password1',
            'password2',
        ]

        labels = {
            'first_name': 'Name',
        }


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = [
            'name', 'username', 'email',
            'headline', 'bio', 'location',
            'user_image', 'git_link', 'linkedin_link',
            'twitter_link'
        ]