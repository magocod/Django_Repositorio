#formato
import json

#xml
from rest_framework_xml.parsers import XMLParser
from rest_framework_xml.renderers import XMLRenderer

#retornar respuesta url
from django.http import HttpResponse

#vista generica
from rest_framework.viewsets import ModelViewSet

#paginacion
from rest_framework.pagination import LimitOffsetPagination

#renderizado
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response


#serializadores
from backend.api.serializers import Item_serializer, Collection_serializer, Item_type_serializer, Tag_serializer, Category_serializer, Theme_serializer, Item_type_serializerv2

#modelos
from backend.storage.models import Item_type, Tag, Collection, Item, Category, Theme

#vistas

#rest

class Collection_viewset(ModelViewSet):
    
    #API endpoint that allows users to be viewed or edited.
    queryset = Collection.objects.order_by('id').prefetch_related('categorias')
    serializer_class = Collection_serializer

class Item_viewset(ModelViewSet):
    
    #API endpoint that allows users to be viewed or edited.
    queryset = Item.objects.order_by('id').prefetch_related('tags','colecciones')
    serializer_class = Item_serializer

class Item_typeviewset(ModelViewSet):
    queryset = Item_type.objects.all()
    serializer_class = Item_type_serializerv2
    parser_classes = (XMLParser,)
    renderer_classes = (XMLRenderer,)


