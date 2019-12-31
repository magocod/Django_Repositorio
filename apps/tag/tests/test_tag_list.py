"""
Pruebas listar tags
"""

# standard library
# import json

# local Django
# from apps.tag.models import Tag
# from apps.tag.serializers import TagSerializer
from apps.tests.fixtures import RepositoryTestCase


class TagListTest(RepositoryTestCase):
    """
    ...
    """

    def test_get_all(self):
        """
        ...
        """
        response = self.admin_client.get('/api/tags/')
        # response_data = json.loads(response.content)
        # serializer = TagSerializer(
        #     Tag.objects.all(),
        #     many=True,
        # )
        self.assertEqual(response.status_code, 200)
        # self.assertEqual(serializer.data, response_data)

    def test_get_all_authenticated(self):
        """
        ...
        """
        response = self.public_client.get('/api/tags/')
        self.assertEqual(response.status_code, 401)
