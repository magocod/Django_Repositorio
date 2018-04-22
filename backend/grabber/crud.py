#enviar data a vistas
from django.shortcuts import render
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

#modelos
from backend.storage.models import Item_type, Tag, Collection, Item, Category, Theme

#queries
from backend.seeker.queries import registros_totales

#formularios
from backend.grabber.forms import Tag_form, Collection_form, Item_type_form, Item_form, Theme_form, Category_form

#retornar respuesta url
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

#CRUD categoria

class Category_list(ListView):
    #modelo
    model = Category
    #template
    template_name = 'grabber/category/list.html'

class Category_create(SuccessMessageMixin, CreateView):
    #modelo
    model = Category
    #formulario
    form_class = Category_form

    template_name = 'grabber/category/form.html'
    #redirigir
    success_url = reverse_lazy('grabber:category_list')
    success_message = "Registrada la categoria"

class Category_update(SuccessMessageMixin, UpdateView):
    #modelo
    model = Category
    #formulario
    form_class = Category_form

    template_name = 'grabber/category/form.html'
    #redirigir
    success_url = reverse_lazy('grabber:category_list')
    success_message = "Actualizada la categoria"

class Category_delete(DeleteView):
    model = Category
    template_name = 'grabber/category/delete.html'
    success_message = "Eliminada la categoria"
    success_url = reverse_lazy('grabber:category_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(Category_delete, self).delete(request, *args, **kwargs)

#CRUD tag

class Tag_list(ListView):
    #modelo
    model = Tag
    #template
    template_name = 'grabber/tag/list.html'

class Tag_create(SuccessMessageMixin, CreateView):
    #modelo
    model = Tag
    #formulario
    form_class = Tag_form

    template_name = 'grabber/tag/form.html'
    #redirigir
    success_url = reverse_lazy('grabber:tag_list')
    success_message = "Registrada la etiqueta"

class Tag_update(SuccessMessageMixin, UpdateView):
    #modelo
    model = Tag
    #formulario
    form_class = Tag_form

    template_name = 'grabber/tag/form.html'
    #redirigir
    success_url = reverse_lazy('grabber:tag_list')
    success_message = "Actualizada la etiqueta"

class Tag_delete(DeleteView):
    model = Tag
    template_name = 'grabber/tag/delete.html'
    success_message = "Eliminada la etiqueta"
    success_url = reverse_lazy('grabber:tag_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(Tag_delete, self).delete(request, *args, **kwargs)


#CRUD item

class Item_list(ListView):
    #modelo
    model = Item
    #template
    template_name = 'grabber/item/list.html'

class Item_Create(SuccessMessageMixin, CreateView):
    #modelo
    model = Item
    #formulario
    form_class = Item_form

    template_name = 'grabber/item/form.html'
    #redirigir
    success_url = reverse_lazy('grabber:item_list')
    success_message = "Registrado el recurso digital"

class Item_update(SuccessMessageMixin, UpdateView):
    #modelo
    model = Item
    #formulario
    form_class = Item_form

    template_name = 'grabber/item/form.html'
    #redirigir
    success_url = reverse_lazy('grabber:item_list')
    success_message = "Actualizado el recurso digital"

class Item_delete(DeleteView):
    model = Item
    template_name = 'grabber/item/delete.html'
    success_message = "Eliminado el recurso digital"
    success_url = reverse_lazy('grabber:item_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(Item_delete, self).delete(request, *args, **kwargs)


#CRUD tipo item

class Item_type_list(ListView):
    #modelo
    model = Item_type
    #template
    template_name = 'grabber/item_type/list.html'


class Item_type_create(SuccessMessageMixin, CreateView):
    #modelo
    model = Item_type
    #formulario
    form_class = Item_type_form

    template_name = 'grabber/item_type/form.html'
    #redirigir
    success_url = reverse_lazy('grabber:item_type_list')
    success_message = "Registrado el tipo de item"

class Item_type_update(SuccessMessageMixin, UpdateView):
    #modelo
    model = Item_type
    #formulario
    form_class = Item_type_form

    template_name = 'grabber/item_type/form.html'
    #redirigir
    success_url = reverse_lazy('grabber:item_type_list')
    success_message = "Actualizado el tema"

class Item_type_delete(DeleteView):
    model = Item_type
    template_name = 'grabber/item_type/delete.html'
    success_message = "Eliminado el tipo de item"
    success_url = reverse_lazy('grabber:item_type_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(Item_type_delete, self).delete(request, *args, **kwargs)


#CRUD tema

class Theme_list(ListView):
    #modelo
    model = Theme
    #template
    template_name = 'grabber/theme/list.html'

class Theme_create(SuccessMessageMixin, CreateView):
    #modelo
    model = Theme
    #formulario
    form_class = Theme_form

    template_name = 'grabber/theme/form.html'
    #redirigir
    success_url = reverse_lazy('grabber:theme_list')
    success_message = "Registrada la categoria"

class Theme_update(SuccessMessageMixin, UpdateView):
    #modelo
    model = Theme
    #formulario
    form_class = Theme_form

    template_name = 'grabber/theme/form.html'
    #redirigir
    success_url = reverse_lazy('grabber:theme_list')
    success_message = "Actualizado el tema"

class Theme_delete(DeleteView):
    model = Theme
    template_name = 'grabber/theme/delete.html'
    success_message = "Eliminado el tema"
    success_url = reverse_lazy('grabber:theme_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(Theme_delete, self).delete(request, *args, **kwargs)


#CRUD coleccion

class Collection_list(ListView):
    #modelo
    model = Collection
    #template
    template_name = 'grabber/collection/list.html'


class Collection_create(SuccessMessageMixin, CreateView):
    #modelo
    model = Collection
    #formulario
    form_class = Collection_form

    template_name = 'grabber/collection/form.html'
    #redirigir
    success_url = reverse_lazy('grabber:collection_list')
    success_message = "Registrada la coleccion"

class Collection_update(SuccessMessageMixin, UpdateView):
    #modelo
    model = Collection
    #formulario
    form_class = Collection_form

    template_name = 'grabber/collection/form.html'
    #redirigir
    success_url = reverse_lazy('grabber:collection_list')
    success_message = "Actualizada la coleccion"

class Collection_delete(DeleteView):
    model = Collection
    template_name = 'grabber/collection/delete.html'
    success_message = "Eliminada la coleccion"
    success_url = reverse_lazy('grabber:collection_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(Collection_delete, self).delete(request, *args, **kwargs)

