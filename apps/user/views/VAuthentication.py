# Django
from django.contrib.auth.models import User, Group

# third-party
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view, permission_classes, authentication_classes, parser_classes
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework import status

# local Django
from apps.user.serializers import AuthTokenSerializer

class CustomAuthToken(ObtainAuthToken):
  serializer_class = AuthTokenSerializer

  def post(self, request, *args, **kwargs):
    serializer = self.serializer_class(
      data=request.data,
      context={ 'request': request },
    )
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data['user']
    token, created = Token.objects.get_or_create(user=user)
    return Response({
      'token': token.key,
      'staff_status': user.is_staff,
      'super_user': user.is_superuser,
      'email': user.email,
      'first_name': user.first_name,
      'last_name': user.last_name,
      'username': user.username,
      'date_joined': user.date_joined,
      'id': user.id,
    }, status=status.HTTP_201_CREATED)


@api_view(['POST'])
@parser_classes((JSONParser,))
@permission_classes((AllowAny,))
def Emailexist(request, format=None):
  try:
    userdata = User.objects.get(email__exact= request.data['email'])
    return Response(status=status.HTTP_200_OK)
    # return Response({'received data': request.data['email']}, status=status.HTTP_200_OK)
  except:
    return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
@parser_classes((JSONParser,))
@authentication_classes([TokenAuthentication,])
@permission_classes([IsAuthenticated,])
def VUserLogout(request, format=None):
  try:
    # res = { 'token': request.auth.key }
    Token.objects.get(key= request.auth.key).delete()
    return Response(status=status.HTTP_200_OK)
  except Token.DoesNotExist as e:
    return Response(status=status.HTTP_200_OK)
