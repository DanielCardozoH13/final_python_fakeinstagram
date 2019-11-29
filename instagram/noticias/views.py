from django.shortcuts import render, redirect
from datetime import timedelta
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from noticias.models import Noticia
from perfiles.models import Like, Foto, Perfil, Comentario
from django.db.models import Count



@login_required
def listar_noticias(request):
	noticias = Noticia.objects.all().order_by('-created')

	today = timezone.now()
	yesterday = today - timedelta(days=1)
	historias = Foto.objects.all().filter(is_historia=True, created__range=[yesterday, today]).order_by('-created')
	
	return render(request, 'noticias/noticias.html', {'noticias':noticias, 'historias':historias})
	# return render(request, 'noticias/noticias.html', {'noticias':noticias})

@login_required
def me_gusta(request, foto_id=None, perfil_id=None):
	if foto_id and perfil_id:
		try:
			#si existe el like, lo elimna.
			like_validation = Like.objects.get(foto_id=foto_id, perfil_id=perfil_id)
			like_validation.delete()
		except:
			#si no existe el like lo crea.
			perfil = Perfil.objects.get(id=perfil_id)
			foto = Foto.objects.get(id=foto_id)

			like = Like(perfil=perfil,
						foto=foto,)
			like.save(force_insert=True)

	return redirect('noticias')

@login_required
def add_comment(request, foto_id=None, perfil_id=None):
	if foto_id and perfil_id:
		if request.method == 'POST':
			perfil = Perfil.objects.get(id=perfil_id)
			foto = Foto.objects.get(id=foto_id)

			if request.POST['comentario']:
				cometario = request.POST['comentario']
				coment = Comentario(perfil=perfil,
							foto=foto, 
							descripcion=cometario,)
				coment.save(force_insert=True)

	return redirect('noticias')