from django.urls import path
from . import views

app_name = "almacen"

urlpatterns = [
    path("almacen/", views.menu_almacen, name="menu_almacen"),
    path("almacen/alta_almacen/", views.alta_almacen, name="alta_almacen"),
    path("almacen/baja_almacen/", views.baja_almacen, name="baja_almacen"),
    path("almacen/listar_almacenes/", views.listar_almacenes, name="listar_almacenes"),
    path("almacen/alta_lote/", views.alta_lote, name="alta_lote"),
    path("almacen/baja_lote/", views.baja_lote, name="baja_lote"),
    path("almacen/listar_lotes/", views.listar_lotes, name="listar_lotes")
]
