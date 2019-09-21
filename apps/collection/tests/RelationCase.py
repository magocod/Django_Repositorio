# standard library
# import json

# third-party
from rest_framework.test import APIClient

# Django
from django.test import TestCase

# local Django
from apps.collection.models import Collection
from apps.collection.serializers import CollectionHeavySerializer
from apps.tests.auth import create_user
from apps.tests.db import DBpopulate

class CRUDTest(TestCase):

  def setUp(self):
    # user an token
    auth = create_user(True)
    self.client = APIClient()
    self.client.credentials(HTTP_AUTHORIZATION= 'Token ' + auth['token'].key)
    # data
    DBpopulate(tag= 1, category= 1, collection= 1)

  def test_collection_add_relations(self):
    oldvalues = CollectionHeavySerializer(
      Collection.objects.get(id= 1)
    )
    relationdata = {
      'collection_id': 1,
      'categories': [1],
      'tags': [1],
    }
    response = self.client.put('/api/collection/relations/' + str(1) + '/', relationdata)
    # print(response.data)
    newvalues = CollectionHeavySerializer(
      Collection.objects.get(id= 1)
    )
    self.assertEqual(response.status_code, 200)
    # self.assertNotEqual(newvalues.data['tags'], oldvalues.data['tags'])
    # self.assertNotEqual(newvalues.data['categories'], oldvalues.data['categories'])
    self.assertEqual(newvalues.data, response.data)

  def test_collection_remove_relations(self):
    relationdata = {
      'collection_id': 1,
      'categories': [1],
      'tags': [1],
    }
    response = self.client.put('/api/collection/relations/' + str(1) + '/', relationdata)
    oldvalues = CollectionHeavySerializer(
      Collection.objects.get(id= 1)
    )
    response = self.client.delete('/api/collection/relations/' + str(1) + '/', relationdata)
    # print(response.data)
    newvalues = CollectionHeavySerializer(
      Collection.objects.get(id= 1)
    )
    self.assertEqual(response.status_code, 200)
    # self.assertNotEqual(newvalues.data['tags'], oldvalues.data['tags'])
    # self.assertNotEqual(newvalues.data['categories'], oldvalues.data['categories'])
    self.assertEqual(newvalues.data, response.data)