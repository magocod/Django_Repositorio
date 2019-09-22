"""
Fabrica de modelos Theme
"""

# third-party
import factory

# local Django
from apps.theme.models import Theme

class ThemeFactory(factory.django.DjangoModelFactory):
	"""
	Fabrica
	"""
	name = factory.Sequence(lambda n: 'theme n:{}'.format(n))
	description = '---'

	class Meta:
		"""
		Metadatos
		"""
	    model = Theme