from django.shortcuts import render

def index(request):
    return render(request, 'index.html', {})

def cadastro_candidato(request):
    return render(request, 'cadastro_candidato.html', {})
