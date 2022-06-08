from django.db import models

class Corretor(models.Model):
    nome = models.CharField(max_length=30)
    sobrenome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'tb_corretores'