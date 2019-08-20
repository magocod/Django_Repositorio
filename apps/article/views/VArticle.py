# third-party
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAdminUser

# Django
from django.http import Http404

# local Django
from apps.article.models import Article
from apps.article.serializers.article import ArticleSerializer, ArticleHeavySerializer

class VArticleList(APIView):
  permission_classes = (IsAdminUser,)
  serializer = ArticleSerializer

  def get_object(self, pk):
    try:
      return Article.objects.get(pk=pk)
    except Article.DoesNotExist:
      raise Http404

  def get(self, request, format=None):
    # consulta
    listr = Article.objects.all()
    # respuesta
    response = ArticleHeavySerializer(listr, many=True)
    return Response(response.data, status=status.HTTP_200_OK)

  def post(self, request, format=None):
    response = self.serializer(data=request.data)
    if response.is_valid():
      response.save()
      res = ArticleHeavySerializer(
        self.get_object(response.data['id'])
      )
      return Response(res.data, status=status.HTTP_201_CREATED)
    else:
      return Response(response.errors, status=status.HTTP_400_BAD_REQUEST)

class VArticleDetail(APIView):
  permission_classes = (IsAdminUser,)
  serializer = ArticleSerializer

  def get_object(self, pk):
    try:
      return Article.objects.get(pk=pk)
    except Article.DoesNotExist:
      raise Http404

  def get(self, request, pk, format=None):
    article = self.get_object(pk)
    response = self.serializer(article)
    return Response(response.data, status=status.HTTP_200_OK)

  def put(self, request, pk, format=None):
    article = self.get_object(pk)
    response = self.serializer(article, data=request.data)
    if response.is_valid():
      result = response.save()
      res = ArticleHeavySerializer(
        self.get_object(response.data['id'])
      )
      return Response(res.data, status=status.HTTP_201_CREATED)
    else:
      return Response(response.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk, format=None):
    article = self.get_object(pk)
    article.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)