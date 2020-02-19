from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Article(models.Model):
    STATUS_CHOICES = [
        ("draft", "Draft"),
        ("published", "Published"),
    ]
    title = models.CharField(max_length=80)
    slug = models.SlugField(max_length=80)
    content = models.TextField()
    seo_title = models.CharField(max_length=80)
    seo_description = models.CharField(max_length=80)
    authors = models.ManyToManyField(User, related_name="articles")
    date_published = models.DateTimeField(default=timezone.now)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    def __str__(self):
        return self.title

