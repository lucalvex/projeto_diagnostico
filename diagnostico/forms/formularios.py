from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.hashers import make_password, check_password

from diagnostico.models import Empresa

# Customizando campos para o formulário de login
class DiagnosticoLoginForm(forms.Form):
  
  cnpj = forms.CharField (
    label = "CNPJ",
    widget = forms.TextInput(
      attrs = {
        'id' : 'cnpj',
        'placeholder': 'Digite o cnpj',
      },
    ),
    required = True
  )
  
  senha = forms.CharField (
    label = "Senha",
    widget = forms.PasswordInput(
      attrs = {
        "placeholder" : "Digite a senha"
      },
    ),
    required=True
  )
  
  def clean(self):
    
    cleaned_data = super().clean()
    cnpj = cleaned_data.get('cnpj')
    senha = cleaned_data.get('senha')
    
    if not cnpj or not senha:
      raise forms.ValidationError("CNPJ e senha não campos obrigatórios. ")
    
    try:
      
      empresa = Empresa.objects.get(cnpj = cnpj)
      
      if not check_password(senha, empresa.senha):
        raise forms.ValidationError("Senha incorreta.")
      
    except Empresa.DoesNotExist:
      raise forms.ValidationError("CNPJ não encontrado.")
    
    return cleaned_data
  
  def __init__(self, *args, **kwargs):
    
    self.request = kwargs.pop('request', None)
    super().__init__(*args, **kwargs)
    
# Formulário de criação e atualização de informações do modelo Empresa
class DiagnosticoForm(forms.ModelForm): 
  
  nomeEmpresa = forms.CharField(
    label = "Nome da Empresa",
    widget = forms.TextInput (
      attrs = {
        'placeholder' : 'Digite o nome completo da empresa'
      }
    )
  )

  cnpj = forms.CharField (
    label = "CNPJ",
    widget = forms.TextInput (
      attrs = {
        'id' : 'cnpj',
        'placeholder' : 'XX.XXX.XXX/0001-XX'
      }
    )
  )

  nmrContato = forms.CharField (
    label = "Número de Contato",
    widget = forms.TextInput (
      attrs = { 
        'id' : 'nmrContato',      
        'placeholder' : '(XX) 9XX.XX-XX.XX'
      }
    )
  )

  email = forms.CharField (
    label = "E-mail",
    widget = forms.TextInput(
      attrs = {
        'placeholder' : 'Digite o e-mail de sua empresa'
      }
    )
  )

  senha = forms.CharField (
    label = "Senha",
    widget = forms.PasswordInput(
      attrs = {
        'placeholder' : 'Digite uma senha'
      }
    ), 
    min_length = 8,
    max_length = 100,
    required = True
  )

  confirmarSenha = forms.CharField (
    label = "Confirmar Senha",
    widget = forms.PasswordInput(
      attrs = {
        'placeholder' : 'Confirme sua senha'
      }
    ),
    required = True
    
  )

  class Meta: 
    model = Empresa
    fields = ["nomeEmpresa", "cnpj", "nmrContato", "email", "senha"]
  
  def __init__(self, *args, **kwargs):
    
    self.request = kwargs.pop('request', None)
    super().__init__(*args, **kwargs)
    
    
  def clean_confirmarSenha(self):

    senha = self.cleaned_data.get('senha')
    confirmarSenha = self.cleaned_data.get('confirmarSenha')

    if senha and confirmarSenha and senha !=confirmarSenha:
      raise forms.ValidationError("As senhas não coincidem.")
    
    return confirmarSenha
    