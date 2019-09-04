# third-party
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.pagination import PageNumberPagination

# Django
from django.http import Http404

# local Django
from apps.category.models import Category
from apps.category.serializers import CategorySlugSerializer

class VCategorySlugList(APIView, PageNumberPagination):
  permission_classes = (AllowAny,)
  serializer = CategorySlugSerializer

  def get(self, request, format=None):
    # consulta
    listr = Category.objects.all().order_by('id')
    # respuesta
    results = self.paginate_queryset(listr, request)
    serializer = self.serializer(results, many=True)
    return self.get_paginated_response(serializer.data)