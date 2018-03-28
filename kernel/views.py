#vista genericas
from django.views.generic import TemplateView, View, ListView

#cargar plantilla
from django.template import loader

#añade contexto a plantilla
from django.shortcuts import render

#retornar respuesta url
from django.http import HttpResponse, HttpRequest

#modelos
from backend.storage.models import Item

# Create your views here.

#vista pantalla de inicio aplicacion 
class Indexv1(TemplateView):
	#plantilla
    template_name = "index.html"

