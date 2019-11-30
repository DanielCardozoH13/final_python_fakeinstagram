from django.db import models
from django import template

from django.contrib.auth.models import User

register = template.Library()

class Perfil(models.Model):
	SEXO_STATUS = (
        ('m', 'Mujer'),
        ('h', 'Hombre'),
        ('n', 'No_definido'),
    )
	user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
	biografia = models.TextField(max_length=1000, blank = True, null =True)
	sitio_web = models.CharField(max_length=45, blank=True, null = True)
	sexo = models.CharField(blank=True, null=True, max_length=1, choices=SEXO_STATUS, default='n')
	telefono = models.CharField(blank=True, max_length=20, null=True)
	created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
	modified = models.DateTimeField(auto_now=True, blank=True, null = True)
	foto_perfil = models.ImageField(upload_to='perfiles/fotos',
		blank=True,
		null=True,
		default='https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSf_Bf0-x44hsGqqcQwrTcNeLUSnYjlDuoql-hQHydDdBwxeCT2'
		)
	seguidores = models.ManyToManyField('self', through='Seguidores',
                                      symmetrical=False)

	def __str__(self):
		return '{}, {}, {}, {}, {}, {}, {}, {}'.format(self.id, 
														self.biografia, 
														self.sitio_web, 
														self.sexo,
														self.telefono,
														self.foto_perfil,
														self.created,
														self.modified,
														)

	@property
	def seguidores(self):
		seguidores = Seguidores.objects.filter(seguido=self.id)
		return seguidores

	@property
	def seguidos(self):
		seguidos = Seguidores.objects.filter(seguidor=self.id)
		return seguidos

	

class Foto(models.Model):
	perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, blank=True, null=True)
	titulo = models.TextField(max_length=250, blank=False, null=True)
	foto = models.ImageField(upload_to='perfiles/fotos',
		blank=False,
		null=False,
		)
	is_historia = models.BooleanField(default=False)
	descripcion = models.TextField(max_length=1000, blank=True, null=True)
	created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
	modified = models.DateTimeField(auto_now=True, blank=True, null = True)

	@property
	def comentarios(self):
		comentarios = Comentario.objects.all().filter(foto_id=self.id)
		return comentarios

class Comentario(models.Model):
	perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, blank=True, null=True)
	foto = models.ForeignKey(Foto, on_delete=models.CASCADE, blank=True, null=True)
	descripcion = models.TextField(max_length=1000, blank=True, null=True)
	created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
	modified = models.DateTimeField(auto_now=True, blank=True, null = True)

class Like(models.Model):
	perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, blank=True, null=True)
	foto = models.ForeignKey(Foto, on_delete=models.CASCADE, blank=True, null=True)
	created = models.DateTimeField(auto_now_add=True, blank=True, null=True)


class Seguidores(models.Model):
	seguido = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='Seguido')
	seguidor = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='Seguidor')
	created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
