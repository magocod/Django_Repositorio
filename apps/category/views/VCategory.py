"""
Vistas edicion categorias
"""

# standard library
from typing import Union

# Django
from django.http import Http404
# third-party
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

# local Django
from apps.category.models import Category
from apps.category.serializers import CategorySerializer


class VCategoryList(APIView, PageNumberPagination):
    """
    ...
    """
    permission_classes = (IsAdminUser,)
    serializer = CategorySerializer

    def get(self, request, format=None):
        """
        ...
        """
        listr = Category.objects.all().order_by('id')
        results = self.paginate_queryset(listr, request)
        serializer = self.serializer(results, many=True)
        return self.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        """
        ...
        """
        response = self.serializer(data=request.data)
        if response.is_valid():
            response.save()
            return Response(response.data, status=status.HTTP_201_CREATED)

        return Response(response.errors, status=status.HTTP_400_BAD_REQUEST)


class VCategoryDetail(APIView):
    """
    ...
    """
    permission_classes = (IsAdminUser,)
    serializer = CategorySerializer

    def get_object(self, pk_category: Union[int, str]):
        """
        ...
        """
        try:
            return Category.objects.get(pk=pk_category)
        except Category.DoesNotExist:
            raise Http404

    def get(self, request, pk: Union[int, str], format=None):
        """
        ...
        """
        category = self.get_object(pk)
        response = self.serializer(category)
        return Response(response.data, status=status.HTTP_200_OK)

    def put(self, request, pk: Union[int, str], format=None):
        """
        ...
        """
        category = self.get_object(pk)
        response = self.serializer(category, data=request.data)
        if response.is_valid():
            response.save()
            return Response(response.data, status=status.HTTP_200_OK)

        return Response(response.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk: Union[int, str], format=None):
        """
        ...
        """
        category = self.get_object(pk)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
