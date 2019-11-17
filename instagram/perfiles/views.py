from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from perfiles.models import Perfil

def logout_view(request):
	return render(request, 'perfiles/login.html')

@login_required
def perfil_view(request):
	return render(request, 'perfiles/perfil.html')

def logup_view(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('login')
	else:
		form = UserCreationForm()

	return render(request,'registration/logup.html', {'form':form})

@login_required
def update_profile(request):
	profile = request.user.perfil

	if request.method == 'POST':
		form = PerfilForm(request.POST, request.FILES)
		if form.is_valid():
			data = form.cleaned_data
			profile.biografia = data['biografia']
			profile.sitio_web = data['sitio_web']
			profile.sexo = data['sexo']
			profile.telefono = data['telefono']
			profile.foto_perfil = data['foto_perfil']
			profile.save()

			return redirect('update_profile')

	else:
		form = PerfilForm()

	return render(
		request=request,
		template_name = 'users/update_profile.html',
		context = {
			'profile': profile,
			'user':	request.user,
			'form' : form
			}
		)
