#filtros
from backend.seeker.filters import Item_filter, Theme_filter, Collection_filter

#paginador django
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

#añade contexto a plantilla
from django.shortcuts import render

#modelos
from backend.storage.models import Collection, Item, Theme
from django.shortcuts import get_object_or_404

#vistas

def Theme_searchv1(request):
    theme_list = Theme.objects.all()
    theme_filter = Theme_filter(request.GET, queryset=theme_list)
    return render(request, 'seeker/theme/base.html', {'filter': theme_filter})

def Theme_search_collection(request, pk):
	collection_list = Collection.objects.filter(tema=pk)
	collection_filter = Collection_filter(request.GET, queryset=collection_list)
	return render(request, 'seeker/theme/collection.html', {'filter': collection_filter})

def Theme_search_items(request, pk):
	#busqueda de la coleccion
	coleccion = get_object_or_404(Collection, id=pk)

	item_list = coleccion.items.all()

	item_filter = Collection_filter(request.GET, queryset=item_list)
	return render(request, 'seeker/theme/item.html', {'filter': item_filter})