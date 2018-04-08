#manipular urls
from django.urls import path

#reestringir urls
from django.contrib.auth.decorators import login_required

#vistas modulo
from backend.account.views import Dashboard
#crud
from backend.account.views import User_list, User_create, User_update, User_delete, User_detail, User_active


#nombre
app_name = 'account'

urlpatterns = [
	
	#principal
	path('dashboard', login_required(Dashboard.as_view()), name='dashboard'),

	#operaciones
	path('user/active/<int:pk>/', login_required(User_active.as_view()), name='user_active'),

	#crud
	path('user/list', login_required(User_list.as_view()), name='user_list'),
	path('user/agregar', login_required(User_create.as_view()), name='user_create'),
	path('user/detalles/<int:pk>/', login_required(User_detail.as_view()), name='user_detail'),
	path('user/modificar/<int:pk>/', login_required(User_update.as_view()), name='user_update'),
	path('user/eliminar/<int:pk>/', login_required(User_delete.as_view()), name='user_delete'),

	
]