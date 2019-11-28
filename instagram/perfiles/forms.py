from django import forms

from django.contrib.auth.models import User
from perfiles.models import Perfil, Foto
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class SignupForm(forms.Form):
	username = forms.CharField(min_length=4, max_length=50, label='usuario')
	password = forms.CharField(max_length=70, widget=forms.PasswordInput(), label='Contraseña')
	password_confirmation = forms.CharField(max_length=70, widget=forms.PasswordInput(), label='Confirmacion de Contraseña')
	first_name = forms.CharField(min_length=2, max_length=50, label='Nombres')
	last_name = forms.CharField(min_length=2, max_length=50, label='Apellidos')
	email = forms.CharField(min_length=6, max_length=70, widget=forms.EmailInput(), label='Correo Electrónico')

	def clean_username(self):
		username = self.cleaned_data['username']
		username_taken = User.objects.filter(username=username).exists()
		if username_taken:
			raise forms.ValidationError('Usuario ya esta registrado')
		return username

	def clean(self):
		data = super().clean()
		password = data['password']
		password_confirmation = data['password_confirmation']
		if password != password_confirmation:
			raise forms.ValidationError('Password no son iguales')
		return data

	def save(self):
		data = self.cleaned_data
		data.pop('password_confirmation')
		user = User.objects.create_user(**data)
		profile = Perfil(user=user)
		profile.save()


class updatePerfilForm(forms.Form):
	SEXO_STATUS = [
		('m', 'Mujer'),
		('h', 'Hombre'),
		('n', 'No_definido'),
	]
	foto = forms.ImageField(label = "Foto de Perfil", required=False)
	website = forms.URLField(max_length=200, required=False, label='Sitio Web')
	biografia = forms.CharField(max_length=500, required=False, label='Biografía')
	telefono = forms.CharField(max_length=20, required=False, label='Telefono')
	sexo = forms.ChoiceField(required=False, choices=SEXO_STATUS, widget=forms.RadioSelect, label='sexo')

	class Meta:
		model = Perfil
		fields = (
		    'foto_perfil',
		    'sitio_web',
		    'biografia',
		    'sexo'
		)

class addPostForm(forms.Form):
	foto = forms.ImageField(label = "Foto", required=True)
	titulo = forms.CharField(max_length=20, required=True, label='Titulo')
	descripcion = forms.CharField(max_length=500, required=False, label='Descripción')


	class Meta:
		model = Foto
		fields = (
		    'titulo',
		    'foto',
		    'descripcion',
		)

