
from django.db import models

class Tarefa(models.Model):

    titulo = models.CharField(max_length = 200)
    descricao = models.TextField(blank = True, null = True)
    data_criacao = models.DateTimeField(auto_now_add = True)
    concluida = models.BooleanField(default = False)



    #exibir titulo por padrao
    def __str__(self):
        return self.titulo