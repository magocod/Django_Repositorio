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

#colecciones 
def Search_collection_category(request, pk):
	categoria = get_object_or_404(Category, id=pk)
	#busqueda de la coleccion
	consulta = Collection.objects.filter(categorias=categoria.id).prefetch_related('categorias')
	#paginador
	paginator = Paginator(consulta, 20)
	page = request.GET.get('page')
	colecciones = paginator.get_page(page)
	
	#enviar data a la vista
	return render(request, 'seeker/category/collections.html', {'object_list': colecciones})

#clave primaria
def Search_collection_pk(request, pk):
	#busqueda de la coleccion
	coleccion = Collection.objects.filter(id=pk).prefetch_related('categorias').get(id=pk)
	#get_object_or_404(Collection, id=pk)
	
	#enviar data a la vista
	return render(request, 'seeker/category/collection.html', {'collection': coleccion})

#clave nombre
def Search_collection_string(request):
	#optener dato del request
	q = request.GET.get('q', '')
	#busqueda de la coleccion
	consulta = get_object_or_404(Collection, nombre__exact=q)
	#get_object_or_404(Collection, id=pk)
	
	#enviar data a la vista
	return render(request, 'seeker/category/collection.html', {'collection': consulta})

#Items de coleccion	
def Search_collection_items(request, pk):
	#busqueda de la coleccion
	coleccion = get_object_or_404(Collection, id=pk)
	consulta = Item.objects.filter(colecciones=coleccion.pk).select_related('tipo')

	#paginador
	paginator = Paginator(consulta, 20)
	page = request.GET.get('page')
	items = paginator.get_page(page)
	
	#enviar data a la vista
	return render(request, 'seeker/category/items.html', {'object_list': items})

#string exacto
def Search_letters_exacts(request):
	#optener dato del request
	q = request.GET.get('q', '')
	#busqueda de items
	consulta = get_object_or_404(Item, nombre__exact=q)
	#paginador

	#enviar data a la vista
	return render(request, 'seeker/item/detail.html', {'item': consulta})
	
#string
def Search_letters(request):
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

#char
def Search_letter(request, slug):
	#optener dato del request
	#busqueda de items
	consulta = Item.objects.filter(nombre__contains=slug).select_related('tipo')
	#paginador
	paginator = Paginator(consulta, 20)
	page = request.GET.get('page')
	items = paginator.get_page(page)
	#enviar data a la vista
	return render(request, 'seeker/title/letters.html', {'object_list': items})

#campo tema
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

def Search_theme_collections(request, pk):
	collection_list = Collection.objects.filter(tema=pk)
	#paginador
	paginator = Paginator(collection_list, 20)
	page = request.GET.get('page')
	collections = paginator.get_page(page)
	#enviar data a la vista
	return render(request, 'seeker/theme/collection.html', {'object_list': collections})

#campo autor
def Search_author(request):
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
		
#campo fecha

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

#campo fecha de publicacion
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

