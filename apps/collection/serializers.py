# standard library
import json

# third-party
from rest_framework import serializers

# Django
from django.db import IntegrityError

# local Django
from apps.collection.models import Collection
from apps.theme.models import Theme
from apps.category.models import Category
from apps.tag.models import Tag

from apps.category.serializers import CategorySerializer
from apps.tag.serializers import TagSerializer
from apps.theme.serializers import ThemeSerializer

class CollectionSerializer(serializers.ModelSerializer):
  class Meta:
    model = Collection
    fields = ('id', 'name', 'theme_id', 'description', 'timestamp', 'updated')

class CollectionHeavySerializer(serializers.ModelSerializer):
  theme = ThemeSerializer()
  categories = CategorySerializer(many=True)
  tags = TagSerializer(many=True)

  class Meta:
    model = Collection
    fields = (
      'id', 'name', 'description', 'timestamp', 'updated',
      'theme', 'categories', 'tags',
    )

class CollectionUpdateSerializer(serializers.Serializer):
  name = serializers.CharField(max_length=100)
  description = serializers.CharField(max_length=255)
  updated = serializers.DateTimeField()
  theme = serializers.IntegerField()
  categories = serializers.ListField(
    child=serializers.IntegerField(),
  )
  tags = serializers.ListField(
    child=serializers.IntegerField(),
  )

  def create(self, validated_data):
    try:
      # return validated_data
      theme = Theme.objects.get(id= validated_data['theme'])
      collection = Collection.objects.create(
        name= validated_data['name'],
        description= validated_data['description'],
        updated= validated_data['updated'],
        theme_id= theme.id,
      )

      for category_id in validated_data['categories']:
        category = Category.objects.get(id= category_id)
        collection.categories.add(category)

      for tag_id in validated_data['tags']:
        tag = Tag.objects.get(id= tag_id)
        collection.tags.add(tag)

      return collection
    except IntegrityError as e:
      return str(e)
    except Theme.DoesNotExist as e:
      return str(e)
    except Category.DoesNotExist as e:
      return str(e)
    except Tag.DoesNotExist as e:
      return str(e)
    except Exception as e:
      return str(e)