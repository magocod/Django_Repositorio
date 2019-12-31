"""
Pruebas listar category
"""

# standard library
# import json

# local Django
# from apps.category.models import Category
from apps.category.serializers import CategorySerializer
from apps.tests.fixtures import RepositoryTestCase


class CategoryListTest(RepositoryTestCase):
    """
    ...
    """
    serializer = CategorySerializer

    def test_get_all(self) -> None:
        """
        ...
        """
        response = self.admin_client.get('/api/categories/')
        # response_data = json.loads(response.content)
        # serializer = CategorySerializer(
        #       Category.objects.all(),
        #       many=True,
        # )
        self.assertEqual(response.status_code, 200)
        # self.assertEqual(serializer.data, response_data)

    def test_get_all_authenticated(self) -> None:
        """
        ...
        """
        response = self.public_client.get('/api/categories/')
        self.assertEqual(response.status_code, 401)
