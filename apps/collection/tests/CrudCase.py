# standard library
# import json

# third-party
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token

# Django
from django.test import TestCase
from django.contrib.auth.models import User

# local Django
from apps.collection.models import Collection
from apps.theme.models import Theme
from apps.collection.serializers import CollectionHeavySerializer

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
    self.theme = Theme.objects.create(name= 'TEST', description= ' test description')
    self.collection = Collection.objects.create(
      name= 'TEST',
      description= '---',
      updated= '2019-09-19 10:00:00',
      theme_id= 1,
    )

  def test_create_collection(self):
    data = {
      'name': 'YSON',
      'description': '---',
      'updated': '2019-09-19 10:00:00',
      'theme_id': 1,
    }
    response = self.client.post('/api/collections/', data)
    # print(response)
    serializer = CollectionHeavySerializer(
      Collection.objects.get(id = response.data['id']),
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
    response  = self.client.get('/api/collection/' + str(self.collection.pk) + '/')
    serializer = CollectionHeavySerializer(
      Collection.objects.get(id= response.data['id'])
    )
    self.assertEqual(response.status_code, 200)
    self.assertEqual(serializer.data, response.data)
  
  def test_update_collection(self):
    oldvalues = CollectionHeavySerializer(self.collection)
    newdata = {
      'name': 'YSON2',
      'description': 'updated',
      'theme_id': 1,
    }
    response = self.client.put('/api/collection/' + str(self.collection.pk) + '/', newdata)
    # print(response.data)
    newvalues = CollectionHeavySerializer(
      Collection.objects.get(id= self.collection.pk)
    )
    self.assertEqual(response.status_code, 200)
    self.assertNotEqual(newvalues.data, oldvalues.data)
    self.assertEqual(newvalues.data, response.data)

  def test_delete_collection(self):
    response = self.client.delete('/api/collection/' + str(self.collection.pk) + '/')
    self.assertEqual(response.status_code, 204)