# third-party
import factory

# local Django
from apps.theme.models import Theme

class ThemeFactory(factory.django.DjangoModelFactory):
	name = factory.Sequence(lambda n: 'theme n:{}'.format(n))
	description = '---'

  class Meta:
    model = Theme