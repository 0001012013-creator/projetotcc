from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib import messages

from administrador.models import Turma
from .models import Atividade, CriterioAtividade

from professor.services.gemini_services import GeminiService

from google import genai
import os


# ─────────────────────────────────────────────
# DASHBOARD PROFESSOR
# ─────────────────────────────────────────────
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


# ─────────────────────────────────────────────
# DETALHE TURMA
# ─────────────────────────────────────────────
def detalhe_turma(request, turma_id):

    turma = get_object_or_404(
        Turma,
        id=turma_id,
        professor=request.user
    )

    atividades = turma.atividades.all().order_by('-data_criacao')

    return render(
        request,
        'professor/detalhe_turma.html',
        {
            'turma': turma,
            'atividades': atividades
        }
    )


# ─────────────────────────────────────────────
# CRIAR ATIVIDADE
# ─────────────────────────────────────────────
def criar_atividade(request, turma_id):

    turma = get_object_or_404(
        Turma,
        id=turma_id,
        professor=request.user
    )

    if request.method == 'POST':

        atividade = Atividade.objects.create(
            turma=turma,
            titulo=request.POST.get('titulo'),
            descricao=request.POST.get('descricao'),
            data_entrega=request.POST.get('data_entrega')
        )

        criterios = request.POST.getlist('criterio[]')
        pesos = request.POST.getlist('peso[]')

        for criterio, peso in zip(criterios, pesos):

            if criterio.strip():

                CriterioAtividade.objects.create(
                    atividade=atividade,
                    nome=criterio,
                    descricao="Critério definido pelo professor",
                    peso=peso or 1
                )

        messages.success(
            request,
            'Atividade criada com sucesso!'
        )

        return redirect('detalhe_turma', turma_id=turma.id)

    return render(
        request,
        'professor/criar_atividade.html',
        {
            'turma': turma
        }
    )


# ─────────────────────────────────────────────
# GERENCIAR CRITÉRIOS
# ─────────────────────────────────────────────
def gerenciar_criterios(request, atividade_id):

    atividade = get_object_or_404(
        Atividade,
        id=atividade_id
    )

    if request.method == 'POST':

        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')
        peso = request.POST.get('peso')

        CriterioAtividade.objects.create(
            atividade=atividade,
            nome=nome,
            descricao=descricao,
            peso=peso
        )

        messages.success(
            request,
            'Critério adicionado!'
        )

        return redirect('gerenciar_criterios', atividade_id=atividade.id)

    criterios = atividade.criterios.all()

    return render(
        request,
        'professor/gerenciar_criterios.html',
        {
            'atividade': atividade,
            'criterios': criterios
        }
    )


# ─────────────────────────────────────────────
# DETALHE ATIVIDADE
# ─────────────────────────────────────────────
def detalhe_atividade(request, atividade_id):

    atividade = get_object_or_404(
        Atividade,
        id=atividade_id
    )

    entregas = atividade.entregas.all()

    return render(
        request,
        'professor/detalhe_atividade.html',
        {
            'atividade': atividade,
            'entregas': entregas
        }
    )

# ─────────────────────────────────────────────
# EDITAR ATIVIDADE
# ─────────────────────────────────────────────
def editar_atividade(request, atividade_id):

    atividade = get_object_or_404(
        Atividade,
        id=atividade_id,
        turma__professor=request.user
    )

    if request.method == 'POST':

        atividade.titulo = request.POST.get(
            'titulo'
        )

        atividade.descricao = request.POST.get(
            'descricao'
        )

        atividade.data_entrega = request.POST.get(
            'data_entrega'
        )

        atividade.save()

        messages.success(
            request,
            'Atividade atualizada com sucesso!'
        )

        return redirect(
            'detalhe_turma',
            turma_id=atividade.turma.id
        )

    return render(
        request,
        'professor/editar_atividade.html',
        {
            'atividade': atividade
        }
    )


# ─────────────────────────────────────────────
# EXCLUIR ATIVIDADE
# ─────────────────────────────────────────────
def excluir_atividade(request, atividade_id):

    atividade = get_object_or_404(
        Atividade,
        id=atividade_id,
        turma__professor=request.user
    )

    turma_id = atividade.turma.id

    atividade.delete()

    messages.success(
        request,
        'Atividade excluída com sucesso!'
    )

    return redirect(
        'detalhe_turma',
        turma_id=turma_id
    )

# ─────────────────────────────────────────────
# LISTAR TURMAS
# ─────────────────────────────────────────────
def listar_turmas(request):

    turmas = Turma.objects.filter(
        professor=request.user
    )

    return render(
        request,
        'professor/listar_turmas.html',
        {
            'turmas': turmas
        }
    )


# ─────────────────────────────────────────────
# TESTE DA IA (CORREÇÃO)
# ─────────────────────────────────────────────
def testar_ia(request):

    prompt = "Explique o que é a LGPD em 2 linhas."

    try:
        resposta = GeminiService().gerar(prompt)

    except Exception as e:
        return JsonResponse({
            "erro": str(e)
        })

    return JsonResponse({
        "resposta": resposta
    })


# ─────────────────────────────────────────────
# LISTAR MODELOS DISPONÍVEIS (IMPORTANTE)
# ─────────────────────────────────────────────
def listar_modelos(request):

    try:
        client = genai.Client(
            api_key=os.getenv("GEMINI_API_KEY")
        )

        models = client.models.list()

        return JsonResponse({
            "modelos": [m.name for m in models]
        })

    except Exception as e:

        return JsonResponse({
            "erro": str(e)
        })


# ─────────────────────────────────────────────
# EDITAR CRITÉRIO
# ─────────────────────────────────────────────
def editar_criterio(request, criterio_id):

    criterio = get_object_or_404(
        CriterioAtividade,
        id=criterio_id
    )

    if request.method == 'POST':

        criterio.nome = request.POST.get('nome')

        criterio.peso = request.POST.get('peso')

        criterio.save()

        messages.success(
            request,
            'Critério atualizado com sucesso!'
        )

        return redirect(
            'detalhe_atividade',
            atividade_id=criterio.atividade.id
        )

    return render(
        request,
        'professor/editar_criterio.html',
        {
            'criterio': criterio
        }
    )


# ─────────────────────────────────────────────
# ADICIONAR CRITÉRIO
# ─────────────────────────────────────────────
def adicionar_criterio(request, atividade_id):

    atividade = get_object_or_404(
        Atividade,
        id=atividade_id,
        turma__professor=request.user
    )

    if request.method == 'POST':

        CriterioAtividade.objects.create(
            atividade=atividade,
            nome=request.POST.get('nome'),
            peso=request.POST.get('peso')
        )

        messages.success(
            request,
            'Critério adicionado com sucesso!'
        )

    return redirect(
        'editar_atividade',
        atividade_id=atividade.id
    )


# ─────────────────────────────────────────────
# EXCLUIR CRITÉRIO
# ─────────────────────────────────────────────
def excluir_criterio(request, criterio_id):

    criterio = get_object_or_404(
        CriterioAtividade,
        id=criterio_id
    )

    atividade_id = criterio.atividade.id

    criterio.delete()

    messages.success(
        request,
        'Critério excluído com sucesso!'
    )

    return redirect(
        'detalhe_atividade',
        atividade_id=atividade_id
    )