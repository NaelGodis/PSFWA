from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def index(request):
    return render(request, 'index.html', {})

def cadastro_candidato(request):
    return render(request, 'cadastro_candidato.html', {})


def principal_candidato(request):
    return render(request, 'principal_candidato.html', {})



"""test"""
def fazer_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirecionar para a página principal ou qualquer outra página após o login bem-sucedido
            return redirect('')  # Altere 'index' para o nome da sua página inicial
        else:
            # Se o login falhar, você pode adicionar uma mensagem de erro para exibir no template
            error_message = "Credenciais inválidas. Por favor, tente novamente."
            return render(request, '', {'error_message': error_message})
    else:
        return render(request, '')

