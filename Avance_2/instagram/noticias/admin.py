from django.contrib import admin

from noticias.models import Noticia

# Register your models here.
#admin.site.register(Noticias)

@admin.register(Noticia)
class NoticiasAdmin(admin.ModelAdmin):
	list_display = ('pk', 'titulo', 'descripcion', 'fecha')
	list_display_links = ('pk',)
	list_editable = ('titulo',)

	search_fields = ('titulo', 'fecha')

	list_filter = ('created', 'modified', 'fecha')
