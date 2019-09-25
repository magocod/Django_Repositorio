# standard library
# import json

# third-party
from rest_framework.test import APIClient

# Django
from django.test import TestCase

# local Django
from apps.article.models import Article
from apps.article.serializers.article import ArticleHeavySerializer
from apps.tests.auth import create_user
from apps.tests.db import db_populate

class RelationTest(TestCase):
  """
  ...
  """
  serializer = ArticleHeavySerializer

  def setUp(self):
    # user an token
    auth = create_user(True)
    self.client = APIClient()
    self.client.credentials(HTTP_AUTHORIZATION= 'Token ' + auth['token'].key)
    # data
    db_populate(tag=1, theme=1, collection=1, article=1)

  def test_add_relations(self):
    oldvalues = self.serializer(
      Article.objects.get(id= 1)
    )
    relationdata = {
      'article_id': 1,
      'collections': [1],
      'tags': [1],
    }
    response = self.client.put('/api/article/relations/' + str(1) + '/', relationdata)
    # print(response.data)
    newvalues = self.serializer(
      Article.objects.get(id= 1)
    )
    self.assertEqual(response.status_code, 200)
    # self.assertNotEqual(newvalues.data['tags'], oldvalues.data['tags'])
    # self.assertNotEqual(newvalues.data['collections'], oldvalues.data['collections'])
    self.assertEqual(newvalues.data, response.data)

  def test_remove_relations(self):
    relationdata = {
      'article_id': 1,
      'collections': [1],
      'tags': [1],
    }
    response = self.client.put('/api/article/relations/' + str(1) + '/', relationdata)
    oldvalues = self.serializer(
      Article.objects.get(id= 1)
    )
    response = self.client.delete('/api/article/relations/' + str(1) + '/', relationdata)
    # print(response.data)
    newvalues = self.serializer(
      Article.objects.get(id= 1)
    )
    self.assertEqual(response.status_code, 200)
    # self.assertNotEqual(newvalues.data['tags'], oldvalues.data['tags'])
    # self.assertNotEqual(newvalues.data['collections'], oldvalues.data['collections'])
    self.assertEqual(newvalues.data, response.data)