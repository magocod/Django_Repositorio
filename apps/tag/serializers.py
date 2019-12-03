"""
Serializadores
"""

# standard library
from typing import Tuple

# third-party
from rest_framework import serializers

# Django
from apps.tag.models import Tag

class TagSerializer(serializers.ModelSerializer):
    """
    Serializador basico tag
    """
    class Meta:
        model = Tag
        fields: Tuple[str] = ('id', 'name', 'timestamp', 'updated')
