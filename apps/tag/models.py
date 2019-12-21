"""
Modelos
"""

# Django
from django.db import models
from django.utils import timezone


class Tag(models.Model):
    """
    Palabras clave ubicar colecciones y articulos
    """
    name = models.CharField(max_length=100, unique=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
