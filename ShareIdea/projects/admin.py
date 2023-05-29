from django.contrib import admin

from .models import Idea, Tags

admin.site.register(Idea)
admin.site.register(Tags)