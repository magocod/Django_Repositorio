"""
Modelos
"""

# Django
from django.db import models
from django.utils import timezone


class Category(models.Model):
    """
    ...
    """
    name = models.CharField(max_length=40, unique=True)
    meta = models.TextField(null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(default=timezone.now)
