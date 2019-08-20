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
from apps.collection.serializers import CollectionSerializer, CollectionUpdateSerializer, CollectionHeavySerializer

class VCollectionList(APIView):
  permission_classes = (IsAdminUser,)

  def get(self, request, format=None):
    # consulta
    listr = Collection.objects.all()
    # respuesta
    response = CollectionHeavySerializer(listr, many=True)
    return Response(response.data, status=status.HTTP_200_OK)

  @transaction.atomic
  def post(self, request, format=None):
    # return Response(request.data, status=status.HTTP_201_CREATED)
    response = CollectionUpdateSerializer(data=request.data)
    if response.is_valid():
      result = response.save()
      if type(result) == str:
        return Response(result, status=status.HTTP_400_BAD_REQUEST)
      else:
        res = CollectionHeavySerializer(result)
        return Response(res.data, status=status.HTTP_201_CREATED)
    else:
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

  @transaction.atomic
  def put(self, request, pk, format=None):
    response = CollectionSerializer(self.get_object(pk), data=request.data)
    if response.is_valid():
      result = response.save()
      if type(result) == str:
        return Response(result, status=status.HTTP_400_BAD_REQUEST)
      else:
        res = self.serializer(result)
        return Response(res.data, status=status.HTTP_201_CREATED)
    else:
      return Response(response.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk, format=None):
    collection = self.get_object(pk)
    collection.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)