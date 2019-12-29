# standard library
# import json

# Django
from django.test import TestCase
# third-party
from rest_framework.test import APIClient

# local Django
from apps.article.models import Article
from apps.article.serializers.article import ArticleHeavySerializer
from apps.tests.auth import create_user
from apps.tests.db import db_populate


class SpecificationCrudTest(TestCase):

    serializer = ArticleHeavySerializer

    def setUp(self):
        # user an token
        auth = create_user(True)
        self.client = APIClient()
        self.client.credentials(
            HTTP_AUTHORIZATION='Token ' + auth['token'].key
        )
        # data
        db_populate(article=1)

    def test_create_specification(self):
        data = {
            'description': 'create',
            'article_id': 1,
        }
        response = self.client.post(
            '/api/articles/specification/',
            data
        )
        # print(response.data)
        # print(response)
        serializer = self.serializer(
            Article.objects.get(id=response.data['id']),
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(serializer.data, response.data)

    def test_create_error_params(self):
        data = {
            'name': 'YSON',
            'description': '---',
            'updated': '2019-09-19',
        }
        response = self.client.post(
            '/api/articles/specification/',
            data
        )
        self.assertEqual(response.status_code, 400)

    def test_create_error_duplicate(self):
        data = {
            'description': '---',
            'article': 1,
        }
        response = self.client.post('/api/articles/specification/', data)
        self.assertEqual(response.status_code, 400)

    def test_update_specification(self):
        data = {
            'description': 'create',
            'article_id': 1,
        }
        self.client.post('/api/articles/specification/', data)
        # article = Article.objects.get(id=1)
        # oldvalues = self.serializer(article)
        newdata = {
            'description': 'UPDATED',
            'article_id': 1,
        }
        response = self.client.put(
            '/api/article/specification/' + str(1) + '/',
            newdata
        )
        # print(response.data)
        newvalues = self.serializer(
            Article.objects.get(id=1)
        )
        self.assertEqual(response.status_code, 200)
        # self.assertNotEqual(newvalues.data, oldvalues.data)
        self.assertEqual(newvalues.data, response.data)

    def test_delete_specification(self):
        data = {
            'description': 'create',
            'article_id': 1,
        }
        self.client.post('/api/articles/specification/', data)
        response = self.client.delete(
            '/api/article/specification/' + str(1) + '/'
        )
        self.assertEqual(response.status_code, 204)
