# Generated by Django 4.0.4 on 2022-06-09 20:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('setores', '0004_remove_setor_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='setor',
            name='usuario',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
