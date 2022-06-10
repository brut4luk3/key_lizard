from django.contrib.auth.models import User
from django.db import models
from setores.models import Setor

class Corretor(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    setor = models.ForeignKey(Setor, on_delete=models.CASCADE)
    nome = models.CharField(max_length=30, default='Imobiliária')

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'tb_corretores'