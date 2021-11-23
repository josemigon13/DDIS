from django.urls import path
from . import views

urlpatterns = [
    path("rrhh/", views.menu_rrhh, name="menu_rrhh")
]
