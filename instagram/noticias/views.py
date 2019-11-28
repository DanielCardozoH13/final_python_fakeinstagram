from django.shortcuts import render, redirect
from datetime import timedelta
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from noticias.models import Noticia
from perfiles.models import Like, Foto

noticias = Noticia.objects.all().order_by('-created')

today = timezone.now()
yesterday = today - timedelta(days=1)
historias = Foto.objects.all().filter(is_historia=True, created__range=[yesterday, today]).order_by('-created')

@login_required
def listar_noticias(request):
	return render(request, 'noticias/noticias.html', {'noticias':noticias, 'historias':historias})

@login_required
def me_gusta(request, foto_id=None, perfil_id=None):
	if foto_id and perfil_id:
		try:
			like = Like(perfil_id=perfil_id,
						foto_id=foto_id,)
			like.save(force_insert=True)
		except:
			pass

	return redirect('noticias')