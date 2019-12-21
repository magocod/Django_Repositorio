"""
Fabrica de modelos TAG
"""

# third-party
import factory

# local Django
from apps.tag.models import Tag


class TagFactory(factory.django.DjangoModelFactory):
	"""
	Fabrica
	"""
    name = factory.Sequence(lambda n: 'tag n:{}'.format(n))

    class Meta:
    	"""
    	Metadatos
    	"""
        model = Tag
