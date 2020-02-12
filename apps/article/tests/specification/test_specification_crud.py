# standard library
# import json

# local Django
from apps.article.models import Article, Specification
from apps.article.serializers.article import ArticleHeavySerializer
from apps.tests.fixtures import RepositoryTestCase


class SpecificationCrudTest(RepositoryTestCase):
    """
    ...
    """

    serializer = ArticleHeavySerializer

    def test_create_specification(self):
        data = {
            "description": "create",
            "article_id": 1,
        }
        response = self.admin_client.post("/api/articles/specification/", data)
        # print(response.data)
        # print(response)
        serializer = self.serializer(Article.objects.get(id=response.data["id"]),)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(serializer.data, response.data)

    # def test_create_an_item_specification_that_does_not_exist(self):
    #     data = {
    #         'description': 'create',
    #         'article_id': 10000,
    #     }
    #     response = self.admin_client.post(
    #         '/api/articles/specification/',
    #         data
    #     )
    #     self.assertEqual(response.status_code, 404)

    def test_create_error_params(self):
        data = {
            "name": "YSON",
            "description": "---",
            "updated": "2019-09-19",
        }
        response = self.admin_client.post("/api/articles/specification/", data)
        self.assertEqual(response.status_code, 400)

    def test_create_error_duplicate(self):
        data = {
            "description": "---",
            "article": 1,
        }
        response = self.admin_client.post("/api/articles/specification/", data)
        self.assertEqual(response.status_code, 400)

    def test_update_specification(self):
        Specification.objects.create(description="---", article_id=1)
        # oldvalues = self.serializer(article)
        newdata = {
            "description": "UPDATED",
            "article_id": 1,
        }
        response = self.admin_client.put(f"/api/article/specification/{1}/", newdata)
        # print(response.data)
        newvalues = self.serializer(Article.objects.get(id=1))
        self.assertEqual(response.status_code, 200)
        # self.assertNotEqual(newvalues.data, oldvalues.data)
        self.assertEqual(newvalues.data, response.data)

    def test_error_parameters_update_specification(self):
        Specification.objects.create(description="---", article_id=1)
        newdata = {
            "descrip": "UPDATED",
            "article": 1,
        }
        response = self.admin_client.put(f"/api/article/specification/{1}/", newdata)
        self.assertEqual(response.status_code, 400)

    def test_delete_specification(self):
        data = {
            "description": "create",
            "article_id": 1,
        }
        self.admin_client.post("/api/articles/specification/", data)
        response = self.admin_client.delete(f"/api/article/specification/{1}/")
        self.assertEqual(response.status_code, 204)

    def test_remove_an_item_specification_that_does_not_exist(self):
        data = {
            "description": "create",
            "article_id": 10000,
        }
        response = self.admin_client.post(f"/api/articles/specification/{10000}/", data)
        self.assertEqual(response.status_code, 404)
