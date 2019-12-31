"""
...
"""

# standard library
import json
from typing import Any, Dict

# local Django
from apps.tag.models import Tag
from apps.tag.serializers import TagSerializer
from apps.tests.fixtures import RepositoryTestCase


class TagCrudTest(RepositoryTestCase):
    """
    ...
    """

    def test_create_tag(self) -> None:
        """
        ...
        """
        data: Dict[str, Any] = {
            'name': 'YSON',
        }
        response = self.admin_client.post('/api/tags/', data)
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
        response = self.admin_client.post('/api/tags/', data)
        self.assertEqual(response.status_code, 400)

    def test_create_error_duplicate(self):
        """
        ...
        """
        data: Dict[str, Any] = {
            'name': 'TEST_TAG_1',
        }
        response = self.admin_client.post('/api/tags/', data)
        self.assertEqual(response.status_code, 400)

    def test_get_tag(self):
        """
        ...
        """
        response = self.admin_client.get(f'/api/tag/{1}/')
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
        response = self.admin_client.put(f'/api/tag/{1}/', newdata)
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
        response = self.admin_client.delete(f'/api/tag/{1}/')
        self.assertEqual(response.status_code, 204)
