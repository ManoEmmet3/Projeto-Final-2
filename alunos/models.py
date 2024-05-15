from django.db import models

class aluno(models.Model):
    
   nome = models.CharField(max_length=100)
   data_nascimento = models.DateField()
   endereco = models.CharField(max_length=200)
   telefone = models.CharField(max_length=20)
   email = models.EmailField()
   cpf = models.CharField(max_length=11, unique=True)


   def __str__(self):
   
    return self.nome



