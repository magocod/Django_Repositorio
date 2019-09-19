from django.test import Client, TestCase
from django.urls import resolve, reverse
from django.contrib.auth.models import User
import json

from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token

from apps.tag.models import Tag
# from apps.tag.views import VTag
from apps.tag.serializers import TagSerializer

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
    self.tag = Tag.objects.create(name= 'test')

  def test_get_all(self):
    response = self.client.get('/api/tags/')
    response_data = json.loads(response.content)
    serializer = TagSerializer(
      Tag.objects.all(),
      many= True,
    )
    self.assertEqual(response.status_code, 200)
    # self.assertEqual(serializer.data, response_data)

  def test_get_all_authenticated(self):
    response = self.noauthclient.get('/api/tags/')
    self.assertEqual(response.status_code, 401)