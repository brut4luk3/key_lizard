# Generated by Django 4.0.4 on 2022-06-08 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Setor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_setor', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'tb_setores',
            },
        ),
    ]
