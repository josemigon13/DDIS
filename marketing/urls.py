from django.urls import path
from . import views

app_name = "marketing"  # lo añado justo esto porque es necesario para que funcione
                        # la redirección de url en el boton de "Volver Atrás" de cada html

urlpatterns = [
    path("marketing/", views.menu_marketing, name="menu_marketing"),
    path("marketing/alta_ofer_prod/", views.alta_ofer_prod, name="alta_ofer_prod"),
    path("marketing/baja_ofer_prod/", views.baja_ofer_prod, name="baja_ofer_prod"),
    path("marketing/consultar_ofer_prod/", views.consultar_ofer_prod, name="consultar_ofer_prod"),
    path("marketing/alta_camp_pub/", views.alta_camp_pub, name="alta_camp_pub"),
    path("marketing/alta_camp_pub/opciones", views.opciones_alta_camp_pub, name="opciones_alta_camp_pub"),
    path("marketing/alta_camp_pub/opciones/uno", views.opcion_1_aniadir_oferta_prod_promociona, name="opcion1"),
    path("marketing/baja_camp_pub/", views.baja_camp_pub, name="baja_camp_pub"),
    path("marketing/consultar_camp_pub/", views.consultar_camp_pub, name="consultar_camp_pub")
]