"""
Prueba edicion Theme
"""

# standard library
import json
from typing import Any, Dict

# local Django
from apps.theme.models import Theme
from apps.theme.serializers import ThemeSerializer
from apps.tests.fixtures import RepositoryTestCase


class ThemeCrudTest(RepositoryTestCase):
    """
    ...
    """
    serializer = ThemeSerializer

    def test_create_theme(self):
        """
        ...
        """
        data: Dict[str, Any] = {
            'name': 'test create',
            'description': 'test create description'
        }
        response = self.admin_client.post('/api/themes/', data)
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
        response = self.admin_client.post('/api/themes/', data)
        self.assertEqual(response.status_code, 400)

    def test_create_error_duplicate(self):
        """
        ...
        """
        data: Dict[str, Any] = {
            'name': 'TEST_THEME_1',
            'description': 'test create duplicate'
        }
        response = self.admin_client.post('/api/themes/', data)
        self.assertEqual(response.status_code, 400)

    def test_get_theme(self):
        """
        ...
        """
        response = self.admin_client.get(f'/api/theme/{1}/')
        serializer = self.serializer(
            Theme.objects.get(id=1)
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(serializer.data, response.data)

    def test_get_theme_not_found(self):
        """
        ...
        """
        response = self.admin_client.get(f'/api/theme/{1000}/')
        self.assertEqual(response.status_code, 404)

    def test_update_theme(self):
        """
        ...
        """
        oldvalues = self.serializer(Theme.objects.get(id=1))
        newdata: Dict[str, Any] = {
            'name': 'test update',
            'description': 'test update description'
        }
        response = self.admin_client.put(f'/api/theme/{1}/', newdata)
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(oldvalues.data, response.data)

    def test_error_params_update_theme(self):
        """
        ...
        """
        oldvalues = self.serializer(Theme.objects.get(id=1))
        newdata: Dict[str, Any] = {
            'name_error': 'test update',
            'invalid_description': 'test update description'
        }
        response = self.admin_client.put(f'/api/theme/{1}/', newdata)
        values = self.serializer(Theme.objects.get(id=1))
        self.assertEqual(response.status_code, 400)
        self.assertEqual(oldvalues.data, values.data)

    def test_delete_theme(self):
        """
        ...
        """
        theme_id: int = Theme.objects.create(name='Hello').id
        response = self.admin_client.delete(f'/api/theme/{theme_id}/')
        self.assertEqual(response.status_code, 204)
