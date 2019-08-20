# third-party
from rest_framework import serializers

# Django
from django.db import IntegrityError

# local Django
from apps.article.models import Specification

class SpecificationSerializer(serializers.ModelSerializer):
  article_id = serializers.IntegerField(read_only=False)

  class Meta:
    model = Specification
    fields = (
      'id', 'name', 'description', 'timestamp', 'updated',
      'platform', 'installation', 'extension', 'meta', 'article_id',
    )
