#manipular urls
from django.urls import path

#reestringir urls
from django.contrib.auth.decorators import login_required

#vistas modulos base
from backend.seeker.views import Info_seeker, Title_seeker_base, Category_seeker_base, Author_seeker_base, Date_seeker_base, Theme_seeker_base

from backend.seeker.searches import Search_collection_pk, Search_author, Search_letters_exacts, Search_collection_items, Search_date, Search_date_publication 
from backend.seeker.searches import Search_theme_letters, Search_letters, Search_letter, Search_theme_collections, Search_collection_category, Search_letters_exacts
from backend.seeker.views import All_seeker, Records_seeker, Item_seeker, Recent_items
from backend.seeker.filter_views import Theme_searchv1, Theme_search_collection, Theme_search_items

#vistas categoria


#nombre
app_name = 'seeker'

urlpatterns = [

	#detalles item
	path('item/detalles/<int:pk>/', Item_seeker.as_view(), name='seeker_item'),

	#informacion del repositorio
	path('informacion', Info_seeker.as_view(), name='seeker_info'),
	#recientes
	path('recursos/ultimos', Recent_items.as_view(), name='recent_items'),

	#pruebas
	path('todo', All_seeker.as_view(), name='all'),
	path('registros', Records_seeker.as_view(), name='records'),

	#busqueda por titulos
	path('titulo', Title_seeker_base.as_view(), name='seeker_title_base'),
	path('titulo/letras', Search_letters, name='seeker_title_letters'),
	path('titulo/autocompletado', Search_letters_exacts, name='seeker_title_letters_exacts'),
	path('titulo/letra/<slug:slug>/', Search_letter, name='seeker_title_letter'),

	#busqueda por categoria
	path('categoria', Category_seeker_base.as_view(), name='seeker_category_base'),
	path('categoria/colecciones/<int:pk>/', Search_collection_category, name='seeker_category_collections'),
	path('categoria/coleccion/<int:pk>/', Search_collection_pk, name='seeker_category_collection'),
	path('categoria/coleccion/itemslist/<int:pk>', Search_collection_items, name='seeker_category_listitems'),
	path('categoria/coleccion/item/', Search_letters_exacts, name='seeker_category_item'),

	#busqueda por tema
	path('tema', Theme_seeker_base.as_view(), name='seeker_theme_base'),
	path('tema/busqueda', Search_theme_letters, name='seeker_theme_letters'),
	path('tema/colecciones/<int:pk>/', Search_theme_collections, name='seeker_theme_collections'),

	#busqueda por autores
	path('autor', Author_seeker_base.as_view(), name='seeker_author_base'),
	path('autor/busqueda', Search_author, name='seeker_author_search'),

	#busqueda por fechas
	path('fecha', Date_seeker_base.as_view(), name='seeker_date_base'),
	path('fecha/creacion', Search_date, name='seeker_date_creation'),
	path('fecha/año', Search_date_publication, name='seeker_date_publication'),

	
]