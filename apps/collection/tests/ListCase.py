"""
Pruebas Listar Collection
"""

# standard library
import json

# third-party
from rest_framework.test import APIClient

# Django
from django.test import TestCase

# local Django
from apps.collection.models import Collection
from apps.collection.serializers import CollectionHeavySerializer
from apps.tests.auth import create_user
from apps.tests.db import db_populate

class ListTest(TestCase):
  """
  ...
  """
  serializer = CollectionHeavySerializer

  def setUp(self):
    # user an token
    auth = create_user(True)
    self.client = APIClient()
    self.client.credentials(HTTP_AUTHORIZATION= 'Token ' + auth['token'].key)
    # no authenticated
    self.noauthclient = APIClient()
    self.noauthclient.credentials(HTTP_AUTHORIZATION= 'Token ' + '123')
    # data
    db_populate(theme=1, category=1, collection=1)

  def test_get_all(self):
    response = self.client.get('/api/collections/')
    response_data = json.loads(response.content)
    serializer = self.serializer(
      Collection.objects.all(),
      many= True,
    )
    self.assertEqual(response.status_code, 200)
    # self.assertEqual(serializer.data, response_data)

  def test_get_all_authenticated(self):
    response = self.noauthclient.get('/api/collections/')
    self.assertEqual(response.status_code, 401)
