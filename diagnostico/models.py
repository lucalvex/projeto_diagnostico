import uuid

from django.db import models

class Empresa(models.Model): 

  id = models.CharField(primary_key = True, max_length = 36, default = uuid.uuid4, editable = False)
  nomeEmpresa = models.CharField(verbose_name = "Nome da empresa", null = False, blank = False, max_length = 100)
  cnpj = models.CharField(verbose_name = "CNPJ", null = False, blank = False, max_length = 100)
  nmrContato = models.CharField(verbose_name = "Número de Contato", null = False, blank = False, max_length = 100)
  email = models.CharField(verbose_name = "E-mail", null = False, blank = False, max_length = 100)
  senha = models.CharField(verbose_name = "Senha", null = False, blank = False, max_length = 100)
  confirmarSenha = models.CharField(verbose_name = "Confirmar Senha", null = False, blank = False, max_length = 100) 
  