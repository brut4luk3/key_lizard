# Generated by Django 4.0.4 on 2022-06-18 13:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('chaves', '0005_alter_chave_codigo_imovel_crm_alter_chave_corretor_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='chave',
            name='horario',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]