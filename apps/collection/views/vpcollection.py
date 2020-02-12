# third-party
# Django
# from django.http import Http404
# from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny

# from rest_framework.response import Response
from rest_framework.views import APIView

# local Django
from apps.collection.models import Collection
from apps.collection.serializers import CollectionSlugSerializer


class VCollectionSlugList(APIView, PageNumberPagination):
    permission_classes = (AllowAny,)
    serializer = CollectionSlugSerializer

    def get(self, request, format=None):
        # consulta
        listr = Collection.objects.all().order_by("id")
        # respuesta
        results = self.paginate_queryset(listr, request)
        serializer = self.serializer(results, many=True)
        return self.get_paginated_response(serializer.data)
