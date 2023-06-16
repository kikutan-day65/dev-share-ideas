from django.db import models

from users.models import Profile

import uuid

class Idea(models.Model):
    owner = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True, default="idea-default.jpg")
    idea_link = models.CharField(max_length=2000, null=True, blank=True)
    view_total = models.IntegerField(default=0, null=True, blank=True)
    like = models.IntegerField(default=0, null=True, blank=True)
    dislike = models.IntegerField(default=0, null=True, blank=True)
    tags = models.ManyToManyField('Tag', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        primary_key=True,
        editable=False
    )

    @property
    def image_url(self):
        try:
            url = self.image.url
        except:
            url = ''

        return url

    @property
    def reviewers(self):
        queryset = self.review_set.all().values_list('owner_id', flat=True)
        return queryset
    
    @property
    def get_vote_count(self):
        reviews = self.review_set.all()
        like_votes = reviews.filter(value='like').count()
        dislike_votes = reviews.filter(value='dislike').count()

        self.like = like_votes
        self.dislike = dislike_votes

        self.save()
    
    @property
    def view_count(self):
        self.view_total += 1
        self.save()

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-like', 'title', '-created']


class Review(models.Model):
    VOTE_TYPE = (
        ('like', 'like'),
        ('dislike', 'dislike')
    )
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    idea = models.ForeignKey(Idea, on_delete=models.CASCADE)
    body = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=200, choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        primary_key=True,
        editable=False
    )

    class Meta:
        unique_together = [
            ['owner', 'idea']
        ]
    
    def __str__(self):
        return self.value
    

class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        primary_key=True,
        editable=False
    )

    def __str__(self):
        return self.name