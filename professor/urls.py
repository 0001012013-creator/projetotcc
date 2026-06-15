from django.urls import path
from . import views

urlpatterns = [

    path(
        '',
        views.dashboard_professor,
        name='dashboard_professor'
    ),

    path(
        'turma/<int:turma_id>/',
        views.detalhe_turma,
        name='detalhe_turma'
    ),

    path(
        'turma/<int:turma_id>/atividade/nova/',
        views.criar_atividade,
        name='criar_atividade'
    ),

    path(
        'atividade/<int:atividade_id>/criterios/',
        views.gerenciar_criterios,
        name='gerenciar_criterios'
    ),

    path(
        'atividade/<int:atividade_id>/',
        views.detalhe_atividade,
        name='detalhe_atividade'
    ),

    path(
        'atividade/<int:atividade_id>/editar/',
        views.editar_atividade,
        name='editar_atividade'
    ),

    path(
        'turmas/',
        views.listar_turmas,
        name='listar_turmas'
    ),

    # 🧠 TESTE DA IA (TEMPORÁRIO)
    path(
        'testar-ia/',
        views.testar_ia,
        name='testar_ia'
    ),

    # 🔥 LISTAR MODELOS DO GEMINI (ESSENCIAL PRA RESOLVER O ERRO)
    path(
        'modelos/',
        views.listar_modelos,
        name='modelos'
    ),

    path(
    'atividade/<int:atividade_id>/editar/',
    views.editar_atividade,
    name='editar_atividade'
),

    path(
        'atividade/<int:atividade_id>/excluir/',
        views.excluir_atividade,
        name='excluir_atividade'
),

path(
    'criterio/<int:criterio_id>/editar/',
    views.editar_criterio,
    name='editar_criterio'
),

path(
    'criterio/<int:criterio_id>/excluir/',
    views.excluir_criterio,
    name='excluir_criterio'
),

path(
    'atividade/<int:atividade_id>/criterio/adicionar/',
    views.adicionar_criterio,
    name='adicionar_criterio'
),

]