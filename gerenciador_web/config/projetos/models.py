from django.db import models

class Projeto(models.Model):

    nome = models.CharField(max_length = 200)
    descricao = models.TextField(blank = True, null = True)
    data_criacao = models.DateTimeField(auto_now_add = True)


    #exibir titulo por padrao
    def __str__(self):
        return self.nome