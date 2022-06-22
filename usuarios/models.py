from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'tb_profile'