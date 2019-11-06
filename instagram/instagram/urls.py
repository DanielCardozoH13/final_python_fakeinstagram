from django.contrib import admin
from django.urls import path
from noticias import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('noticias/', views.listar_noticias),
    #path('saludo/<str:nombre>/<int:edad>/', views.saludar)
]
