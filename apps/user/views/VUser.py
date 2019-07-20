# Django
from django.contrib.auth.models import User, Group

# third-party
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser
from rest_framework import status

# local Django
from apps.user.serializers import UserSerializer, UserRegisterSerializer

class VUserList(APIView):
  permission_classes = (IsAdminUser,)
  serializer = UserSerializer

  def serialize_user(self, pk):
    try:
      user = User.objects.get(pk=pk)
      res = self.serializer(user)
      return res.data 
    except User.DoesNotExist:
      raise Http404

  def get(self, request, format=None):
    # consulta
    listr = User.objects.all()
    # respuesta
    response = self.serializer(listr, many=True)
    return Response(response.data, status=status.HTTP_200_OK)

  def post(self, request, format=None):
    response = UserRegisterSerializer(data=request.data)
    if response.is_valid():
      iduser = response.save()
      res = self.serialize_user(pk= iduser)
      return Response(res, status= status.HTTP_201_CREATED)

    else:
      return Response(response.errors, status=status.HTTP_400_BAD_REQUEST)

class VUserDetail(APIView):
  permission_classes = (IsAdminUser,)
  serializer = UserSerializer

  def get_object(self, pk):
    try:
      return User.objects.get(pk=pk)
    except User.DoesNotExist:
      raise Http404

  def get(self, request, pk, format=None):
    user = self.get_object(pk)
    response = self.serializer(user)
    return Response(response.data, status=status.HTTP_200_OK)

  def put(self, request, pk, format=None):
    user = self.get_object(pk)
    response = self.serializer(user, data=request.data)
    if response.is_valid():
      response.save()
      return Response(response.data, status=status.HTTP_200_OK)
    else:
      return Response(response.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk, format=None):
    user = self.get_object(pk)
    value = user.id
    user.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
