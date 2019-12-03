"""
Prueba edicion Theme
"""

# standard library
import json
from typing import Dict, Any

# third-party
from rest_framework.test import APIClient

# Django
from django.test import TestCase

# local Django
from apps.theme.models import Theme
from apps.theme.serializers import ThemeSerializer
from apps.tests.auth import create_user
from apps.tests.db import db_populate

class CRUDTest(TestCase):
    """
    ...
    """
    serializer = ThemeSerializer

    def setUp(self):
        """
        ...
        """
        # user an token
        auth = create_user(True)
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + auth['token'].key)
        # data
        # self.theme = Theme.objects.create(name= 'test', description= ' test description')
        db_populate(theme=1)

    def test_create_theme(self):
        """
        ...
        """
        data: Dict[str, Any] = {
            'name': 'test create',
            'description' : 'test create description'
        }
        response = self.client.post('/api/themes/', data)
        response_data = json.loads(response.content)
        serializer = self.serializer(
            Theme.objects.get(id=response_data['id']),
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(serializer.data, response_data)

    def test_create_error_params(self):
        """
        ...
        """
        data: Dict[str, Any] = {
            'name': 'test create',
        }
        response = self.client.post('/api/themes/', data)
        self.assertEqual(response.status_code, 400)

    def test_create_error_duplicate(self):
        """
        ...
        """
        data: Dict[str, Any] = {
            'name': 'TEST_THEME',
            'description' : 'test create duplicate'
        }
        response = self.client.post('/api/themes/', data)
        self.assertEqual(response.status_code, 400)

    def test_get_theme(self):
        """
        ...
        """
        response = self.client.get('/api/theme/' + str(1) + '/')
        serializer = self.serializer(
            Theme.objects.get(id=1)
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(serializer.data, response.data)

    def test_update_theme(self):
        """
        ...
        """
        oldvalues = self.serializer(Theme.objects.get(id=1))
        newdata: Dict[str, Any] = {
            'name': 'test update',
            'description' : 'test update description'
        }
        response = self.client.put('/api/theme/' + str(1) + '/', newdata)
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(oldvalues.data, response.data)

    def test_delete_theme(self):
        """
        ...
        """
        response = self.client.delete('/api/theme/' + str(1) + '/')
        self.assertEqual(response.status_code, 204)
