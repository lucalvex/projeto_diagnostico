from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views

from diagnostico.views import (
  DiagnosticoFormLogin,
  DiagnosticoView,
  DiagnosticoCreate
)

urlpatterns = [
  path("admin/", admin.site.urls),
  path("login/", DiagnosticoFormLogin.as_view(template_name="registration/login.html"), name="diagnosticoLogin"),
  path("", DiagnosticoView.as_view(template_name="diagnostico/diag_main.html"), name="diagnosticoHome"),
  path("create/", DiagnosticoCreate.as_view(template_name="diagnostico/diag_form.html"), name = "diagnosticoCreate")
    
]
