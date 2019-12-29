# Django
from django.db import models
from django.utils import timezone

# local Django
from apps.category.models import Category
from apps.tag.models import Tag
from apps.theme.models import Theme


class Collection(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(default=timezone.now)
    # relaciones
    theme = models.ForeignKey(
        Theme,
        related_name='collection_theme',
        on_delete=models.PROTECT
    )
    categories = models.ManyToManyField(
        Category,
        related_name='collection_categories'
    )
    tags = models.ManyToManyField(
        Tag,
        related_name='collection_tags'
    )

    def __str__(self):
        return self.name
