#nota:	Factory boy de python para ingresar data de prueba
#		comando create_batch(size=cantidad)

#factory boy
import factory
import factory.fuzzy

#sistema
import random
import string
import datetime

#zona horaria
from pytz import UTC

#proveedores
from backend.fabricator.providers import random_string, random_metadato

#modelos
from backend.storage.models import Collection, Category, Theme, Item, Item_type, Tag


#llamar desde el shell y test
#from backend.fabricator.factories import Themefactory, Collectionfactory, Categoryfactory, Item_typefactory, Tagfactory, Itemfactory

class Themefactory(factory.django.DjangoModelFactory):
	class Meta:
		model = Theme  
		#django_get_or_create = ('nombre','descripcion',)

	#añadir valores aleatorios
	nombre = factory.Sequence(lambda n: 'tema_{}'.format(n))
	descripcion = factory.LazyAttribute(lambda t: random_string())
	metadato_1 = factory.LazyAttribute(lambda t: random_metadato())
	metadato_2 = factory.LazyAttribute(lambda t: random_metadato())
	metadato_3 = factory.LazyAttribute(lambda t: random_metadato())

class Collectionfactory(factory.django.DjangoModelFactory):
	class Meta:
		model = Collection  
		#django_get_or_create = ('nombre','descripcion', 'tema', 'autor', 'identificador',)

	#añadir valores aleatorios
	nombre = factory.Sequence(lambda n: 'coleccion_{}'.format(n))
	autor = factory.Faker('first_name', locale='en_US')
	descripcion = factory.LazyAttribute(lambda t: random_string())
	identificador = factory.Sequence(lambda n: 'identificador_coleccion{}'.format(n))
	#relacion clave foranea
	#tema = factory.SubFactory(Themefactory)
	tema = factory.Iterator(Theme.objects.all())

	#relacion muchos a muchos
	@factory.post_generation
	def categorias(self, create, extracted, **kwargs):
		if not create:
			return
		if extracted:
			for Category in extracted:
				self.categorias.add(Category)
	

class Categoryfactory(factory.django.DjangoModelFactory):
	class Meta:
		model = Category
		#django_get_or_create = ('nombre','colecciones',)

	#añadir valores aleatorios
	nombre = factory.Sequence(lambda n: 'categoria_{}'.format(n))
	descripcion = factory.LazyAttribute(lambda t: random_string())
	


class Item_typefactory(factory.django.DjangoModelFactory):
	class Meta:
		model = Item_type 
		#django_get_or_create = ('nombre','descripcion', 'metadato_1', 'metadato_2', 'metadato_3',)

	#añadir valores aleatorios
	nombre = factory.Sequence(lambda n: 'tipo_item_{}'.format(n))
	descripcion = factory.LazyAttribute(lambda t: random_string())
	metadato_1 = factory.LazyAttribute(lambda t: random_metadato())
	metadato_2 = factory.LazyAttribute(lambda t: random_metadato())
	metadato_3 = factory.LazyAttribute(lambda t: random_metadato())

class Tagfactory(factory.django.DjangoModelFactory):
	class Meta:
		model = Tag 
		#django_get_or_create = ('nombre',)

	#añadir valores aleatorios
	nombre = factory.Sequence(lambda n: 'tag_{}'.format(n))

class Itemfactory(factory.django.DjangoModelFactory):
	class Meta:
		model = Item
		#django_get_or_create = ('nombre','descripcion', 'identificador', 'autor', tipo', 'colecciones','tags',)

	#añadir valores aleatorios
	nombre = factory.Sequence(lambda n: 'item_{}'.format(n))
	descripcion = factory.LazyAttribute(lambda t: random_string())
	autor = factory.Faker('first_name', locale='en_US')
	identificador = factory.Sequence(lambda n: 'identificador_item{}'.format(n))
	#tipo = factory.SubFactory(Item_typefactory)
	tipo = factory.Iterator(Item_type.objects.all())
	tema = factory.Iterator(Theme.objects.all())

	#fechas -> desde -> hasta
	fecha = factory.fuzzy.FuzzyDate(datetime.date(2005, 1, 2), datetime.date(2018, 3, 16))
	# desde + onahoraria ---> hasta + zonahoraria
	#actualizado = factory.fuzzy.FuzzyDateTime(datetime.datetime(2018, 5, 12, tzinfo=UTC), datetime.datetime(2020, 2, 9, tzinfo=UTC))
	actualizado = factory.fuzzy.FuzzyDate(datetime.date(2005, 1, 2), datetime.date(2018, 3, 16))

	@factory.post_generation
	def tags(self, create, extracted, **kwargs):
		if not create:
			return
		if extracted:
			for Tag in extracted:
				self.tags.add(Tag)

	@factory.post_generation
	def colecciones(self, create, extracted, **kwargs):
		if not create:
			return
		if extracted:
			for Collection in extracted:
				self.colecciones.add(Collection)


	