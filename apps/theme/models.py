from django.db import models
from django.utils import timezone

class Theme(models.Model):
  name = models.CharField(max_length=100, unique=True)
  description = models.TextField(max_length=600)
  meta = models.TextField(null=True)
  timestamp = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(default = timezone.now)

  def __str__(self):
      return self.name
