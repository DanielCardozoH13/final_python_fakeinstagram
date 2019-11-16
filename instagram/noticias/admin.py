from django.contrib import admin

from noticias.models import Noticia

# Register your models here.
#admin.site.register(Noticias)

@admin.register(Noticia)
class NoticiasAdmin(admin.ModelAdmin):
	list_display = ('pk', 'perfil', 'titulo', 'descripcion', 'fecha', 'created', 'foto')
	list_display_links = ('pk',)
	list_editable = ('titulo', 'foto')

	search_fields = ('titulo', 'created')

	list_filter = ('created', 'modified', 'fecha')
