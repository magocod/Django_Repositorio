"""
...
"""

# standard library
import json
from typing import Any, Dict

# local Django
from django.contrib.auth.models import User

# Django
from apps.tests.fixtures import AuthConfigTestCase
from apps.user.serializers import UserHeavySerializer


class UserCrudTest(AuthConfigTestCase):
    """
    user crud test
    """

    serializer = UserHeavySerializer

    def test_create_user(self):
        """
        ...
        """
        data: Dict[str, Any] = {
            "username": "NEW",
            "email": "newemail@gmail.com",
            "password": "123",
            "first_name": "name",
            "last_name": "name2",
            "is_staff": False,
        }
        response = self.admin_client.post("/api/users/", data)
        response_data = json.loads(response.content)
        serializer = self.serializer(User.objects.get(id=response_data["id"]),)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(serializer.data, response_data)

    def test_create_error_params(self):
        """
        ...
        """
        data: Dict[str, Any] = {
            "names": "NEW_USER",
        }
        response = self.admin_client.post("/api/users/", data)
        self.assertEqual(response.status_code, 400)

    def test_create_error_duplicate(self):
        """
        ...
        """
        User.objects.create_user(
            "NEW", "newemail@gmail.com", "123",
        )
        data: Dict[str, Any] = {
            "username": "NEW",
            "email": "newemail@gmail.com",
            "password": "123",
            "first_name": "name",
            "last_name": "name2",
            "is_staff": False,
        }
        response = self.admin_client.post("/api/users/", data)
        self.assertEqual(response.status_code, 400)

    def test_get_user(self):
        """
        ...
        """
        response = self.admin_client.get(f"/api/user/{1}/")
        serializer = self.serializer(User.objects.get(id=1))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(serializer.data, response.data)

    def test_get_user_not_found(self):
        """
        ...
        """
        response = self.admin_client.get(f"/api/user/{1900}/")
        self.assertEqual(response.status_code, 404)

    def test_update_user(self):
        """
        ...
        """
        oldvalues = self.serializer(User.objects.get(id=1))
        newdata: Dict[str, Any] = {
            "username": "NEW",
            "first_name": "new name",
            "last_name": "new name2",
        }
        response = self.admin_client.put("/api/user/" + str(1) + "/", newdata)
        newvalues = self.serializer(User.objects.get(id=1))
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(newvalues.data, oldvalues.data)
        self.assertEqual(newvalues.data, response.data)

    def test_error_params_update_user(self):
        """
        ...
        """
        newdata: Dict[str, Any] = {
            "invalid": "NEW",
        }
        response = self.admin_client.put("/api/user/" + str(1) + "/", newdata)
        self.assertEqual(response.status_code, 400)

    def test_delete_user(self):
        """
        ...
        """
        response = self.admin_client.delete(f"/api/user/{2}/")
        self.assertEqual(response.status_code, 204)

    def test_not_allowed_to_delete_user(self):
        """
        ...
        """
        response = self.user_client.delete(f"/api/user/{4}/")
        self.assertEqual(response.status_code, 403)
        response = self.public_client.delete(f"/api/user/{4}/")
        self.assertEqual(response.status_code, 401)

    def test_user_does_not_delete_himself(self):
        """
        ...
        """
        response = self.admin_client.delete(f"/api/user/{1}/")
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data, "can't delete himself")

    def test_not_delete_superuser(self):
        """
        ...
        """
        response = self.admin_client.delete(f"/api/user/{3}/")
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data, "super users cannot be deleted")

    def test_delete_admin_user(self):
        """
        ...
        """
        response = self.staff_client.delete(f"/api/user/{5}/")
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data, "user cannot delete administrators")
        response = self.admin_client.delete(f"/api/user/{5}/")
        self.assertEqual(response.status_code, 204)
