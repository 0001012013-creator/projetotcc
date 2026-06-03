from django.shortcuts import render


def dashboard_adm(request):
    return render(
        request,
        'accounts/dashboardadm.html'
    )


def cadastro_usuario(request):
    return render(
        request,
        'administrador/cadastro_usuario.html'
    )


def gerenciar_usuarios(request):
    return render(
        request,
        'administrador/gerenciar_usuarios.html'
    )