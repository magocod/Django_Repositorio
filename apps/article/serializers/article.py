# third-party
from rest_framework import serializers

# Django
from django.db import IntegrityError

# local Django
from apps.article.models import Article

from apps.tag.serializers import TagSerializer
from apps.collection.serializers import CollectionSerializer
from apps.article.serializers.specification import SpecificationSerializer

class ArticleSerializer(serializers.ModelSerializer):
  class Meta:
    model = Article
    fields = (
      'id', 'name', 'description', 'timestamp', 'updated',
      'identifier', 'author', 'license', 'url', 'created',
    )

class ArticleHeavySerializer(serializers.ModelSerializer):
  article_specification = SpecificationSerializer()
  collections = CollectionSerializer(many=True)
  tags = TagSerializer(many=True)

  class Meta:
    model = Article
    fields = (
      'id', 'name', 'description', 'timestamp', 'updated',
      'identifier', 'author', 'license', 'url', 'created',
      'tags', 'collections', 'article_specification',
    )