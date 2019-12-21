"""
Serializers
"""

# standard library
from typing import Tuple

# third-party
from rest_framework import serializers

# local Django
from apps.category.models import Category


class CategorySerializer(serializers.ModelSerializer):
    """
    ...
    """

    class Meta:
        model = Category
        fields: Tuple[str] = ['id', 'name', 'meta', 'timestamp', 'updated']

class CategorySlugSerializer(serializers.ModelSerializer):
    """
    ...
    """
    collection_categories = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )

    class Meta:
        model = Category
        fields: Tuple[str] = ['id', 'name', 'meta', 'timestamp', 'updated', 'collection_categories']
