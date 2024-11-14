from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin

from diagnostico.models import Empresa

# Customizando campos para o formulário de login
class DiagnosticoLoginForm(AuthenticationForm):
  username = forms.CharField(
    label="Usuário",
    widget=forms.TextInput(attrs={'class': 'form-control'})
  )
  password = forms.CharField(
    label="Senha",
    widget=forms.PasswordInput(attrs={'class': 'form-control'})
  )

# Formulário de criação e atualização de informações do modelo Empresa
class DiagnosticoForm(LoginRequiredMixin, forms.ModelForm): 
  
  nomeEmpresa = forms.CharField(
    label = "Nome da Empresa",
    widget = forms.TextInput (
      attrs = {
        'class' : 'form-control',
        'placeholder' : 'Digite o nome completo da empresa'
      }
    )
  )

  cnpj = forms.CharField (
    label = "CNPJ",
    widget = forms.TextInput (
      attrs = {
        'id' : 'cnpj',
        'class' : 'form-control',
        'placeholder' : 'XX.XXX.XXX/0001-XX'
      }
    )
  )

  nmrContato = forms.CharField (
    label = "Número de Contato",
    widget = forms.TextInput (
      attrs = { 
        'id' : 'nmrContato',      
        'class' : 'form-control',
        'placeholder' : '(XX) 9XX.XX-XX.XX'
      }
    )
  )

  email = forms.CharField (
    label = "E-mail",
    widget = forms.TextInput(
      attrs = {
        'class' : 'form-control',
        'placeholder' : 'Digite o e-mail de sua empresa'
      }
    )
  )

  senha = forms.CharField (
    label = "Senha",
    widget = forms.TextInput(
      attrs = {
        'class' : 'form-control',
        'placeholder' : 'Digite uma senha'
      }
    )
  )

  confirmarSenha = forms.CharField (
    label = "Confirmar Senha",
    widget = forms.TextInput(
      attrs = {
        'class' : 'form-control',
        'placeholder' : 'Confirme sua senha'
      }
    )
  )

  class Meta: 
    model = Empresa
    fields = ["nomeEmpresa", "cnpj", "nmrContato", "email", "senha", "confirmarSenha"]
  
  def clean_confirmarSenha(self):

    senha = self.cleaned_data.get('senha')
    confirmarSenha = self.cleaned_data.get('confirmarSenha')

    if senha != confirmarSenha: 
      raise forms.ValidationError("O valor inserido no campo 'Senha' tem que ser o mesmo que no campo 'Confirmar Senha' ")
    else:
      return senha 