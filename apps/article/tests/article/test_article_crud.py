# standard library
# import json

# local Django
from apps.article.models import Article
from apps.article.serializers.article import ArticleHeavySerializer
from apps.tests.fixtures import RepositoryTestCase


class ArticleCrudTest(RepositoryTestCase):
    """
    ...
    """

    serializer = ArticleHeavySerializer

    def test_create_article(self):
        data = {
            "name": "YSON",
            "description": "---",
            "identifier": "123334",
            "author": "YSON",
            "license": "ls",
            "url": "https://www.google.com",
            "created": "2019-09-19",
        }
        response = self.admin_client.post("/api/articles/", data)
        # print(response.data)
        # print(response)
        serializer = self.serializer(Article.objects.get(id=response.data["id"]),)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(serializer.data, response.data)

    def test_create_error_params(self):
        data = {
            "name": "YSON",
            "description": "---",
            "updated": "2019-09-19",
        }
        response = self.admin_client.post("/api/collections/", data)
        self.assertEqual(response.status_code, 400)

    def test_create_error_duplicate(self):
        data = {
            "name": "TEST_ARTICLE_1",
            "description": "---",
            "updated": "2019-09-19",
        }
        response = self.admin_client.post("/api/articles/", data)
        self.assertEqual(response.status_code, 400)

    def test_get_article(self):
        response = self.admin_client.get(f"/api/article/{1}/")
        # print(response.data)
        serializer = self.serializer(Article.objects.get(id=response.data["id"]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(serializer.data, response.data)

    def test_get_article_not_found(self):
        response = self.admin_client.get(f"/api/article/{1000}/")
        self.assertEqual(response.status_code, 404)

    def test_update_article(self):
        oldvalues = self.serializer(Article.objects.get(id=1))
        newdata = {
            "name": "UPDATED",
            "description": "---",
            "identifier": "11121234",
            "author": "YSON",
            "license": "ls",
            "url": "https://www.google.com",
            "created": "2019-09-19",
        }
        response = self.admin_client.put(f"/api/article/{1}/", newdata)
        # print(response.data)
        newvalues = self.serializer(Article.objects.get(id=1))
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(newvalues.data, oldvalues.data)
        self.assertEqual(newvalues.data, response.data)

    def test_error_params_update_article(self):
        oldvalues = self.serializer(Article.objects.get(id=1))
        newdata = {
            "names": "UPDATED",
        }
        response = self.admin_client.put(f"/api/article/{1}/", newdata)
        values = self.serializer(Article.objects.get(id=1))
        self.assertEqual(response.status_code, 400)
        self.assertEqual(values.data, oldvalues.data)

    def test_delete_article(self):
        response = self.admin_client.delete(f"/api/article/{1}/")
        self.assertEqual(response.status_code, 204)
