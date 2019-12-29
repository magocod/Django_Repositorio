"""
Pruebas listar tags
"""

# standard library
# import json

# Django
from django.test import TestCase
# third-party
from rest_framework.test import APIClient

# local Django
# from apps.tag.models import Tag
# from apps.tag.serializers import TagSerializer
from apps.tests.auth import create_user
from apps.tests.db import db_populate

# from django.urls import resolve, reverse


class TagListTest(TestCase):
    """
    ...
    """

    def setUp(self):
        """
        ...
        """
        # user an token
        auth = create_user(True)
        self.client = APIClient()
        self.client.credentials(
            HTTP_AUTHORIZATION='Token ' + auth['token'].key
        )
        # no authenticated
        self.noauthclient = APIClient()
        self.noauthclient.credentials(
            HTTP_AUTHORIZATION='Token ' + '123'
        )
        # data
        db_populate(tag=1)

    def test_get_all(self):
        """
        ...
        """
        response = self.client.get('/api/tags/')
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
        response = self.noauthclient.get('/api/tags/')
        self.assertEqual(response.status_code, 401)
