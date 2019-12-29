# standard library
# import json

# Django
from django.test import TestCase
# third-party
from rest_framework.test import APIClient

# local Django
from apps.collection.models import Collection
from apps.collection.serializers import CollectionHeavySerializer
from apps.tests.auth import create_user
from apps.tests.db import db_populate


class CollectionRelationTest(TestCase):
    """
    ...
    """
    serializer = CollectionHeavySerializer

    def setUp(self):
        # user an token
        auth = create_user(True)
        self.client = APIClient()
        self.client.credentials(
            HTTP_AUTHORIZATION='Token ' + auth['token'].key
        )
        # data
        db_populate(tag=1, category=1, collection=1)

    def test_collection_add_relations(self):
        # oldvalues = self.serializer(
        #     Collection.objects.get(id=1)
        # )
        relationdata = {
            'collection_id': 1,
            'categories': [1],
            'tags': [1],
        }
        response = self.client.put(
            '/api/collection/relations/' + str(1) + '/',
            relationdata
        )
        # print(response.data)
        newvalues = self.serializer(
            Collection.objects.get(id=1)
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(newvalues.data, response.data)

    def test_collection_remove_relations(self):
        relationdata = {
            'collection_id': 1,
            'categories': [1],
            'tags': [1],
        }
        response = self.client.put(
            '/api/collection/relations/' + str(1) + '/',
            relationdata
        )
        # oldvalues = self.serializer(
        #     Collection.objects.get(id=1)
        # )
        response = self.client.delete(
            '/api/collection/relations/' + str(1) + '/',
            relationdata
        )
        # print(response.data)
        newvalues = self.serializer(
            Collection.objects.get(id=1)
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(newvalues.data, response.data)
