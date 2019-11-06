from django.db import models

# Create your models here.
class Noticias(models.Model):
	titulo = models.CharField(max_length=50)
	descripcion = models.TextField(blank=True)
	fecha = models.DateField(blank=True, null=True)
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)
	foto = models.ImageField(upload_to='noticias/fotos', 
		blank=True,
		null=True
		)

