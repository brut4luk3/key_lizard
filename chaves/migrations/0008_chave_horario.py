# Generated by Django 4.0.4 on 2022-06-21 11:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('chaves', '0007_remove_chave_horario'),
    ]

    operations = [
        migrations.AddField(
            model_name='chave',
            name='horario',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
