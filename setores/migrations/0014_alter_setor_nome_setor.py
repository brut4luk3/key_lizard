# Generated by Django 4.0.4 on 2022-07-05 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('setores', '0013_alter_setor_nome_setor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setor',
            name='nome_setor',
            field=models.CharField(default='Administrativo', max_length=30),
        ),
    ]