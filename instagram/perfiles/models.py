from django.db import models

from django.contrib.auth.models import User

class Perfil(models.Model):
	user = models. OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
	biografia = models.TextField(max_length=1000, blank = True, null =True)
	sitio_web = models.CharField(max_length=45, blank=True, null = True)
	sexo = models.PositiveIntegerField(blank=True, null=True)
	telefono = models.CharField(blank=True, max_length=20, null=True)
	created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
	modified = models.DateTimeField(auto_now=True, blank=True, null = True)
	foto_perfil = models.ImageField(upload_to='perfiles/fotos', 
		blank=True,
		null=True,
		)
	seguidores = models.ManyToManyField('self', through='Seguidor',
                                      symmetrical=False)


class Foto(models.Model):
	user_id = models.ForeignKey(Perfil, on_delete=models.CASCADE, blank=True, null=True)
	created = models.DateTimeField(null=False, blank=False)
	foto = models.ImageField(upload_to='perfiles/fotos', 
		blank=False,
		null=False,
		)
	descripcion = models.TextField(max_length=1000, blank=True, null=True)
	created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
	modified = models.DateTimeField(auto_now=True, blank=True, null = True)

class Comentario(models.Model):
	user_id = models.ForeignKey(Perfil, on_delete=models.CASCADE, blank=True, null=True)
	foto_id = models.ForeignKey(Foto, on_delete=models.CASCADE, blank=True, null=True)
	descripcion = models.TextField(max_length=1000, blank=True, null=True)
	created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
	modified = models.DateTimeField(auto_now=True, blank=True, null = True)

class Like(models.Model):
	user_id = models.OneToOneField(Perfil, on_delete=models.CASCADE, blank=True, null=True)
	foto_id = models.ForeignKey(Foto, on_delete=models.CASCADE, blank=True, null=True)
	created = models.DateTimeField(auto_now_add=True, blank=True, null=True)


class Seguidor(models.Model):
	user_id = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='Seguido')
	followed_user_id = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='Seguidor')
	created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
