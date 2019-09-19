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
from apps.category.models import Category
from apps.tag.models import Tag
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
    self.category = Category.objects.create(name= 'TEST_CATEGORY')
    self.tag = Tag.objects.create(name= 'TEST_TAG')
    self.theme = Theme.objects.create(name= 'TEST_THEME', description= ' test description')
    self.collection = Collection.objects.create(
      name= 'TEST_COLLECTION',
      description= '---',
      updated= '2019-09-19 10:00:00',
      theme_id= 1,
    )

  def test_collection_add_relations(self):
    oldvalues = CollectionHeavySerializer(self.collection)
    relationdata = {
      'collection_id': 1,
      'categories': [1],
      'tags': [1],
    }
    response = self.client.put('/api/collection/relations/' + str(self.collection.pk) + '/', relationdata)
    # print(response.data)
    newvalues = CollectionHeavySerializer(
      Collection.objects.get(id= self.collection.pk)
    )
    self.assertEqual(response.status_code, 200)
    self.assertNotEqual(newvalues.data, oldvalues.data)
    self.assertEqual(newvalues.data, response.data)

  def test_collection_remove_relations(self):
    oldvalues = CollectionHeavySerializer(self.collection)
    relationdata = {
      'collection_id': 1,
      'categories': [1],
      'tags': [1],
    }
    response = self.client.delete('/api/collection/relations/' + str(self.collection.pk) + '/', relationdata)
    # print(response.data)
    newvalues = CollectionHeavySerializer(
      Collection.objects.get(id= self.collection.pk)
    )
    self.assertEqual(response.status_code, 200)
    self.assertNotEqual(newvalues.data, oldvalues.data)
    self.assertEqual(newvalues.data, response.data)