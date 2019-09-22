"""
Fabrica de modelos TAG
"""

# third-party
import factory

# local Django
from apps.tag.models import Tag

class TagFactory(factory.django.DjangoModelFactory):
    name = factory.Sequence(lambda n: 'tag n:{}'.format(n))

    class Meta:
        model = Tag
