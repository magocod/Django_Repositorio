#manipular urls
from django.urls import path

#reestringir urls
from django.contrib.auth.decorators import login_required

#vistas modulo
from backend.account.views import Dashboard


#nombre
app_name = 'account'

urlpatterns = [
	
	#principal
	path('account', login_required(Dashboard.as_view()), name='dashboard'),

	#operaciones

	
]