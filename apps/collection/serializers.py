# standard library
# import json

# Django
from django.db import IntegrityError
# third-party
from rest_framework import serializers

from apps.category.models import Category
from apps.category.serializers import CategorySerializer
# local Django
from apps.collection.models import Collection
from apps.tag.models import Tag
from apps.tag.serializers import TagSerializer
# from apps.theme.models import Theme
from apps.theme.serializers import ThemeSerializer


class CollectionSerializer(serializers.ModelSerializer):
    theme_id = serializers.IntegerField(read_only=False)

    class Meta:
        model = Collection
        fields = (
            'id', 'name', 'theme_id',
            'description', 'timestamp', 'updated'
        )


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


class CollectionRelationSerializer(serializers.Serializer):
    collection_id = serializers.IntegerField()
    categories = serializers.ListField(
        child=serializers.IntegerField(),
    )
    tags = serializers.ListField(
        child=serializers.IntegerField(),
    )

    def create(self, validated_data):
        try:

            collection = Collection.objects.get(
                id=validated_data['collection_id']
            )

            for category_id in validated_data['categories']:
                category = Category.objects.get(id=category_id)
                collection.categories.add(category)

            for tag_id in validated_data['tags']:
                tag = Tag.objects.get(id=tag_id)
                collection.tags.add(tag)

            return collection
        except IntegrityError as e:
            return str(e)
        except Collection.DoesNotExist as e:
            return str(e)
        except Category.DoesNotExist as e:
            return str(e)
        except Tag.DoesNotExist as e:
            return str(e)
        except Exception as e:
            return str(e)


class CollectionSlugSerializer(serializers.ModelSerializer):
    theme = ThemeSerializer()
    categories = CategorySerializer(many=True)
    tags = TagSerializer(many=True)

    article_collections = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )

    class Meta:
        model = Collection
        fields = (
            'id', 'name', 'description', 'timestamp', 'updated',
            'theme', 'categories', 'tags', 'article_collections',
        )
