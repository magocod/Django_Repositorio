#formularios django
from django import forms

#modelos -> registros
from backend.storage.models import Collection, Item_type, Tag, Item, Theme, Category

#modelos -> archivos

#formularios -> captors

#formularios -> crud

class Tag_form(forms.ModelForm):

	#modelo base
	class Meta:
		#modelo
		model = Tag
		#campos
		fields = [
			'nombre',
		]
		#etiquetas
		labels = {
			'nombre':'Nombre',
		}
		#diseño del campo
		widgets = {
			'nombre':forms.TextInput(attrs={'class':'form-control','placeholder':'Tag','required': True}),
		}


class Category_form(forms.ModelForm):

	#modelo base
	class Meta:
		#modelo
		model = Category
		#campos
		fields = [
			'nombre',
			'descripcion',
		]
		#etiquetas
		labels = {
			'nombre': 'Nombre',
			'descripcion': 'Descripcion',
		}
		#diseño del campo
		widgets = {
			'nombre':forms.TextInput(attrs={'class':'form-control','placeholder':'Nombre','required': True}),
			'descripcion':forms.Textarea(attrs={'class':'form-control','placeholder':'breve descripcion','required': True}),
		}


class Item_type_form(forms.ModelForm):
	
	#modelo base
	class Meta:
		#modelo
		model = Item_type
		#campos
		fields = [
			'nombre',
			'descripcion',
			'plataforma',
			'instalar',
			'extension',
		]
		#etiquetas
		labels = {
			'nombre': 'Nombre',
			'descripcion': 'Descripcion',
			'plataforma': 'Plataforma',
			'instalar': 'Instalar',
			'extension': 'Extension',
		}
		#diseño del campo
		widgets = {
			'nombre':forms.TextInput(attrs={'class':'form-control','placeholder':'nombre','required': True}),
			'descripcion':forms.Textarea(attrs={'class':'form-control editor','placeholder':'breve descripcion','required': True}),
			'plataforma':forms.TextInput(attrs={'class':'form-control','placeholder':'ej. linux(UBUNTU/DEBIAN), windows 8.1/10'}),
			'instalar':forms.TextInput(attrs={'class':'form-control','placeholder':'ej. plugin google chrome, mozilla firefox'}),
			'extension':forms.TextInput(attrs={'class':'form-control','placeholder':'ej. Apache OpenOffice'}),
		}


class Theme_form(forms.ModelForm):
	
	#modelo base
	class Meta:
		#modelo
		model = Theme
		#campos
		fields = [
			'nombre',
			'descripcion',
			'dirigido_a',
			'metadato_2',
			'metadato_3',
		]
		#etiquetas
		labels = {
			'nombre': 'Nombre',
			'descripcion': 'Descripcion',
			'dirigido_a': 'Dirigido_a',
			'metadato_2': 'Metadato_2',
			'metadato_3': 'Metadato_3',
		}
		#diseño del campo
		widgets = {
			'nombre':forms.TextInput(attrs={'class':'form-control','placeholder':'nombre','required': True}),
			'descripcion':forms.Textarea(attrs={'class':'form-control','placeholder':'breve descripcion','required': True}),
			'dirigido_a':forms.TextInput(attrs={'class':'form-control','placeholder':'descripcion'}),
			'metadato_2':forms.TextInput(attrs={'class':'form-control','placeholder':'descripcion'}),
			'metadato_3':forms.TextInput(attrs={'class':'form-control','placeholder':'descripcion'}),
		}
		
class Item_form(forms.ModelForm):

	#modelo base
	class Meta:
		#modelo
		model = Item
		#campos
		fields = [
			'nombre',
			'descripcion',
			'tipo',
			'tema',
			'autor',		
			'tags',
			'colecciones',
			'fecha',
			'url',
			'archivo_1',
			'archivo_2',
		]
		#etiquetas
		labels = {
			'nombre': 'Nombre',
			'descripcion': 'Descripcion',
			'tipo':'Tipo',
			'tema':'Tema',
			'autor':'Autor',
			'tags':'Tags',
			'colecciones':'Colecciones',
			'fecha':'Fecha',
			'url':'Url',
			'archivo_1': 'Archivo_1',
			'archivo_2':'Archivo_2',
		}
		#diseño del campo
		widgets = {
			'nombre':forms.TextInput(attrs={'class':'form-control','placeholder':'item','required': True}),
			'descripcion':forms.Textarea(attrs={'class':'form-control trumbowyg-area','placeholder':'breve descripcion','required': True}),
			'autor':forms.TextInput(attrs={'class':'form-control','placeholder':'autor','required': True}),
			#fechas
			'fecha': forms.DateInput(attrs={'class':'form-control','type':'date','required': True}),
			#url
			'url':forms.URLInput(attrs={'class':'form-control','placeholder':'url-pagina'}),
			#llave foranea
			'tipo': forms.Select(attrs={'class':'chosen-select-one form-control'}),
			'tema': forms.Select(attrs={'class':'chosen-select-two form-control'}),
			#multiples opciones
			'tags': forms.SelectMultiple(attrs={'class':'form-control chosen-select-t'}),
			'colecciones': forms.SelectMultiple(attrs={'class':'form-control chosen-select'}),
			#ficheros
			'archivo_1':forms.ClearableFileInput(attrs={'class':'form-control'}),
			'archivo_2':forms.ClearableFileInput(attrs={'class':'form-control'}),
		}

class Collection_form(forms.ModelForm):

	#modelo base
	class Meta:
		#modelo
		model = Collection
		#campos
		fields = [
			'nombre',
			'descripcion',
			'tema',
			'categorias',
		]
		#etiquetas
		labels = {
			'nombre': 'Nombre',
			'descripcion': 'Descripcion',
			'tema': 'Tema',
			'categorias':'Categorias',
		}
		#diseño del campo
		widgets = {
			'nombre':forms.TextInput(attrs={'class':'form-control','placeholder':'Coleccion','required': True}),
			'descripcion':forms.Textarea(attrs={'class':'form-control editor','placeholder':'breve descripcion','required': True}),
			'tema':forms.Select(attrs={'class':'form-control chosen-select-one','placeholder':'categoria','required': True}),
			#multiples opciones
			'categorias': forms.SelectMultiple(attrs={'class':'form-control chosen-select'}),
		}
