import json

from django.test import Client, TestCase
from django.urls import resolve, reverse
from django.contrib.auth.models import User

from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token

from apps.tag.models import Tag
# from apps.tag.views import VTag
from apps.tag.serializers import TagSerializer

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
    self.tag = Tag.objects.create(name= 'test')

  def test_create_tag(self):
    data = {
      'name': 'YSON',
    }
    response = self.client.post('/api/tags/', data)
    response_data = json.loads(response.content)
    serializer = TagSerializer(
      Tag.objects.get(id = response_data['id']),
    )
    self.assertEqual(response.status_code, 201)
    self.assertEqual(serializer.data, response_data)
  
  def test_get_tag(self):
    # url = reverse('api_tag_detail', kwargs={'pk': self.tag.pk})
    # response = self.client.get(url)
    response  = self.client.get('/api/tag/' + str(self.tag.pk) + '/')
    serializer = TagSerializer(
      Tag.objects.get(id= self.tag.pk)
    )
    self.assertEqual(response.status_code, 200)
    self.assertEqual(serializer.data, response.data)
  
  def test_update_tag(self):
    oldvalues = TagSerializer(self.tag)
    newdata = {
      'name': 'YSON2',
    }
    # url = reverse('api_tag_detail', kwargs={'pk': self.tag.pk})
    newvalues = TagSerializer(
      Tag.objects.get(id= self.tag.pk)
    )
    # response = self.client.put(url, newdata)
    response = self.client.put('/api/tag/' + str(self.tag.pk) + '/', newdata)
    self.assertEqual(response.status_code, 200)

  def test_delete_tag(self):
    # url = reverse('api_tag_detail', kwargs={'pk': self.tag.pk})
    # response = self.client.delete(url)
    response = self.client.delete('/api/tag/' + str(self.tag.pk) + '/')
    self.assertEqual(response.status_code, 204)