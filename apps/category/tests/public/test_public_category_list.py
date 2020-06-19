"""
...
"""

# Django
from django.conf import settings

# local Django
from apps.category.models import Category
from apps.category.serializers import CategorySlugSerializer
from apps.tests.fixtures import RepositoryTestCase


PAGE_SIZE = settings.REST_FRAMEWORK["PAGE_SIZE"]


class CategoryPublicListTest(RepositoryTestCase):
    """
    ...
    """

    serializer = CategorySlugSerializer

    def test_request_all_categories_without_parameters_in_the_route(self):
        """
        ...
        """
        response = self.admin_client.get("/api/categories/collections/")
        serializer = self.serializer(Category.objects.all()[:PAGE_SIZE], many=True,)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data["results"]), PAGE_SIZE)
        self.assertEqual(serializer.data, response.data["results"])

    def test_request_all_categories_with_parameters_in_the_route(self):
        """
        ...
        """
        response = self.admin_client.get("/api/categories/collections/?page=2")
        serializer = self.serializer(
            Category.objects.all()[PAGE_SIZE : PAGE_SIZE + PAGE_SIZE], many=True,
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data["results"]), PAGE_SIZE)
        self.assertEqual(serializer.data, response.data["results"])
