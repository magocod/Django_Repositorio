# third-party
# Django
from django.http import Http404
from rest_framework import status
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

# local Django
from apps.article.models import Article, Specification
from apps.article.serializers.article import ArticleHeavySerializer
from apps.article.serializers.specification import SpecificationSerializer


class VSpecificationList(APIView):
  permission_classes = (IsAdminUser,)
  serializer = SpecificationSerializer

  def get_article(self, pk):
    try:
      return Article.objects.get(pk=pk)
    except Article.DoesNotExist:
      raise Http404

  def post(self, request, format=None):
    response = self.serializer(data=request.data)
    if response.is_valid():
      response.save()
      res = ArticleHeavySerializer(
        self.get_article(response.data['article_id'])
      )
      return Response(res.data, status=status.HTTP_201_CREATED)

    else:
      return Response(response.errors, status=status.HTTP_400_BAD_REQUEST)

class VSpecificationDetail(APIView):
  permission_classes = (IsAdminUser,)
  serializer = SpecificationSerializer

  def get_object(self, pk):
    try:
      return Specification.objects.get(pk=pk)
    except Specification.DoesNotExist:
      raise Http404

  def get_article(self, pk):
    try:
      return Article.objects.get(pk=pk)
    except Article.DoesNotExist:
      raise Http404

  def put(self, request, pk, format=None):
    specification = self.get_object(pk)
    response = self.serializer(specification, data=request.data)
    if response.is_valid():
      response.save()
      res = ArticleHeavySerializer(
        self.get_article(response.data['article_id'])
      )
      return Response(res.data, status=status.HTTP_200_OK)
    else:
      return Response(response.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk, format=None):
    specification = self.get_object(pk)
    specification.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
