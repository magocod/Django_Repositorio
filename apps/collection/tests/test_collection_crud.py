"""
Pruebas edicion Collection
"""

# standard library
# import json

# local Django
from apps.collection.models import Collection
from apps.collection.serializers import CollectionHeavySerializer
from apps.tests.fixtures import RepositoryTestCase


class CollectionCrudTest(RepositoryTestCase):
    """
    ...
    """
    serializer = CollectionHeavySerializer

    def test_create_collection(self):
        data = {
            'name': 'YSON',
            'description': '---',
            'updated': '2019-09-19 10:00:00',
            'theme_id': 1,
        }
        response = self.admin_client.post('/api/collections/', data)
        # print(response)
        serializer = self.serializer(
            Collection.objects.get(id=response.data['id']),
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(serializer.data, response.data)

    def test_create_error_params(self):
        data = {
            'name': 'YSON',
            'description': '---',
            'updated': '2019-09-19',
        }
        response = self.admin_client.post('/api/collections/', data)
        self.assertEqual(response.status_code, 400)

    def test_create_error_duplicate(self):
        data = {
            'name': 'TEST_COLLECTION_1',
            'description': '---',
            'updated': '2019-09-19 10:00:00',
            'theme_id': 1,
        }
        response = self.admin_client.post('/api/collections/', data)
        self.assertEqual(response.status_code, 400)

    def test_get_collection(self):
        response = self.admin_client.get(f'/api/collection/{1}/')
        serializer = self.serializer(
            Collection.objects.get(id=response.data['id'])
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(serializer.data, response.data)

    def test_update_collection(self):
        collection = Collection.objects.get(id=1)
        oldvalues = self.serializer(collection)
        newdata = {
            'name': 'YSON2',
            'description': 'updated',
            'theme_id': 1,
        }
        response = self.admin_client.put(f'/api/collection/{1}/', newdata)
        # print(response.data)
        newvalues = self.serializer(
            Collection.objects.get(id=1)
        )
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(newvalues.data, oldvalues.data)
        self.assertEqual(newvalues.data, response.data)

    def test_delete_collection(self):
        response = self.admin_client.delete(f'/api/collection/{1}/')
        self.assertEqual(response.status_code, 204)
