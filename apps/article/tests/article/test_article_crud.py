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

class ArticleCrudTest(TestCase):
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
    db_populate(article=1)

  def test_create_article(self):
    data = {
      'name': 'YSON',
      'description': '---',
      'identifier' : '1234',
      'author': 'YSON',
      'license': 'ls',
      'url': 'https://www.google.com',
      'created': '2019-09-19',
    }
    response = self.client.post('/api/articles/', data)
    # print(response.data)
    # print(response)
    serializer = self.serializer(
      Article.objects.get(id =response.data['id']),
    )
    self.assertEqual(response.status_code, 201)
    self.assertEqual(serializer.data, response.data)

  def test_create_error_params(self):
    data = {
      'name': 'YSON',
      'description': '---',
      'updated': '2019-09-19',
    }
    response = self.client.post('/api/collections/', data)
    self.assertEqual(response.status_code, 400)

  def test_create_error_duplicate(self):
    data = {
      'name': 'TEST_ARTICLE',
      'description': '---',
      'updated': '2019-09-19',
    }
    response = self.client.post('/api/articles/', data)
    self.assertEqual(response.status_code, 400)
  
  def test_get_collection(self):
    response  = self.client.get('/api/article/' + str(1) + '/')
    # print(response.data)
    serializer = self.serializer(
      Article.objects.get(id= response.data['id'])
    )
    self.assertEqual(response.status_code, 200)
    self.assertEqual(serializer.data, response.data)
  
  def test_update_collection(self):
    collection = Article.objects.get(id= 1)
    oldvalues = self.serializer(collection)
    newdata = {
      'name': 'UPDATED',
      'description': '---',
      'identifier' : '1234',
      'author': 'YSON',
      'license': 'ls',
      'url': 'https://www.google.com',
      'created': '2019-09-19',
    }
    response = self.client.put('/api/article/' + str(1) + '/', newdata)
    # print(response.data)
    newvalues = self.serializer(
      Article.objects.get(id= 1)
    )
    self.assertEqual(response.status_code, 200)
    self.assertNotEqual(newvalues.data, oldvalues.data)
    self.assertEqual(newvalues.data, response.data)

  def test_delete_collection(self):
    response = self.client.delete('/api/article/' + str(1) + '/')
    self.assertEqual(response.status_code, 204)