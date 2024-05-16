from django.db import models
from instrutores.models import Instrutor

class Atividade(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    instrutores = models.ManyToManyField(Instrutor)
    data = models.DateField()
    hora_inicio = models.TimeField()
    hora_fim = models.TimeField()
    capacidade_maxima = models.PositiveIntegerField()
   

    def __str__(self):
        return self.nome
