from django.shortcuts import render
from datetime import datetime
from django.contrib.auth.decorators import login_required
from noticias.models import Noticia


noticias = Noticia.objects.all().order_by('-created')

@login_required
def listar_noticias(request):
	return render(request, 'noticias/noticias.html', {'noticias':noticias})
