# Generated by Django 4.0.4 on 2022-06-29 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chaves', '0013_alter_chave_horario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chave',
            name='horario',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
