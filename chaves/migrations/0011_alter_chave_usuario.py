# Generated by Django 4.0.4 on 2022-06-21 17:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chaves', '0010_chave_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chave',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='id_usuario_chave', to=settings.AUTH_USER_MODEL),
        ),
    ]