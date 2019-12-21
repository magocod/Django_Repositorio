"""
Listar Theme
"""

# standard library
# import json

# Django
from django.test import TestCase
# standard library
from rest_framework.test import APIClient

from apps.tests.auth import create_user
from apps.tests.db import db_populate
# local Django
# from apps.theme.models import Theme
from apps.theme.serializers import ThemeSerializer

# from django.urls import resolve, reverse


class ThemeListTest(TestCase):
    """
    ...
    """
    serializer = ThemeSerializer

    def setUp(self):
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
        # self.theme = Theme.objects.create(name= 'test', description= ' test description')
        db_populate(theme=1)

    def test_get_all(self):
        """
        ...
        """
        response = self.client.get('/api/themes/')
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
        response = self.noauthclient.get('/api/tags/')
        self.assertEqual(response.status_code, 401)
