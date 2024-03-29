from django.contrib import admin
from django.urls import path
from noticias import views as noticias_views
from perfiles import views as perfiles_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', noticias_views.listar_noticias, name='noticias'),
    path('perfiles/login/', perfiles_views.login_view, name="login"),
    path('perfil/', perfiles_views.perfil_view, name="perfil"),
    #path('saludo/<str:nombre>/<int:edad>/', views.saludar)
]
