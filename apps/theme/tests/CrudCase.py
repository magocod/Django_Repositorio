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
    self.theme = Theme.objects.create(name= 'test', description= ' test description')

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
      'name': 'test',
      'description' : 'test create duplicate'
    }
    response = self.client.post('/api/themes/', data)
    self.assertEqual(response.status_code, 400)

  def test_get_theme(self):
    response  = self.client.get('/api/theme/' + str(self.theme.pk) + '/')
    serializer = ThemeSerializer(
      Theme.objects.get(id= self.theme.pk)
    )
    self.assertEqual(response.status_code, 200)
    self.assertEqual(serializer.data, response.data)
  
  def test_update_theme(self):
    oldvalues = ThemeSerializer(self.theme)
    newdata = {
      'name': 'test update',
      'description' : 'test update description'
    }
    response = self.client.put('/api/theme/' + str(self.theme.pk) + '/', newdata)
    self.assertEqual(response.status_code, 200)
    self.assertNotEqual(oldvalues.data, response.data)

  def test_delete_theme(self):
    response = self.client.delete('/api/theme/' + str(self.theme.pk) + '/')
    self.assertEqual(response.status_code, 204)