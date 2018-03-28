#manipular urls
from django.urls import path, include

#reestringir urls
from django.contrib.auth.decorators import login_required

#vistas
from backend.api.views import Api_data_test, Records_API, Api_link_test, List_API
#basico
from backend.api.views import Collection_API, Item_APIv1, Item_type_API, Tag_API, Category_API, Theme_API
#paginado
from backend.api.viewsv2 import Item_APIv2, Theme_APIv2


from rest_framework import routers

from backend.api.viewsets import Collection_viewset, Item_viewset, Item_typeviewset

router = routers.DefaultRouter()
router.register('api_rest_collection', Collection_viewset)
router.register('api_rest_item', Item_viewset)
router.register('api_rest_itemtype', Item_typeviewset)

#nombre
app_name = 'api'

urlpatterns = [
	#repository
	path('storage/data_coleccion', Collection_API.as_view(), name='api_data_coleccion'),
	path('storage/data_item', Item_APIv2.as_view(), name='api_data_item'),
	path('storage/data_item_type', Item_type_API.as_view(), name='api_data_item_type'),
	path('storage/data_tag', Tag_API.as_view(), name='api_data_tag'),
	path('storage/data_categoria', Category_API.as_view(), name='api_data_category'),
	path('storage/data_tema', Theme_APIv2.as_view(), name='api_data_theme'),

	#renderizado
	path('records', Records_API.as_view(), name='api_records'),
	path('elements', List_API.as_view(), name='api_element_lists'),

	#test-data
	path('data', Api_data_test.as_view(), name='api_data'),
	path('links', Api_link_test.as_view(), name='api_data_links'),
	

	#api-router
	path('rest', include(router.urls))


	
]