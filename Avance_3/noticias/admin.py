from django.contrib import admin

from noticias.models import Noticia

# Register your models here.
#admin.site.register(Noticias)

@admin.register(Noticia)
class NoticiasAdmin(admin.ModelAdmin):
	list_display = ('pk', 'perfil_id', 'foto_id')
	list_display_links = ('pk',)
	list_editable = ('foto_id',)

	search_fields = ('titulo',)

	list_filter = ('modified',)
