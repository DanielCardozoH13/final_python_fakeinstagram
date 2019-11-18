from django.db import models

from django.contrib.auth.models import User

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
	seguidores = models.ManyToManyField('self', through='Seguidor',
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


class Foto(models.Model):
	perfil_id = models.ForeignKey(Perfil, on_delete=models.CASCADE, blank=True, null=True)
	titulo = models.TextField(max_length=1000, blank=False, null=True)
	foto = models.ImageField(upload_to='perfiles/fotos',
		blank=False,
		null=False,
		)
	descripcion = models.TextField(max_length=1000, blank=True, null=True)
	created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
	modified = models.DateTimeField(auto_now=True, blank=True, null = True)

class Comentario(models.Model):
	perfil_id = models.ForeignKey(Perfil, on_delete=models.CASCADE, blank=True, null=True)
	foto_id = models.ForeignKey(Foto, on_delete=models.CASCADE, blank=True, null=True)
	descripcion = models.TextField(max_length=1000, blank=True, null=True)
	created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
	modified = models.DateTimeField(auto_now=True, blank=True, null = True)

class Like(models.Model):
	perfil_id = models.OneToOneField(Perfil, on_delete=models.CASCADE, blank=True, null=True)
	foto_id = models.ForeignKey(Foto, on_delete=models.CASCADE, blank=True, null=True)
	created = models.DateTimeField(auto_now_add=True, blank=True, null=True)


class Seguidor(models.Model):
	perfil_id = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='Seguido')
	followed_user_id = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='Seguidor')
	created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
