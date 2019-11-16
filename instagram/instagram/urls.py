from django.contrib import admin
from django.urls import path
from noticias import views as noticias_views
from perfiles import views as perfiles_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', noticias_views.listar_noticias, name='noticias'),
    path('perfiles/login/', perfiles_views.login_view, name="login"),
    path('perfiles/logout/', perfiles_views.logout_view, name="logout"),
    path('perfil/', perfiles_views.perfil_view, name="perfil"),
    #path('saludo/<str:nombre>/<int:edad>/', views.saludar)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
