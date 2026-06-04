from django.shortcuts import render


def dashboard_adm(request):
    return render(
        request,
        'accounts/dashboardadm.html'
    )


def cadastro_usuario(request):

    if request.method == 'POST':

        print("FORMULÁRIO RECEBIDO")

        print("Nome:", request.POST.get('first_name'))
        print("Tipo:", request.POST.get('tipo_usuario'))
        print("CPF:", request.POST.get('cpf'))

    return render(
        request,
        'administrador/cadastro_usuario.html'
    )


def gerenciar_usuarios(request):
    return render(
        request,
        'administrador/gerenciar_usuarios.html'
    )