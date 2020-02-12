# standard library
# import json

# local Django
from apps.article.models import Article
from apps.article.serializers.article import ArticleHeavySerializer
from apps.collection.models import Collection
from apps.tag.models import Tag
from apps.tests.fixtures import RepositoryTestCase


class ArticleRelationTest(RepositoryTestCase):
    """
    ...
    """

    serializer = ArticleHeavySerializer

    def test_add_relation_in_the_article_that_does_not_exist(self):
        relationdata = {
            "article_id": 1,
            "collections": [1],
            "tags": [1],
        }
        response_add = self.admin_client.put(
            "/api/article/relations/" + str(1000) + "/", relationdata,
        )
        response_remove = self.admin_client.delete(
            "/api/article/relations/" + str(1000) + "/", relationdata,
        )
        self.assertEqual(response_add.status_code, 404)
        self.assertEqual(response_remove.status_code, 404)

    def test_add_relations(self):
        # oldvalues = self.serializer(
        #     Article.objects.get(id=1)
        # )
        relationdata = {
            "article_id": 1,
            "collections": [1],
            "tags": [1],
        }
        response = self.admin_client.put(
            "/api/article/relations/" + str(1) + "/", relationdata,
        )
        # print(response.data)
        newvalues = self.serializer(Article.objects.get(id=1))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(newvalues.data, response.data)

    def test_add_elements_that_do_not_exist_to_the_relationship(self):
        oldvalues = self.serializer(Article.objects.get(id=1))
        relationdata = {
            "article_id": 1,
            "collections": [1, 10000],
            "tags": [1, 20000],
        }
        response = self.admin_client.put(f"/api/article/relations/{1}/", relationdata)
        # print(response.data)
        values = self.serializer(Article.objects.get(id=1))
        self.assertEqual(response.status_code, 400)
        self.assertEqual(values.data, oldvalues.data)

    def test_error_parameters_collection_add_relations(self):
        oldvalues = self.serializer(Article.objects.get(id=1))
        relationdata = {
            "art_id": 1,
            "cls": [1],
            "tgs": [1],
        }
        response = self.admin_client.put(f"/api/article/relations/{1}/", relationdata)
        newvalues = self.serializer(Article.objects.get(id=1))
        self.assertEqual(response.status_code, 400)
        self.assertEqual(newvalues.data, oldvalues.data)

    def test_remove_relations(self):
        """
        ...
        """
        relationdata = {
            "article_id": 1,
            "collections": [1, 2, 3],
            "tags": [1, 3],
        }

        article = Article.objects.get(pk=relationdata["article_id"])

        for collection_id in relationdata["collections"]:
            collection = Collection.objects.get(pk=collection_id)
            article.collections.add(collection)

        for tag_id in relationdata["tags"]:
            tag = Tag.objects.get(pk=tag_id)
            article.tags.add(tag)

        response = self.admin_client.put(f"/api/article/relations/{1}/", relationdata,)
        # oldvalues = self.serializer(
        #     Article.objects.get(id=1),
        # )
        response = self.admin_client.delete(
            f"/api/article/relations/{1}/", relationdata
        )
        # print(response.data)
        newvalues = self.serializer(Article.objects.get(id=1))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(newvalues.data, response.data)

    def test_error_parameters_collection_remove_relations(self):
        oldvalues = self.serializer(Article.objects.get(id=1))
        relationdata = {
            "art_id": 1,
            "cls": [1],
            "tgs": [1],
        }
        response = self.admin_client.delete(
            f"/api/article/relations/{1}/", relationdata
        )
        newvalues = self.serializer(Article.objects.get(id=1))
        self.assertEqual(response.status_code, 400)
        self.assertEqual(newvalues.data, oldvalues.data)

    def test_remove_elements_that_do_not_exist_to_the_relationship(self):
        oldvalues = self.serializer(Article.objects.get(id=1))
        relationdata = {
            "article_id": 1,
            "collection": [1, 10000],
            "tags": [1, 20000],
        }
        response = self.admin_client.delete(
            f"/api/article/relations/{1}/", relationdata
        )
        # print(response.data)
        values = self.serializer(Article.objects.get(id=1))
        self.assertEqual(response.status_code, 400)
        self.assertEqual(values.data, oldvalues.data)
