# standard library
import json

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

class ListTest(TestCase):

  def setUp(self):
    # user an token
    user = User.objects.create_user(
      USERDATA[0],
      USERDATA[1],
      USERDATA[2],
    )
    user.is_staff = True
    user.save()             
    Token.objects.get_or_create(user= user)
    # auth token 
    token = Token.objects.get(user__username= USERDATA[0])
    self.client = APIClient()
    self.client.credentials(HTTP_AUTHORIZATION= 'Token ' + token.key)
    # no authenticated
    self.noauthclient = APIClient()
    self.noauthclient.credentials(HTTP_AUTHORIZATION= 'Token ' + '123')
    # data
    self.theme = Theme.objects.create(name= 'TEST', description= ' test description')
    self.collection = Collection.objects.create(
      name= 'TEST',
      description= '---',
      updated= '2019-09-19 10:00:00',
      theme_id= 1,
    )

  def test_get_all(self):
    response = self.client.get('/api/collections/')
    response_data = json.loads(response.content)
    serializer = CollectionHeavySerializer(
      Collection.objects.all(),
      many= True,
    )
    self.assertEqual(response.status_code, 200)
    # self.assertEqual(serializer.data, response_data)

  def test_get_all_authenticated(self):
    response = self.noauthclient.get('/api/collections/')
    self.assertEqual(response.status_code, 401)