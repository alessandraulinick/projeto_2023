from django.shortcuts import render, get_object_or_404
from .models import Produto

def index(request):
    produtos = Produto.objects.all()
    context = {
        'curso': 'Programação web com django',
        'produtos': produtos
    }
    return render(request, 'index.html', context)

def contato(request):
    return render(request, 'contato.html')

def produto(request, id):
    prod = get_object_or_404(Produto, id=id)
    context = {
        'produto': prod
    }
    return render(request, 'produto.html', context)