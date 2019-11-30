from django.db import models
from django.contrib.auth.models import User
from perfiles.models import Perfil, Foto, Like, Comentario
from django.db.models import Count




class Noticia(models.Model):
	user = models. ForeignKey(User, on_delete=models.CASCADE, null=True)
	perfil = models. ForeignKey(Perfil, on_delete=models.CASCADE, null=True)
	foto = models. ForeignKey(Foto, on_delete=models.CASCADE, null=True)
	created = models.DateTimeField(auto_now_add=True, null=True)
	modified = models.DateTimeField(auto_now=True)

	@property
	def likes_foto(self):
		"Returns los likes de la foto del id enviado."
		likes = Like.objects.filter(foto_id=self.foto).count()
		return likes

	@property
	def liked_foto(self):
		##retornara 1 si hay un like del usuario sobre la foto
		liked = Like.objects.filter(foto_id=self.foto, perfil_id = self.perfil).count()
		return liked
	
	@property
	def comentarios(self):
		comentarios = Comentario.objects.filter(foto_id=self.foto.id)
		return comentarios
	
	
