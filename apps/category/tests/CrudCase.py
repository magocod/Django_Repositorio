# standard library
import json

# third-party
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token

# Django
from django.test import Client, TestCase
from django.contrib.auth.models import User

# local Django
from apps.category.models import Category
from apps.category.serializers import CategorySerializer

USERDATA = ('usertest', 'user@test.com', '123')

class CRUDTest(TestCase):

  def setUp(self):
    # user an token
    user = User.objects.create_user(
      USERDATA[0],
      USERDATA[1],
      USERDATA[2],
    )
    # admin
    user.is_staff = True
    user.save()             
    Token.objects.get_or_create(user= user)
    # auth token 
    token = Token.objects.get(user__username= USERDATA[0])
    self.client = APIClient()
    self.client.credentials(HTTP_AUTHORIZATION= 'Token ' + token.key)
    # data
    self.category = Category.objects.create(name= 'test')

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
      'name': 'test',
    }
    response = self.client.post('/api/categories/', data)
    self.assertEqual(response.status_code, 400)

  def test_get_category(self):
    response  = self.client.get('/api/category/' + str(self.category.pk) + '/')
    serializer = CategorySerializer(
      Category.objects.get(id= self.category.pk)
    )
    self.assertEqual(response.status_code, 200)
    self.assertEqual(serializer.data, response.data)
  
  def test_update_category(self):
    oldvalues = CategorySerializer(self.category)
    newdata = {
      'name': 'test update',
    }
    response = self.client.put('/api/category/' + str(self.category.pk) + '/', newdata)
    self.assertEqual(response.status_code, 200)
    self.assertNotEqual(oldvalues.data, response.data)

  def test_delete_categorye(self):
    response = self.client.delete('/api/category/' + str(self.category.pk) + '/')
    self.assertEqual(response.status_code, 204)