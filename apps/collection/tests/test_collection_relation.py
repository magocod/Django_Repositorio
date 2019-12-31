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
