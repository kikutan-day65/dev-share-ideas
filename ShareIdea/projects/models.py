from django.db import models

import uuid

class Idea(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    # image = 
    idea_link = models.CharField(max_length=2000, null=True, blank=True)
    view_total = models.IntegerField(default=0, null=True, blank=True)
    like = models.IntegerField(default=0, null=True, blank=True)
    # tags =
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        primary_key=True,
        editable=False
    )

    def __str__(self):
        return self.title