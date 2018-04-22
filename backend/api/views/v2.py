#formato
import json

#retornar respuesta url
from django.http import HttpResponse

#vista generica
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView

#paginacion
from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination

#renderizado
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response


#serializadores
from backend.api.serializers import Item_serializer, Collection_serializer, Item_type_serializer, Tag_serializer, Category_serializer, Theme_serializer

#modelos
from backend.storage.models import Item_type, Tag, Collection, Item, Category, Theme

#vistas

#serializador api

class Item_APIv2(ListAPIView):

	queryset = Item.objects.all().prefetch_related('tags','colecciones')
	serializer_class = Item_serializer
	pagination_class = PageNumberPagination
	

class Theme_APIv2(ListAPIView):

	queryset = Theme.objects.all()
	serializer_class = Theme_serializer
	pagination_class = LimitOffsetPagination

class Tag_APIv2(ListAPIView):

	queryset = Tag.objects.all()
	serializer_class = Tag_serializer
	pagination_class = LimitOffsetPagination

class Collection_APIv2(ListAPIView):

	queryset = Collection.objects.all().prefetch_related('categorias')
	serializer_class = Collection_serializer
	pagination_class = LimitOffsetPagination

class Item_type_APIv2(ListAPIView):

	queryset = Item_type.objects.all()
	serializer_class = Item_type_serializer
	pagination_class = LimitOffsetPagination

class Category_APIv2(ListAPIView):

	queryset = Category.objects.all()
	serializer_class = Category_serializer
	pagination_class = LimitOffsetPagination