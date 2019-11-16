from django.db import models
from django.contrib.auth.models import User
from perfiles.models import Perfil



class Noticia(models.Model):
	user = models. ForeignKey(User, on_delete=models.CASCADE, null=True)
	perfil = models. ForeignKey(Perfil, on_delete=models.CASCADE, null=True)
	titulo = models.CharField(max_length=50)
	descripcion = models.TextField(blank=True)
	fecha = models.DateField(blank=True, null=True)
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)
	foto = models.ImageField(upload_to='noticias/fotos',blank=True,
		null=True,)
