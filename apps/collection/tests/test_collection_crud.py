"""
Pruebas edicion Collection
"""

# standard library
# import json

# Django
from django.test import TestCase
# third-party
from rest_framework.test import APIClient

# local Django
from apps.collection.models import Collection
from apps.collection.serializers import CollectionHeavySerializer
from apps.tests.auth import create_user
from apps.tests.db import db_populate


class CollectionCrudTest(TestCase):
  """
  ...
  """
  serializer = CollectionHeavySerializer

  def setUp(self):
    # user an token
    auth = create_user(True)
    self.client = APIClient()
    self.client.credentials(HTTP_AUTHORIZATION= 'Token ' + auth['token'].key)
    # data
    db_populate(theme=1, category=1, collection=1)

  def test_create_collection(self):
    data = {
      'name': 'YSON',
      'description': '---',
      'updated': '2019-09-19 10:00:00',
      'theme_id': 1,
    }
    response = self.client.post('/api/collections/', data)
    # print(response)
    serializer = self.serializer(
      Collection.objects.get(id=response.data['id']),
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
      'name': 'TEST',
      'description': '---',
      'updated': '2019-09-19',
    }
    response = self.client.post('/api/collections/', data)
    self.assertEqual(response.status_code, 400)
  
  def test_get_collection(self):
    response  = self.client.get('/api/collection/' + str(1) + '/')
    serializer = self.serializer(
      Collection.objects.get(id= response.data['id'])
    )
    self.assertEqual(response.status_code, 200)
    self.assertEqual(serializer.data, response.data)
  
  def test_update_collection(self):
    collection = Collection.objects.get(id= 1)
    oldvalues = self.serializer(collection)
    newdata = {
      'name': 'YSON2',
      'description': 'updated',
      'theme_id': 1,
    }
    response = self.client.put('/api/collection/' + str(1) + '/', newdata)
    # print(response.data)
    newvalues = self.serializer(
      Collection.objects.get(id= 1)
    )
    self.assertEqual(response.status_code, 200)
    self.assertNotEqual(newvalues.data, oldvalues.data)
    self.assertEqual(newvalues.data, response.data)

  def test_delete_collection(self):
    response = self.client.delete('/api/collection/' + str(1) + '/')
    self.assertEqual(response.status_code, 204)
