from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.views.generic import View, CreateView
from django.urls import reverse_lazy

import logging
from django.contrib.auth import authenticate, login

# Configuração do log
logger = logging.getLogger(__name__)

from diagnostico.forms.formularios import DiagnosticoLoginForm, DiagnosticoForm
from diagnostico.models import Empresa

class DiagnosticoLogin(LoginView):
  
  form_class  = DiagnosticoLoginForm
  template_name = "registration/login.html"
  success_url = reverse_lazy('diagnosticoHome')
  title = "LOGIN"
  
  def form_valid(self, form):
    # Captura dos dados do formulário
    cnpj = form.cleaned_data['cnpj']
    senha = form.cleaned_data['senha']
    
    try:
      # Verifica se a empresa existe
      empresa = Empresa.objects.get(cnpj=cnpj)

      # Autentica o usuário (se houver um campo relacionado à autenticação)
      user = authenticate(self.request, username=empresa.user.username, password=senha)

      if user is not None:
        # Usuário autenticado com sucesso
        login(self.request, user)
        self.request.session['empresa_id'] = empresa.id
        logger.info(f"Login bem-sucedido para a empresa {empresa.cnpj}")

        # Chama o método da superclasse
        response = super().form_valid(form)
        return response
      else:
        logger.warning(f"Falha na autenticação para a empresa {empresa.cnpj}. Senha incorreta.")
        form.add_error('senha', 'CNPJ ou senha inválidos.')
        return super().form_invalid(form)
    
    except Empresa.DoesNotExist:
      # Caso a empresa não exista
      logger.error(f"Empresa com CNPJ {cnpj} não encontrada.")
      form.add_error('cnpj', 'CNPJ não encontrado.')
      return super().form_invalid(form)
  
  def form_invalid(self, form):
    print("Login mal-sucessida")
    return super().form_invalid(form)
  
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['title'] = self.title
    context['form'] = self.form_class(request = self.request)
    
    return context

class DiagnosticoCreate(CreateView):
  
  model = Empresa
  form_class = DiagnosticoForm
  success_url = reverse_lazy("diagnosticoHome")
  template_name = "diagnostico/diag_form.html"
  title = 'CRIE JÁ SUA CONTA'
  
  def form_valid(self, form):
    
    response = super().form_valid(form)
    previous_url = self.request.session.get('previous_url')

    if previous_url:
      # Redireciona para a URL anterior armazenada na sessão
      return HttpResponseRedirect(previous_url)
    else:
      # Caso não haja URL anterior, redireciona para o success_url
      return response
    
  def form_invalid(self, form):
    return super().form_invalid(form)
  
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['title'] = self.title 
    referer = self.request.META.get('HTTP_REFERER')
    
    if referer:
      self.request.session['previous_url'] = referer

    return context

class DiagnosticoView(View):
  template_name = 'diagnostico/diag_main.html'

  def get(self, request):
    return render(request, self.template_name)
  
class DiagnosticoQuestionario(View):
  template_name = 'diagnostico/diag_questionario.html'

  def get(self, request):
    return render(request, self.template_name)

