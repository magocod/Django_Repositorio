#manipular urls
from django.urls import path, include

#reestringir urls
from django.contrib.auth.decorators import login_required

#vistas
from backend.api.views.links import Api_data, Api_link
#basico
from backend.api.views.v1 import Collection_APIv1, Item_APIv1, Item_type_APIv1, Tag_APIv1, Category_APIv1, Theme_APIv1, List_API, Records_API
#paginado
from backend.api.views.v2 import Item_APIv2, Theme_APIv2, Category_APIv2, Collection_APIv2, Item_type_APIv2, Tag_APIv2

#GET
from backend.api.views.get import Item_id

from rest_framework import routers
from backend.api.views.viewsets import Collection_viewset, Item_viewset, Item_typeviewset

router = routers.DefaultRouter()
router.register('api_rest_collection', Collection_viewset)
router.register('api_rest_item', Item_viewset)
router.register('api_rest_itemtype', Item_typeviewset)

#nombre
app_name = 'api'

urlpatterns = [
	#repository -JSON -v1
	path('storage/data_coleccion', Collection_APIv1.as_view(), name='api_data_coleccion'),
	path('storage/data_item', Item_APIv1.as_view(), name='api_data_item'),
	path('storage/data_item_type', Item_type_APIv1.as_view(), name='api_data_item_type'),
	path('storage/data_tag', Tag_APIv1.as_view(), name='api_data_tag'),
	path('storage/data_categoria', Category_APIv1.as_view(), name='api_data_category'),
	path('storage/data_tema', Theme_APIv1.as_view(), name='api_data_theme'),

	#repository -JSON -v2
	path('colecciones', Collection_APIv2.as_view(), name='api_coleccion'),
	path('items', Item_APIv2.as_view(), name='api_item'),
	path('item_types', Item_type_APIv2.as_view(), name='api_item_type'),
	path('tags', Tag_APIv2.as_view(), name='api_tag'),
	path('categorias', Category_APIv2.as_view(), name='api_category'),
	path('temas', Theme_APIv2.as_view(), name='api_theme'),

	#repository -JSON -GET
	path('detail/item/<int:pk>', Item_id, name='api_item_id'),

	#renderizado
	path('records', Records_API.as_view(), name='api_records'),
	path('elements', List_API.as_view(), name='api_element_lists'),

	#links
	path('data', Api_data.as_view(), name='api_data'),
	path('', Api_link.as_view(), name='api_data_links'),
	

	#api-router
	path('rest', include(router.urls))


	
]