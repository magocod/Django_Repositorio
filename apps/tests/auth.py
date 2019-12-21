"""
Authenticacion pruebas
"""

# standard library
from typing import Any, Dict

# Django
from django.contrib.auth.models import User
# third-party
from rest_framework.authtoken.models import Token


def create_user(staff: bool = False) -> Dict[str, Any]:
    """
    [creacion de usuarios]

    Arguments:
        staff {bol} -- [description]

    Returns:
        dicc [user, token] -- [description]
    """
    user = User.objects.create_user(
        'usertest',
        'user@test.com',
        '123',
    )
    # admin
    user.is_staff = staff
    user.save()
    # auth token
    tokentuple = Token.objects.get_or_create(user=user)
    return {'user': user, 'token': tokentuple[0]}
