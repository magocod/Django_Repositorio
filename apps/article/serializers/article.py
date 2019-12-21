# third-party
# Django
from django.db import IntegrityError
from rest_framework import serializers

# local Django
from apps.article.models import Article
from apps.article.serializers.specification import SpecificationSerializer
from apps.collection.models import Collection
from apps.collection.serializers import CollectionSerializer
from apps.tag.models import Tag
from apps.tag.serializers import TagSerializer


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

class ArticleRelationSerializer(serializers.Serializer):
  article_id = serializers.IntegerField()
  collections = serializers.ListField(
    child=serializers.IntegerField(),
  )
  tags = serializers.ListField(
    child=serializers.IntegerField(),
  )

  def create(self, validated_data):
    try:
      # return validated_data
      article = Article.objects.get(pk= validated_data['article_id'])

      for collection_id in validated_data['collections']:
        collection = Collection.objects.get(pk= collection_id)
        article.collections.add(collection)

      for tag_id in validated_data['tags']:
        tag = Tag.objects.get(pk= tag_id)
        article.tags.add(tag)

      return article
    except IntegrityError as e:
      return str(e)
    except Collection.DoesNotExist as e:
      return str(e)
    except Tag.DoesNotExist as e:
      return str(e)
    except Exception as e:
      return str(e)
