from django.urls import path
from . import views

urlpatterns = [

    path(
        '',
        views.dashboard_adm,
        name='dashboard_adm'
    ),

    path(
        'usuarios/cadastrar/',
        views.cadastro_usuario,
        name='cadastro_usuario'
    ),

    path(
        'usuarios/gerenciar/',
        views.gerenciar_usuarios,
        name='gerenciar_usuarios'
    ),
]