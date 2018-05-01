#formato
import json

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

#retornar respuesta url
from django.http import HttpResponse

from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination

#modelos
from backend.storage.models import Item_type, Tag, Collection, Item, Category, Theme
from django.shortcuts import get_object_or_404

#serializadores
from backend.api.serializers import Item_serializer, Collection_serializer, Item_type_serializer, Tag_serializer, Category_serializer, Theme_serializer

#items

@api_view(['GET'])
def Item_id(request, pk):

	item = get_object_or_404(Item, id=pk)
	if request.method == 'GET':
		serializer = Item_serializer(item)
		#return Response(serializer.data)
		return HttpResponse(json.dumps(serializer.data), content_type='application/json')

@api_view(["GET"])
def Item_list(request):

    pagination_class = PageNumberPagination
    paginator = pagination_class()

    queryset = Item.objects.all()
    page = paginator.paginate_queryset(queryset, request)

    serializer = Item_serializer(page, many=True)

    #return paginator.get_paginated_response(serializer.data)
    response = paginator.get_paginated_response(serializer.data)
    return HttpResponse(json.dumps(response.data), content_type='application/json')

@api_view(["GET"])
def Item_letters(request, slug):

    pagination_class = PageNumberPagination
    paginator = pagination_class()

    queryset = Item.objects.filter(nombre__contains=slug).select_related('tipo')
    page = paginator.paginate_queryset(queryset, request)

    serializer = Item_serializer(page, many=True)

    #return paginator.get_paginated_response(serializer.data)
    response = paginator.get_paginated_response(serializer.data)
    return HttpResponse(json.dumps(response.data), content_type='application/json')

#categorias
@api_view(["GET"])
def Categories_list(request):

    pagination_class = PageNumberPagination
    paginator = pagination_class()

    queryset = Category.objects.all()
    page = paginator.paginate_queryset(queryset, request)

    serializer = Category_serializer(page, many=True)

    #return paginator.get_paginated_response(serializer.data)
    response = paginator.get_paginated_response(serializer.data)
    return HttpResponse(json.dumps(response.data), content_type='application/json')