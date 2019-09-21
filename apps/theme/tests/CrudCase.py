# standard library
import json

# third-party
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token

# Django
from django.test import Client, TestCase
from django.contrib.auth.models import User

# local Django
from apps.theme.models import Theme
from apps.theme.serializers import ThemeSerializer
from apps.tests.auth import create_user
from apps.tests.db import DBpopulate

class CRUDTest(TestCase):

  def setUp(self):
    # user an token
    auth = create_user(True)
    self.client = APIClient()
    self.client.credentials(HTTP_AUTHORIZATION= 'Token ' + auth['token'].key)
    # data
    # self.theme = Theme.objects.create(name= 'test', description= ' test description')
    DBpopulate(theme= 1)

  def test_create_theme(self):
    data = {
      'name': 'test create',
      'description' : 'test create description'
    }
    response = self.client.post('/api/themes/', data)
    response_data = json.loads(response.content)
    serializer = ThemeSerializer(
      Theme.objects.get(id = response_data['id']),
    )
    self.assertEqual(response.status_code, 201)
    self.assertEqual(serializer.data, response_data)

  def test_create_error_params(self):
    data = {
      'name': 'test create',
    }
    response = self.client.post('/api/themes/', data)
    self.assertEqual(response.status_code, 400)

  def test_create_error_duplicate(self):
    data = {
      'name': 'TEST_THEME',
      'description' : 'test create duplicate'
    }
    response = self.client.post('/api/themes/', data)
    self.assertEqual(response.status_code, 400)

  def test_get_theme(self):
    response  = self.client.get('/api/theme/' + str(1) + '/')
    serializer = ThemeSerializer(
      Theme.objects.get(id= 1)
    )
    self.assertEqual(response.status_code, 200)
    self.assertEqual(serializer.data, response.data)
  
  def test_update_theme(self):
    theme = Theme.objects.get(id= 1)
    oldvalues = ThemeSerializer(theme)
    newdata = {
      'name': 'test update',
      'description' : 'test update description'
    }
    response = self.client.put('/api/theme/' + str(1) + '/', newdata)
    self.assertEqual(response.status_code, 200)
    self.assertNotEqual(oldvalues.data, response.data)

  def test_delete_theme(self):
    response = self.client.delete('/api/theme/' + str(1) + '/')
    self.assertEqual(response.status_code, 204)