# Generated by Django 4.0.4 on 2022-06-21 17:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chaves', '0009_remove_chave_usuario_alter_chave_corretor'),
    ]

    operations = [
        migrations.AddField(
            model_name='chave',
            name='usuario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]