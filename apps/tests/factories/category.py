# third-party
import factory

# local Django
from apps.category.models import Category

class CategoryFactory(factory.django.DjangoModelFactory):
	name = factory.Sequence(lambda n: 'category n:{}'.format(n))

  class Meta:
    model = Category