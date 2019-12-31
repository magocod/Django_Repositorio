"""
Inicializar credenciales para pruebas
"""

# standard library
# import json
# from typing import Dict

# Django
from django.test import TestCase
# third-party
from rest_framework.test import APIClient
# local Django
from apps.tests.auth import (user_list, TOKENS)
from apps.tests.db import db_populate


class AuthConfigTestCase(TestCase):
    """
    auth test case
    """

    def setUp(self) -> None:
        """
        ...
        """
        self.auth_set_up()

    def auth_set_up(self) -> None:
        # example users
        user_list()
        # http clients
        self.public_client = APIClient()
        self.admin_client = APIClient()
        self.admin_client.credentials(
            HTTP_AUTHORIZATION='Token ' + TOKENS['super_user']
        )
        self.user_client = APIClient()
        self.user_client.credentials(
            HTTP_AUTHORIZATION='Token ' + TOKENS['user']
        )
        self.staff_client = APIClient()
        self.staff_client.credentials(
            HTTP_AUTHORIZATION='Token ' + TOKENS['user_staff']
        )


class RepositoryTestCase(AuthConfigTestCase):
    """
    repository test case
    """

    def setUp(self) -> None:
        """
        ...
        """
        self.auth_set_up()
        self.repository_set_up()

    def repository_set_up(self) -> None:
        """
        ...
        """
        # base models
        db_populate(
            tag=5,
            theme=5,
            category=5,
            collection=5,
            article=5,
        )
        # many to many relationships
        # ...
        # others
        # ...
