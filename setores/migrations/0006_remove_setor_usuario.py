# Generated by Django 4.0.4 on 2022-06-09 20:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('setores', '0005_setor_usuario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='setor',
            name='usuario',
        ),
    ]
