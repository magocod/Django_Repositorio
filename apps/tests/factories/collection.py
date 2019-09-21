# third-party
import factory

# local Django
from apps.collection.models import Collection
from apps.tag.models import Tag
from apps.theme.models import Theme

class CollectionFactory(factory.django.DjangoModelFactory):
	name = factory.Sequence(lambda n: 'category n:{}'.format(n))
	description = '---'
	theme = factory.Iterator(Theme.objects.all())

  class Meta:
    model = Collection

  @factory.post_generation
  def relations(self, create, extracted, **kwargs):
    if not create:
      return
    else:
      # collection.categories.add(category)
      # collection.tags.add(category)
      pass