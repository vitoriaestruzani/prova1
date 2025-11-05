from django.test import TestCase
from projetos.models import Projeto
from tarefas.models import Tarefa


class TarefaModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.projeto = Projeto.objects.create(nome='Projeto de Teste para Models')

    def test_criacao_tarefa_com_valores_padrao(self):
        tarefa = Tarefa.objects.create(titulo='Minha Tarefa', projeto=self.projeto)
        self.assertFalse(tarefa.concluida) # Verifica se 'concluida' é False por padrão
        self.assertIsNotNone(tarefa.data_criacao) # Verifica se a data foi preenchida

    def test_tarefa_requer_associacao_a_projeto(self):
        tarefa = Tarefa.objects.create(titulo='Tarefa de Teste', projeto=self.projeto)
        self.assertEqual(tarefa.projeto.nome, 'Projeto de Teste para Models')