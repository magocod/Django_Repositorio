#formato
import json

#retornar respuesta url
from django.http import HttpResponse

#vista generica
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView

#paginacion
from rest_framework.pagination import LimitOffsetPagination

#renderizado
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

#consultas
from backend.seeker.queries import registros_totales, lista_elementosv2

#serializadores
from backend.api.serializers import Item_serializer, Collection_serializer, Item_type_serializer, Tag_serializer, Category_serializer, Theme_serializer

#modelos
from backend.storage.models import Item_type, Tag, Collection, Item, Category, Theme

#serializador api
class Item_APIv1(APIView):

	serializer = Item_serializer

	#sobreescribir
	def get(self, request, format=None):
		#consulta
		lista = Item.objects.all().prefetch_related('tags','colecciones')
		#respuesta
		response = self.serializer(lista, many=True)

		return HttpResponse(json.dumps(response.data), content_type='application/json')
		
		
class Collection_APIv1(APIView):
	serializer = Collection_serializer

	#sobreescribir
	def get(self, request, format=None):
		#consulta
		lista = Collection.objects.all().prefetch_related('categorias')
		#respuesta
		response = self.serializer(lista, many=True)

		return HttpResponse(json.dumps(response.data), content_type='application/json')

class Item_type_APIv1(APIView):
	serializer = Item_type_serializer

	#sobreescribir
	def get(self, request, format=None):
		#consulta
		lista = Item_type.objects.all()
		#respuesta
		response = self.serializer(lista, many=True)

		return HttpResponse(json.dumps(response.data), content_type='application/json')

class Tag_APIv1(APIView):
	serializer = Tag_serializer

	#sobreescribir
	def get(self, request, format=None):
		#consulta
		lista = Tag.objects.all()
		#respuesta
		response = self.serializer(lista, many=True)

		return HttpResponse(json.dumps(response.data), content_type='application/json')

class Category_APIv1(APIView):
	serializer = Category_serializer

	#sobreescribir
	def get(self, request, format=None):
		#consulta
		lista = Category.objects.all()
		#respuesta
		response = self.serializer(lista, many=True)

		return HttpResponse(json.dumps(response.data), content_type='application/json')

class Theme_APIv1(APIView):
	serializer = Theme_serializer

	#sobreescribir
	def get(self, request, format=None):
		#consulta
		lista = Theme.objects.all()
		#respuesta
		response = self.serializer(lista, many=True)

		return HttpResponse(json.dumps(response.data), content_type='application/json')



#renderizado
class Records_API(APIView):
	#renderizador
    renderer_classes = (JSONRenderer, )

    def get(self, request, format=None):
    	#consulta
        registros = registros_totales()
        #data en arreglo
        content = {'registros': registros}
        return Response(content)

#renderizado
class List_API(APIView):
	#renderizador
    renderer_classes = (JSONRenderer, )

    def get(self, request, format=None):
    	#consulta
        lista_elementos = lista_elementosv2()
        #data en arreglo
        content = {'registros': lista_elementos}
        return Response(content)

