from django.shortcuts import render
from datetime import datetime
from django.contrib.auth.decorators import login_required
from noticias.models import Noticia


noticias = Noticia.objects.all()#.select_related("foto_id")

# Create your views here.}
@login_required
def listar_noticias(request):
	return render(request, 'noticias/noticias.html', {'noticias':noticias})
