# third-party
from rest_framework import serializers

# local Django
from apps.category.models import Category

class CategorySerializer(serializers.ModelSerializer):
  class Meta:
    model = Category
    fields = ['id', 'name', 'meta', 'timestamp', 'updated']
