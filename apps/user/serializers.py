# third-party
from rest_framework import serializers
from rest_framework.views import exception_handler
from rest_framework.exceptions import APIException

# Django
from django.contrib.auth import authenticate
from django.contrib.auth.models import User, Group


class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ('id', 'username', 'email', 'first_name', 'last_name', 'is_staff')

class UserRegisterSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = User
    fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name', 'is_staff')

  def create(self, validated_data):
    user = User.objects.create_user(
      validated_data['username'],
      validated_data['email'],
      validated_data['password'],
    )
    return user.id

class GroupSerializer(serializers.ModelSerializer):
  class Meta:
    model = Group
    fields = ('url', 'name')

class AuthTokenSerializer(serializers.Serializer):
  email = serializers.EmailField()
  password = serializers.CharField(max_length=40)

  def validate(self, data):
    email = data.get('email')
    password = data.get('password')

    if email and password:
      try:
        userdata = User.objects.get(email__exact= email)
      except:
        msg = ('User no exist.')
        raise APIException(msg)

      user = authenticate(username=userdata.username, password=password)

      if user:
        if not user.is_active:
          msg = ('User account is disabled.')
          raise APIException(msg)
      else:
        msg = ('Unable to log in with provided credentials.')
        raise APIException(msg)
    else:
      msg = ('Must include "email" and "password".')
      raise APIException(msg)

    data['user'] = user
    return data