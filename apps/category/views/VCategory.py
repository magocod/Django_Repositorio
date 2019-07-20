# third-party
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAdminUser

# Django
from django.http import Http404

# local Django
from apps.category.models import Category
from apps.category.serializers import CategorySerializer

class VCategoryList(APIView):
  permission_classes = (IsAdminUser,)
  serializer = CategorySerializer

  def get(self, request, format=None):
    # consulta
    listr = Category.objects.all()
    # respuesta
    response = self.serializer(listr, many=True)
    return Response(response.data, status=status.HTTP_200_OK)

  def post(self, request, format=None):
    response = self.serializer(data=request.data)
    if response.is_valid():
      response.save()
      return Response(response.data, status=status.HTTP_201_CREATED)

    else:
      return Response(response.errors, status=status.HTTP_400_BAD_REQUEST)

class VCategoryDetail(APIView):
  permission_classes = (IsAdminUser,)
  serializer = CategorySerializer

  def get_object(self, pk):
    try:
      return Category.objects.get(pk=pk)
    except Category.DoesNotExist:
      raise Http404

  def get(self, request, pk, format=None):
    category = self.get_object(pk)
    response = self.serializer(category)
    return Response(response.data, status=status.HTTP_200_OK)

  def put(self, request, pk, format=None):
    category = self.get_object(pk)
    response = self.serializer(category, data=request.data)
    if response.is_valid():
      response.save()
      return Response(response.data, status=status.HTTP_200_OK)
    else:
      return Response(response.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk, format=None):
    category = self.get_object(pk)
    category.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
