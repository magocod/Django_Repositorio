#cargar plantilla
from django.template import loader

#añade contexto a plantilla
from django.shortcuts import render

#retornar respuesta url
from django.http import HttpResponse, HttpRequest

#vista django
from django.views.generic import View, TemplateView

#queries
from backend.api.queries import registros_totales

# Create your views here.

class User_login(TemplateView):
    #plantilla
    template_name = "account/authenticate/login.html"

class User_register(TemplateView):
    #plantilla
    template_name = "account/authenticate/register.html"

class User_password(TemplateView):
    #plantilla
    template_name = "account/authenticate/password_change.html"

class Dashboard(View):

    def get(self, request, *args, **kwargs):
        #variable almacena consulta
        datos = request.user
        registros = registros_totales()

        template = loader.get_template('account/base.html')
        #enviar contexto -> convertir en diccionario
        context = {
        'user': datos,
        'registros':registros,
        }
        #enviar data a la vista
        return HttpResponse(template.render(context, request))
