# standard library
import json

# local Django
from apps.article.models import Article
from apps.article.serializers.article import ArticleHeavySerializer
from apps.tests.fixtures import RepositoryTestCase


class ListArticleTest(RepositoryTestCase):
    """
    ...
    """

    serializer = ArticleHeavySerializer

    def test_get_all(self):
        response = self.admin_client.get("/api/articles/")
        response_data = json.loads(response.content)
        serializer = self.serializer(Article.objects.all(), many=True,)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(serializer.data, response_data)

    def test_get_all_authenticated(self):
        response = self.public_client.get("/api/articles/")
        self.assertEqual(response.status_code, 401)
