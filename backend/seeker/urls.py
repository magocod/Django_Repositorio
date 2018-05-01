#manipular urls
from django.urls import path

#reestringir urls
from django.contrib.auth.decorators import login_required

#vistas busquedas base
from backend.seeker.views import  Title_seeker_base, Category_seeker_base, Author_seeker_base, Theme_seeker_base, Tag_seeker_base

#vistas busquedas por parametros
from backend.seeker.searches import Search_item_letters, Search_item_letter, Search_item_exacts
from backend.seeker.searches import Search_category_collections, Search_collection_exact, Search_collection_pk, Search_collection_items
from backend.seeker.searches import Search_theme_letters, Search_theme_collections, Search_theme_exact, Search_author_letters
from backend.seeker.searches import Search_item_id, Search_theme_id

#vistas busquedas sin parametros
from backend.seeker.views import Info_seeker, Recent_items
from backend.seeker.views import All_seeker, Records_seeker


#nombre
app_name = 'seeker'

urlpatterns = [

	#busquedas sin parametros ################################################

	#informacion del repositorio
	path('informacion', Info_seeker.as_view(), name='info'),
	#recientes
	path('recursos/ultimos', Recent_items.as_view(), name='recent_items'),
	#pruebas
	path('prueba/capacidad', Records_seeker.as_view(), name='test_records'),
	path('prueba/carga', All_seeker.as_view(), name='test_charge'),

	#busquedas con parametros ###############################################

	#titulo
	path('titulo', Title_seeker_base.as_view(), name='title_base'),
	path('titulo/letras', Search_item_letters, name='title_letters'),
	path('titulo/letra/<slug:slug>/', Search_item_letter, name='title_letter'),
	
	#categoria
	path('categoria', Category_seeker_base.as_view(), name='category_base'),
	path('categoria/colecciones/<int:pk>/', Search_category_collections, name='category_collections'),

	#coleccion
	path('coleccion/<int:pk>/', Search_collection_pk, name='collection_pk'),
	path('coleccion/items/<int:pk>/', Search_collection_items, name='search_collection_items'),

	#tema
	path('tematica', Theme_seeker_base.as_view(), name='theme_base'),
	path('tematica/letras', Search_theme_letters, name='theme_letters'),
	path('tematica/colecciones/<int:pk>/', Search_theme_collections, name='theme_collections'),

	#autor
	path('autor', Author_seeker_base.as_view(), name='author_base'),
	path('autor/items', Search_author_letters, name='author_letters'),


	#autocompletado
	path('recurso/busqueda', Search_item_exacts, name='item_exacts'),
	path('coleccion/busqueda', Search_collection_exact, name='collection_exact'),
	path('tematica/busqueda', Search_theme_exact, name='theme_exact'),

	#detalles 
	path('item/detalles/<int:pk>/', Search_item_id.as_view(), name='item_pk'),
	path('tematica/detalles/<int:pk>/', Search_theme_id.as_view(), name='theme_pk'),
	

	
]