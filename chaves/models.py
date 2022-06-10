from django.contrib.auth.models import User
from django.db import models
from corretores.models import Corretor
from setores.models import Setor

class Chave(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    corretor = models.ForeignKey(Corretor, on_delete=models.CASCADE)
    setor_atribuido = models.ForeignKey(Setor, on_delete=models.SET_NULL, null=True)
    codigo = models.CharField(max_length=3)
    codigo_imovel_crm = models.CharField(max_length=30)

    def __str__(self):
        return self.codigo

    class Meta:
        db_table = 'tb_chaves'