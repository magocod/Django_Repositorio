#cargar plantilla
from django.template import loader

#añade contexto a plantilla
from django.shortcuts import render

#redirigir url
from django.urls import reverse_lazy

#retornar respuesta url
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect

#mensajes -> django
from django.contrib import messages

#vista django
from django.views.generic import View, TemplateView, CreateView, ListView, UpdateView, DetailView, DeleteView
#Incorporar mensajes en vistas -> django
from django.contrib.messages.views import SuccessMessageMixin

#queries
from backend.seeker.queries import registros_totales, recent_activities

#formularios
from backend.account.forms import User_form, User_activate

#modelos
from django.contrib.auth.models import User

# Create your views here.

class Dashboard(View):

    def get(self, request, *args, **kwargs):
        #variable almacena consulta
        datos = request.user
        registros = registros_totales()
        reciente = recent_activities()

        template = loader.get_template('account/base.html')
        #enviar contexto -> convertir en diccionario
        context = {
        'user': datos,
        'registros':registros,
        'reciente': reciente
        }
        #enviar data a la vista
        return HttpResponse(template.render(context, request))


#crud

class User_list(ListView):
    #modelo
    model = User
    #template
    template_name = 'account/user/list.html'


class User_create(SuccessMessageMixin, CreateView):
    model = User
    template_name = 'account/user/form.html'
    form_class = User_form
    success_message = "Registrado el usuario"
    success_url = reverse_lazy('account:user_list')


class User_update(SuccessMessageMixin, UpdateView):
    #modelo
    model = User
    #formulario
    form_class = User_form

    template_name = 'account/user/form.html'
    #redirigir
    success_url = reverse_lazy('account:user_list')
    success_message = "Actualizado los datos del usuario"

class User_delete(DeleteView):
    model = User
    template_name = 'account/user/delete.html'
    success_message = "Eliminada el usuario"
    success_url = reverse_lazy('account:user_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(User_delete, self).delete(request, *args, **kwargs)


class User_detail(DetailView):
    #modelo
    model = User
    #template
    template_name = 'account/user/detail.html'

class User_active(SuccessMessageMixin, UpdateView):
    #modelo
    model = User
    #formulario
    form_class = User_activate

    template_name = 'account/user/active.html'
    #redirigir
    success_url = reverse_lazy('account:user_list')
    success_message = "Actualizado el estado del usuario"


#sin usar

class User_login(TemplateView):
    #plantilla
    template_name = "account/authenticate/login.html"

class User_register(TemplateView):
    #plantilla
    template_name = "account/authenticate/register.html"