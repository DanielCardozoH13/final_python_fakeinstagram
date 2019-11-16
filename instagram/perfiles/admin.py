from django.contrib import admin

from perfiles.models import *
# Register your models here.

@admin.register(Perfil)
class PerfilesAdmin(admin.ModelAdmin):
	list_display = ('pk', 'sitio_web', 'sexo', 'telefono', 'created', 'foto_perfil')
	list_display_links = ('pk',)
	list_editable = ('sitio_web', 'foto_perfil')

@admin.register(Foto)
class FotosAdmin(admin.ModelAdmin):
	list_display = ('pk', 'foto', 'descripcion')
	list_display_links = ('pk',)
	list_editable = ('descripcion',)
	search_fields = ('modified', 'created')

@admin.register(Comentario)
class FotosAdmin(admin.ModelAdmin):
	list_display = ('pk', 'descripcion')
	list_display_links = ('pk',)
	list_editable = ('descripcion',)
	search_fields = ('modified', 'created')
