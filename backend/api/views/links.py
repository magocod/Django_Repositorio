from django.views.generic import TemplateView, View

#cargar plantilla
from django.template import loader
#retornar respuesta url
from django.http import HttpResponse


#funciones
def default_item():
	dicc={"id":1,"nombre":"nombre",}
	return dicc


#vistas enlaces

class Api_data(TemplateView):
	#plantilla
    template_name = "api/data.html"

class Api_link(TemplateView):
	#plantilla
    template_name = "api/links.html"




