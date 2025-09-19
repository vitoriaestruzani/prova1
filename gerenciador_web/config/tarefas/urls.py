from django.urls import path
from . import views #importa view do app

urlpatterns = [
    #qnd a URL for vazia (ex: /tarefas/), chame a view 'listar_tarefas'
    path('', views.listar_tarefas, name='listar_tarefas'),
]