from django.db import models

from crawler.core.models import TimeStampedModel


class Review(TimeStampedModel):
    """Entity that represents a google play store app review."""

    id = models.CharField(primary_key=True, max_length=100)
    user_name = models.CharField(max_length=40)
    content = models.TextField()
    score = models.IntegerField()
