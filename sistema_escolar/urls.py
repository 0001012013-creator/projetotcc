from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('accounts.urls')),
     path(
        'dashboard-adm/',
        include('administrador.urls')
    ),
    path('admin-django/', admin.site.urls),
]