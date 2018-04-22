from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

#modelos
from backend.storage.models import Item_type, Tag, Collection, Item, Category, Theme
from django.shortcuts import get_object_or_404

#serializadores
from backend.api.serializers import Item_serializer, Collection_serializer, Item_type_serializer, Tag_serializer, Category_serializer, Theme_serializer


@api_view(['GET'])
def Item_id(request, pk):

	item = get_object_or_404(Item, id=pk)
	if request.method == 'GET':
		serializer = Item_serializer(item)
		return Response(serializer.data)