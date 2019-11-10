from django.db import models

# Create your models here.
class Perfile(models.Model):
	biografia = models.TextField(max_length=1000, blank = True, null =True)
	sitio_web = models.CharField(max_length=45, blank=True, null = True)
	sexo = models.PositiveIntegerField(blank=True, null=True)
	foto_perfil = models.ImageField(upload_to='perfiles/fotos', 
		blank=True,
		null=True,
		)

class Foto(models.Model):
	created = models.DateTimeField(null=False, blank=False)
	foto = models.ImageField(upload_to='perfiles/fotos', 
		blank=False,
		null=False,
		)
	descripcion = models.TextField(max_length=1000, blank=True, null=True)
	modified = models.DateTimeField(null=True, blank=True)

class Comentario(models.Model):
	descripcion = models.TextField(max_length=1000, blank=True, null=True)
	created = models.DateTimeField(null=False, blank=False)
	modified = models.DateTimeField(null=True, blank=True)

		