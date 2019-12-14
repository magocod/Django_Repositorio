"""
Pruebas listar category
"""

# standard library
# import json

# third-party
from rest_framework.test import APIClient

# Django
from django.test import TestCase

# local Django
# from apps.category.models import Category
from apps.category.serializers import CategorySerializer
from apps.tests.auth import create_user
from apps.tests.db import db_populate

class CategoryListTest(TestCase):
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
        # no authenticated
        self.noauthclient = APIClient()
        self.noauthclient.credentials(HTTP_AUTHORIZATION='Token ' + '123')
        # data
        db_populate(category=1)

    def test_get_all(self) -> None:
        """
        ...
        """
        response = self.client.get('/api/categories/')
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
        response = self.noauthclient.get('/api/categories/')
        self.assertEqual(response.status_code, 401)
