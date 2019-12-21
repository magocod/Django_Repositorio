# standard library
import json

# Django
from django.test import TestCase
# third-party
from rest_framework.test import APIClient

# local Django
from apps.article.models import Article
from apps.article.serializers.article import ArticleHeavySerializer
from apps.tests.auth import create_user
from apps.tests.db import db_populate


class ListTest(TestCase):
    """
    ...
    """
    serializer = ArticleHeavySerializer

    def setUp(self):
        # user an token
        auth = create_user(True)
        self.client = APIClient()
        self.client.credentials(
            HTTP_AUTHORIZATION='Token ' + auth['token'].key,
        )
        # no authenticated
        self.noauthclient = APIClient()
        self.noauthclient.credentials(HTTP_AUTHORIZATION='Token ' + '123')
        # data
        db_populate(article=1)

    def test_get_all(self):
        response = self.client.get('/api/articles/')
        response_data = json.loads(response.content)
        serializer = self.serializer(
            Article.objects.all(),
            many=True,
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(serializer.data, response_data)

    def test_get_all_authenticated(self):
        response = self.noauthclient.get('/api/articles/')
        self.assertEqual(response.status_code, 401)
