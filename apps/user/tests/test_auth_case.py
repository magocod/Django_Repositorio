"""
...
"""

# standard library
# import json
from typing import Dict

# Django
from django.contrib.auth.models import User

# local Django
from apps.tests.fixtures import AuthConfigTestCase


class UserAuthTest(AuthConfigTestCase):
    """
    ...
    """

    def test_search_email(self):
        """
        ...
        """
        data: Dict[str, str] = {
            'email': 'admin@django.com',
        }
        response = self.public_client.post('/api/email/', data)
        # print(response.data)
        self.assertEqual(response.status_code, 200)

    def test_email_does_not_exist(self):
        """
        ...
        """
        data: Dict[str, str] = {
            'email': 'user10@test.com',
        }
        response = self.public_client.post('/api/email/', data)
        # print(response.data)
        self.assertEqual(response.status_code, 404)

    def test_invalid_search_email_params(self):
        """
        ...
        """
        data: Dict[str, str] = {
            'emails': 'novalid@django.com',
        }
        response = self.public_client.post('/api/email/', data)
        self.assertEqual(response.status_code, 400)

    def test_success_request_token(self):
        """
        ...
        """
        data: Dict[str, str] = {
            'email': 'admin@django.com',
            'password': '123',
        }
        response = self.public_client.post('/api/token-auth/', data)
        self.assertEqual(response.status_code, 200)

    def test_error_credentials(self):
        """
        ...
        """
        data: Dict[str, str] = {
            'e': 'notexist@django.com',
            'pass': '123',
        }
        response = self.public_client.post('/api/token-auth/', data)
        self.assertEqual(response.status_code, 400)

    def test_error_user_account_is_disabled(self):
        """
        ...
        """
        User.objects.filter(id=1).update(is_active=False)
        data: Dict[str, str] = {
            'email': 'admin@django.com',
            'password': '123',
        }
        response = self.public_client.post('/api/token-auth/', data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.data[
                'non_field_errors'
            ][0],
            'User account is disabled.'
        )

    def test_error_user_not_exist(self):
        """
        ...
        """
        data: Dict[str, str] = {
            'email': 'notexist@django.com',
            'password': '123',
        }
        response = self.public_client.post('/api/token-auth/', data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.data[
                'non_field_errors'
            ][0], 'User no exist.'
        )

    def test_error_invalid_password(self):
        """
        ...
        """
        data: Dict[str, str] = {
            'email': 'admin@django.com',
            'password': 'novalid',
        }
        response = self.public_client.post('/api/token-auth/', data)
        self.assertEqual(response.status_code, 400)
        # print(response.data)
        self.assertEqual(
            response.data[
                'non_field_errors'
            ][0],
            'Unable to log in with provided credentials.'
        )

    def test_logout(self):
        """
        ...
        """
        response = self.admin_client.post('/api/user/logout/')
        self.assertEqual(response.status_code, 200)

    def test_repeat_logout(self):
        """
        ...
        """
        self.admin_client.post('/api/user/logout/')
        response = self.admin_client.post('/api/user/logout/')
        self.assertEqual(response.status_code, 401)
