# Generated by Django 4.0.4 on 2022-06-07 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Corretor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('sobrenome', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'tb_corretores',
            },
        ),
    ]
