# Generated by Django 5.0.6 on 2024-11-11 17:39

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Empresa",
            fields=[
                (
                    "id",
                    models.CharField(
                        default=uuid.uuid4,
                        editable=False,
                        max_length=36,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "nomeEmpresa",
                    models.CharField(max_length=100, verbose_name="Nome da empresa"),
                ),
                ("cnpj", models.IntegerField(verbose_name="CNPJ")),
                ("nmrContato", models.IntegerField(verbose_name="Número de Contato")),
                ("email", models.CharField(max_length=100, verbose_name="E-mail")),
                ("senha", models.CharField(max_length=100, verbose_name="Senha")),
                (
                    "confirmarSenha",
                    models.CharField(max_length=100, verbose_name="Confirmar Senha"),
                ),
            ],
        ),
    ]
