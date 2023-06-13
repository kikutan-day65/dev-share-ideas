from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Profile, Skill, Message


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
    
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control mb-3'})


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = [
            'name', 'username', 'email',
            'headline', 'bio', 'location',
            'user_image', 'git_link', 'linkedin_link',
            'twitter_link'
        ]

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control mb-3'})


class SkillForm(ModelForm):
    class Meta:
        model = Skill
        fields = [
            'name',
            'description'
        ]

    def __init__(self, *args, **kwargs):
        super(SkillForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control mb-3'})


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = [
            'name',
            'email',
            'subject',
            'body'
        ]
    
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control mb-3'})