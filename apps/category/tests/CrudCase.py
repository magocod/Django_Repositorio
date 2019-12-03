"""
Pruebas edicion Category
"""

# standard library
import json
from typing import Dict, Any

# third-party
from rest_framework.test import APIClient

# Django
from django.test import TestCase

# local Django
from apps.category.models import Category
from apps.category.serializers import CategorySerializer
from apps.tests.auth import create_user
from apps.tests.db import db_populate

class CRUDTest(TestCase):
    """
    ...
    """
    serializer = CategorySerializer

    def setUp(self) -> None:
        """
        ...
        """
        # user an token
        auth = create_user(True)
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + auth['token'].key)
        # data
        db_populate(category=1)

    def test_create_category(self) -> None:
        """
        ...
        """
        data: Dict[str, Any] = {
            'name': 'test create',
            'description' : 'test create description'
        }
        response = self.client.post('/api/categories/', data)
        response_data = json.loads(response.content)
        serializer = self.serializer(
            Category.objects.get(id=response_data['id']),
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(serializer.data, response_data)

    def test_create_error_params(self) -> None:
        """
        ...
        """
        data: Dict[str, Any] = {
            'names': 'test create',
        }
        response = self.client.post('/api/categories/', data)
        self.assertEqual(response.status_code, 400)

    def test_create_error_duplicate(self) -> None:
        """
        ...
        """
        data: Dict[str, Any] = {
            'name': 'TEST_CATEGORY',
        }
        response = self.client.post('/api/categories/', data)
        self.assertEqual(response.status_code, 400)

    def test_get_category(self) -> None:
        """
        ...
        """
        response = self.client.get('/api/category/' + str(1) + '/')
        serializer = self.serializer(
            Category.objects.get(id=1)
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(serializer.data, response.data)

    def test_update_category(self) -> None:
        """
        ...
        """
        category = Category.objects.get(id=1)
        oldvalues = self.serializer(category)
        newdata: Dict[str, Any] = {
            'name': 'test update',
        }
        response = self.client.put('/api/category/' + str(1) + '/', newdata)
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(oldvalues.data, response.data)

    def test_delete_category(self) -> None:
        """
        ...
        """
        response = self.client.delete('/api/category/' + str(1) + '/')
        self.assertEqual(response.status_code, 204)
