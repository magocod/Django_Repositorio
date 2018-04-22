#nota: usando django-filter

#modelos
from backend.storage.models import Collection, Item, Item_type, Tag, Category, Theme
#filtros
import django_filters

class Item_filter(django_filters.FilterSet):
    class Meta:
        model = Item
        fields = ('nombre', 'autor', 'tipo', 'tags')

class Theme_filter(django_filters.FilterSet):

	class Meta:
		#modelo
		model = Theme
		#campos
		fields = {
            'nombre': ['exact','icontains'],

        }

class Collection_filter(django_filters.FilterSet):

	class Meta:
		#modelo
		model = Collection
		#campos
		fields = ('nombre','autor')