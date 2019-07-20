# third-party
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAdminUser

# Django
from django.http import Http404
from django.db import transaction

# local Django
from apps.collection.models import Collection
from apps.collection.serializers import CollectionSerializer, CollectionUpdateSerializer

class VCollectionList(APIView):
  permission_classes = (IsAdminUser,)
  serializer = CollectionSerializer

  def get(self, request, format=None):
    # consulta
    listr = Collection.objects.all()
    # respuesta
    response = self.serializer(listr, many=True)
    return Response(response.data, status=status.HTTP_200_OK)

  @transaction.atomic
  def post(self, request, format=None):
    # return Response(request.data, status=status.HTTP_201_CREATED)
    response = CollectionUpdateSerializer(data=request.data)
    if response.is_valid():
      response.save()
      return Response(response.data, status=status.HTTP_201_CREATED)

    else:
      return Response(response.errors, status=status.HTTP_400_BAD_REQUEST)


class VCollectionDetail(APIView):
  permission_classes = (IsAdminUser,)
  serializer = CollectionSerializer

  def get_object(self, pk):
    try:
      return Collection.objects.get(pk=pk)
    except Collection.DoesNotExist:
      raise Http404

  def get(self, request, pk, format=None):
    collection = self.get_object(pk)
    response = self.serializer(collection)
    return Response(response.data, status=status.HTTP_200_OK)

  @transaction.atomic
  def put(self, request, pk, format=None):
    collection = self.get_object(pk)
    response = CollectionUpdateSerializer(collection, data=request.data)
    if response.is_valid():
      response.save()
      return Response(response.data, status=status.HTTP_200_OK)
    else:
      return Response(response.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk, format=None):
    collection = self.get_object(pk)
    collection.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)