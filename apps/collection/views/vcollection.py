# third-party
from django.db import transaction

# Django
from django.http import Http404
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

# local Django
from apps.category.models import Category
from apps.collection.models import Collection
from apps.collection.serializers import (
    CollectionHeavySerializer,
    CollectionRelationSerializer,
    CollectionSerializer,
)
from apps.tag.models import Tag


class VCollectionList(APIView, PageNumberPagination):
    permission_classes = (IsAdminUser,)
    serializer = CollectionSerializer

    def get(self, request, format=None):
        # consulta
        listr = Collection.objects.all().order_by("id")
        # respuesta
        results = self.paginate_queryset(listr, request)
        serializer = CollectionHeavySerializer(results, many=True)
        return self.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        # return Response(request.data, status=status.HTTP_201_CREATED)
        response = self.serializer(data=request.data)
        if response.is_valid():
            result = response.save()
            res = CollectionHeavySerializer(result)
            return Response(res.data, status=status.HTTP_201_CREATED)

        return Response(response.errors, status=status.HTTP_400_BAD_REQUEST)


class VCollectionDetail(APIView):
    permission_classes = (IsAdminUser,)
    serializer = CollectionHeavySerializer

    def get_object(self, pk):
        try:
            return Collection.objects.get(pk=pk)
        except Collection.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        response = self.serializer(self.get_object(pk))
        return Response(response.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        response = CollectionSerializer(self.get_object(pk), data=request.data)
        if response.is_valid():
            response.save()
            res = self.serializer(self.get_object(pk))
            return Response(res.data, status=status.HTTP_200_OK)

        return Response(response.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        collection = self.get_object(pk)
        collection.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class VCollectionRelation(APIView):
    """
    edicion relaciones muchos a muchos
    """

    permission_classes = (IsAdminUser,)
    serializer = CollectionRelationSerializer

    def get_object(self, pk):
        return Collection.objects.get(pk=pk)

    @transaction.atomic
    def put(self, request, pk, format=None):
        try:
            with transaction.atomic():
                response = self.serializer(data=request.data)
                if response.is_valid():
                    response.save()
                    res = CollectionHeavySerializer(self.get_object(pk))
                    return Response(res.data, status=status.HTTP_200_OK)

                return Response(response.errors, status=status.HTTP_400_BAD_REQUEST)
        except Collection.DoesNotExist:
            raise Http404
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

    @transaction.atomic
    def delete(self, request, pk, format=None):
        try:
            with transaction.atomic():
                response = self.serializer(data=request.data)
                if response.is_valid():

                    collection = self.get_object(pk)

                    for category_id in response.validated_data["categories"]:
                        category = Category.objects.get(id=category_id)
                        collection.categories.remove(category)

                    for tag_id in response.validated_data["tags"]:
                        tag = Tag.objects.get(id=tag_id)
                        collection.tags.remove(tag)

                    res = CollectionHeavySerializer(self.get_object(pk))
                    return Response(res.data, status=status.HTTP_200_OK)

                return Response(response.errors, status=status.HTTP_400_BAD_REQUEST)
        except Collection.DoesNotExist:
            raise Http404
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
