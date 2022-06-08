from django.db import models

class Setor(models.Model):
    nome_setor = models.CharField(max_length=30)

    def __str__(self):
        return self.nome_setor

    class Meta:
        db_table = 'tb_setores'
