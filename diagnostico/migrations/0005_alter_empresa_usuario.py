# Generated by Django 5.1.3 on 2024-11-19 18:58

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diagnostico', '0004_empresa_usuario'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresa',
            name='usuario',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='empresa', to=settings.AUTH_USER_MODEL),
        ),
    ]
