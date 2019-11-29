from django.contrib import admin
from django.urls import path
from noticias import views as noticias_views
from perfiles import views as perfiles_views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', noticias_views.listar_noticias, name='noticias'),
    path('perfil/', perfiles_views.perfil_view, name="perfil"),
    path('perfil/<int:perfil_id>', perfiles_views.perfil_view, name="perfil_id"),

    path('perfiles/logup', perfiles_views.logup_view, name="logup"),
    path('perfiles/login/', LoginView.as_view(), name="login"),
    path('perfiles/logout/', LogoutView.as_view(next_page='login'), name="logout"),
    path('users/me/profile/', perfiles_views.update_profile, name='update_profile'),
    path('perfiles/add_post', perfiles_views.add_post, name='add_post'),
    path('perfiles/add_post/<str:history>', perfiles_views.add_post, name='add_history'),
    path('perfiles/edit_post', perfiles_views.edit_post, name='edit_post'),
    path('perfiles/delete_post/<int:post_id>', perfiles_views.delete_post, name='delete_post'),
    path('perfiles/delete_post/<int:post_id>/noticias', perfiles_views.delete_historia, name='delete_noticia'),
    path('noticias/me_gusta/<int:foto_id>/<int:perfil_id>', noticias_views.me_gusta, name='me_gusta'),
    path('noticias/comentario/<int:foto_id>/<int:perfil_id>', noticias_views.add_comment, name='comentario'),
    path('perfiles/seguir/<int:perfil_id>', perfiles_views.seguir, name='seguir'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
