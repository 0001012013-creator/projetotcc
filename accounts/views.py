from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import SolicitacaoRecuperacao


def login_view(request):

    # 🔍 DEBUG (VER O QUE REALMENTE ESTÁ CHEGANDO)
    print("METHOD:", request.method)
    print("POST DATA:", request.POST)

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        print("USERNAME RECEBIDO:", username)
        print("PASSWORD RECEBIDA:", password)

        user = authenticate(
            request,
            username=username,
            password=password
        )

        print("USER AUTENTICADO:", user)

        if user is not None:
            login(request, user)

            # ADMIN
            if user.is_superuser:
                return redirect('dashboard_adm')

            # fallback
            return redirect('dashboard_adm')

        else:
            return render(request, 'accounts/login.html', {
                'error': 'Usuário ou senha inválidos'
            })

    return render(request, 'accounts/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')


def solicitar_recuperacao(request):

    if request.method == 'POST':

        email = request.POST.get('email')

        SolicitacaoRecuperacao.objects.create(
            email=email
        )

        return render(
            request,
            'accounts/solicitar_recuperacao.html',
            {
                'sucesso': 'Solicitação enviada com sucesso!'
            }
        )

    return render(
        request,
        'accounts/solicitar_recuperacao.html'
    )