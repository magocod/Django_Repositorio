#nota: ficheros eliminados media django cleanup y django unused_media
#	   directorios eliminados por comandos sistema operativo linux

#sistema
import os
import shutil

#señales
from django.db.models.signals import post_delete, pre_save, post_save
from django.dispatch import receiver

#libreria valores aleatorios
import random

#fecha
from datetime import date

from django.conf import settings

#modelos - django
from django.db import models
from django.contrib.auth.models import User

#validadores de extension
from django.core.validators import FileExtensionValidator
from backend.storage.utilities import validate_file_extension

# Create your models here.

class Theme(models.Model):
    #atributos
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(max_length=600)
    dirigido_a = models.CharField(max_length=100, null=True, blank=True)
    metadato_2 = models.CharField(max_length=100, null=True, blank=True)
    metadato_3 = models.CharField(max_length=100, null=True, blank=True)

    #fechas
    publicado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateField(null=True, blank=True)

    #metodos
    def __str__(self):
        return self.nombre

    class Meta:
        ordering = ('id',)

    def items_asignados(instance):
        cantidad= Item.objects.filter(tema=instance.id).count()
        return cantidad

    def items_registrados(instance):
        registros= Item.objects.filter(tema=instance.id).select_related('tipo')
        return registros

    def collections_asignados(instance):
        cantidad= Collection.objects.filter(tema=instance.id).count()
        return cantidad

    def collections_registrados(instance):
        registros= Collection.objects.filter(tema=instance.id).prefetch_related('categorias')
        return registros


class Item_type(models.Model):
    #atributos
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(max_length=600)
    plataforma = models.CharField(max_length=100, null=True, blank=True)
    instalar = models.CharField(max_length=100, null=True, blank=True)
    extension = models.CharField(max_length=100, null=True, blank=True)

    #fechas
    publicado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateField(null=True, blank=True)

    #metodos
    def __str__(self):
        return self.nombre

    class Meta:
        ordering = ('id',)

    def items_asignados(instance):
        cantidad= Item.objects.filter(tipo=instance.id).count()
        return cantidad

    def items_registrados(instance):
        registros= Item.objects.filter(tipo=instance.id).select_related('tema')
        return registros


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
    descripcion = models.TextField(max_length=600)

    #fechas
    publicado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.nombre

    class Meta:
        ordering = ('id',)

    def collections_cantidad(instance):
        cantidad = Collection.objects.filter(categorias=instance.id).count()
        return cantidad

    def collections_registrados(instance):
        cantidad = Collection.objects.filter(categorias=instance.id)
        return cantidad


class Collection(models.Model):

    #atributos
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=600)
    autor = models.CharField(max_length=100)
    tema = models.ForeignKey(Theme,  on_delete=models.SET_NULL, null=True)

    #fechas
    publicado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateField(null=True, blank=True)

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
    descripcion = models.TextField(max_length=600)
    autor = models.CharField(max_length=100)
    licencia = models.CharField(max_length=100)

    identificador = models.CharField(max_length=500)

    #fechas
    fecha = models.DateField() 
    publicado = models.DateField(auto_now_add=True)
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


#codigo idenficador generado a partir de tema y id, segunda parte aleatoria
#identificar archivos en disco
@receiver(pre_save, sender=Item)
def generate_identifier(sender, instance, using, **kwargs):

    if instance.identificador == "":
        #codigo de tema y tipo
        tema = instance.tema.id
        st = "t="+str(tema)
        tipo = instance.tipo.id
        stp = "ti="+str(tipo)
        #aleatorio
        numero = random.randint(1,100000)
        n = "r="+str(numero)
        letra = random.choice('abcdefghijqlmnopqrstuvwxyz')
        codigo = st+stp+n+letra
        instance.identificador = codigo
    else:
        pass
    

#actualizar campos al moficar elementos

@receiver(pre_save, sender=Item)
def to_update_item(sender, instance, using, **kwargs):
    fecha = date.today()
    instance.actualizado = fecha

@receiver(pre_save, sender=Collection)
def to_update_collection(sender, instance, using, **kwargs):
    fecha = date.today()
    instance.actualizado = fecha

@receiver(pre_save, sender=Category)
def to_update_category(sender, instance, using, **kwargs):
    fecha = date.today()
    instance.actualizado = fecha

@receiver(pre_save, sender=Item_type)
def to_update_item_type(sender, instance, using, **kwargs):
    fecha = date.today()
    instance.actualizado = fecha

@receiver(pre_save, sender=Theme)
def to_update_theme(sender, instance, using, **kwargs):
    fecha = date.today()
    instance.actualizado = fecha