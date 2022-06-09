from django.db import models
from corretores.models import Corretor

class Chave(models.Model):
    codigo = models.CharField(max_length=3)
    codigo_imovel_crm = models.CharField(max_length=30)

    def __str__(self):
        return self.codigo

    class Meta:
        db_table = 'tb_chaves'