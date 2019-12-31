"""
populate database
"""

# standard library
import random
from typing import List

# Django
from django.utils import timezone

# local Django
from apps.article.models import Article
from apps.category.models import Category
from apps.collection.models import Collection
from apps.tag.models import Tag
from apps.theme.models import Theme


def db_populate(tag=0, theme=0, category=0, collection=0, article=0):
    """
    ...
    """
    themes_id: List[int] = []

    for n in range(tag):
        Tag.objects.create(name=f'TEST_TAG_{n}')

    for n in range(theme):
        themes_id.append(
            Theme.objects.create(
                name=f'TEST_THEME_{n}',
                description='test description'
            ).id
        )

    for n in range(category):
        Category.objects.create(name=f'TEST_CATEGORY_{n}')

    for n in range(collection):
        Collection.objects.create(
            name=f'TEST_COLLECTION_{n}',
            description='test description',
            updated=timezone.now(),
            theme_id=random.choice(themes_id),
        )

    for n in range(article):
        Article.objects.create(
            name=f'TEST_ARTICLE_{n}',
            description='test description',
            identifier=f'123{n}',
            author='YSON',
            license='FREE',
            url='https://www.google.com/',
            created='2019-09-21',
        )
