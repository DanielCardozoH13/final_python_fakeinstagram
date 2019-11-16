from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm 



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
