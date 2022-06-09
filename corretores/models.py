from django.db import models
from setores.models import Setor

class Corretor(models.Model):
    setor = models.ForeignKey(Setor, on_delete=models.SET_NULL, null=True)
    nome = models.CharField(max_length=30, default='Imobiliária')

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'tb_corretores'