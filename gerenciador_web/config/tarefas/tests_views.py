from django.test import TestCase
from django.urls import reverse
from projetos.models import Projeto
from tarefas.models import Tarefa


class TarefaEProjetoViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.projeto1 = Projeto.objects.create(nome='Website Cliente X')
        cls.tarefa1 = Tarefa.objects.create(titulo='Criar layout', projeto=cls.projeto1)
        cls.tarefa2 = Tarefa.objects.create(titulo='Desenvolver backend', projeto=cls.projeto1)
        cls.projeto2 = Projeto.objects.create(nome='App Interno')
        cls.tarefa3 = Tarefa.objects.create(titulo='Configurar banco de dados', projeto=cls.projeto2)

    def test_adicionar_tarefa_com_sucesso(self):
        url = reverse('adicionar_tarefa')
        dados = {'titulo': 'Nova Tarefa', 'projeto': self.projeto1.id}
        self.client.post(url, data=dados)
        self.assertTrue(Tarefa.objects.filter(titulo='Nova Tarefa').exists())
