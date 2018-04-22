#enviar data a vistas
from django.shortcuts import render, redirect
#cargar plantilla
from django.template import loader

#redirigir url
from django.urls import reverse_lazy

#mensajes -> django
from django.contrib import messages
#Incorporar mensajes en vistas -> django
from django.contrib.messages.views import SuccessMessageMixin
#vista -> django
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView, TemplateView, View
from django.views.generic.edit import FormView

#modelos
from backend.storage.models import Item_type, Tag, Collection, Item, Category, Theme
from django.shortcuts import get_object_or_404

#queries
from backend.seeker.queries import registros_totales, lista_elementos

#formularios
from backend.grabber.forms import Tag_form, Collection_form, Item_type_form, Item_form, Theme_form, Category_form

#retornar respuesta url
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
#funciones


class Enter_data(View):

    def get(self, request, *args, **kwargs):
        #variable almacena consulta
        registros = registros_totales()

        template = loader.get_template('account/enter.html')
        #enviar contexto -> convertir en diccionario
        context = {
        'registros':registros,
        }
        #enviar data a la vista
        return HttpResponse(template.render(context, request))

class Autocomplete_search(View):

    def get(self, request, *args, **kwargs):
        #variable almacena consulta
        registros = registros_totales()
        elementos = lista_elementos()
        template = loader.get_template('account/search.html')
        #enviar contexto -> convertir en diccionario
        context = {
        'registros':registros,
        'listas':elementos,
        }
        #enviar data a la vista
        return HttpResponse(template.render(context, request))

# busquedas

def Search_category(request):
    #optener dato del request
    q = request.GET.get('q', '')
    #busqueda de items
    consulta = get_object_or_404(Category, id=q)
    #paginador

    #enviar data a la vista
    return render(request, 'grabber/category/detail.html', {'category': consulta})

def Search_collection(request):
    #optener dato del request
    q = request.GET.get('q', '')
    #busqueda de items
    consulta = get_object_or_404(Collection, id=q)
    #paginador

    #enviar data a la vista
    return render(request, 'grabber/collection/detail.html', {'collection': consulta})

def Search_item(request):
    #optener dato del request
    q = request.GET.get('q', '')
    #busqueda de items
    consulta = get_object_or_404(Item, id=q)
    #paginador

    #enviar data a la vista
    return render(request, 'grabber/item/detail.html', {'item': consulta})

def Search_theme(request):
    #optener dato del request
    q = request.GET.get('q', '')
    #busqueda de items
    consulta = get_object_or_404(Theme, id=q)
    #paginador

    #enviar data a la vista
    return render(request, 'grabber/theme/detail.html', {'theme': consulta})

def Search_item_type(request):
    #optener dato del request
    q = request.GET.get('q', '')
    #busqueda de items
    consulta = get_object_or_404(Item_type, id=q)
    #paginador

    #enviar data a la vista
    return render(request, 'grabber/item_type/detail.html', {'item_type': consulta})

def Search_tag(request):
    #optener dato del request
    q = request.GET.get('q', '')
    #busqueda de items
    consulta = get_object_or_404(Tag, id=q)
    #paginador

    #enviar data a la vista
    return render(request, 'grabber/tag/detail.html', {'tag': consulta})


#detalles
class Category_detail(DetailView):
    #modelo
    model = Category
    #template
    template_name = 'grabber/category/detail.html' 

class Collection_detail(DetailView):
    #modelo
    model = Collection
    #template
    template_name = 'grabber/collection/detail.html'


class Item_detail(DetailView):
    #modelo
    model = Item
    #template
    template_name = 'grabber/item/detail.html'

class Theme_detail(DetailView):
    #modelo
    model = Theme
    #template
    template_name = 'grabber/theme/detail.html'

class Item_type_detail(DetailView):
    #modelo
    model = Item_type
    #template
    template_name = 'grabber/item_type/detail.html'

