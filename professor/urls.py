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

]