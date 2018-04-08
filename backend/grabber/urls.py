#manipular urls
from django.urls import path

#reestringir urls
from django.contrib.auth.decorators import login_required

#vistas crud
from backend.grabber.captors import Enter_data
from backend.grabber.captors import Autocomplete_search, Search_category, Search_collection, Search_item, Search_theme, Search_item_type, Search_tag
from backend.grabber.captors import Item_type_detail, Item_detail, Category_detail, Collection_detail, Theme_detail

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
	path('registros', login_required(Enter_data.as_view()), name='enter_data'),
	path('busqueda', login_required(Autocomplete_search.as_view()), name='autocomplete_search'),

	#detalles
	path('coleccion/detalles/<int:pk>', login_required(Collection_detail.as_view()), name='collection_detail'),
	path('item/detalles/<int:pk>', login_required(Item_detail.as_view()), name='item_detail'),
	path('tipo_item/detalles/<int:pk>', login_required(Item_type_detail.as_view()), name='item_type_detail'),
	path('tema/detalles/<int:pk>', login_required(Theme_detail.as_view()), name='theme_detail'),
	path('categoria/detalles/<int:pk>', login_required(Category_detail.as_view()), name='category_detail'),


	#CRUD Collection -> storage
	path('coleccion', login_required(Collection_list.as_view()), name='collection_list'),
	path('coleccion/agregar', login_required(Collection_create.as_view()), name='collection_create'),
	path('coleccion/modificar/<int:pk>/', login_required(Collection_update.as_view()), name='collection_update'),
	path('coleccion/eliminar/<int:pk>/', login_required(Collection_delete.as_view()), name='collection_delete'),

	#CRUD Item -> storage
	path('item', login_required(Item_list.as_view()), name='item_list'),
	path('item/agregar', login_required(Item_Create.as_view()), name='item_create'),
	path('item/modificar/<int:pk>/', login_required(Item_update.as_view()), name='item_update'),
	path('item/eliminar/<int:pk>/', login_required(Item_delete.as_view()), name='item_delete'),

	#CRUD Tag -> storage
	path('tag', login_required(Tag_list.as_view()), name='tag_list'),
	path('tag/agregar', login_required(Tag_create.as_view()), name='tag_create'),
	path('tag/modificar/<int:pk>/', login_required(Tag_update.as_view()), name='tag_update'),
	path('tag/eliminar/<int:pk>/', login_required(Tag_delete.as_view()), name='tag_delete'),

	#CRUD Item_type -> storage
	path('tipo_item', login_required(Item_type_list.as_view()), name='item_type_list'),
	path('tipo_item/agregar', login_required(Item_type_create.as_view()), name='item_type_create'),
	path('tipo_item/modificar/<int:pk>/', login_required(Item_type_update.as_view()), name='item_type_update'),
	path('tipo_item/eliminar/<int:pk>/', login_required(Item_type_delete.as_view()), name='item_type_delete'),

	#CRUD Theme -> storage
	path('tema', login_required(Theme_list.as_view()), name='theme_list'),
	path('tema/agregar', login_required(Theme_create.as_view()), name='theme_create'),
	path('tema/modificar/<int:pk>/', login_required(Theme_update.as_view()), name='theme_update'),
	path('tema/eliminar/<int:pk>/', login_required(Theme_delete.as_view()), name='theme_delete'),

	#CRUD Category -> storage
	path('categoria', login_required(Category_list.as_view()), name='category_list'),
	path('categoria/agregar', login_required(Category_create.as_view()), name='category_create'),
	path('categoria/modificar/<int:pk>/', login_required(Category_update.as_view()), name='category_update'),
	path('categoria/eliminar/<int:pk>/', login_required(Category_delete.as_view()), name='category_delete'),

	#busqueda avanzada
	path('categoria/busqueda', login_required(Search_category), name='category_search'),
	path('coleccion/busqueda', login_required(Search_collection), name='collection_search'),
	path('item/busqueda', login_required(Search_item), name='item_search'),
	path('tema/busqueda', login_required(Search_theme), name='theme_search'),
	path('tipo_item/busqueda', login_required(Search_item_type), name='item_type_search'),
	path('tag/busqueda', login_required(Search_tag), name='tag_search'),

]
















	