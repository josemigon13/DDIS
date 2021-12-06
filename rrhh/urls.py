from django.urls import path
from . import views

app_name = "rrhh"

urlpatterns = [
    path("rrhh/", views.menu_rrhh, name="menu_rrhh")
]
