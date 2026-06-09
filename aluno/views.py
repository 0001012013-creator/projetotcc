from django.shortcuts import render
from administrador.models import Turma


def dashboard_aluno(request):

    turmas = Turma.objects.filter(
        alunos=request.user
    )

    return render(
        request,
        'aluno/dashboard_aluno.html',
        {
            'turmas': turmas
        }
    )