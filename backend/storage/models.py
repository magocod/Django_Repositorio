#nota: ficheros eliminados media django cleanup y django unused_media
#	   directorios eliminados por comandos sistema operativo linux

#sistema
import os
import shutil

from django.conf import settings

#modelos - django
from django.db import models
from django.contrib.auth.models import User

#señales
from django.db.models.signals import post_delete, pre_save, post_save
from django.dispatch import receiver

#validadores de extension
from django.core.validators import FileExtensionValidator
from backend.storage.utilities import validate_file_extension

# Create your models here.

class Theme(models.Model):
    #atributos
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(max_length=500)
    metadato_1 = models.CharField(max_length=100, null=True, blank=True)
    metadato_2 = models.CharField(max_length=100, null=True, blank=True)
    metadato_3 = models.CharField(max_length=100, null=True, blank=True)

    #metodos
    def __str__(self):
        return self.nombre

    class Meta:
        ordering = ('id',)


class Item_type(models.Model):
    #atributos
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(max_length=500)
    metadato_1 = models.CharField(max_length=100, null=True, blank=True)
    metadato_2 = models.CharField(max_length=100, null=True, blank=True)
    metadato_3 = models.CharField(max_length=100, null=True, blank=True)

    #metodos
    def __str__(self):
        return self.nombre

    class Meta:
        ordering = ('id',)


class Tag(models.Model):
    #atributos
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre

    class Meta:
        ordering = ('id',)


class Category(models.Model):
    #atributos
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(max_length=500)

    def __str__(self):
        return self.nombre

    class Meta:
        ordering = ('id',)


class Collection(models.Model):

    #atributos
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=500)
    autor = models.CharField(max_length=100)
    identificador = models.CharField(max_length=100, unique=True)
    tema = models.ForeignKey(Theme,  on_delete=models.SET_NULL, null=True)
    url_video = models.URLField(max_length=200, null=True, blank=True)

    #fechas
    publicado = models.DateTimeField(auto_now_add=True)

    #relacion muchos a muchos
    categorias = models.ManyToManyField(Category, blank=True)
    
    def __str__(self):
        return self.nombre

    class Meta:
        ordering = ('id',)

    def items_registrados(instance):
        items= Item.objects.filter(colecciones=instance.id).select_related('tipo')
        return items
    
    def items_cantidad(instance):
        cantidad= Item.objects.filter(colecciones=instance.id).count()
        return cantidad


class Item(models.Model):

    #atributos
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=500)
    autor = models.CharField(max_length=100)
    identificador = models.CharField(max_length=100, unique=True)

    #fechas
    fecha = models.DateField() 
    publicado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateField(null=True, blank=True)

    #relacion muchos a muchos
    tags = models.ManyToManyField(Tag, blank=True)
    colecciones = models.ManyToManyField(Collection, blank=True)

    #relaciones
    tema = models.ForeignKey(Theme,  on_delete=models.SET_NULL, null=True)
    tipo = models.ForeignKey(Item_type, on_delete=models.SET_NULL, null=True)
 
    #metodo guardar en disco
    def directorio_files(instance, filename):
        return os.path.join("repositorio/" + str(instance.tema) + "/" + str(instance.tipo) + "/"+ str(instance.identificador), filename)

    #url
    url = models.URLField(max_length=200, null=True, blank=True)
    url_video = models.URLField(max_length=200, null=True, blank=True)

    #archivos
    archivo_1 = models.FileField(upload_to=directorio_files, blank=True)
    archivo_2 = models.FileField(upload_to=directorio_files, blank=True)

    #metodos

    #devolver string
    def __str__(self):
        return self.nombre

    class Meta:
        ordering = ('id',)

    def tamaño_archivo1(instance):
        tamaño = instance.archivo_1.size
        calcular = tamaño/1048576
        mb = round(calcular, 4)
        return mb

    def nombre_archivo1(instance):
        file_path  = instance.archivo_1.name
        file_name  = os.path.basename(file_path)
        fichero = os.path.splitext(file_name )[0]
        return fichero

    def extension_archivo1(instance):
        file_path  = instance.archivo_1.name
        file_name  = os.path.basename(file_path )
        extension = os.path.splitext(file_name)[1]
        return extension

    def tamaño_archivo2(instance):
        tamaño = instance.archivo_2.size
        calcular = tamaño/1048576
        mb = round(calcular, 4)
        return mb

    def nombre_archivo2(instance):
        file_path  = instance.archivo_2.name
        file_name  = os.path.basename(file_path )
        fichero = os.path.splitext(file_name )[0]
        return fichero

    def extension_archivo2(instance):
        file_path  = instance.archivo_2.name
        file_name  = os.path.basename(file_path )
        extension = os.path.splitext(file_name)[1]
        return extension



