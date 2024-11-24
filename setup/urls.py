from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views

from diagnostico.views import (
  DiagnosticoLogin,
  DiagnosticoCreate,
  DiagnosticoView,
  DiagnosticoQuestionario,

)

urlpatterns = [
  path("admin/", admin.site.urls),
  path("login/", DiagnosticoLogin.as_view(template_name="registration/login.html"), name="diagnosticoLogin"),
  path("create/", DiagnosticoCreate.as_view(template_name="diagnostico/diag_form.html"), name = "diagnosticoCreate"),
  path("", DiagnosticoView.as_view(template_name="diagnostico/diag_main.html"), name="diagnosticoHome"),
  path("questionario/", DiagnosticoQuestionario.as_view(template_name="diagnostico/diag_questionario.html"), name="diagnosticoQuestionario"),
  
    
]
