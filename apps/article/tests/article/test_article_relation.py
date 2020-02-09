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

    def test_add_relations(self):
        # oldvalues = self.serializer(
        #     Article.objects.get(id=1)
        # )
        relationdata = {
            'article_id': 1,
            'collections': [1],
            'tags': [1],
        }
        response = self.admin_client.put(
            '/api/article/relations/' + str(1) + '/',
            relationdata,
        )
        # print(response.data)
        newvalues = self.serializer(
            Article.objects.get(id=1)
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(newvalues.data, response.data)

    def test_remove_relations(self):
        """
        ...
        """
        relationdata = {
            'article_id': 1,
            'collections': [1, 2, 3],
            'tags': [1, 3],
        }

        article = Article.objects.get(pk=relationdata['article_id'])

        for collection_id in relationdata['collections']:
            collection = Collection.objects.get(pk=collection_id)
            article.collections.add(collection)

        for tag_id in relationdata['tags']:
            tag = Tag.objects.get(pk=tag_id)
            article.tags.add(tag)

        response = self.admin_client.put(
            f'/api/article/relations/{1}/',
            relationdata,
        )
        # oldvalues = self.serializer(
        #     Article.objects.get(id=1),
        # )
        response = self.admin_client.delete(
            f'/api/article/relations/{1}/',
            relationdata
        )
        # print(response.data)
        newvalues = self.serializer(
            Article.objects.get(id=1)
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(newvalues.data, response.data)

    def test_add_relation_in_the_article_that_does_not_exist(self):
        relationdata = {
            'article_id': 1,
            'collections': [1],
            'tags': [1],
        }
        response = self.admin_client.put(
            '/api/article/relations/' + str(1000) + '/',
            relationdata,
        )
        self.assertEqual(response.status_code, 404)
