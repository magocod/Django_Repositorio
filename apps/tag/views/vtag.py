"""
Vistas edicion tag
"""

# standard library
from typing import Union

# Django
from django.http import Http404
from rest_framework import status
from rest_framework.permissions import IsAdminUser

# third-party
from rest_framework.response import Response
from rest_framework.views import APIView

# local Django
from apps.tag.models import Tag
from apps.tag.serializers import TagSerializer


class VTagList(APIView):
    """
    Listar y guardar
    """

    permission_classes = (IsAdminUser,)
    serializer = TagSerializer

    def get(self, request, format=None):
        """
        ...
        """
        listr = Tag.objects.all()
        response = self.serializer(listr, many=True)
        return Response(response.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        """
        ...
        """
        response = self.serializer(data=request.data)
        if response.is_valid():
            response.save()
            return Response(response.data, status=status.HTTP_201_CREATED)

        return Response(response.errors, status=status.HTTP_400_BAD_REQUEST)


class VTagDetail(APIView):
    """
    Busqueda, edicion, eliminacion -> id
    """

    permission_classes = (IsAdminUser,)
    serializer = TagSerializer

    @staticmethod
    def get_object(pk_tag: Union[int, str]):
        """
        buscar tag
        """
        try:
            return Tag.objects.get(pk=pk_tag)
        except Tag.DoesNotExist:
            raise Http404

    def get(self, request, pk: Union[int, str], format=None):
        """
        ...
        """
        tag = self.get_object(pk)
        response = self.serializer(tag)
        return Response(response.data, status=status.HTTP_200_OK)

    def put(self, request, pk: Union[int, str], format=None):
        """
        ...
        """
        tag = self.get_object(pk)
        response = self.serializer(tag, data=request.data)
        if response.is_valid():
            response.save()
            return Response(response.data, status=status.HTTP_200_OK)

        return Response(response.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk: Union[int, str], format=None):
        """
        ...
        """
        tag = self.get_object(pk)
        tag.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
