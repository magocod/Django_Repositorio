#manipular urls
from django.urls import path

#reestringir urls
from django.contrib.auth.decorators import login_required

#vistas crud
from backend.grabber.captors import Enter_data
from backend.grabber.captors import Autocomplete_search, Search_category, Search_collection, Search_item, Search_theme, Search_item_type, Search_tag
from backend.grabber.crud import Category_list, Category_create, Category_update, Category_delete
from backend.grabber.crud import Collection_list, Collection_create, Collection_update, Collection_delete
from backend.grabber.crud import Theme_list, Theme_create, Theme_update, Theme_delete
from backend.grabber.crud import Tag_list, Tag_create, Tag_update, Tag_delete
from backend.grabber.crud import Item_list, Item_Create, Item_update, Item_delete 
from backend.grabber.crud import Item_type_list, Item_type_create, Item_type_update, Item_type_delete


#nombre
app_name = 'grabber'

urlpatterns = [
	
	#enter data
	path('registros', Enter_data.as_view(), name='enter_data'),
	path('busqueda', Autocomplete_search.as_view(), name='autocomplete_search'),
	
	#CRUD Collection -> storage
	path('coleccion', Collection_list.as_view(), name='collection_list'),
	path('coleccion/agregar', Collection_create.as_view(), name='collection_create'),
	path('coleccion/modificar/<int:pk>/', Collection_update.as_view(), name='collection_update'),
	path('coleccion/eliminar/<int:pk>/', Collection_delete.as_view(), name='collection_delete'),

	#CRUD Item -> storage
	path('item', Item_list.as_view(), name='item_list'),
	path('item/agregar', Item_Create.as_view(), name='item_create'),
	path('item/modificar/<int:pk>/', Item_update.as_view(), name='item_update'),
	path('item/eliminar/<int:pk>/', Item_delete.as_view(), name='item_delete'),

	#CRUD Tag -> storage
	path('tag', Tag_list.as_view(), name='tag_list'),
	path('tag/agregar', Tag_create.as_view(), name='tag_create'),
	path('tag/modificar/<int:pk>/', Tag_update.as_view(), name='tag_update'),
	path('tag/eliminar/<int:pk>/', Tag_delete.as_view(), name='tag_delete'),

	#CRUD Item_type -> storage
	path('tipo_item', Item_type_list.as_view(), name='item_type_list'),
	path('tipo_item/agregar', Item_type_create.as_view(), name='item_type_create'),
	path('tipo_item/modificar/<int:pk>/', Item_type_update.as_view(), name='item_type_update'),
	path('tipo_item/eliminar/<int:pk>/', Item_type_delete.as_view(), name='item_type_delete'),

	#CRUD Theme -> storage
	path('tema', Theme_list.as_view(), name='theme_list'),
	path('tema/agregar', Theme_create.as_view(), name='theme_create'),
	path('tema/modificar/<int:pk>/', Theme_update.as_view(), name='theme_update'),
	path('tema/eliminar/<int:pk>/', Theme_delete.as_view(), name='theme_delete'),

	#CRUD Category -> storage
	path('categoria', Category_list.as_view(), name='category_list'),
	path('categoria/agregar', Category_create.as_view(), name='category_create'),
	path('categoria/modificar/<int:pk>/', Category_update.as_view(), name='category_update'),
	path('categoria/eliminar/<int:pk>/', Category_delete.as_view(), name='category_delete'),

	#busqueda avanzada
	path('categoria/busqueda', Search_category, name='category_search'),
	path('coleccion/busqueda', Search_collection, name='collection_search'),
	path('item/busqueda', Search_item, name='item_search'),
	path('tema/busqueda', Search_theme, name='theme_search'),
	path('tipo_item/busqueda', Search_item_type, name='item_type_search'),
	path('tag/busqueda', Search_tag, name='tag_search'),

]
















	