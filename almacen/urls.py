from django.urls import path
from . import views

urlpatterns = [
    path("almacen/", views.menu_almacen, name="menu_almacen")
]
