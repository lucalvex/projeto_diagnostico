from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.views.generic import View, CreateView
from django.urls import reverse_lazy

from diagnostico.forms.formularios import DiagnosticoLoginForm, DiagnosticoForm
from diagnostico.models import Empresa

class DiagnosticoFormLogin(LoginView):
  form_class  = DiagnosticoLoginForm
  template_name = "registration/login.html"

class DiagnosticoView(LoginRequiredMixin, View):
  template_name = 'diagnostico/diag_main.html'

  def get(self, request):
    return render(request, self.template_name)

class DiagnosticoCreate(CreateView):
  model = Empresa
  form_class = DiagnosticoForm
  success_url = reverse_lazy("diagnosticoHome")
  template_name = "diagnostico/diag_form.html"