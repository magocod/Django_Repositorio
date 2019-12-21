"""
Fabrica de modelos articulos
"""

# third-party
import factory

# local Django
from apps.article.models import Article

# from apps.collection.models import Collection
# from apps.tag.models import Tag

class ArticleFactory(factory.django.DjangoModelFactory):
    """
    Fabrica
    """
    name = factory.Sequence(lambda n: 'article n:{}'.format(n))
    description = '---'
    identifier = factory.Sequence(lambda n: '1234{}'.format(n))
    author = '---'
    license = '---'
    url = factory.Sequence(lambda n: 'https://www.google.com/{}'.format(n))
    created = '2019-10-10'

    class Meta:
        """
        Metadatos
        """
        model = Article

    # @factory.post_generation
    # def relations(self, create, extracted, **kwargs):
    #     if not create:
    #         return
        # else:
            # collection.collections.add(category)
            # collection.tags.add(category)
            # pass
