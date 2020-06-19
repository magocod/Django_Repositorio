"""
...
"""

# Django
from django.conf import settings

# local Django
from apps.collection.models import Collection
from apps.collection.serializers import CollectionSlugSerializer
from apps.tests.fixtures import RepositoryTestCase


PAGE_SIZE = settings.REST_FRAMEWORK["PAGE_SIZE"]


class CollectionPublicListTest(RepositoryTestCase):
    """
    ...
    """

    serializer = CollectionSlugSerializer

    def test_request_all_collections_without_parameters_in_the_route(self):
        """
        ...
        """
        response = self.public_client.get("/api/collections/slug_articles/")
        serializer = self.serializer(Collection.objects.all()[:PAGE_SIZE], many=True,)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data["results"]), PAGE_SIZE)
        self.assertEqual(serializer.data, response.data["results"])

    def test_request_all_collections_with_parameters_in_the_route(self):
        """
        ...
        """
        response = self.public_client.get("/api/collections/slug_articles/?page=1")
        serializer = self.serializer(Collection.objects.all()[:PAGE_SIZE], many=True,)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data["results"]), PAGE_SIZE)
        self.assertEqual(serializer.data, response.data["results"])
