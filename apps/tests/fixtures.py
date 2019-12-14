"""
Inicializar credenciales para pruebas
"""

# standard library
# import json
from typing import Dict

# third-party
from rest_framework.test import APIClient

# Django
from django.test import TestCase

# local Django
from apps.tests.auth import create_user

class AuthConfigTestCase(TestCase):
    """
    edicion de tag
    """

    def setUp(self) -> None:
        """
        ...
        """
        # user an token
        auth = create_user(True)
        self.public_client = APIClient()
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + auth['token'].key)
