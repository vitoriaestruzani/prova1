from django.shortcuts import render, get_object_or_404, redirect
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

def adicionar_tarefa(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')
        Tarefa.objects.create(titulo=titulo, descricao=descricao)
        return redirect ('listar_tarefas')
    return render(request, 'tarefas/form_tarefa.html')

#métodos http
# POST: Envia dados para o servidor 
# GET: Busca dados no servidor
# PUT: Atualiza recursos existentes
# DELETE:Remove recursos seleconados 