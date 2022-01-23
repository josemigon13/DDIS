from django.urls import path
from . import views

app_name = "logistica"  # lo añado justo esto porque es necesario para que funcione
                        # la redirección de url en el boton de "Volver Atrás" de cada html

urlpatterns = [
    path("logistica/", views.menu_logistica, name="menu_logistica"),
    path("logistica/alta_pedido/", views.alta_pedido, name="alta_pedido"),
    path("logistica/baja_pedido/", views.baja_pedido, name="baja_pedido"),
    path("logistica/consultar_pedido/", views.consultar_pedido, name="consultar_pedido"),
    path("logistica/alta_proveedor/", views.alta_proveedor, name="alta_proveedor"),
    path("logistica/baja_proveedor/", views.baja_proveedor, name="baja_proveedor"),
    path("logistica/consultar_proveedor/", views.consultar_proveedor, name="consultar_proveedor")
]
