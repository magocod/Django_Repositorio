"""
Pruebas edicion Category
"""

# standard library
import json
from typing import Any, Dict

# local Django
from apps.category.models import Category
from apps.category.serializers import CategorySerializer
from apps.tests.fixtures import RepositoryTestCase


class CategoryCrudTest(RepositoryTestCase):
    """
    ...
    """
    serializer = CategorySerializer

    def test_create_category(self) -> None:
        """
        ...
        """
        data: Dict[str, Any] = {
            'name': 'test create',
            'description': 'test create description'
        }
        response = self.admin_client.post('/api/categories/', data)
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
        response = self.admin_client.post('/api/categories/', data)
        self.assertEqual(response.status_code, 400)

    def test_create_error_duplicate(self) -> None:
        """
        ...
        """
        data: Dict[str, Any] = {
            'name': 'TEST_CATEGORY_1',
        }
        response = self.admin_client.post('/api/categories/', data)
        self.assertEqual(response.status_code, 400)

    def test_get_category(self) -> None:
        """
        ...
        """
        response = self.admin_client.get(f'/api/category/{1}/')
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
        response = self.admin_client.put(f'/api/category/{1}/', newdata)
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(oldvalues.data, response.data)

    def test_delete_category(self) -> None:
        """
        ...
        """
        response = self.admin_client.delete(f'/api/category/{1}/')
        self.assertEqual(response.status_code, 204)
