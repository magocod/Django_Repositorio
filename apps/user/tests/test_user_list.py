"""
...
"""

# local Django
from django.contrib.auth.models import User

# Django
from apps.tests.fixtures import AuthConfigTestCase
from apps.user.serializers import UserHeavySerializer


class UserListTest(AuthConfigTestCase):
    """
    user list test
    """

    serializer = UserHeavySerializer

    def test_list_all_users(self):
        """
        ...
        """
        response = self.admin_client.get("/api/users/")
        serializer = self.serializer(User.objects.all(), many=True,)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(serializer.data, response.data)
