# Generated by Django 4.0.4 on 2022-06-15 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('setores', '0011_rename_user_setor_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setor',
            name='nome_setor',
            field=models.CharField(default='Administrativo', max_length=30),
        ),
    ]