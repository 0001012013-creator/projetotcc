from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path(
        '',
        include('accounts.urls')
    ),

    path(
        'dashboard-adm/',
        include('administrador.urls')
    ),

    path(
        'admin-django/',
        admin.site.urls
    ),

    path(
        'dashboard-professor/',
        include('professor.urls')
),
]

# Serve arquivos de mídia (fotos dos usuários)
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )