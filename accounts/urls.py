from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),

    # ✅ LOGOUT (FALTAVA ISSO)
    path('logout/', views.logout_view, name='logout'),

    path(
        'recuperar-senha/',
        views.solicitar_recuperacao,
        name='solicitar_recuperacao'
    ),
]