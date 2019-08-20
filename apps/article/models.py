# standard library
import os

# Django
from django.db import models
from django.utils import timezone

# local Django
from apps.collection.models import Collection
from apps.tag.models import Tag

class Article(models.Model):
  name = models.CharField(max_length=100, unique=True)
  description = models.TextField()
  identifier = models.CharField(max_length=255, unique=True)
  author = models.CharField(max_length=100)
  license = models.CharField(max_length=100)
  url = models.URLField(max_length=255, null=True)
  created = models.DateField() 
  timestamp = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(default = timezone.now)
  # relaciones
  tags = models.ManyToManyField(Tag, related_name='tags')
  collections = models.ManyToManyField(Collection, related_name='collections')

  def __str__(self):
    return self.name

  def file_directory(instance, filename):
    """[summary]
    metodo guardar en disco
    Arguments:
      instance {[type]} -- [description]
      filename {[type]} -- [description]
    """
    return os.path.join(
      'repository/'
      + str(instance.theme)
      + '/'
      + str(instance.specification)
      + '/'
      + str(instance.identifier), filename)

  file = models.FileField(upload_to= file_directory, null=True)

class Specification(models.Model):
  name = models.CharField(max_length=100, unique=True)
  description = models.TextField()
  platform = models.CharField(max_length=100, null=True, blank=True)
  installation = models.CharField(max_length=100, null=True, blank=True)
  extension = models.CharField(max_length=100, null=True, blank=True)
  meta = models.TextField(null=True)
  timestamp = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(default = timezone.now)
  article = models.ForeignKey(
    Article,
    related_name='article_specification',
    on_delete=models.PROTECT,
  )

  def __str__(self):
    return self.name