from django.shortcuts import render, redirect
from datetime import timedelta
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from noticias.models import Noticia
from perfiles.models import Like, Foto, Perfil
from django.db.models import Count



@login_required
def listar_noticias(request):
	#noticias = Noticia.objects.all().annotate(cuenta_likes = Count('foto__id')).order_by('-created')
	noticias = Noticia.objects.all().order_by('-created')
	likes = Like.objects.all().annotate(foto_count = Count('foto'))

	today = timezone.now()
	yesterday = today - timedelta(days=1)
	historias = Foto.objects.all().filter(is_historia=True, created__range=[yesterday, today]).order_by('-created')

	return render(request, 'noticias/noticias.html', {'noticias':noticias, 'historias':historias, 'likes':likes})

@login_required
def me_gusta(request, foto_id=None, perfil_id=None):
	if foto_id and perfil_id:
		perfil = Perfil.objects.get(id=perfil_id)
		foto = Foto.objects.get(id=foto_id)
		print(foto)

		like = Like(perfil=perfil,
					foto=foto,)
		like.save(force_insert=True)

	return redirect('noticias')