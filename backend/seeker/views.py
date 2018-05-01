#cargar plantilla
from django.template import loader

#añade contexto a plantilla
from django.shortcuts import render

#retornar respuesta url
from django.http import HttpResponse, HttpRequest

#vista django
from django.views.generic import View, TemplateView, ListView, DetailView

#modelos
from backend.storage.models import Category, Item, Theme, Tag

#queries
from backend.seeker.queries import registros_totales, recent_uploads

from django.db.models.aggregates import Count

#proveedores
from backend.fabricator.providers import alphabet

# Create your views here.

#informacion del repositorio
class Info_seeker(TemplateView):
    #plantilla
    template_name = "seeker/info.html"

#pruebas
class Records_seeker(View):

    def get(self, request, *args, **kwargs):
        #variable almacena consulta
        registros = registros_totales()

        template = loader.get_template('seeker/test/records.html')
        #enviar contexto -> convertir en diccionario
        context = {
        'registros':registros,
        }
        #enviar data a la vista
        return HttpResponse(template.render(context, request))
    
class All_seeker(ListView):
    #modelo
    queryset = Item.objects.order_by('id')
    context_object_name = 'object_list'
    #plantilla
    template_name = 'seeker/test/all.html'


#recientes
class Recent_items(View):

    def get(self, request, *args, **kwargs):
        #variable almacena consulta
        
        ultimos= recent_uploads()

        template = loader.get_template('seeker/recent.html')
        #enviar contexto -> convertir en diccionario
        context = {
        'registros': ultimos,
        }
        #enviar data a la vista
        return HttpResponse(template.render(context, request))

#bases busquedas
class Title_seeker_base(View):

    def get(self, request, *args, **kwargs):

        registros = alphabet()

        template = loader.get_template('seeker/title/base.html')
        #enviar contexto -> convertir en diccionario
        context = {
        'registros':registros,
        }
        #enviar data a la vista
        return HttpResponse(template.render(context, request))

class Category_seeker_base(ListView):
    #modelos -> relacionados
    queryset = Category.objects.order_by('id')
    context_object_name = 'object_list'
    #plantilla
    template_name = 'seeker/category/base.html'

class Theme_seeker_base(ListView):
    #modelos -> relacionados
    queryset = Theme.objects.order_by('id')
    context_object_name = 'object_list'
    paginate_by = 20
    #plantilla
    template_name = 'seeker/theme/base.html'


class Author_seeker_base(ListView):
    #modelo
    queryset = Item.objects.order_by('autor').values('id','autor')
    context_object_name = 'object_list'
    paginate_by = 20
    #plantilla
    template_name = 'seeker/author/base.html'

class Date_seeker_base(TemplateView):
    #plantilla
    template_name = "seeker/date/base.html"


class Tag_seeker_base(ListView):
    #modelo
    queryset = Tag.objects.values('id','nombre')
    context_object_name = 'object_list'
    #plantilla
    template_name = "seeker/tag/base.html"
