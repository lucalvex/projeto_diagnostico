# Generated by Django 5.1.3 on 2024-11-19 17:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diagnostico', '0002_alter_empresa_cnpj_alter_empresa_nmrcontato'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empresa',
            name='confirmarSenha',
        ),
    ]
