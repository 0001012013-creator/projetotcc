from django.shortcuts import render, get_object_or_404, redirect
from administrador.models import Turma
from professor.models import Atividade, EntregaAtividade
from professor.services.corretor import corrigir_entrega

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


def detalhe_turma_aluno(request, turma_id):

    turma = get_object_or_404(
        Turma,
        id=turma_id,
        alunos=request.user
    )

    atividades = turma.atividades.all()

    return render(
        request,
        'aluno/detalhe_turma_aluno.html',
        {
            'turma': turma,
            'atividades': atividades
        }
    )

def responder_atividade(request, atividade_id):


    atividade = get_object_or_404(
        Atividade,
        id=atividade_id
    )

    if request.method == 'POST':

        resposta = request.POST.get(
            'resposta'
        )

        entrega = EntregaAtividade.objects.create(
            atividade=atividade,
            aluno=request.user,
            resposta=resposta
        )

        corrigir_entrega(
            entrega
        )

        return redirect(
            'detalhe_turma_aluno',
            turma_id=atividade.turma.id
        )

    return render(
        request,
        'aluno/responder_atividade.html',
        {
            'atividade': atividade
        }
    )
