from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.views.generic import View, CreateView
from django.urls import reverse_lazy

from diagnostico.forms.formularios import DiagnosticoLoginForm, DiagnosticoForm
from diagnostico.models import Empresa

class DiagnosticoLogin(LoginView):
  
  form_class  = DiagnosticoLoginForm
  template_name = "registration/login.html"
  success_url = 'diagnosticoHome'
  title = "LOGIN"
  
  def form_valid(self, form):
    
    cnpj = form.cleaned_data['cnpj']
    senha = form.cleaned_data['senha']
    
    # Autenticação com CNPJ e senha
    empresa = Empresa.objects.get(cnpj = cnpj)
    request = self.request
    request.session['empresa_id'] = empresa.id
        
    return super().form_valid(form)
  
  def form_invalid(self, form):
    return super().form_invalid(form)
  
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['title'] = self.title
    context['form'] = self.form_class(request = self.request)
    
    return context
  

class DiagnosticoView(LoginRequiredMixin, View):
  template_name = 'diagnostico/diag_main.html'

  def get(self, request):
    return render(request, self.template_name)

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
  
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['title'] = self.title
    context['form'] = self.form_class(request = self.request)
    
    referer = self.request.META.get('HTTP_REFERER')
    
    if referer:
      self.request.session['previous_url'] = referer
      
    return context