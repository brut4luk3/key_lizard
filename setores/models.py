from django.contrib.auth.models import User
from django.db import models

class Setor(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nome_setor = models.CharField(max_length=30, default='Imobiliária')

    def __str__(self):
        return self.nome_setor

    class Meta:
        db_table = 'tb_setores'
