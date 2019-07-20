# third-party
from rest_framework import serializers

# Django
from apps.tag.models import Tag

class TagSerializer(serializers.ModelSerializer):
  class Meta:
    model = Tag
    fields = ('id', 'name', 'timestamp', 'updated')