from django.db import models
from django.forms import CharField

# Create your models here.
class Pessoas(models.Model):
    nome = models.CharField(max_length=80)
    idade = models.CharField(max_length=2)
    departamento = models.CharField(max_length=20)
    telefone = models.CharField(max_length=11)
    
    def _str_(self):
        return self.nome