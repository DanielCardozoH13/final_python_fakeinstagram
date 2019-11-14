from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.
def login_view(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user:
			login(request, user)
			return redirect('noticias')
		else:
			return render(request, 'perfiles/login.html', {'error' : 'Credenciales invalidas'})
	return render(request, 'perfiles/login.html')

@login_required
def perfil_view(request):
	return render(request, 'perfiles/perfil.html', {'perfil':perfil, 'publicaciones':publicaciones})
