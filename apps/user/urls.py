# Django
from django.urls import path

# local Django
from apps.user.views import VAuthentication, VUser

urlpatterns = [
	# auth
  path('token-auth/', VAuthentication.CustomAuthToken.as_view(), name='api_token_auth'),
  path('email/', VAuthentication.VEmail.as_view(), name='api_email_check'),
  path('user/logout/', VAuthentication.VLogout.as_view(), name='api_users_logout'),

  # user
  path('users/', VUser.VUserList.as_view(), name='api_users'),
  path('user/<int:pk>/', VUser.VUserDetail.as_view(), name='api_user_detail'),
]