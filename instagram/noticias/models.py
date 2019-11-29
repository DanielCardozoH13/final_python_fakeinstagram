from django.db import models
from django.contrib.auth.models import User
from perfiles.models import Perfil, Foto, Like
from django.db.models import Count




class Noticia(models.Model):
	user = models. ForeignKey(User, on_delete=models.CASCADE, null=True)
	perfil = models. ForeignKey(Perfil, on_delete=models.CASCADE, null=True)
	foto = models. ForeignKey(Foto, on_delete=models.CASCADE, null=True)
	#titulo = models.CharField(max_length=50)
	#descripcion = models.TextField(blank=True)
	#fecha = models.DateField(blank=True, null=True)
	created = models.DateTimeField(auto_now_add=True, null=True)
	modified = models.DateTimeField(auto_now=True)
	#foto = models.ImageField(upload_to='noticias/fotos',blank=True,
	#	null=True,)

	@property
	def likes_foto(self):
		"Returns los likes de la foto del id enviado."
		likes = Like.objects.filter(foto_id=self.foto).count()

		return likes

