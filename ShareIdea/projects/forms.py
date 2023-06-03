from django.forms import ModelForm
from django import forms

from .models import Idea, Review, Tag


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


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = [
            'value',
            'body'
        ]

        labels = {
            'value': 'Like / Dislike',
            'body': 'Add a comment with your vote'
        }


class TagForm(ModelForm):
    class Meta:
        model = Tag
        fields = [
            'name'
        ]

        label = {
            'name': 'new tag'
        }