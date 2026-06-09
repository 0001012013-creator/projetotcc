from django.shortcuts import render, redirect, get_object_or_404
from administrador.models import Turma
from .models import Atividade
from django.contrib import messages
from .models import CriterioAtividade

def dashboard_professor(request):

    turmas = Turma.objects.filter(
        professor=request.user
    )

    return render(
        request,
        'professor/dashboard_professor.html',
        {
            'turmas': turmas
        }
    )


def detalhe_turma(request, turma_id):

    turma = get_object_or_404(
        Turma,
        id=turma_id,
        professor=request.user
    )

    atividades = turma.atividades.all().order_by(
        '-data_criacao'
    )

    return render(
        request,
        'professor/detalhe_turma.html',
        {
            'turma': turma,
            'atividades': atividades
        }
    )

def criar_atividade(request, turma_id):

    turma = get_object_or_404(
        Turma,
        id=turma_id,
        professor=request.user
    )

    if request.method == 'POST':

        Atividade.objects.create(
            turma=turma,
            titulo=request.POST.get('titulo'),
            descricao=request.POST.get('descricao'),
            data_entrega=request.POST.get('data_entrega')
        )

        messages.success(
            request,
            'Atividade criada com sucesso!'
        )

        return redirect(
            'detalhe_turma',
            turma_id=turma.id
        )

    return render(
        request,
        'professor/criar_atividade.html',
        {
            'turma': turma
        }
    )

def gerenciar_criterios(request, atividade_id):

    atividade = get_object_or_404(
        Atividade,
        id=atividade_id
    )

    if request.method == 'POST':

        palavra_chave = request.POST.get(
            'palavra_chave'
        )

        peso = request.POST.get(
            'peso'
        )

        CriterioAtividade.objects.create(
            atividade=atividade,
            palavra_chave=palavra_chave,
            peso=peso
        )

        messages.success(
            request,
            'Critério adicionado!'
        )

        return redirect(
            'gerenciar_criterios',
            atividade_id=atividade.id
        )

    criterios = atividade.criterios.all()

    return render(
        request,
        'professor/gerenciar_criterios.html',
        {
            'atividade': atividade,
            'criterios': criterios
        }
    )