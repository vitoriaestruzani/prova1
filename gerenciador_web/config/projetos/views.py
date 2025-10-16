from django.shortcuts import render, get_object_or_404, redirect
from .models import Projeto


def listar_projetos(request):
    #1. A busca no banco de dados
    projetos_salvos = Projeto.objects.all()

    #2. Criamos um "dicionário de contexto" para enviar os dados ao tempate.
    #3. A chave 'minhas_projetos' será a variável que usaremos no HTML.
    contexto = {
        'meus_projetos': projetos_salvos
    }

    #3. Renderizamos o template, passando a requisição e o contexto com s dados.
    return render(request, 'projetos/lista.html', contexto)