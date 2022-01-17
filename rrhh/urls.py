from django.urls import path
from . import views

app_name = "rrhh"

urlpatterns = [
    path("rrhh/", views.menu_rrhh, name="menu_rrhh"),
    path("rrhh/alta_contrato/", views.alta_contrato, name="alta_contrato"),
    path("rrhh/baja_contrato/", views.baja_contrato, name="baja_contrato"),
    path("rrhh/consultar_contrato/", views.consultar_contrato, name="consultar_contrato"),
    path("rrhh/alta_oferta_emp/", views.alta_oferta_emp, name="alta_oferta_emp"),
    path("rrhh/baja_oferta_emp/", views.baja_oferta_emp, name="baja_oferta_emp"),
    path("rrhh/mostrar_informacion/", views.mostrar_informacion, name="mostrar_informacion")
]
