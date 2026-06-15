from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from administrador.models import Turma
from professor.models import Atividade, EntregaAtividade
from professor.services.corretor import corrigir_com_ia


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

    entrega_existente = EntregaAtividade.objects.filter(
        atividade=atividade,
        aluno=request.user
    ).first()

    if request.method == 'POST':

        if entrega_existente:

            messages.error(
                request,
                'Você já enviou esta atividade.'
            )

            return redirect(
                'detalhe_turma_aluno',
                turma_id=atividade.turma.id
            )

        resposta = request.POST.get(
            'resposta'
        )

        entrega = EntregaAtividade.objects.create(
            atividade=atividade,
            aluno=request.user,
            resposta=resposta
        )

        corrigir_com_ia(
            entrega
        )

        messages.success(
            request,
            'Atividade enviada com sucesso!'
        )

        return redirect(
            'detalhe_turma_aluno',
            turma_id=atividade.turma.id
        )

    return render(
        request,
        'aluno/responder_atividade.html',
        {
            'atividade': atividade,
            'entrega_existente': entrega_existente
        }
    )