from django.shortcuts import render, get_object_or_404
from .models import Tarefa


def listar_tarefas(request):
    #1. A busca no banco de dados
    tarefas_salvas = Tarefa.objects.all()

    #2. Criamos um "dicionário de contexto" para enviar os dados ao tempate.
    #3. A chave 'minhas_tarefas' será a variável que usaremos no HTML.
    contexto = {
        'minhas_tarefas': tarefas_salvas
    }

    #3. Renderizamos o template, passando a requisição e o contexto com s dados.
    return render(request, 'tarefas/lista.html', contexto)

def detalhe_tarefa(request, tarefa_id):
    #busca uma  tarefa pelo id
    #se não encontrar retorna erro 404
    tarefa = get_object_or_404 (Tarefa, pk=tarefa_id)
    return render (request, 'tarefas/detalhe.html', {'tarefa': tarefa})