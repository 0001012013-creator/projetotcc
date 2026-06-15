from django.urls import path
from . import views

urlpatterns = [

    path(
        '',
        views.dashboard_aluno,
        name='dashboard_aluno'
    ),

    path(
        'turma/<int:turma_id>/',
        views.detalhe_turma_aluno,
        name='detalhe_turma_aluno'
    ),

    path(
        'atividade/<int:atividade_id>/responder/',
        views.responder_atividade,
        name='responder_atividade'
    ),

]