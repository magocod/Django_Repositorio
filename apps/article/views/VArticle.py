# third-party
# Django
from django.db import transaction
from django.http import Http404
from rest_framework import status
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

# local Django
from apps.article.models import Article
from apps.article.serializers.article import (
    ArticleHeavySerializer,
    ArticleRelationSerializer,
    ArticleSerializer,
)
from apps.collection.models import Collection
from apps.tag.models import Tag


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
        response = ArticleHeavySerializer(article)
        return Response(response.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        article = self.get_object(pk)
        response = self.serializer(article, data=request.data)
        if response.is_valid():
            response.save()
            res = ArticleHeavySerializer(
                self.get_object(pk)
            )
            return Response(res.data, status=status.HTTP_200_OK)

        return Response(response.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        article = self.get_object(pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class VArticleRelation(APIView):
    """
    edicion relaciones muchos a muchoa
    """
    permission_classes = (IsAdminUser,)
    serializer = ArticleRelationSerializer

    def get_object(self, pk):
        try:
            return Article.objects.get(pk=pk)
        except Article.DoesNotExist:
            raise Http404

    @transaction.atomic
    def put(self, request, pk, format=None):
        response = self.serializer(data=request.data)
        if response.is_valid():
            response.save()
            res = ArticleHeavySerializer(
                self.get_object(pk)
            )
            return Response(res.data, status=status.HTTP_200_OK)

        return Response(response.errors, status=status.HTTP_400_BAD_REQUEST)

    @transaction.atomic
    def delete(self, request, pk, format=None):
        response = self.serializer(data=request.data)
        if response.is_valid():

            article = self.get_object(pk)

            for collection_id in response.validated_data['collections']:
                collection = Collection.objects.get(id=collection_id)
                article.collections.remove(collection)

            for tag_id in response.validated_data['tags']:
                tag = Tag.objects.get(id=tag_id)
                article.tags.remove(tag)

            res = ArticleHeavySerializer(
                self.get_object(pk)
            )
            return Response(res.data, status=status.HTTP_200_OK)

        return Response(response.errors, status=status.HTTP_400_BAD_REQUEST)
