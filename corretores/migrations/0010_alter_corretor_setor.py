# Generated by Django 4.0.4 on 2022-07-05 12:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('setores', '0013_alter_setor_nome_setor'),
        ('corretores', '0009_corretor_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='corretor',
            name='setor',
            field=models.ForeignKey(default='Administrativo', on_delete=django.db.models.deletion.SET_DEFAULT, to='setores.setor'),
        ),
    ]
