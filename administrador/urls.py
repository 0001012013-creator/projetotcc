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
        'usuarios/cadastrar/<str:tipo>/',
        views.cadastro_usuario,
        name='cadastro_usuario_tipo'
    ),

    path(
        'usuarios/gerenciar/',
        views.gerenciar_usuarios,
        name='gerenciar_usuarios'
    ),

    path(
        'usuarios/excluir/<int:usuario_id>/',
        views.excluir_usuario,
        name='excluir_usuario'
    ),

    path(
        'usuarios/editar/<int:usuario_id>/',
        views.editar_usuario,
        name='editar_usuario'
    ),

    path(
    'recuperacoes/',
    views.gerenciar_recuperacoes,
    name='gerenciar_recuperacoes'
),

path(
    'recuperacoes/aprovar/<int:solicitacao_id>/',
    views.aprovar_recuperacao,
    name='aprovar_recuperacao'
),

path(
    'recuperacoes/rejeitar/<int:solicitacao_id>/',
    views.rejeitar_recuperacao,
    name='rejeitar_recuperacao'
),
]