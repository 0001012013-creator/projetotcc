from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
import secrets
from django.contrib.auth.hashers import make_password

from accounts.models import User, SolicitacaoRecuperacao


# ─────────────────────────────────────────────
# DASHBOARD
# ─────────────────────────────────────────────
def dashboard_adm(request):
    return render(request, 'accounts/dashboardadm.html')


# ─────────────────────────────────────────────
# CADASTRO DE USUÁRIO
# ─────────────────────────────────────────────
def cadastro_usuario(request, tipo=None):

    if request.method == 'POST':

        nome = request.POST.get('first_name')
        tipo = request.POST.get('tipo_usuario')
        cpf = request.POST.get('cpf')
        telefone = request.POST.get('telefone')
        endereco = request.POST.get('endereco')
        data_nascimento = request.POST.get('data_nascimento')

        email = request.POST.get('email', '').strip()
        senha = request.POST.get('senha_gerada', '').strip()

        if not email or not senha:
            messages.error(request, 'Email ou senha não foram gerados.')
            return render(request, 'administrador/cadastro_usuario.html')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Já existe um usuário com este e-mail.')
            return render(request, 'administrador/cadastro_usuario.html')

        usuario = User.objects.create_user(
            username=email,
            email=email,
            password=senha,
            first_name=nome,
            user_type=tipo,
            cpf=cpf,
            telefone=telefone,
            endereco=endereco,
            data_nascimento=data_nascimento
        )

        if 'foto' in request.FILES:
            usuario.foto = request.FILES['foto']
            usuario.save()

        messages.success(request, 'Usuário cadastrado com sucesso!')
        return redirect('gerenciar_usuarios')

    return render(
        request,
        'administrador/cadastro_usuario.html',
        {'tipo_inicial': tipo}
    )


# ─────────────────────────────────────────────
# GERENCIAMENTO DE USUÁRIOS
# ─────────────────────────────────────────────
def gerenciar_usuarios(request):

    usuarios = User.objects.all().order_by('first_name')

    return render(
        request,
        'administrador/gerenciar_usuarios.html',
        {'usuarios': usuarios}
    )


def excluir_usuario(request, usuario_id):

    usuario = get_object_or_404(User, id=usuario_id)
    usuario.delete()

    messages.success(request, 'Usuário excluído com sucesso!')
    return redirect('gerenciar_usuarios')


def editar_usuario(request, usuario_id):

    usuario = get_object_or_404(User, id=usuario_id)

    if request.method == 'POST':

        usuario.first_name = request.POST.get('first_name')
        usuario.email = request.POST.get('email')
        usuario.telefone = request.POST.get('telefone')

        if 'foto' in request.FILES:
            usuario.foto = request.FILES['foto']

        usuario.save()

        messages.success(request, 'Usuário atualizado com sucesso!')
        return redirect('gerenciar_usuarios')

    return render(
        request,
        'administrador/editar_usuario.html',
        {'usuario': usuario}
    )


# ─────────────────────────────────────────────
# RECUPERAÇÃO DE SENHA (SISTEMA COMPLETO)
# ─────────────────────────────────────────────
def gerenciar_recuperacoes(request):

    solicitacoes = SolicitacaoRecuperacao.objects.filter(
        status='pendente'
    ).order_by('-data_solicitacao')

    historico = SolicitacaoRecuperacao.objects.exclude(
        status='pendente'
    ).order_by('-data_solicitacao')

    return render(
        request,
        'administrador/gerenciar_recuperacoes.html',
        {
            'solicitacoes': solicitacoes,
            'historico': historico
        }
    )


def aprovar_recuperacao(request, solicitacao_id):

    solicitacao = get_object_or_404(SolicitacaoRecuperacao, id=solicitacao_id)

    usuario = User.objects.filter(email=solicitacao.email).first()

    if usuario:

        nova_senha = secrets.token_hex(4)

        usuario.password = make_password(nova_senha)
        usuario.save()

        solicitacao.status = 'aprovado'
        solicitacao.save()

        messages.success(
            request,
            f'Senha redefinida com sucesso! Nova senha: {nova_senha}'
        )

    else:
        messages.error(request, 'Usuário não encontrado para este e-mail.')

    return redirect('gerenciar_recuperacoes')


def rejeitar_recuperacao(request, solicitacao_id):

    solicitacao = get_object_or_404(SolicitacaoRecuperacao, id=solicitacao_id)

    solicitacao.status = 'rejeitado'
    solicitacao.save()

    messages.warning(request, 'Solicitação rejeitada.')

    return redirect('gerenciar_recuperacoes')