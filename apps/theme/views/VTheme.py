# third-party
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAdminUser

# Django
from django.http import Http404

# local Django
from apps.theme.models import Theme
from apps.theme.serializers import ThemeSerializer

class VThemeList(APIView):
  permission_classes = (IsAdminUser,)
  serializer = ThemeSerializer

  def get(self, request, format=None):
    # consulta
    listr = Theme.objects.all()
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


class VThemeDetail(APIView):
  permission_classes = (IsAdminUser,)
  serializer = ThemeSerializer

  def get_object(self, pk):
    try:
      return Theme.objects.get(pk=pk)
    except Theme.DoesNotExist:
      raise Http404

  def get(self, request, pk, format=None):
    theme = self.get_object(pk)
    response = self.serializer(theme)
    return Response(response.data, status=status.HTTP_200_OK)

  def put(self, request, pk, format=None):
    theme = self.get_object(pk)
    response = self.serializer(theme, data=request.data)
    if response.is_valid():
      response.save()
      return Response(response.data, status=status.HTTP_200_OK)
    else:
      return Response(response.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk, format=None):
    theme = self.get_object(pk)
    theme.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)