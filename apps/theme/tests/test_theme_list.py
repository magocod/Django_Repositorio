"""
Listar Theme
"""

# standard library
# import json

# local Django
# from apps.theme.models import Theme
from apps.theme.serializers import ThemeSerializer
from apps.tests.fixtures import RepositoryTestCase


class ThemeListTest(RepositoryTestCase):
    """
    ...
    """
    serializer = ThemeSerializer

    def test_get_all(self):
        """
        ...
        """
        response = self.admin_client.get('/api/themes/')
        # response_data = json.loads(response.content)
        # serializer = self.serializer(
        #     Theme.objects.all(),
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
