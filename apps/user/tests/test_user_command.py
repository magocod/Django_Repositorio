"""
...
"""

# Django
from django.contrib.auth.models import User
from django.core.management import call_command
from django.test import TestCase

# local Django
from apps.user.database.seeders import DEFAULT_USERS


class AuthConfigTestCase(TestCase):
    """
    auth test case
    """

    def setUp(self):
        """
        ...
        """
        pass

    def test_command_create_default_users(self):
        """
        ...
        """
        call_command('default_users')

        self.assertEqual(User.objects.count(), DEFAULT_USERS['total'])
        self.assertEqual(
            User.objects.filter(
                is_superuser=True,
                is_staff=True
            ).count(),
            DEFAULT_USERS['super']
        )
        self.assertEqual(
            User.objects.filter(
                is_superuser=False,
                is_staff=True
            ).count(),
            DEFAULT_USERS['staff']
        )
        self.assertEqual(
            User.objects.filter(
                is_superuser=False,
                is_staff=False
            ).count(),
            DEFAULT_USERS['basic']
        )
