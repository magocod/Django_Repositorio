"""
Poblacion base de dato pruebas
"""

# standard library
from typing import Dict

# Django
from django.utils import timezone

# local Django
from apps.article.models import Article
from apps.category.models import Category
from apps.collection.models import Collection
from apps.tag.models import Tag
from apps.theme.models import Theme

def db_populate(**kwargs: Dict[str, int]) -> None:
    """[summary]
    creacion basica en bd (1 un elemento)
    Nota: colocar en ultimo lugar objetos relacionados (...., collection, article)

    Arguments:
      **kwargs {[type]} -- [description]
    """
    for key, value in kwargs.items():
        if key == 'tag' and value > 0:
            Tag.objects.create(name='TEST_TAG')
        elif key == 'theme' and value > 0:
            Theme.objects.create(name='TEST_THEME', description='test description')
        elif key == 'category' and value > 0:
            Category.objects.create(name='TEST_CATEGORY')
        elif key == 'collection' and value > 0:

            if Theme.objects.count() > 0:
                pass
            else:
                print('generate theme -> set -> collection')
                Theme.objects.create(name='TEST_THEME_RELATION', description='test description')

            Collection.objects.create(
                name='TEST_COLLECTION',
                description='test description',
                updated=timezone.now(),
                theme_id=1,
            )
        elif key == 'article' and value > 0:
            Article.objects.create(
                name='TEST_ARTICLE',
                description='test description',
                identifier='123',
                author='YSON',
                license='FREE',
                url='https://www.google.com/',
                created='2019-09-21',
            )
        else:
            print('model no exist')
