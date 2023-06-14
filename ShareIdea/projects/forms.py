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
            # 'tags'
        ]

        # widgets = {
        #     'tags': forms.CheckboxSelectMultiple()
        # }

    def __init__(self, *args, **kwargs):
        super(IdeaForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control mb-3'})


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