# Django
from django.db import models
from django.utils import timezone

# local Django
from apps.category.models import Category
from apps.tag.models import Tag
from apps.theme.models import Theme

class Collection(models.Model):
  name = models.CharField(max_length=100)
  description = models.TextField()
  timestamp = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(default = timezone.now)
  # relaciones
  theme = models.ForeignKey(Theme, related_name='theme_collection', on_delete=models.PROTECT)
  categories = models.ManyToManyField(Category, related_name='categories_collection')
  tags = models.ManyToManyField(Tag, related_name='tags_collection')
  
  def __str__(self):
    return self.name
