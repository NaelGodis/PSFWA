from django.shortcuts import render

def index(request):
    return render(request, 'index.html', {})

def cadastro_candidato(request):
    return render(request, 'cadastro_candidato.html', {})


def principal_candidato(request):
    return render(request, 'principal_candidato.html', {})


def cadastrar(request):
    return render(request, 'cadastrar.html', {})

def login_usuario(request):
    return render(request, 'login_usuario.html', {})

