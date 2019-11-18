from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from perfiles.models import Perfil, Foto
from perfiles.forms import updatePerfilForm, SignupForm, addPostForm



def logout_view(request):
	return render(request, 'perfiles/login.html')

@login_required
def perfil_view(request):
	user = User.objects.get(username=request.user)
	# perfil = Perfil.objects.filter(user=user.id).values()
	perfil = Perfil.objects.all().filter(user=user.id)
	if perfil[0].foto_perfil:
		foto_perfil = perfil[0].foto_perfil.url
	else:
		foto_perfil=""

	return render(request, 'perfiles/perfil.html', {'perfil':perfil, 'foto_perfil':foto_perfil})

def logup_view(request):
	if request.method == 'POST':
		form = SignupForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('login')
	else:
		form = SignupForm()

	return render(request,'registration/logup.html', {'form':form})

@login_required
def update_profile(request):
	user = User.objects.get(username=request.user)
	perfil = Perfil.objects.get(user=user.id)

	if request.method == 'POST':
		template_name = 'perfiles/perfil.html'
		form = updatePerfilForm(request.POST, request.FILES)
		if form.is_valid():
			data = form.cleaned_data
			perfil.sitio_web = data['website']
			perfil.telefono = data['telefono']
			perfil.biografia = data['biografia']
			perfil.foto_perfil = data['foto']
			perfil.sexo = data['sexo']
			perfil.save()

			return redirect('perfil')
		else:
			form = updatePerfilForm() 
			args = {'form': form}
			return render(request, template_name, args)
	else:
		form = updatePerfilForm()

	return render(
		request=request,
		template_name = 'perfiles/update_profile.html',
		context = {
			'perfil': perfil,
			'user':	user,
			'form' : form
			}
		)

@login_required
def add_post(request):
	template_name='perfiles/add_post.html'
	user = User.objects.get(username=request.user)
	perfil = Perfil.objects.get(user=user.id)

	if request.method == 'POST':
		form = addPostForm(request.POST, request.FILES)
		if form.is_valid():
			data = form.cleaned_data
			foto = Foto(perfil=perfil, 
						titulo=data['titulo'],
						descripcion=data['descripcion'],
						foto=data['foto'],
						)
			foto.save(force_insert=True)

			return redirect('perfil')
		else:
			form = addPostForm() 
			args = {'form': form}
			return render(request, template_name, args)
	else:
		form = addPostForm()

	return render(
		request=request,
		template_name = template_name,
		context = {
			'form':form
			}
		)
