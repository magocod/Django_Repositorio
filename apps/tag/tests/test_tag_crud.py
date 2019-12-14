"""
Prueba creacion de tag
"""

# standard library
import json
from typing import Dict, Any

# third-party
from rest_framework.test import APIClient

# Django
from django.test import TestCase
# from django.urls import resolve, reverse

# local Django
from apps.tag.models import Tag
from apps.tag.serializers import TagSerializer
from apps.tests.auth import create_user
from apps.tests.db import db_populate

class TagCrudTest(TestCase):
    """
    edicion de tag
    """

    def setUp(self) -> None:
        """
        ...
        """
        # user an token
        auth = create_user(True)
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + auth['token'].key)
        # data
        # self.tag = Tag.objects.create(name= 'test')
        db_populate(tag=1)

    def test_create_tag(self) -> None:
        """
        ...
        """
        data: Dict[str, Any] = {
            'name': 'YSON',
        }
        response = self.client.post('/api/tags/', data)
        response_data = json.loads(response.content)
        serializer = TagSerializer(
            Tag.objects.get(id=response_data['id']),
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(serializer.data, response_data)

    def test_create_error_params(self):
        """
        ...
        """
        data: Dict[str, Any] = {
            'names': 'NEW_TAG',
        }
        response = self.client.post('/api/tags/', data)
        self.assertEqual(response.status_code, 400)

    def test_create_error_duplicate(self):
        """
        ...
        """
        data: Dict[str, Any] = {
            'name': 'TEST_TAG',
        }
        response = self.client.post('/api/tags/', data)
        self.assertEqual(response.status_code, 400)

    def test_get_tag(self):
        """
        ...
        """
        # url = reverse('api_tag_detail', kwargs={'pk': self.tag.pk})
        # response = self.client.get(url)
        response = self.client.get('/api/tag/' + str(1) + '/')
        serializer = TagSerializer(
            Tag.objects.get(id=1)
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(serializer.data, response.data)

    def test_update_tag(self):
        """
        ...
        """
        tag = Tag.objects.get(id=1)
        oldvalues = TagSerializer(tag)
        newdata: Dict[str, Any] = {
            'name': 'YSON2',
        }
        # url = reverse('api_tag_detail', kwargs={'pk': self.tag.pk})
        # response = self.client.put(url, newdata)
        response = self.client.put('/api/tag/' + str(1) + '/', newdata)
        newvalues = TagSerializer(
            Tag.objects.get(id=1)
        )
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(newvalues.data, oldvalues.data)
        self.assertEqual(newvalues.data, response.data)

    def test_delete_tag(self):
        """
        ...
        """
        # url = reverse('api_tag_detail', kwargs={'pk': self.tag.pk})
        # response = self.client.delete(url)
        response = self.client.delete('/api/tag/' + str(1) + '/')
        self.assertEqual(response.status_code, 204)
