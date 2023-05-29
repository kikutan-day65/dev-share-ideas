from django.forms import ModelForm
from django import forms

from .models import Idea


class IdeaForm(ModelForm):
    class Meta:
        model = Idea
        fields = [
            'title',
            'description',
            'image',
            'idea_link',
            'tags'
        ]

        widgets = {
            'tags': forms.CheckboxSelectMultiple()
        }