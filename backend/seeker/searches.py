#añade contexto a plantilla
from django.shortcuts import render

#retornar respuesta url
from django.http import HttpResponse, HttpRequest

#vista django
from django.views.generic import View, TemplateView, ListView, DetailView

#modelos
from backend.storage.models import Collection, Item, Theme, Category

from django.shortcuts import get_object_or_404

#paginador django
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


#vistas

#busqueda colecciones de categoria
def Search_category_collections(request, pk):
	categoria = get_object_or_404(Category, id=pk)
	#busqueda de la coleccion
	consulta = Collection.objects.filter(categorias=categoria.id).prefetch_related('categorias')
	#paginador
	paginator = Paginator(consulta, 20)
	page = request.GET.get('page')
	colecciones = paginator.get_page(page)
	
	#enviar data a la vista
	return render(request, 'seeker/collection/search.html', {'object_list': colecciones})

#busqueda coleccion  -> clave primaria
def Search_collection_pk(request, pk):
	#busqueda de la coleccion
	coleccion = Collection.objects.filter(id=pk).prefetch_related('categorias').get(id=pk)
	#get_object_or_404(Collection, id=pk)
	
	#enviar data a la vista
	return render(request, 'seeker/collection/detail.html', {'collection': coleccion})

#busqueda coleccion -> nombre exacto
def Search_collection_exact(request):
	#optener dato del request
	q = request.GET.get('q', '')
	#busqueda de la coleccion
	consulta = get_object_or_404(Collection, nombre__exact=q)
	#get_object_or_404(Collection, id=pk)
	
	#enviar data a la vista
	return render(request, 'seeker/collection/detail.html', {'collection': consulta})

#busqueda items en colecciones
def Search_collection_items(request, pk):
	#busqueda de la coleccion
	coleccion = get_object_or_404(Collection, id=pk)
	consulta = Item.objects.filter(colecciones=coleccion.pk).select_related('tipo')

	#paginador
	paginator = Paginator(consulta, 20)
	page = request.GET.get('page')
	items = paginator.get_page(page)
	
	#enviar data a la vista
	return render(request, 'seeker/collection/items.html', {'object_list': items})



#busqueda item -> nombre exacto
def Search_item_exacts(request):
	#optener dato del request
	q = request.GET.get('q', '')
	#busqueda de items
	consulta = get_object_or_404(Item, nombre__exact=q)

	return render(request, 'seeker/item/detail.html', {'item': consulta})


#busqueda items -> cadena de caracteres 
def Search_item_letters(request):
	#optener dato del request
	q = request.GET.get('q', '')
	#busqueda de items
	consulta = Item.objects.filter(nombre__contains=q).select_related('tipo')
	#paginador
	paginator = Paginator(consulta, 20)
	page = request.GET.get('page')
	items = paginator.get_page(page)
	#enviar data a la vista
	return render(request, 'seeker/title/letters.html', {'object_list': items})

#busqueda items -> caracter
def Search_item_letter(request, slug):
	#optener dato del request
	#busqueda de items
	consulta = Item.objects.filter(nombre__contains=slug).select_related('tipo')
	#paginador
	paginator = Paginator(consulta, 20)
	page = request.GET.get('page')
	items = paginator.get_page(page)
	#enviar data a la vista
	return render(request, 'seeker/title/letters.html', {'object_list': items})

#busqueda item -> id
class Search_item_id(DetailView):
    #modelo
    model = Item
    #template
    template_name = 'seeker/item/detail.html'

#busqueda de tema -> cadena de caracteres
def Search_theme_letters(request):
	#optener dato del request
	q = request.GET.get('q', '')
	#busqueda de items
	consulta = Theme.objects.filter(nombre__contains=q)
	#paginador
	paginator = Paginator(consulta, 20)
	page = request.GET.get('page')
	items = paginator.get_page(page)
	#enviar data a la vista
	return render(request, 'seeker/theme/letters.html', {'object_list': items})

#busqueda de colecciones -> tema
def Search_theme_collections(request, pk):
	collection_list = Collection.objects.filter(tema=pk)
	#paginador
	paginator = Paginator(collection_list, 20)
	page = request.GET.get('page')
	collections = paginator.get_page(page)
	#enviar data a la vista
	return render(request, 'seeker/collection/search.html', {'object_list': collections})

#busqueda de tema -> nombre exacto
def Search_theme_exact(request):
	#optener dato del request
	q = request.GET.get('q', '')
	#busqueda de items
	consulta = get_object_or_404(Theme, nombre__exact=q)

	return render(request, 'seeker/theme/detail.html', {'theme': consulta})

#busqueda de tema -> id
class Search_theme_id(DetailView):
    #modelo
    model = Theme
    #template
    template_name = 'seeker/theme/detail.html'

#busqueda de items -> autor
def Search_author_letters(request):
	#optener dato del request
	q = request.GET.get('q', '')
	#busqueda de items
	consulta = Item.objects.filter(autor__icontains=q).select_related('tipo')
	#paginador
	paginator = Paginator(consulta, 20)
	page = request.GET.get('page')
	items = paginator.get_page(page)

	#enviar data a la vista
	return render(request, 'seeker/author/letters.html', {'object_list': items})

		
#busqueda de item -> fecha
def Search_date(request):
	#optener dato del request
	q = request.GET.get('q', '')
	#busqueda de items
	consulta = Item.objects.filter(fecha__gte=q).select_related('tipo')

	#paginador
	paginator = Paginator(consulta, 20)
	page = request.GET.get('page')
	items = paginator.get_page(page)

	#enviar data a la vista
	return render(request, 'seeker/date/items.html', {'object_list': items})

#busqueda de item -> fecha de publicacion
def Search_date_publication(request):
	#optener dato del request
	q = request.GET.get('q', '')
	#busqueda de items
	consulta = Item.objects.filter(publicado__gte=q).select_related('tipo')
	#paginador
	paginator = Paginator(consulta, 20)
	page = request.GET.get('page')
	items = paginator.get_page(page)

	#enviar data a la vista
	return render(request, 'seeker/date/items.html', {'object_list': items})

