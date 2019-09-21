# standard library
import json

# third-party
from rest_framework.test import APIClient

# Django
from django.test import TestCase

# local Django
from apps.category.models import Category
from apps.category.serializers import CategorySerializer
from apps.tests.auth import create_user
from apps.tests.db import DBpopulate

class CRUDTest(TestCase):

  def setUp(self):
    # user an token
    auth = create_user(True)
    self.client = APIClient()
    self.client.credentials(HTTP_AUTHORIZATION= 'Token ' + auth['token'].key)
    # data
    DBpopulate(category= 1)

  def test_create_category(self):
    data = {
      'name': 'test create',
      'description' : 'test create description'
    }
    response = self.client.post('/api/categories/', data)
    response_data = json.loads(response.content)
    serializer = CategorySerializer(
      Category.objects.get(id = response_data['id']),
    )
    self.assertEqual(response.status_code, 201)
    self.assertEqual(serializer.data, response_data)

  def test_create_error_params(self):
    data = {
      'names': 'test create',
    }
    response = self.client.post('/api/categories/', data)
    self.assertEqual(response.status_code, 400)

  def test_create_error_duplicate(self):
    data = {
      'name': 'TEST_CATEGORY',
    }
    response = self.client.post('/api/categories/', data)
    self.assertEqual(response.status_code, 400)

  def test_get_category(self):
    response  = self.client.get('/api/category/' + str(1) + '/')
    serializer = CategorySerializer(
      Category.objects.get(id= 1)
    )
    self.assertEqual(response.status_code, 200)
    self.assertEqual(serializer.data, response.data)
  
  def test_update_category(self):
    category = Category.objects.get(id = 1)
    oldvalues = CategorySerializer(category)
    newdata = {
      'name': 'test update',
    }
    response = self.client.put('/api/category/' + str(1) + '/', newdata)
    self.assertEqual(response.status_code, 200)
    self.assertNotEqual(oldvalues.data, response.data)

  def test_delete_category(self):
    response = self.client.delete('/api/category/' + str(1) + '/')
    self.assertEqual(response.status_code, 204)