#formularios django
from django import forms


from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class User_form(UserCreationForm):

	class Meta:
		model = User
		fields = [
				'username',
				'first_name',
				'last_name',
				'email',
			]
		labels = {
				'username': 'Nombre de usuario',
				'first_name': 'Nombre',
				'last_name': 'Apellidos',
				'email': 'Correo',
		}
		#diseño del campo
		widgets = {
			'username':forms.TextInput(attrs={'class':'form-control','placeholder':'username','required': True}),
			'first_name':forms.TextInput(attrs={'class':'form-control','placeholder':'nombre','required': True}),
			'last_name':forms.TextInput(attrs={'class':'form-control','placeholder':'apellido','required': True}),
			'email':forms.TextInput(attrs={'class':'form-control','type':'email','placeholder':'correo','required': True}),
		}


class User_activate(UserCreationForm):

	class Meta:
		model = User
		fields = [
				'is_active',

			]
		labels = {
				'is_active': 'estado',

		}