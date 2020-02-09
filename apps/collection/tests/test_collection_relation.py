# standard library
# import json

# local Django
from apps.category.models import Category
from apps.collection.models import Collection
from apps.collection.serializers import CollectionHeavySerializer
from apps.tag.models import Tag
from apps.tests.fixtures import RepositoryTestCase


class CollectionRelationTest(RepositoryTestCase):
    """
    ...
    """
    serializer = CollectionHeavySerializer

    def test_update_the_collection_that_does_not_exist(self):
        relationdata = {
            'collection_id': 1,
            'categories': [1],
            'tags': [1],
        }
        response_add = self.admin_client.put(
            f'/api/collection/relations/{10000}/',
            relationdata
        )
        response_remove = self.admin_client.delete(
            f'/api/collection/relations/{10000}/',
            relationdata
        )
        self.assertEqual(response_add.status_code, 404)
        self.assertEqual(response_remove.status_code, 404)

    def test_collection_add_relations(self):
        # oldvalues = self.serializer(
        #     Collection.objects.get(id=1)
        # )
        relationdata = {
            'collection_id': 1,
            'categories': [1],
            'tags': [1],
        }
        response = self.admin_client.put(
            f'/api/collection/relations/{1}/',
            relationdata
        )
        # print(response.data)
        newvalues = self.serializer(
            Collection.objects.get(id=1)
        )
        self.assertEqual(response.status_code, 200)
        # self.assertNotEqual(oldvalues.data, response.data)
        self.assertEqual(newvalues.data, response.data)

    def test_add_elements_that_do_not_exist_to_the_relationship(self):
        oldvalues = self.serializer(
            Collection.objects.get(id=1)
        )
        relationdata = {
            'collection_id': 1,
            'categories': [1, 10000],
            'tags': [1, 20000],
        }
        response = self.admin_client.put(
            f'/api/collection/relations/{1}/',
            relationdata
        )
        # print(response.data)
        values = self.serializer(
            Collection.objects.get(id=1)
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(values.data, oldvalues.data)

    def test_error_parameters_collection_add_relations(self):
        oldvalues = self.serializer(
            Collection.objects.get(id=1)
        )
        relationdata = {
            'col_id': 1,
            'cts': [1],
            'tgs': [1],
        }
        response = self.admin_client.put(
            f'/api/collection/relations/{1}/',
            relationdata
        )
        newvalues = self.serializer(
            Collection.objects.get(id=1)
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(newvalues.data, oldvalues.data)

    def test_collection_remove_relations(self):
        """
        ...
        """
        collection = Collection.objects.get(id=1)

        for category_id in [1, 2]:
            category = Category.objects.get(id=category_id)
            collection.categories.add(category)

        for tag_id in [1, 2]:
            tag = Tag.objects.get(id=tag_id)
            collection.tags.add(tag)

        # oldvalues = self.serializer(
        #     Collection.objects.get(id=1)
        # )

        relationdata = {
            'collection_id': 1,
            'categories': [1],
            'tags': [1],
        }

        response = self.admin_client.delete(
            f'/api/collection/relations/{1}/',
            relationdata
        )
        # print(response.data)
        newvalues = self.serializer(
            Collection.objects.get(id=1)
        )
        self.assertEqual(response.status_code, 200)
        # self.assertNotEqual(oldvalues.data, response.data)
        self.assertEqual(newvalues.data, response.data)

    def test_error_parameters_collection_remove_relations(self):
        oldvalues = self.serializer(
            Collection.objects.get(id=1)
        )
        relationdata = {
            'col_id': 1,
            'cts': [1],
            'tgs': [1],
        }
        response = self.admin_client.delete(
            f'/api/collection/relations/{1}/',
            relationdata
        )
        newvalues = self.serializer(
            Collection.objects.get(id=1)
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(newvalues.data, oldvalues.data)

    def test_remove_elements_that_do_not_exist_to_the_relationship(self):
        oldvalues = self.serializer(
            Collection.objects.get(id=1)
        )
        relationdata = {
            'collection_id': 1,
            'categories': [1, 10000],
            'tags': [1, 20000],
        }
        response = self.admin_client.delete(
            f'/api/collection/relations/{1}/',
            relationdata
        )
        # print(response.data)
        values = self.serializer(
            Collection.objects.get(id=1)
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(values.data, oldvalues.data)
