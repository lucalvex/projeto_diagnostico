import re

from django import forms

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
  
  def __init__(self, *args, **kwargs):
  
    self.request = kwargs.pop('request', None)
    super().__init__(*args, **kwargs)
  
  
  # Limpa a máscara aplicada ao campo cnpj
  def clean_cnpj(self):
    cnpj = self.cleaned_data.get('cnpj')
    
    if cnpj:
      cnpj = re.sub(r'\D', '', cnpj) # Remove todos os caracteres que não são números
    
    return cnpj

  # def clean(self):
    
  #   cleaned_data = super().clean()
  #   cnpj = cleaned_data.get('cnpj')
  #   senha = cleaned_data.get('senha')
    
  #   try:
      
  #     empresa = Empresa.objects.get(cnpj = cnpj)
      
  #     if not check_password(senha, empresa.senha):
  #       raise forms.ValidationError("Senha incorreta.")
      
  #   except Empresa.DoesNotExist:
  #     raise forms.ValidationError("CNPJ não encontrado.")
    
  #   return cleaned_data
  
    
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

    if senha and confirmarSenha and senha != confirmarSenha:
      raise forms.ValidationError("As senhas não coincidem. Tente novamente !")
    
    return confirmarSenha
  
  # Limpa a máscara aplicada ao campo cnpj
  def clean_cnpj(self):
    cnpj = self.cleaned_data.get('cnpj')
    
    if cnpj:
      cnpj = re.sub(r'\D', '', cnpj) # Remove todos os caracteres que não são números
    
    return cnpj
  
  # Limpa a máscara aplicada ao campo nrmContato
  def clean_nmrContato(self):
    nmr_contato = self.cleaned_data.get('nmrContato')
    if nmr_contato:
      nmr_contato = re.sub(r'\D', '', nmr_contato)  # Remove todos os caracteres que não são números
    return nmr_contato
    