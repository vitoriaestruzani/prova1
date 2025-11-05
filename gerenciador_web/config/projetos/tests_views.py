from django.test import TestCase
from django.urls import reverse

from projetos.models import Projeto
from tarefas.models import Tarefa


class CasosDeBordaViewsTest(TestCase): 
    def setUp(self): 
        self.projeto = Projeto.objects.create(nome='Projeto para Exclusão') 
        self.tarefa_para_excluir = Tarefa.objects.create(titulo='Excluir esta', projeto=self.projeto) 
 
    def test_excluir_tarefa_remove_objeto_do_banco(self): 
        url = reverse('excluir_tarefa', args=[self.tarefa_para_excluir.id]) 
        tarefas_antes = Tarefa.objects.count() 
 
        response = self.client.post(url) 
 
        self.assertEqual(Tarefa.objects.count(), tarefas_antes - 1) 
        self.assertRedirects(response, reverse('listar_tarefas')) 
        with self.assertRaises(Tarefa.DoesNotExist): 
            Tarefa.objects.get(pk=self.tarefa_para_excluir.id) 
 
    
 