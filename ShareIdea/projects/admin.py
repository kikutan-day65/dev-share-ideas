from django.contrib import admin

from .models import Idea, Tag, Review

admin.site.register(Idea)
admin.site.register(Tag)
admin.site.register(Review)