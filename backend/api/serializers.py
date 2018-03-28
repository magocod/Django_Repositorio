#importar 
from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer

#modelos
from backend.storage.models import Item_type, Tag, Collection, Item, Category, Theme


#serializadores JSON

class Item_serializer(ModelSerializer):

	class Meta:
		#modelo
		model = Item
		#campos
		fields = ('id','nombre','descripcion', 'autor', 'identificador', 'publicado','tipo', 'tags', 'colecciones', 'url','url_video','archivo_1','archivo_2')


class Collection_serializer(ModelSerializer):

	class Meta:
		#modelo
		model = Collection
		#campos
		fields = ('id','nombre','descripcion', 'tema', 'publicado','categorias','identificador','url_video')


class Item_type_serializer(ModelSerializer):

	class Meta:
		#modelo
		model = Item_type
		#campos
		fields = ('id','nombre','descripcion', 'metadato_1', 'metadato_2', 'metadato_3')


class Tag_serializer(ModelSerializer):

	class Meta:
		#modelo
		model = Tag
		#campos
		fields = ('id','nombre')

class Category_serializer(ModelSerializer):

	class Meta:
		#modelo
		model = Category
		#campos
		fields = ('id','nombre','descripcion')

class Theme_serializer(ModelSerializer):

	class Meta:
		#modelo
		model = Theme
		#campos
		fields = ('id', 'nombre', 'metadato_1', 'metadato_2', 'metadato_3')


#serializadores XML

class Item_type_serializerv2(HyperlinkedModelSerializer):
	
    class Meta:
    	model = Item_type
    	fields = ('id','nombre','descripcion', 'metadato_1', 'metadato_2', 'metadato_3')