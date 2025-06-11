from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # App principal
    path('', include('productos.urls')),

    # App de contacto (si existe)
    path('contacto/', include('contacto.urls')),

    # Autenticación básica: login, logout, reset
    path('accounts/', include('django.contrib.auth.urls')),  # login/logout/password
    path('accounts/', include('accounts.urls')),  # Registro personalizado (signup)

    # Logout explícito
    path('logout/', auth_views.LogoutView.as_view(next_page='/accounts/login/'), name='logout'),
]

# Archivos media
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

