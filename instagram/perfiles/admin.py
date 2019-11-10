from django.contrib import admin

from perfiles.models import *
# Register your models here.
	
@admin.register(Perfile)
class PerfilesAdmin(admin.ModelAdmin):
	list_display = ('pk', 'sitio_web', 'sexo')
	list_display_links = ('pk',)
	list_editable = ('sitio_web',)

	#search_fields = ('titulo', 'fecha')

	#list_filter = ('created', 'modified', 'fecha')

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