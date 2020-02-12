"""
Pruebas Listar Collection
"""

# standard library
# import json

# local Django
# from apps.collection.models import Collection
from apps.collection.serializers import CollectionHeavySerializer
from apps.tests.fixtures import RepositoryTestCase


class CollectionListTest(RepositoryTestCase):
    """
    ...
    """

    serializer = CollectionHeavySerializer

    def test_get_all(self):
        response = self.admin_client.get("/api/collections/")
        # response_data = json.loads(response.content)
        # serializer = self.serializer(
        #     Collection.objects.all(),
        #     many=True,
        # )
        self.assertEqual(response.status_code, 200)
        # self.assertEqual(serializer.data, response_data)

    def test_get_all_authenticated(self):
        response = self.public_client.get("/api/collections/")
        self.assertEqual(response.status_code, 401)
