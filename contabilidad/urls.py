from django.urls import path
from . import views

app_name = "contabilidad"

urlpatterns = [
    path("contabilidad/", views.menu_contabilidad, name="menu_contabilidad"),
    path("contabilidad/computar_salario/", views.computar_salario, name="computar_salario"),
    path("contabilidad/computar_pagoProveedor/", views.computar_pagoProveedor, name="computar_pagoProveedor"),
    path("contabilidad/computar_beneficiosPOS/", views.computar_beneficiosPOS, name="computar_beneficiosPOS"),
    path("contabilidad/computar_impuestos/", views.computar_impuestos, name="computar_impuestos"),
    path("contabilidad/computar_costeCampaña/", views.computar_costeCampaña, name="computar_costeCampaña"),
    path("contabilidad/listar_informes/", views.listar_informes, name="listar_informes")
]