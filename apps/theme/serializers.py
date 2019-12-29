"""
Serializadores
"""

# standard library
from typing import Tuple

# third-party
from rest_framework import serializers

# Django
from apps.theme.models import Theme


class ThemeSerializer(serializers.ModelSerializer):
    """
    ...
    """
    class Meta:
        model = Theme
        fields: Tuple[str] = (
            'id', 'name', 'description',
            'meta', 'timestamp', 'updated',
        )
